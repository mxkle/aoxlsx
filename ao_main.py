from ao_helper import helper
from ao_excel import init_wb, insert_values, save_file
import sys

def call_helper(ins):
    #will be replaced with sys.argv call
	#del(sys.argv[0])
    #print(sys.argv)
	return helper(['gold','-a','222','-b','-P','32232'])

args=call_helper(0)
print(args)

worksheet,workbook=init_wb(args.get('item').title())
insert_values(worksheet,args)

save_file(workbook)