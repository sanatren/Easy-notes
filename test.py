import pickle

tokenizer_path = '/Users/sanatankhemariya/Desktop/easy-notes-main/tokenizer.pkl'

try:
    with open(tokenizer_path, 'rb') as f:
        tokenizer = pickle.load(f)
    print("Tokenizer loaded successfully.")
    print("Sample words:", list(tokenizer.word_index.keys())[:10])  # Print first 10 words
except Exception as e:
    print(f"Error loading tokenizer: {e}")
