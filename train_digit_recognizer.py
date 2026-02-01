import os

import cv2
import numpy as np
import tensorflow as tf
from PIL import Image


def prepare(cell: np.ndarray) -> np.ndarray:
    h, w = cell.shape
    margin = int(min(h, w) * 0.15)

    cell = cell[
        margin: h - margin,
        margin: w - margin,
    ]

    # Преобразуем в uint8 0-255 перед threshold
    cell_uint8 = (cell * 255).astype(np.uint8)

    # Binarize
    _, cell_bin = cv2.threshold(
        cell_uint8,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    # Resize to 28x28
    cell_bin = cv2.resize(cell_bin, (28, 28))

    # Center the digit using image moments
    M = cv2.moments(cell_bin)
    if M["m00"] > 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        shift_x = 14 - cx
        shift_y = 14 - cy
        M_shift = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
        cell_bin = cv2.warpAffine(cell_bin, M_shift, (28, 28), flags=cv2.INTER_LINEAR, borderValue=0)

    # Нормализуем в [0,1] уже после всех операций
    cell_bin = cell_bin.astype("float32") / 255.0

    # Возвращаем просто (28,28,1), без batch-оси
    return cell_bin.reshape(28, 28, 1)

def load_custom_dataset(dataset_dir: str):
    x_data = []
    y_data = []

    for filename in os.listdir(dataset_dir):
        if not filename.endswith(".png"):
            continue
        label = int(filename.split("_")[0])

        # Загружаем исходное изображение
        img_path = os.path.join(dataset_dir, filename)
        img = Image.open(img_path).convert("L")
        img_array = np.array(img, dtype=np.float32) / 255.0

        # Добавляем исходное изображение
        x_data.append(prepare(img_array))
        y_data.append(label)

    x_data = np.array(x_data)
    y_data = np.array(y_data)
    return x_data, y_data


def generate_augmented_data(x_data, y_data, augment_factor=1000):
    datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.2,
        height_shift_range=0.2,
        zoom_range=0.2
    )

    x_augmented = []
    y_augmented = []

    for i in range(len(x_data)):
        x = np.expand_dims(x_data[i], axis=0)  # datagen требует размер (1, H, W, C)
        aug_iter = datagen.flow(x, batch_size=1)
        for _ in range(augment_factor):
            x_batch = next(aug_iter)
            x_augmented.append(x_batch[0])
            y_augmented.append(y_data[i])

    x_augmented = np.array(x_augmented, dtype=np.float32)
    y_augmented = np.array(y_augmented, dtype=np.int32)
    return x_augmented, y_augmented


def train_and_save(path: str, dataset_dir: str):
    # Загружаем исходные данные
    x_train, y_train = load_custom_dataset(dataset_dir)

    # Генерируем 1000 аугментированных вариантов для каждой картинки
    x_train, y_train = generate_augmented_data(x_train, y_train, augment_factor=1000)
    print(f"Total training samples: {len(x_train)}")

    # Модель CNN
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax"),
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    # Обучение
    model.fit(x_train, y_train, batch_size=64, epochs=20, validation_split=0.1)

    # Сохраняем модель
    directory = os.path.dirname(path)
    if not path.endswith(".keras"):
        path += ".keras"
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    model.save(path)
    print(f"Model saved to {path}")


if __name__ == "__main__":
    train_and_save("models/digit_cnn_model.keras", dataset_dir="dataset")