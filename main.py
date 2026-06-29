import argparse

from modules.enum import basic_info
from modules.directory import directory_enumeration
from modules.subdomain import subdomain_bt


parser = argparse.ArgumentParser("Simple web server inspector")

subparsers = parser.add_subparsers(
    dest="command",
    required=True
)

# inspect command
inspect_parser = subparsers.add_parser(
    "enum",
    help="Inspect target web server"
)

inspect_parser.add_argument(
    "-u",
    "--url",
    required=True,
    help="Target URL"
)
inspect_parser.add_argument(
    "-o",
    "--output",
    metavar="FILE",
    help="Save report to file"
)# accept filename

# dir command
dir_parser = subparsers.add_parser(
    "dir",
    help="Directory brute force"
)

dir_parser.add_argument(
    "-u",
    "--url",
    required=True
)

dir_parser.add_argument(
    "-w",
    "--wordlist",
    required=True
)
dir_parser.add_argument(
    "-o",
    "--output",
    metavar="FILE",
    help="Save report to file",
)

# subdomain parser 
vhost_parser = subparsers.add_parser("subdomain", help = "subdomain brute force");
vhost_parser.add_argument("-u","--url",required=True);
vhost_parser.add_argument("-w","--wordlist",required=True);
vhost_parser.add_argument("-o","--output",metavar="FILE",help="Save report to file");

args = parser.parse_args();



if args.command == "enum":
    basic_info(args.url,args.output);


elif args.command == "dir":
    directory_enumeration(args.url, args.wordlist,args.output);

elif args.command == "subdomain":
    subdomain_bt(args.url,args.wordlist,args.output);
