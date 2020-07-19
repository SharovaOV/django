from sklearn.externals import joblib
import numpy as np
import os

class model_learn:
    rating=0
    positive=False
    def __init__(self, text_val):
        self.model_wordbag= joblib.load('models/wordbag.pkl')
        self.model_rating=joblib.load('models/ratingmodel.pkl')
        self.model_positiv = joblib.load('models/positivmodel.pkl')
        text_val=self.model_wordbag.transform([text_val])
        self.rating = np.argmax(self.model_rating.predict(text_val))+1
        self.positive = round(self.model_positiv.predict(text_val)[0][0])



