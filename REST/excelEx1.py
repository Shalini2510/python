from openpyxl import Workbook

wb= Workbook()

ws1=wb.active

dest_filenamw = 'test.xlsx'

ws1.title= 'range names'

for row in range(1,40):
    ws1.append(range(40))
wb.save(filename = dest_filenamw)
