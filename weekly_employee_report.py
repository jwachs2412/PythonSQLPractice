from fpdf import FPDF
from example_pandas import salary_amount

# Generate a PDF report

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Weekly Employee Report', 0, 1, 'C')
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
        
pdf = PDFReport()
pdf.add_page()

# Add content to the PDF

pdf.set_font('Arial', '', 12)

for index, row in salary_amount.iterrows():
    pdf.cell(0, 10, f"Salary: {row['salary']}, Position: {row['position']}", 0, 1)
    
pdf.output('employee_report.pdf')