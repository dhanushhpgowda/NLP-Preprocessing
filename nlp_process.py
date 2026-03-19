# Import required libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required resources (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

# Given paragraph
text = """Artificial intelligence is becoming an essential part of everyday life by transforming the way people work, learn, and communicate. From smart assistants and recommendation systems to self driving vehicles and medical diagnosis tools, AI is used in many practical applications. Students and professionals are continuously learning new programming languages and analytical skills to adapt to this rapidly evolving technology. In the field of education, intelligent tutoring systems help learners understand complex concepts through personalized feedback and adaptive learning methods. Healthcare organizations use artificial intelligence to analyze patient data, predict diseases, and improve treatment outcomes. Businesses rely on data driven models to understand customer behavior, optimize operations, and enhance decision making processes. At the same time, ethical concerns such as data privacy, bias, and transparency must be addressed to ensure responsible development and deployment of AI systems. Governments and institutions are working on regulations and guidelines to promote fairness and accountability. As artificial intelligence continues to advance, it is important for society to balance innovation with responsibility so that these technologies contribute positively to economic growth, social well being, and sustainable development."""

# 1. Tokenization
tokens = word_tokenize(text)

# 2. Stop-word removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words and word.isalpha()]

# 3. Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_tokens]

# 4. Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_tokens]

# Output
print("Original Tokens:")
print(tokens)

print("\nAfter Stop-word Removal:")
print(filtered_tokens)

print("\nAfter Stemming:")
print(stemmed_words)

print("\nAfter Lemmatization:")
print(lemmatized_words)
