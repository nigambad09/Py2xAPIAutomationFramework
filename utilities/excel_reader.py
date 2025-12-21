import openpyxl


def get_test_data(filepath, sheet_name):
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook[sheet_name]

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)

        return data
