import markdown2pdf
import mdpdf
import markdown2
from docx import Document

def Convert_Markdown_to_PDF(markdown_Path: str, pdf_path: str):
    markdown2pdf.convert_md_2_pdf(markdown_Path, pdf_path)

def Convert_Markdown_to_Word(markdown_Path: str, word_Path: str):
    print("")
    doc = Document()
    with open(markdown_Path, 'r', encoding='utf-8') as md_file:
        for line in md_file:
            doc.add_paragraph(line.strip())

    doc.save(word_Path)