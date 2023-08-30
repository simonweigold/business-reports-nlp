import os
import pdfplumber

def extract_text_from_pdf(pdf_path, txt_path):
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() + "\n\n"
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(full_text)

def traverse_and_convert(main_folder, output_folder):
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                
                # Create a similar folder structure in the output folder
                relative_path = os.path.relpath(root, main_folder)
                new_folder = os.path.join(output_folder, relative_path)
                os.makedirs(new_folder, exist_ok=True)
                
                # Create a .txt file path
                txt_file = os.path.splitext(file)[0] + '.txt'
                txt_path = os.path.join(new_folder, txt_file)
                
                # Extract text and save as .txt
                extract_text_from_pdf(pdf_path, txt_path)

# Example usage
main_folder = "reports_digipay_pdf"
output_folder = "reports_digipay_txt"
traverse_and_convert(main_folder, output_folder)
