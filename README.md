# Sudoku Solver on Python

## Install
```bash
git clone https://github.com/TheDexodus/SudokuSolver
cd SudokuSolver
pip install -r requirements.txt
```

## How run?
In folder "**tasks**" you can add your sudoku in TXT format

And set constant SUDOKU_FILENAME="PATH_TO_SUDOKU.txt" in **main.py**

## TXT Format
Blank example:
```text
+-------+-------+-------+
|       |       |       |
|       |       |       |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|       |       |       |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|       |       |       |
|       |       |       |
+-------+-------+-------+
```

## Train model
```bash
python train_digit_recognizer.py
```

### Dataset
At current moment datasets have 9 digits from website https://sudoku.com/extreme/