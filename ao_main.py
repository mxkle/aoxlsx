from ao_helper import helper
from ao_excel import  bb
from openpyxl import Workbook
import sys

def call_helper(sys.argv):
    del(sys.argv[0])
    print(sys.argv)
    args=helper(['gold','-b','-p','232'])


print(args.get('item').title())
