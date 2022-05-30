from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re 

def lower_case(string: str) -> list:
    return string.lower()


def remove_punctuations(string: str) -> list:
    new_str = ''
    for character in string:
        if character not in punctuation:
            new_str += character
    return new_str


def get_tokens(string: str) -> list:
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(string)
    word_tokens = [word for word in word_tokens if word not in stop_words]
    return word_tokens


def lemmatize(words_list: list) -> list:
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in words_list]

## remove urls and numbers 