from intents import intents

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



# Create training data

sentences = []
labels = []


for intent, examples in intents.items():

    for example in examples:

        sentences.append(example)
        labels.append(intent)



# Convert text into numbers

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(sentences)



def detect_intent(user_input):

    user_vector = vectorizer.transform([user_input])


    similarity = cosine_similarity(
        user_vector,
        vectors
    )


    best_match = similarity.argmax()


    score = similarity[0][best_match]


    if score < 0.3:
        return "unknown"


    return labels[best_match]