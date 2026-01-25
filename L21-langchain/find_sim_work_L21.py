# Title: Find the Most Similar Sentence in the Text
## Logic:
# 1. Split the long paragraph into individual sentences.
# 2. Calculate the similarity score between the query and EACH sentence.
# 3. Sort the sentences by their score (highest to lowest).
#

import spacy

# Load the SpaCy model.
nlp = spacy.load("en_core_web_md")

# --- Function 1: Split Text ---
# SpaCy is smart enough to understand grammar. It knows where a sentence ends
# (looking at periods, exclamation marks, etc.) better than just 'text.split(".")'.
def split_text_into_sentences(text):
    """Split long text into sentences using SpaCy."""
    doc = nlp(text)
    return [sent.text for sent in doc.sents]


# --- Function 2: Calculate Similarity ---
# This function compares the query against every sentence in our list.
def calculate_similarity(reference_sentence, sentences):
    """Calculate similarity between a reference sentence and a list of sentences."""
    similarities = []
    for sentence in sentences: 
        similarity_score = nlp(reference_sentence).similarity(nlp(sentence))
        similarities.append((sentence, similarity_score))
    
    return similarities

def reorder_sentences_by_similarity(similarities): 
    """Render sentences based on similarity scores"""
    return sorted(similarities, key=lambda x: x[1], reverse=True)

# The "Database" text we want to search through.
long_text = """
Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language. 
The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a valuable way. 
Applications of NLP include language translation, sentiment analysis, and chatbots. 
As technology advances, NLP continues to evolve and improve, making it an exciting area of study.
"""

# The "Query" - we want to find sentences similar to this one.
reference_sentence = "NLP enables computers to understand human language."

# Split text
sentences = split_text_into_sentences(long_text)
# find similarities to the reference
similarities = calculate_similarity(reference_sentence, sentences)
# get a list of sentences ordered by their similarity to the reference
ordered_sentences = reorder_sentences_by_similarity(similarities)

print(f"Reference Sentence\n\n{reference_sentence}\n\n")

# Step 4: Display results
print("Sentences ordered by similarity to the reference sentence:")
for sentence, score in ordered_sentences:
    print(f"Similarity: {score:.4f} - Sentence: {sentence}")

