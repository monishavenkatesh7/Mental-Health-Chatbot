import streamlit as st
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import random
import openpyxl

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import re

# Download required NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')


# Function to preprocess words: lowercasing, removing stopwords, lemmatizing, stemming
def preprocess_text(text):
    # Initialize lemmatizer, stemmer, and stopwords list
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    # Tokenize, lowercase, remove special characters, remove stopwords
    words = [re.sub(r'\W+', '', word.lower()) for word in text.split() if word.lower() not in stop_words]
    # Apply lemmatization and stemming
    words = [stemmer.stem(lemmatizer.lemmatize(word)) for word in words]
    return words

# Function to check if any processed job_list word is in the processed user_input
def contains_related_words(user_input, processed_list):
    # Preprocess the user input
    processed_input = preprocess_text(user_input)
    # Check for overlap between processed user input and job-related words
    return bool(processed_list.intersection(processed_input))

# Define the job-related words list
job_list = [
    'job', 'jobs', 'unemployment', 'unemployed', 'career', 'vacancy', 'vacancies', 
    'employment', 'hiring', 'recruitment', 'work', 'occupation', 'position', 'role', 
    'opportunity', 'internship', 'profession', 'freelance', 'gig', 'part-time', 
    'full-time', 'salary', 'wages', 'interview', 'resume', 'CV', 'application', 
    'job opening', 'headhunt', 'staffing', 'placement', 'job hunt', 'job search', 
    'job seeker', 'offer', 'job market', 'boss', 'employer']
# Preprocess job_list
processed_job_list = set(preprocess_text(" ".join(job_list)))
health_list = [
    'cold', 'cough', 'headache', 'stomach', 'fever', 'flu', 'nausea', 'vomit', 
    'fatigue', 'ache', 'pain', 'throat', 'infection', 'allergy', 'asthma', 
    'injury', 'fracture', 'muscle', 'strain', 'arthritis', 'migraine', 
    'dizzy', 'chill', 'swelling', 'diarrhea', 'constipation', 'heartburn', 
    'indigestion', 'ulcer', 'diabetes', 'hypertension', 'pressure', 
    'obesity', 'rash', 'inflammation', 'joint', 'back', 'neck', 'acid', 
    'bronchitis', 'pneumonia', 'virus', 'bacteria', 'immune', 'skin', 
    'eczema', 'psoriasis', 'chronic', 'fatty', 'kidney', 'gallbladder', 
    'thyroid', 'hormone', 'cholesterol', 'anemia', 'dehydration', 
    'sunburn', 'tooth', 'dental', 'eye', 'ear', 'sinus', 'breath', 
    'respiratory', 'spine', 'sprain', 'cardiac', 'cancer', 'tumor', 
    'lesion', 'bruise', 'burn', 'cut', 'wound', 'scar', 'bleeding', 
    'blister', 'abscess', 'ulcer', 'cramp', 'spasm', 'faint', 'seizure', 
    'stroke', 'coma', 'fat', 'sugar', 'pulse', 'vein', 'artery', 'nerve', 
    'brain', 'liver', 'heart', 'lung', 'bowel', 'bladder', 'colon', 'bone', 
    'rib', 'spasm', 'gland', 'groin', 'pelvis', 'hip', 'knee', 'elbow', 
    'wrist', 'ankle', 'toe', 'finger', 'joint', 'mobility', 'balance', 
    'vision', 'hearing', 'speech', 'swallow', 'coordination', 'tremor', 
    'fatty', 'tumor', 'wart', 'cyst', 'polyp', 'clot', 'bleed', 'sweat', 
    'rash', 'itch', 'vomit', 'sneeze', 'cough']
# Preprocess health_list
processed_health_list = set(preprocess_text(" ".join(health_list)))

order_log = pd.read_excel('order_data.xlsx')

# Load JSON data
with open("intent.json") as file:
    data = json.load(file)

# Prepare data
intents = []
for intent in data["intents"]:
    tag = intent["tag"]
    patterns = intent["patterns"]
    responses = intent["responses"]

    for pattern in patterns:
        intents.append({"tag": tag, "pattern": pattern, "response": responses})

df = pd.DataFrame(intents)
df.rename(columns={'pattern': 'patterns', 'response': 'responses'}, inplace=True)
# Train-test split
X = df['patterns'].apply(preprocess_text)  # Preprocess training data
y = df['tag']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the preprocessed text data using TF-IDF
vectorizer = TfidfVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x)  # Use identity functions for preprocessor and tokenizer
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a Support Vector Machine (SVM) classifier
model = SVC()
model.fit(X_train_vec, y_train)

# Function to predict intents based on user input
def predict_intent(user_input):
    try:
        user_input = int(user_input)
        return str(user_input)
    except:
        processed_input = preprocess_text(user_input)  # Preprocess user input
        user_input_vec = vectorizer.transform([processed_input])  # Vectorize preprocessed input
        intent = model.predict(user_input_vec)[0]
    return intent

# Function to generate responses based on predicted intents and specific keywords
def generate_response(intent, user_input):
    try:
        user_input = int(user_input)
        order_details = order_log[order_log['id'] == int(user_input)]
        if order_details.shape[0] == 0:
            response = 'Order Not found contant customer care at +91 9999999999'
        else:
            response = order_details
    except:
        response = ""
        response_options = df[df['tag'] == intent]['responses'].values

        if contains_related_words(user_input, processed_job_list):
            response = """I'm sorry to hear that. I can understand that you are having a hard time with your career.
            I recommend you consult a career adviser for assistance. If you have any questions related to handling stress, I can definitely help you with that."""
        if contains_related_words(user_input, processed_health_list):
            response = """I'm sorry to hear that. I can understand that you are having a hard time with your health.
            I recommend you consult a doctor for assistance. If you have any questions related to handling stress, I can definitely help you with that."""

        # If no specific response is set, choose a random one
        if not response and len(response_options) > 0:
            response = random.choice(response_options[0])
        elif not response:
            response = """I am really sorry for your situation; I can understand something is wrong, which I cannot comprehend.
            But I really want to help you if you can be more precise and specific about your condition; I can help you."""
    return response

# Streamlit app setup
st.title("Chatbot Application")
st.write("""This is a simple chatbot application. Type your message below to start chatting!
        Please provide the Order Number only for checking the order details""")

# Maintain conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", "")

if user_input:
    intent = predict_intent(user_input)
    response = generate_response(intent, user_input)
    st.session_state.history.append({"User": user_input, "Chatbot": response})

# Display chat history
for chat in st.session_state.history:
    st.write("User:", chat["User"])
    st.write("Chatbot:", chat["Chatbot"])
    st.write("---")
