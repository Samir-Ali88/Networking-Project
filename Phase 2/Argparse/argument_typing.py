import argparse

parser= argparse.ArgumentParser(description="Demonstrating type,choice")
#must be an intgar

parser.add_argument("-p","--port",type=int,default=89,help="Target Port")
#must be tcp or udp 
parser.add_argument("--porto",choices=['tcp','udp'],default='tcp',help="Protocol")
args=parser.parse_args()
print(f"Targtet port : {args.port}" )
print(f"Protocol: {args.porto.upper()}")


#how to run python "/home/SOLO/pithon/Phase 2/Argparse/argument_typing.py"