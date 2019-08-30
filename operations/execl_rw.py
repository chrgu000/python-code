
# 读写2007 excel
import openpyxl
file_path=r'/Users/zen/Desktop/服务器.xlsx'

wb = openpyxl.load_workbook(file_path)

sheet = wb["Sheet1"]

# for row in sheet.rows:
#         for cell in row:
#             print(cell.value, "\t", end="")
#         print()

for i in range(sheet.max_row):
    if i == 0:
        continue
    #print(sheet["A"][i].value, "\t", sheet["F"][i].value)
    print("{:30s}{}{}".format(sheet["A"][i].value, "\t", sheet["F"][i].value))