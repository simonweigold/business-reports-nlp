import os

def reformat_text_by_blocks(input_text):
    # Split the text into blocks separated by double newlines
    blocks = input_text.split('\n\n')
    
    # Remove internal line breaks within each block
    new_blocks = [' '.join(block.split('\n')) for block in blocks]
    
    # Reassemble the text
    reformatted_text = '\n\n'.join(new_blocks)
    
    return reformatted_text

def traverse_and_reformat_blocks(main_folder, output_folder):
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file.endswith('.txt'):
                txt_path = os.path.join(root, file)
                
                # Read the original text
                with open(txt_path, 'r', encoding='utf-8') as f:
                    original_text = f.read()
                
                # Reformat the text by blocks
                reformatted_text = reformat_text_by_blocks(original_text)
                
                # Create a similar folder structure in the output folder
                relative_path = os.path.relpath(root, main_folder)
                new_folder = os.path.join(output_folder, relative_path)
                os.makedirs(new_folder, exist_ok=True)
                
                # Save the reformatted text
                new_txt_path = os.path.join(new_folder, file)
                with open(new_txt_path, 'w', encoding='utf-8') as f:
                    f.write(reformatted_text)

# Example usage
main_folder = "reports_digipay_txt/consultancies_pdfminer"
output_folder = "reports_digipay_txt/consultancies_pdfminer_cleaned"
traverse_and_reformat_blocks(main_folder, output_folder)
