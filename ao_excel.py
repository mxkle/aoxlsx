from openpyxl import load_workbook 
import datetime

def init_wb(i):
    wb = load_workbook('excel.xlsx')
    ws = wb[i]

def insert_dtime():
    dt = datetime.datetime.today().strftime("%Y-%m-%d")
    c = 'A'+str(i)
    ws[c] = dt 
    ws[c].number_format

def save_file():
    wb.save(filename = "excel.xlsx")

