from sklearn.feature_extraction.text import CountVectorizer

vocabulary_text = ['The Children of the summers end. Gathered in the dampened grass']
# create the transform
vectorizer = CountVectorizer()
# tokenize and build vocab
vectorizer.fit(vocabulary_text)
# Vocabulary created by above vectorizer
print("Vocabulary learnt", vectorizer.vocabulary_)
# Create vocabulary vector
vector = vectorizer.transform(vocabulary_text)
# Shape of the vector
print("Size of the vector", vector.shape)
# Print the vector in array format
print(vector)

input_text = ['The Children played in the grass. Geronimo']
input_vector = vectorizer.transform(input_text)
print('Vocabulary: ', vectorizer.vocabulary_)
print('Input Vector: ', input_vector)