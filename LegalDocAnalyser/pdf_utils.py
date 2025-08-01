import PyPDF2

def extract_text_from_pdf(file_path):
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)

            if reader.is_encrypted:
                try:
                    reader.decrypt('')
                except:
                    return None, "PDF is encrypted and cannot be decrypted."

            text = ''
            for page_num, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
                else:
                    text += f"\n[Warning: Page {page_num+1} has no extractable text]\n"
            
            return text.strip(), None

    except Exception as e:
        return None, f"Error reading PDF: {str(e)}"