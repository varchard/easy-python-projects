import csv
import re
import PyPDF2
data = open('find_the_link.csv', encoding= 'utf-8')
data_set = csv.reader(data)
data_lines = list(data_set)
# len(data_lines) #displays the number of times to itterate the for loop
letters = []
for i in range(66):
    letters.append(data_lines[i][i])
link = ''.join(letters)

# print(link)  #prints the link location for the pdf to complete the puzzle
f = open('Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
phonenum = []
r = re.compile(r'(\d{3}[-\.\s]\d{3}[-\.\s]\d{4})')
for page in range(pdf_reader.numPages):
    search = pdf_reader.getPage(page)
    phonenum.append(r.findall(search.extractText()))

# print(phonenum) #prints out all the empty returns, and the phone number searched for