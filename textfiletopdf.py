from fpdf import FPDF
pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial',size = 15)

f = open(r'c:\users\dell\desktop\myfile.txt')

for x in f:
    pdf.cell(200,20,txt=x, ln=1, align= 'C')


pdf.output(r'c:\users\dell\desktop\name.pdf')