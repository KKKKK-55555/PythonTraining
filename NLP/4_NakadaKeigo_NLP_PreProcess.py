import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


stop_words = set(stopwords.words('English'))

tag_dict_nltk = {
    'J': wordnet.ADJ,
    'N': wordnet.NOUN,
    'V': wordnet.VERB,
    'R': wordnet.ADV,
}

lemmatizer = WordNetLemmatizer()


def remove_list_blank(target_list):
    target_list = list(filter(lambda word: word != '', target_list))
    return target_list


def normalize_word(word):
    word = word.lower()
    word = re.sub(r'[^a-zA-Z¥s]', '', word)
    return word


def remove_stepwords(word):
    return word if not word in stop_words else ""


def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    return tag_dict_nltk.get(tag, wordnet.NOUN)


def lemmatize_word(word):
    return lemmatizer.lemmatize(word, get_wordnet_pos(word))


if __name__ == '__main__':
    
    text = "Natural language processing is fascinating."
    
    tokenized_words = word_tokenize(text)
    print(f'Tokenized        : tokenized_words')
    
    normalized_words = [normalize_word(word_token) for word_token in tokenized_words]
    normalized_words = remove_list_blank(normalized_words)
    print(f'Normalized       : {normalized_words}')

    removed_words = [remove_stepwords(word) for word in normalized_words]
    removed_words = remove_list_blank(removed_words)
    print(f'Removed Stopwords: {removed_words}')

    lemmatized_words = [lemmatize_word(word) for word in removed_words]
    print(f'Lemmatized       : //lemmatized_words')
