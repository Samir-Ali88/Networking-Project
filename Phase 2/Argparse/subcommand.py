import argparse
parser=argparse.ArgumentParser(
    description="Multi tool CLI",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
sub_parser=parser.add_subparsers(dest="command",help="Chose a tool")


#scan tool
scanner=sub_parser.add_parser("Scan",help="Run network scan")
scanner.add_argument("-t","--target",required=True,help="target ip")
scanner.add_argument("-p","--port",type=int,default=80,help="Port to scan")

#brute force tool
brute=sub_parser.add_parser("Brute",help="Run to brute force attack")
brute.add_argument("-w","--wordlist",required=True,help="Path to Wordlist")

args=parser.parse_args()
if args.command == "Scan":
    print(f"Running SCAN on {args.target} on port {args.port}")
elif args.command == "Brute":
    print(f"Running BRUTE attack using {args.wordlist}")
else:
    parser.print_help()