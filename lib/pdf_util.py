import subprocess, os
from pypdf import PdfReader

def convert_docx_to_pdf(docx_path, output_dir) -> bool:
    """
    Convert DOCX to PDF using LibreOffice in WSL.
    Example: docx_path = "/mnt/c/docs/my_file.docx"
    """
    if not os.path.exists(docx_path):
        print(f"*** file not found : {docx_path}")
        return False
    ## if output directory, then mkdir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    print(f"*** converting '{docx_path}' to pdf file in {output_dir}")
    try:
        # 'soffice' command
        subprocess.run(
            [
                "soffice", "--headless",
                "--convert-to", "pdf",
                docx_path,
                "--outdir", output_dir
            ],
            check=True,  # 오류 발생 시 예외 발생
            capture_output=True,
            text=True
        )
        output_filename = os.path.splitext(os.path.basename(docx_path))[0] + ".pdf"
        print(f"*** result : {os.path.join(output_dir, output_filename)}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"*** failure")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False
    except FileNotFoundError:
        print("*** error : 'soffice' invalid command")
        print("*** Make sure LibreOffice is installed. (sudo apt install libreoffice-writer)")
        return False
        
def extract_text_from_pdf(file_path):
    """ extract text from .pdf files """
    if not os.path.exists(file_path):
        return f"*** file not found : {file_path}"
    print(f"*** reading PDF file : {file_path}")
    try:
        with open(file_path, 'rb') as f:
            reader = PdfReader(f)
            full_text = []
            # extract all text in PDF file
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                if text: # Add only pages with text
                    full_text.append(f"--- [Page {page_num + 1}] ---\n{text}")
            return "\n".join(full_text)
    except Exception as e:
        return f"*** error : {e}"
    
def extract_text_from_docx(docx_path, pdf_dir):
    """
        Extract text from docx file.
        1. Convert docx file to pdf file.
        2. Read the pdf file into text.
    """
    full_text = ''
    if(convert_docx_to_pdf(docx_path, pdf_dir)):
        pdf_file_name = os.path.splitext(os.path.basename(docx_path))[0] + ".pdf"
        pdf_file = os.path.join(pdf_dir,pdf_file_name)
        full_text = extract_text_from_pdf(pdf_file)
    return full_text
