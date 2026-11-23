from openpyxl import load_workbook


def transpose_without_numpy(path: str) -> list:
    wb = load_workbook(filename=path, read_only=True)
    sheet = wb["Sheet1"]

    mx = []
    for row in sheet.iter_rows(values_only=True):
        mx.append(list(row))

    # https://stackoverflow.com/a/6473724/4737417
    return list(map(list, zip(*mx)))


if __name__ == "__main__":
    print(transpose_without_numpy("input.xlsx"))
