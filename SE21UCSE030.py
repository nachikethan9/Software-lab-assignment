
import nltk
nltk.download('omw-1.4')
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer

# Sample words
words = ['running', 'painting', 'walking', 'dressing', 'likely', 'children', 'whom', 'good', 'ate', 'fishing']

# Initialize stemmers
porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer(language='english')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Stemming
print("Stemming:")
print("Original Word\tPorter Stemmer\tLancaster Stemmer\tSnowball Stemmer")
for word in words:
    print(f"{word}\t\t{porter.stem(word)}\t\t{lancaster.stem(word)}\t\t{snowball.stem(word)}")

# Lemmatization
print("\nLemmatization:")
print("Original Word\tLemmatized Word")
for word in words:
    print(f"{word}\t\t{lemmatizer.lemmatize(word)}")
