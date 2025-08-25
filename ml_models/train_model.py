import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Read the training data 
df = pd.read_csv("mood_dataset.csv")

X = df['text']
y = df['mood']

# Create a pipeline using tf-idf
model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2))),
    ("lr", LogisticRegression(max_iter= 1000))
])

# Train the model
model.fit(X,y)

# Save the model
joblib.dump(model, "mood_model.pkl")
print("Model was saved in mood_model.pkl")
