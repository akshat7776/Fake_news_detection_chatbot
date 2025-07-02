#  Fake News Detection Chatbot

This project is a Streamlit-based chatbot that determines whether a given news article or text snippet is fake or true using a fine-tuned BERT model.
The model is hosted on Hugging Face Hub, and the chatbot can be tested both locally and online.
Features of a chatbot:
1. Detects fake vs true news  
2. Shows prediction confidence score
3. Model hosted on Hugging Face for easy deployment

Dependencies to run chatbot:

Install required Python packages:
pip install -r requirements.txt


Contents of `requirements.txt`:
```
streamlit
transformers
torch
pandas
huggingface_hub
```


How to run locally:

1. Clone the repository: https://github.com/akshat7776/Fake_news_detection_chatbot/tree/main/Chatbot_240085

2. Install dependencies:
pip install -r requirements.txt

3. Run the Streamlit app:
“streamlit run chatbot.py”

4. Open your browser → visit: http://localhost:8501

How to run live:

Run  the chatbot on Streamlit Cloud: https://akshatk24.streamlit.app/

Hugging Face model:
The fine-tuned model is hosted on Hugging Face: https://huggingface.co/akshk24/chatbot

Dataset & Training:
1. Data preprocessing and fine-tuning are done in  “chatbot_notebook.ipynb”.
2. The trained model is uploaded to Hugging Face to keep this repo lightweight.
3. URL of full processed dataset from model https://drive.google.com/drive/folders/1MnMt4AqL6PeJMxQSdkiZU_F2GxplBQah?usp=sharing


How it works: 
1. The chatbot takes the user's input text
2. Tokenizes and sends it to the model 
3. Model predicts: Fake / True and Displays result with confidence score
