🧠 NLP Text Preprocessing using Python

📌 Project Description

This project demonstrates the fundamental steps of Natural Language Processing (NLP) preprocessing using Python and the NLTK library.
The script processes a paragraph related to Artificial Intelligence and applies important preprocessing techniques such as tokenization, stop-word removal, stemming, and lemmatization.

These preprocessing steps help convert raw textual data into a clean and structured format suitable for machine learning models, sentiment analysis, chatbots, search engines, and other AI applications.

---

🎯 Objective

The objective of this project is to understand how raw textual data is transformed into meaningful processed text before applying Natural Language Processing or Machine Learning algorithms.

---

🛠️ Technologies Used

- Python
- NLTK (Natural Language Toolkit)

---

📂 Project Structure

NLP-Preprocessing
│
├── nlp_process.py
└── README.md

---

⚙️ Algorithm

1. Import required NLP libraries.
2. Download necessary NLTK datasets.
3. Provide a sample paragraph as input text.
4. Perform tokenization to split text into words.
5. Remove stop-words and unwanted symbols.
6. Apply stemming to obtain root words.
7. Apply lemmatization to obtain meaningful base words.
8. Display the output at each preprocessing stage.

---

▶️ Steps Performed in the Program

Step 1 — Importing Libraries

The program imports NLTK and its modules such as tokenizer, stop-words list, stemmer, and lemmatizer to perform preprocessing operations.

Step 2 — Downloading NLP Resources

Required datasets like punkt, stopwords, wordnet, and punkt_tab are downloaded.
This step is necessary only during the first execution of the program.

Step 3 — Input Text

A paragraph discussing Artificial Intelligence and its real-world applications is stored in a variable.
This paragraph acts as raw input data for preprocessing.

Step 4 — Tokenization

The input paragraph is split into individual words and punctuation symbols.
This helps the computer understand text as smaller meaningful units.

Step 5 — Stop-word Removal

Common English words such as “is”, “the”, “and”, “to” are removed.
Non-alphabetic tokens such as punctuation and numbers are also filtered.
This step retains only meaningful keywords.

Step 6 — Stemming

Words are reduced to their root form using Porter Stemmer.
For example:
learning → learn
systems → system
becoming → becom

This helps reduce vocabulary size in NLP models.

Step 7 — Lemmatization

Words are converted into their dictionary base form using WordNet Lemmatizer.
For example:
systems → system
tools → tool

Lemmatization produces more meaningful root words compared to stemming.

Step 8 — Displaying Output

The program prints the results at four stages:

- Original Tokens
- After Stop-word Removal
- After Stemming
- After Lemmatization

This allows easy comparison of preprocessing effects.

---

📊 Applications

- Sentiment Analysis
- Chatbot Development
- Resume Screening Systems
- Social Media Analytics
- AI Search Engines
- Recommendation Systems

---

🔮 Future Enhancements

- Implement TF-IDF or Word Embeddings
- Accept dataset input from CSV or JSON files
- Integrate preprocessing with Machine Learning models
- Develop a web interface using Flask or Streamlit

---

👨‍💻 Author

Dhanush H P Gowda
GitHub: https://github.com/dhanushhpgowda