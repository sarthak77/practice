"""
Charts::

OpenPyXL supports creating bar, line, scatter, and pie charts using
the data in a sheet’s cells. To make a chart, you need to do the
following:

1.
Create a Reference object from a rectangular selection of cells.

2.
Create a Series object by passing in the Reference object.

3.
Create a Chart object.

4.
Append the Series object to the Chart object.

5.
Add the Chart object to the Worksheet object, optionally specifying
which cell the top left corner of the chart should be positioned..

The Reference object requires some explaining. Reference objects are
created by calling the openpyxl.chart.Reference() function and
passing three arguments:

1) The Worksheet object containing your chart data.

2) A tuple of two integers, representing the top-left cell of the
rectangular selection of cells containing your chart data: The first
integer in the tuple is the row, and the second is the column. Note
that 1 is the first row, not 0.

3) A tuple of two integers, representing the bottom-right cell of the
rectangular selection of cells containing your chart data: The first
integer in the tuple is the row, and the second is the column.

"""
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1, 11):# create some data in column A
    sheet['A' + str(i)] = i
refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
seriesObj = openpyxl.chart.Series(refObj, title='First series')
chartObj = openpyxl.chart.BarChart()
chartObj.title = 'My Chart'
chartObj.append(seriesObj)
sheet.add_chart(chartObj, 'C5')
wb.save('sampleChart.xlsx')

"""
We’ve created a bar chart by calling openpyxl.chart.BarChart(). You
can also create line charts, scatter charts, and pie charts by
calling openpyxl.chart.LineChart(), openpyxl.chart.ScatterChart(),
and openpyxl.chart.PieChart().

Unfortunately, in the current version of OpenPyXL (2.3.3), the
load_workbook() function does not load charts in Excel files. Even if
the Excel file has charts, the loaded Workbook object will not
include them. If you load a Workbook object and immediately save it
to the same .xlsx filename, you will effectively remove the charts
from it.
"""

