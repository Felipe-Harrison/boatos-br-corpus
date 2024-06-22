import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
import nltk
import numpy as np
import os

import pickle

W2VMODELS_PATH = "./w2v_models/"

class Tokenizador:

    def __init__(self) -> None:
        self.tfIdfVectorizer = TfidfVectorizer()
        self.w2v = None
        
    def tfidf(self,texts: list[list]):
        vectorized_text = self.tfIdfVectorizer.fit_transform(texts)
        return vectorized_text
    
    def word2vec(self,texts: pd.Series, vector_len: int, replace = False):
        # Tokenizar os textos
        texts_tokenized = texts.apply(lambda text: nltk.word_tokenize(text))
        
        path_file = os.path.join(W2VMODELS_PATH,f"w2v_{vector_len}.model")
        #Verificar se ja tem treinado
        if (not replace and os.path.exists(path_file)):
            w2v_model = Word2Vec.load(path_file)
        else:
            # Treinar o modelo Word2Vec
            w2v_model = Word2Vec(texts_tokenized, vector_size=vector_len, window=5, min_count=1, workers=4)
            #w2v_model.save(path_file)
        
        self.w2v = w2v_model
        
        # Vectorizar os textos
        vectorized_text = []
        
        for text in texts_tokenized:
            # Remove palavras que não estão no vocabulário do Word2Vec
            text_vector = [word for word in text if word in w2v_model.wv]
            if not text_vector:
                vectorized_text.append(np.zeros(vector_len))
            else:
                vectorized_text.append(np.mean(w2v_model.wv[text_vector],axis=0))
        
        return vectorized_text
