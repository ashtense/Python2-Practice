import os
import time
import numpy as np
import tensorflow as tf

def split_input_target(sequence):
    input_text = sequence[:-1]
    target_text = sequence[1:]
    return input_text, target_text

# File on which we train the RNN 
path_to_file = '/Users/ashwani/GitRepositories/Python2-Practice/ML/shakespeare.txt'

#Open the file and read it
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
print('Length of text: {} characters'.format(len(text)))

#Lets open the first 250 characters of the text
# print(text[:250])

# The unique characters in the file using set function
vocab = sorted(set(text))
# Length of the vocabulary generated in above step
print(f"{len(vocab)} unique characters")
# Here is how the full vocabulary looks like
# print(vocab)

# Vector Map of the whole vocabulary, type: tensor of ints
vocab_to_vector_map = tf.keras.layers.StringLookup(
    vocabulary=list(vocab), mask_token=None
)

# Unicode tensor from the input text and search in tensor vocabulary
input_chars = tf.strings.unicode_split("fff", input_encoding="UTF-8")
input_vector_ids = vocab_to_vector_map(input_chars) # Search in the tensor vocubulary
# print("vector ids of input text: ", input_vector_ids)

# To get input characters from the vector ids - reverse lookup
vector_to_vocab_map = tf.keras.layers.StringLookup(
    vocabulary=vocab_to_vector_map.get_vocabulary(),invert=True, mask_token=None
)

# From the reverse vector vocabular we only pass the vector ids of input/generated text
# print("characters reversed from vector list", vector_to_vocab_map(input_vector_ids))

# Now the vocabular to vector mapping and reverse mapping is also created. Now we start training the model
# Get vector ids of all the characters in training text
training_vectors = vocab_to_vector_map(tf.strings.unicode_split(text, "UTF-8"))
# print("Vector ids of all training text: ", training_vectors)

# Lets create a training dataset from the vector ids
# We will use the tf.data.Dataset.from_tensor_slices function to convert the vector ids into a dataset
vector_dataset = tf.data.Dataset.from_tensor_slices(training_vectors)

# Lets print the first 5 characters from the dataset
for vector in vector_dataset.take(5):
    print("{} -> {}".format(vector, vector_to_vocab_map(vector)))

# This dataset has 1 character elements. Lets convert them into sequences.
seq_length = 100
examples_per_epoch = len(text) // (seq_length + 1)

# The batch method lets us easily convert these individual characters to sequences of the desired size.
vector_sequences = vector_dataset.batch(6, drop_remainder=True)
# Lets take a look inside the vector sequences
for seq in vector_sequences.take(1):
    print(seq)
    for vector in seq:
        print("{} -> {}".format(vector, vector_to_vocab_map(vector)))

input_text, target_text = split_input_target('Tensorflow')
print(input_text)
print(target_text)