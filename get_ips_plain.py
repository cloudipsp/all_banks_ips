import socket
import csv
import sys
import argparse
import os
import get_ips

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some contiries.')
    parser.add_argument('--country', metavar='', type=str, nargs='+', help='contiries (default: all)')
    parser.add_argument('--file', help='file to write (default: stdout)')

    args = parser.parse_args()

    if args.file:
        out = open(args.file,'w')
    else:
        out = sys.stdout

    filename = 'acs_url.csv'
    with open(filename, 'rb') as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        if args.country:
            reader = filter( lambda x: x[2] in args.country, reader)
        for row in reader:
            ret = get_ips.get_ips(row)
            out.writelines([ip + os.linesep for ip in ret[3]])
    
    if args.file:
        out.close()
