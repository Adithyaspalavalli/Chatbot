# Chatbot 

A simple command-line chatbot that detects user intent using **TF‑IDF** and **cosine similarity**.

## 🚀 Setup & Run

### 1. Check the python version and Create a virtual environment
```bat
python --version
python -m venv venv
```

### 2. Activate it
```bat
venv\Scripts\activate
```

### 3. Install dependencies
```bat
pip install nltk
pip install scikit-learn

```

### 4. Start the bot
```bat
python main.py
```

## 🧠 How it works
1. `intents.py` contains example phrases for each intent.
2. `nlp.py` trains a TF‑IDF vectorizer from those example phrases.
3. Your input is vectorized and compared against the training examples.
4. The closest intent is returned if its similarity score is high enough (otherwise: **unknown**).

## 🗂️ Intents included
- **greeting**: hello / hi / hey
- **account_opening**: open/create/need an account
- **account_recommendation**: which account is best / recommend account
- **goodbye**: bye / exit / quit

## 🧪 Testing
You can run `test_nlp.py` to see intent predictions for sample messages:
```bat
python test_nlp.py
```

