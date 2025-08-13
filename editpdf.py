from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()

# Copy all pages except first
for page in reader.pages[1:]:
    writer.add_page(page)

# Save new file
with open("edited.pdf", "wb") as f:
    writer.write(f)