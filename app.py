import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def vectorize(Text):
    return TfidfVectorizer().fit_transform(Text).toarray()

def similarity(doc1, doc2):
    return cosine_similarity([doc1, doc2])

def check_plagiarism():
    global s_vectors
    vector_a = s_vectors[0][1]
    vector_b = s_vectors[1][1]
    sim_score = similarity(vector_a, vector_b)[0][1]
    result = (sim_score)
    return result

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
    vectors = vectorize(text)
    s_vectors = list(zip(text, vectors))
    plagiarism_results = []
    data = check_plagiarism()
    data = data * 100
    st.write("Plagiarism rate: ", data, "%")




