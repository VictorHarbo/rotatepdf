#!/usr/bin/env python3

### CODE TO WORK ON IS COMMENTED OUT
#import subprocess
#import sys

#def install(package):
#    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#install("pyinputplus")
#install("PyPDF2")

import pyinputplus as pyip
from PyPDF2 import PdfFileReader, PdfFileWriter
from os import listdir
from os import getcwd

# Gets the working directory 
cwd = getcwd()
input_dir = cwd + "/input/"
output_dir = cwd + "/output/"

# Makes the user choose how the files should be turned
value = pyip.inputNum("How many degrees should the pdf files be turned clockwise? " , min=0, max=360)

### TODO: DISPLAY HELP TIP IF INPUT IS WRONG

#Turns all the pdf files in input-folder
for x in listdir(input_dir):
    if not x.endswith('.pdf'):
        continue
    pdf_in = open(input_dir + x, 'rb')
    pdf_reader = PdfFileReader(pdf_in)
    pdf_writer = PdfFileWriter()
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(value)
        pdf_writer.addPage(page)
    pdf_out = open(output_dir + x, 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()