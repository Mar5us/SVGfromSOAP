# to extract svg parts of SOAP/XML message
# creates one svg file per <graphic> tag content
# Marcus Kesper, 29.06.2017

import xml.etree.ElementTree as ET
import optparse
import os

parser = optparse.OptionParser(version="%prog 1.0")
parser.add_option("-f", "--file", dest="file", default="", help="Input file", metavar="FILE")
(options, args) = parser.parse_args()
print ('options: ', options)

if options.file != "":
    filetoparse = options.file
else:
    print ("please specify a file name")
    exit(-1)

data = open(filetoparse).read()

root = ET.fromstring(data)
index = 0

for log in root.iter('graphic'):
    index = index + 1
    filename = os.getcwd()+"\graphic"+str(index)+".svg"
    print (filename)
    newSVG = open(filename,"w")
    newSVG.write(log.text)
    newSVG.close()


