import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
print(sheet)
for i in sheet.columns:
    for j in i:
        print(j.value)
