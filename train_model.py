# train_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
import pickle

# Example dataset (replace with your actual compost dataset)
data = {
    'text': [
        'banana peel',
        'plastic bottle',
        'apple core',
        'paper towel',
        'glass jar',
        'food scraps',
        'metal can',
        'tea bag',
        'aluminum foil',
        'cardboard box'
    ],
    'label': [
        'compostable',
        'non-compostable',
        'compostable',
        'compostable',
        'non-compostable',
        'compostable',
        'non-compostable',
        'compostable',
        'non-compostable',
        'compostable'
    ]
}

df = pd.DataFrame(data)

# Create pipeline with TfidfVectorizer and Naive Bayes classifier
pipeline = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

# Train the model
pipeline.fit(df['text'], df['label'])

# Save the pipeline model to a file
with open("smartcompostmodel.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Model trained and saved as 'smartcompostmodel.pkl'")
