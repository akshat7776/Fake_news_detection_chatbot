#  Fake News Detection Chatbot

This project is a Streamlit-based chatbot that determines whether a given news article or text snippet is fake or true using a fine-tuned BERT model.
The model is hosted on Hugging Face Hub, and the chatbot can be tested both locally and online.

Features of a chatbot:
1. Detects **fake vs. true** news articles   
2. Shows **prediction confidence score**
3. Model hosted on Hugging Face for easy deployment
4. Sample video demonstration: https://drive.google.com/drive/folders/1MnMt4AqL6PeJMxQSdkiZU_F2GxplBQah?usp=drive_link

How it works: 
1. The user enters the news article text into the chatbot
2. Text is tokenized and passed to the fine-tuned BERT model
3. Model predicts **Fake** or **True** with a confidence score
4. The chatbot displays the result
   
Dataset & Training:
1. Data preprocessing & model fine-tuning are in “chatbot_notebook.ipynb”
2. Trained model hosted on Hugging Face: https://huggingface.co/akshk24/chatbot
3. Training dataset & processed data available here: https://drive.google.com/drive/folders/1MnMt4AqL6PeJMxQSdkiZU_F2GxplBQah?usp=sharing
  
Dependencies to run the chatbot:

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

How to run live (Streamlit Cloud):

You can test the chatbot live here: https://akshatk24.streamlit.app/
