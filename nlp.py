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


    if score < 0.45:    # it checks for a similarity score below 0.45 (45%) and returns "unknown" if the score is below that threshold. This means that if the user's input is not similar enough to any of the predefined intents, the function will classify it as "unknown".
        return "unknown"


    return labels[best_match]