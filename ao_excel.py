from openpyxl import load_workbook
from collections import OrderedDict
import datetime

def init_wb(i):
	wb = load_workbook('excel.xlsx')
	try:
		ws = wb[i]
	except:
		ws = wb.create_sheet(i)
		hl = ['Date','Action','Amount','Price/1','Price/total','Tier','Location']
		for col in ws.iter_cols(min_row=1, max_col=7, max_row=1):
			for cell in col:
				cell.value=hl.pop(0)
				
	#print(ws,wb.sheetnames)
	return (ws,wb)
	
def init_values(ws,args):
	dt = datetime.datetime.today().strftime("%Y-%m-%d")
	max = ws.max_row
	if max == 1:
		max+=1
	else:
		c = 'A'+str(max)
			while ws[c].value == None or ws[c].value == "Date":
			max -= 1
			c = 'A'+str(max)
		
	del args['item']
	if args['p'] == None:
		args['p'] = args['P']/args['a']
	if args['P'] == None:
		args['P'] = args['p']*args['a']
	
	args['x'] = "buy" if args['x'] == True else "sell"
	vals = {'date':dt}
	vals.update({k:args[k] for k in args.keys() if args[k]})
	
	print(vals,max)
	return (vals, max)
	
def insert_values(ws,args):
	vals, max = init_values(ws,args)
	if ws['A'+str(max)].value != vals['date']:
		max += 1
		for k in vals.keys():
			col=1
			d = ws.cell(row=max, column=col, value=vals[k])
			col+=1
		
		
def save_file(wb):
    wb.save(filename = "excel.xlsx")


