from ao_helper import helper
from ao_excel import init_wb, insert_values, save_file
import sys,datetime
from collections import OrderedDict

def call_helper(ins):
        #will be replaced with sys.argv call
        #del(sys.argv[0])
        #print(sys.argv)
        return helper(['fibre','-t','4','-l','thetford','-a','222','-b','-P','32232'])

args = OrderedDict()
args['date'] = datetime.datetime.today().strftime("%Y-%m-%d")
args.update(call_helper(0))
if args['p'] == None:
        args['p'] = args['P']/args['a']
if args['P'] == None:
        args['P'] = args['p']*args['a']

args['x'] = "buy" if args['x'] == True else "sell"
#print(args,args['item'].title())
if args['item'] == "gold":
        del(args['t'])
        del(args['l'])

worksheet,workbook = init_wb(args['item'].title())
del(args['item'])
insert_values(worksheet,args)
save_file(workbook)
