import socket
from tempfile import NamedTemporaryFile
import shutil
import csv
import logging


def get_ips(row):
    try:
        addrs = list(set([str(i[4][0]) for i in socket.getaddrinfo(row[0], row[1], socket.AF_INET)]))
        logging.info(row[0] + ' has ips: ' + ','.join(addrs))
        if len(row) == 3:
            row.append(addrs)
        elif len(row) == 4:
            row[3] = addrs
    except:
        if len(row) == 3:
            row.append([])
    finally:
        return row

if __name__ == "__main__":
    
    logging.basicConfig(level=logging.INFO)

    filename = 'acs_url.csv'
    tempfile = NamedTemporaryFile(delete=False)

    with open(filename, 'rb') as csvFile, tempfile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        writer = csv.writer(tempfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for row in reader:
            writer.writerow(get_ips(row))

    shutil.move(tempfile.name, filename)
