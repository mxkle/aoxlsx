import argparse

towns=['caerleon','thetford','martlock','lymhurst','fort sterling']
tier=[x for x in range(1,9)]
def helper(parsed):
    parser = argparse.ArgumentParser(description="albion market helper\nwrite down stuff you buy sell, input will get piped to excel sheet for data collection. graphs will be created and such.") 
    parser.add_argument('item',help='item that was bought/sold')
    #parser.add_argument('sheet',help='the excel sheet')
    parser.add_argument('-t',choices=tier,help='tier of the item',metavar='1..8')
    parser.add_argument('-a',type=int,help='amount the item that was traded',nargs=1)
    parser.add_argument('-l',choices=towns,help='location where item was traded')

    group2 = parser.add_mutually_exclusive_group(required=True)
    group2.add_argument('-P',type=int,help='give total price',metavar='S',nargs=1)
    group2.add_argument('-p',type=int,help='give price per item',metavar='S',nargs=1)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-b',help="buy",action='store_true')
    group.add_argument('-s',help="sell",action='store_true')
    if len(parsed) == 0:
      parser.print_help()
    else:
      args = parser.parse_args(parsed)
      return vars(args)
