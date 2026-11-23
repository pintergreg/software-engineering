import numpy as np
from openpyxl import load_workbook


def transpose_without_pandas(path: str) -> np.ndarray:
    wb = load_workbook(filename=path, read_only=True)
    arr = np.array(
        [[cell for cell in row] for row in wb.active.iter_rows(values_only=True)]
    )
    return np.transpose(arr)


if __name__ == "__main__":
    print(transpose_without_pandas("input.xlsx"))
