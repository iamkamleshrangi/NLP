from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

#Stemming to the ROOT word
stemmer = PorterStemmer()
for word in example_words:
    token_word = stemmer.stem(word)
    print(token_word)

#Stemming with the sentence 
sentence = 'I am kamlesh and working on my future with living the persent day'
words = word_tokenize(sentence)
for word in words: 
    stem_word = stemmer.stem(word)
    print(stem_word)


