import os
import glob
import csv
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim import corpora, models

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().lower()

def preprocess_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

def perform_lda(dictionary, corpus):
    lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)
    topics = lda_model.print_topics(num_words=5)
    return topics

def main(folder_path, output_csv):
    results = []
    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)
        if os.path.isdir(subfolder_path):
            txt_files = glob.glob(os.path.join(subfolder_path, '*.txt'))
            for txt_file in txt_files:
                text = read_text_file(txt_file)
                tokens = preprocess_text(text)
                dictionary = corpora.Dictionary([tokens])
                corpus = [dictionary.doc2bow(tokens)]
                topics = perform_lda(dictionary, corpus)
                topic_words = [", ".join(topic[1].split('"')[1::2]) for topic in topics]
                results.append({"Document": os.path.basename(txt_file), "Topics": "; ".join(topic_words)})

    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    folder_path = "examples"  # Replace with your folder path
    output_csv = "topic_modeling_results.csv"  # Output CSV file
    main(folder_path, output_csv)
