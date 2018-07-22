import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
print(tuple(sheet['A1':'C3']))

for i in sheet['A1':'C3']:
    for j in i:
        print(j.value)
    print('end of row')