from fileinput import filename
import PyPDF2
import os
import tkinter
from tkinter import filedialog
#pdf_in_file=open("simple.pdf",'rb')
root = tkinter.Tk()
root.withdraw()

def pdf():
    pdf_folder = r"/home/jarvis/Desktop/BBI/pdf_file_encryption"
    for x,y,z in os.walk(pdf_folder):
        print(x)
        print(y)
        print(z)

def user():
    pdf_folder = r"/home/jarvis/Desktop/BBI/pdf_file_encryption"
    file_name = filedialog.askopenfilename()
    print(file_name)
    # file_name = os.path()
    # pdf_in_file=open("file_name",'rb')

    inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
    # inputpdf = PyPDF2.PdfFileReader(pdf_folder)
    pages_no = inputpdf.numPages
    output = PyPDF2.PdfFileWriter()

    for i in range(pages_no):
         inputpdf=PyPDF2.PdfFileReader(pdf_in_file)
        #  inputpdf=PyPDF2.PdfFileReader(pdf_folder)
         output.addPage(inputpdf.getPage(i))
         output.encrypt('admin@123')

   # with open("gre_password_protected.pdf", "wb") as outputStream:
    

    with open("pdf_file_encryption.pdf","wb")as outputStream:
         output.write(outputStream)
    # pdf_in_file.close()
    pdf_folder.close()
    

# pdf()
user()