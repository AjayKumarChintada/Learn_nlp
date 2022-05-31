from string import punctuation
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re


def lower_case(string: str) -> list:
    return string.lower()


def remove_punctuations(string: str) -> list:
    string = string.replace('.com', '')
    new_str = ''
    for character in string:
        if character not in punctuation:
            new_str += character
    return new_str


def get_tokens(string: str) -> list:
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(string)
    word_tokens = [word for word in word_tokens if word not in stop_words]
    word_tokens = [i for i in word_tokens if i]

    return word_tokens


def lemmatize(words_list: list) -> list:
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in words_list]

## remove urls and numbers


def remove_urls(text):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', text)
    rem_url = re.sub(r'http\S+', '', cleantext)
    text = re.sub('[0-9]+', '', rem_url)

    return text


def process_text(msg: string):

    msg = lower_case(msg)
    msg = remove_punctuations(msg)
    msg = remove_urls(msg)
    msg_words = get_tokens(msg)
    msg_words = lemmatize(msg_words)
    return msg_words

