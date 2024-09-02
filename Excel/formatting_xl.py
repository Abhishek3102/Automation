from openpyxl import load_workbook
from openpyxl.styles import Font

workbook = load_workbook('report.xlsx')
sheet = workbook['Report']

sheet['A1'] = 'Sales Report'
sheet['A2'] = 'January'
sheet['A1'].font = Font('Arial', bold=True, size=20)
sheet['A2'].font = Font('Arial', bold=True, size=10)

workbook.save('report_january.xlsx')