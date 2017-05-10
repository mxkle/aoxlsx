from ao_helper import helper
from ao_excel import init_wb, insert_values, save_file
import sys,datetime
from collections import OrderedDict

call_example1=['fibre','-s','-t','6','-l','martlock','-a','12','-p','1099']
call_example2=['stone','-b','-t','2','-l','fort sterling','-a','36','-p','99']
call_example3=['gold','-b','-a','250','-p','242']

args = OrderedDict()
args['date'] = datetime.datetime.today().strftime("%Y-%m-%d")
args.update(helper(call_example3))
if args['p'] == None:
        args['p'] = args['P']/args['a']
if args['P'] == None:
        args['P'] = args['p']*args['a']

args['x'] = "buy" if args['x'] == True else "sell"
if args['item'] == "gold":
        del(args['t'])
        del(args['l'])

worksheet,workbook = init_wb(args['item'].title())
del(args['item'])
insert_values(worksheet,args)
save_file(workbook)
