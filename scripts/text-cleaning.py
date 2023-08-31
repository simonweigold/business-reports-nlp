import os

def clean_text_no_linebreaks(text):
    text = ""
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            f = text
            f.write(text)
    except Exception as e:
        print(e)
    
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

    try:
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)
    except Exception as e:
        print(e)

def traverse_and_clean(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.txt'):
                txt_path = os.path.join(root, file)
                    
                # Extract text and save as .txt
                clean_text_no_linebreaks(txt_path)


# Application
folder = ""
traverse_and_clean(folder)
