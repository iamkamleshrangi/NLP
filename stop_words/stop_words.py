from  nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('stopwords')

sentence = 'I am kamlesh and working on my future with living the persent day'

stop_word = set(stopwords.words('english'))
filtered = []

#Easy 
words = word_tokenize(sentence)
for word in words:
    if word not in stop_word:
        filtered.append(word)
print(filtered)

#One Liner
filtered_sentence = [word for word in words if word not in stop_word]
print(filtered)

