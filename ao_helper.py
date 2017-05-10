import argparse

towns=['caerleon','thetford','martlock','lymhurst','fort sterling']
tier=[x for x in range(1,9)]
ordered_flags=['item','x','a','p','P','t','l']
def helper(parsed):
        parser = argparse.ArgumentParser(description="albion market helper\nwrite down stuff you buy sell, input will get piped to excel sheet for data collection. graphs will be created and such.") 
        parser.add_argument('item',help='item that was bought/sold')
        #parser.add_argument('sheet',help='the excel sheet')

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-b',help="buy",action='store_true',dest='x')
        group.add_argument('-s',help="sell",action='store_false',dest='x')    

        parser.add_argument('-a',type=int,help='amount the item that was traded')

        group2 = parser.add_mutually_exclusive_group(required=True)
        group2.add_argument('-p',type=int,help='give price per item',metavar='S')
        group2.add_argument('-P',type=int,help='give total price',metavar='S')

        parser.add_argument('-t',choices=[str(i) for i in range(1,9)],help='tier of the item',metavar='1..8')
        parser.add_argument('-l',choices=towns,help='location where item was traded')

        if len(parsed) == 0:
                parser.print_help()
        else:
                args = vars(parser.parse_args(parsed))
                return sorted(args.items(), key=lambda pair: ordered_flags.index(pair[0])) 

#args=helper(['gold','-a','222','-b','-P','32232'])
#print(args)
