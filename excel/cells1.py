import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'Tall row'
sheet['B2'] = 'Wide column'
sheet.row_dimensions[1].height = 70
sheet.column_dimensions['B'].width = 20
wb.save('dimensions.xlsx')
"""
Once you have the RowDimension object, you can set its height.
Once you have the ColumnDimension object, you can set its width.
The row height can be set to an integer or float value between 0 and
409. This value represents the height measured in points, where one
point equals 1/72 of an inch. The default row height is 12.75. The
column width can be set to an integer or float value between 0 and
255. This value represents the number of characters at the default
font size (11 point) that can be displayed in the cell. The default
column width is 8.43 characters. Columns with widths of 0 or rows
with heights of 0 are hidden from the user.
"""