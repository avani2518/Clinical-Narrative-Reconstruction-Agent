import fitz

class PDFReader:

    def extract_text(self, pdf_path):

        text = ""

        pdf = fitz.open(pdf_path)

        for page in pdf:

            text += page.get_text()

        return text