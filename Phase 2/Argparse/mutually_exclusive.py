import argparse
parser=argparse.ArgumentParser(description="This is mutually exclusive")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-t","--target",type=str,help="Scan the ip adress")
group.add_argument("-l","--list",type =str,help="Total user")
args=parser.parse_args()
if args.target:
    print(f"Targetinng the {args.target}")

if args.list:
    print(f"Total in the list are {args.list}")

#ei code ta ekbara ekta run korbe python "/home/SOLO/pithon/Phase 2/Argparse/mutually_exclusive.py" -l 25