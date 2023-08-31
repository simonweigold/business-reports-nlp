import os
import re

def traverse_and_clean(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)
                
                # Read the file content
                with open(file_path, 'r', encoding='utf-8') as file:
                    raw_text = file.read()
                
                # Apply the cleaning function
                cleaned_text = clean_text_no_linebreaks(raw_text)
                
                # Save the cleaned text back into the same file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(cleaned_text)

# The cleaning function
def clean_text_no_linebreaks(text):
    cleaned_text = []
    
    # Remove all line breaks to treat the text as one continuous string
    text = text.replace('\n', ' ')
    
    # Split the text into sentences using regex (. ? ! as sentence delimiters)
    sentences = re.split(r'([.!?])\s+', text)
    sentences = ["".join(x) for x in zip(sentences[::2], sentences[1::2])]  # Pairing sentences with their ending punctuation
    
    for sentence in sentences:
        # Remove leading and trailing whitespaces
        sentence = sentence.strip()
        
        # Check if the sentence is empty, if so skip it
        if not sentence:
            continue
        
        # Check if the sentence is likely to be a header or title (all words capitalized)
        if all(word.istitle() for word in re.findall(r'\b\w+\b', sentence)):
            cleaned_text.append(sentence)
            continue
        
        # Check if the sentence is a complete sentence (starts with capital letter and ends with ., ?, or !)
        if re.match(r'^[A-Z].*[.!?]$', sentence):
            # Remove extra spaces
            cleaned_sentence = re.sub(r'\s+', ' ', sentence)
            cleaned_text.append(cleaned_sentence)
            continue
        
        # For sentences with more than 5 words, consider them as complete sentences
        if len(re.findall(r'\b\w+\b', sentence)) > 5:
            # Remove extra spaces
            cleaned_sentence = re.sub(r'\s+', ' ', sentence)
            cleaned_text.append(cleaned_sentence)
            continue
        
        # For incomplete or nonsensical text, mark it
        cleaned_text.append(f"<!-- {sentence} -->")
    
    return '\n'.join(cleaned_text)



# Application
folder = "reports_digipay_txt"
traverse_and_clean(folder)
