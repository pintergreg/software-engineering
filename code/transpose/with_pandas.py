import pandas as pd


def transpose_with_pandas(path: str) -> pd.DataFrame:
    df = pd.read_excel(path)
    return df.transpose()


if __name__ == "__main__":
    print(transpose_with_pandas("input.xlsx"))
