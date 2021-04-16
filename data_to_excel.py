import xlsxwriter
import json
import xlsxwriter

workbook = xlsxwriter.Workbook('data.xlsx')  # 建立文件
worksheet = workbook.add_worksheet()  # 建立sheet， 可以work.add_worksheet('employee')来指定sheet名，但中文名会报UnicodeDecodeErro的错误

data = open("dzk_file_1.json", 'r', encoding="utf-8").read()
datas = data.splitlines()
for index, dat in enumerate(datas):
    mdict = json.loads(dat)
    keys = (key for key in mdict.keys())
    skeys = sorted(keys)
    if index == 0:
        worksheet.write_row(index, 0, skeys)  # 向A1写入
    worksheet.write_row(index + 1, 0, [mdict[key] for key in skeys])  # 向A1写入

workbook.close()
