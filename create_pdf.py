from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

content = """
content of Pdf

"""

# استبدال الرموز اللي بتسبب مشاكل
content = content.replace("’", "'").replace("–", "-").replace("—", "-")
content = content.replace("“", '"').replace("”", '"')

for line in content.split('\n'):
    pdf.multi_cell(0, 10, line)

pdf.output("name of pdf or path when you need to add your pdf .pdf")

