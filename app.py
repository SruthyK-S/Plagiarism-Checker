import os
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def vectorize(Text): 
    return TfidfVectorizer().fit_transform(Text).toarray()

def similarity(doc1, doc2): 
    return cosine_similarity([doc1, doc2])


def check_plagiarism():
    global s_vectors
    for student_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            #score = (student_pair[0], student_pair[1], sim_score)
            score = (sim_score)
            plagiarism_results.add(score)
    return plagiarism_results


st.title("Plagiarism Checker")
files = []
text = []


data1 = st.file_uploader("Upload first PDF file")
data2 = st.file_uploader("Upload second PDF file")

if data1 is not None and data2 is not None:
    text1 = data1.read()
    text2 = data2.read()
    text.append(text1)
    text.append(text2)
#files = [doc for doc in os.listdir() if doc.endswith('.txt')]
    #text = [open(_file, encoding='utf-8').read() for _file in files]
    vectors = vectorize(text)
    s_vectors = list(zip(text, vectors))
    plagiarism_results = set()
    for data in check_plagiarism():
        st.write("Plagiarism rate: ", data)




