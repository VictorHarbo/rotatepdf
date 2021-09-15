#!/usr/bin/env python3
import pyinputplus as pyip
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter
from os import listdir, getcwd

# Argument parser. Makes the script take command line inputs
parser = argparse.ArgumentParser()
parser.add_argument("INPUT", help="Your input file, remember the .pdf ending. If batch processing just type input")
parser.add_argument("OUTPUT", help="Your output file, remember the .pdf ending. If batch processing just type output")
parser.add_argument("-b", "--batch", action="store_true", help='''Use this argument to process multiple files. 
                    If you are using this argument you have to specify where the files are located.
                    This is done after executing the script. When batch prosessing the default output 
                    folder is the output folder.''')
args = parser.parse_args()

# Gets the working directory and defines our output directory for batch processing
cwd = getcwd()
output_dir = cwd + "/output/"

# Makes the user choose how the files should be turned
value = pyip.inputNum("How many degrees should the pdf file(s) be turned clockwise? " , min=0, max=360)

#Turns all pdf files in the INPUT folder, if --batch/-b is used
if args.batch:
    input_dir = cwd + "/" + input("Path to the INPUT files here: ")
    for x in listdir(input_dir):
        if not x.endswith('.pdf'):
            continue
        pdf_in = open(args.INPUT + "/" + x, 'rb')
        pdf_reader = PdfFileReader(pdf_in)
        pdf_writer = PdfFileWriter()
        for pagenum in range(pdf_reader.numPages):
            page = pdf_reader.getPage(pagenum)
            page.rotateClockwise(value)
            pdf_writer.addPage(page)
        pdf_out = open(args.OUTPUT + "/" + x, 'wb')
        pdf_writer.write(pdf_out)
        pdf_out.close()
        pdf_in.close()

# Turns the INPUT pdf file and saves it as OUTPUT argumentname.
else:
    pdf_in = open(args.INPUT, 'rb')
    pdf_reader = PdfFileReader(pdf_in)
    pdf_writer = PdfFileWriter()
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(value)
        pdf_writer.addPage(page)
    pdf_out = open(args.OUTPUT, 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()