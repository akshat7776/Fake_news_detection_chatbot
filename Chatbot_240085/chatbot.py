import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# fine tune model from hugging face 
model_path = "akshk24/chatbot"  #hugging face model path
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
model.eval() 


st.title("Fake News Detection Chatbot")

user_input = st.text_area("Paste your news article here:", height=200)

if st.button("Check News"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        # Tokenize input
        inputs = tokenizer(
            user_input,
            padding='max_length',
            truncation=True,
            max_length=128,
            return_tensors='pt'
        )

        # Model prediction
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            probs = F.softmax(logits, dim=1)
            predicted_class = torch.argmax(probs, dim=1).item()
            confidence = probs[0][predicted_class].item() * 100

        label = "True" if predicted_class == 1 else "Fake"

        # Results
        st.markdown(f"Prediction: **{label}**")
        st.markdown(f"**Confidence:** {confidence:.2f}%")

        if predicted_class == 1:
            st.success(f"This news is likely **true** with a confidence of {confidence:.2f}%.")
        else:
            st.error(f"This news is likely **fake** with a confidence of {confidence:.2f}%.")
