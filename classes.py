class RemovePunctuationTransformer(BaseEstimator, TransformerMixin):
    def init(self, textcolumn):
        self.text_column = text_column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X[self.text_column] = X[self.textcolumn].apply(lambda x: remove_punctuation(x))
        return X
class TokenizerTransformer(BaseEstimator, TransformerMixin):
    def init(self, textcolumn):
        self.text_column = text_column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X[self.text_column] = X[self.textcolumn].apply(lambda x: tokenizer(x))
        return X
class RemoveStopwordsTransformer(BaseEstimator, TransformerMixin):
    def init(self, textcolumn):
        self.text_column = text_column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X[self.text_column] = X[self.textcolumn].apply(lambda x: remove_stopwords(x))
        return X
class RemoveShortTokensTransformer(BaseEstimator, TransformerMixin):
    def init(self, textcolumn):
        self.text_column = text_column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X[self.text_column] = X[self.textcolumn].apply(lambda x: remove_shorttokens(x))
        return X
class StemmingTransformer(BaseEstimator, TransformerMixin):
    def init(self, textcolumn):
        self.text_column = text_column
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        X = X.copy()
        X[self.text_column] = X[self.textcolumn].apply(lambda x: stemming(x))
        return X
class  ReturnStringTransformer(BaseEstimator, TransformerMixin):
    def init(self, textcolumn):
        self.text_column = text_column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X[self.text_column] = X[self.textcolumn].apply(lambda x: " ".join(x))
        X = pd.Series(X[self.text_column])
        return X