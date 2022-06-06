import csv
import sys
import re
from fqdn import FQDN

if (len(sys.argv)==1):
    print ("need csv filename")
elif (len(sys.argv)==2):
    print("need output filename")
else:
    print(sys.argv)
    namafile = sys.argv[1]
    namafileout = sys.argv[2]
    csv_out = open(namafileout,'w')
    tulis = csv.writer(csv_out)
    with open(namafile) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        for row in csv_reader:
            if (row[0]==""):
                continue
            else:
                baris = row
                domain=row[0]
                check_fqdn = FQDN(domain)
                if (not check_fqdn.is_valid) :
                    print (csv_reader.line_num,' ',row[0],' ',"Invalid")
                    if (not domain.isascii()):
                        print("contain foreign letter")
                        try:
                            clean = domain.encode('idna')
                            print(clean.decode())
                            row[0]=clean.decode()
                            baris=row
                            tulis.writerow(baris)
                        except:
                            print("cannot convert to IDNA")
                    else:
                        print("Totally wrong domain")
                else:
                    tulis.writerow(baris)
print ("selesai")
#from fqdn import FQDN
#domain = "haha hihihi.com"
#check_fqdn = FQDN(domain)
#print(domain ," ", check_fqdn.is_valid)
