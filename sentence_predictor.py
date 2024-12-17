import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
import pickle

class SentencePredictor:
    def __init__(self, model_path, tokenizer_path):
        self.model = load_model(model_path)
        with open(tokenizer_path, 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        self.max_sequence_length = self.model.input_shape[1]

    def predict_next_words(self, seed_text, next_words=3):
        for _ in range(next_words):
            token_list = self.tokenizer.texts_to_sequences([seed_text])[0]
            token_list = pad_sequences([token_list], maxlen=self.max_sequence_length, padding='pre')
            predicted = self.model.predict(token_list, verbose=0)
            predicted_word_index = np.argmax(predicted, axis=-1)[0]
            predicted_word = self.tokenizer.index_word.get(predicted_word_index, '')
            seed_text += ' ' + predicted_word
        return seed_text.split()[-next_words:]

predictor = SentencePredictor('/Users/sanatankhemariya/Desktop/easy-notes-main/sentence_predictor.h5', '/Users/sanatankhemariya/Desktop/easy-notes-main/tokenizer.pkl')

test_sentence = "it is way of"
predicted_words = predictor.predict_next_words(test_sentence, next_words=3)
print(f"Input: {test_sentence}")
print(f"Predicted words: {predicted_words}")