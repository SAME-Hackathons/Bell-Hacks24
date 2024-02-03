from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import string
import nltk
import pandas as pd
nltk.download('punkt')
nltk.download('stopwords')

def remove_punctuation(text):
  cleaned = ''.join([word for word in text if word not in string.punctuation])
  return cleaned

def tokenizer(text):
  #remove uupercase
  lower_text = text.lower()
  #Tokenize
  tokenized_text = nltk.word_tokenize(lower_text)
  return tokenized_text


def remove_stopwords(text):
  stopwords = nltk.corpus.stopwords.words('english')
  without_stopwords = [word for word in text if word not in stopwords]
  return  without_stopwords

def remove_shorttokens(text):
  without_shorttokens = [word for word in text if len(word)>2]
  return  without_shorttokens

def stemming(text):
  stemmer = nltk.PorterStemmer()
  stemmed_words = [stemmer.stem(word) for word in text]
  return stemmed_words

class RemovePunctuationTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, text_column):
        self.text_column = text_column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        X_[self.text_column] = X_[self.text_column].apply(lambda x: remove_punctuation(x))
        return X_
    
class TokenizerTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, text_column):
        self.text_column = text_column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        X_[self.text_column] = X_[self.text_column].apply(lambda x: tokenizer(x))
        return X_
    
class RemoveStopwordsTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, text_column):
        self.text_column = text_column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        X_[self.text_column] = X_[self.text_column].apply(lambda x: remove_stopwords(x))
        return X_
    
class RemoveShortTokensTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, text_column):
        self.text_column = text_column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        X_[self.text_column] = X_[self.text_column].apply(lambda x: remove_shorttokens(x))
        return X_

class StemmingTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, text_column):
        self.text_column = text_column
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        X_ = X.copy()
        X_[self.text_column] = X_[self.text_column].apply(lambda x: stemming(x))
        return X_

class  ReturnStringTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, text_column):
        self.text_column = text_column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        X_[self.text_column] = X_[self.text_column].apply(lambda x: " ".join(x))
        X_ = pd.Series(X_[self.text_column])
        return X_
    
