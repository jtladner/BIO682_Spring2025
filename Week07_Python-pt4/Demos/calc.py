#!/usr/bin/env python3

# Importing modules
import argparse

#Parsing command line arguments
parser = argparse.ArgumentParser()

parser.add_argument("num1", type=float, help="First number to use in calculation")
parser.add_argument("num2", type=float, help="Second number to use in calculation")

# Optional with a default:
#parser.add_argument("-o", "--operation",default="+", choices=["+", "-", "*", "/"], help="Operation to perform")

# Optional in name, but actually required
parser.add_argument("-o", "--operation", required=True, choices=["+", "-", "*", "/"], help="Operation to perform")

args = parser.parse_args()

if args.operation == "+":
	print(args.num1 + args.num2)
elif args.operation == "-":
	print(args.num1 - args.num2)
elif args.operation == "*":
	print(args.num1 * args.num2)
elif args.operation == "/":
	print(args.num1 / args.num2)
