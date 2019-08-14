from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer

input_text = "Hi, I am sam. what about you?"

print("\nSentence tokenizer:")
print(sent_tokenize(input_text))


print("\nword tokenizer:")
print(word_tokenize(input_text))

print("\nword punct tokenizer:")
print(WordPunctTokenizer().tokenize(input_text))
