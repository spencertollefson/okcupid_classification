def f(x):
    return 2 + x

import numpy as np
import joblib

pipeline = joblib.load('../models/flask_SVM.pkl')

example = {

    'age': 28, # int
    'Sex': ,
    'sex_f': ,
    'sex_m': ,
    'signs_fun_fun to think about': ,
    'signs_unimportant_but it': ,
    'signs_important_matters a lot',
       'religion_unserious_not too serious', 'religion_laughing_laughing',
       'religion_somewhat_somewhat', 'religion_serious_very serious',
       'orientation_bisexual', 'orientation_gay', 'orientation_straight',
       'drinks_desperately', 'drinks_not at all', 'drinks_often',
       'drinks_rarely', 'drinks_socially', 'drinks_very often', 'smokes_no',
       'smokes_sometimes', 'smokes_trying to quit', 'smokes_when drinking',
       'smokes_yes', 'drugs_never', 'drugs_often', 'drugs_sometimes',
       'religion_name_agnosticism', 'religion_name_atheism',
       'religion_name_buddhism', 'religion_name_catholicism',
       'religion_name_christianity', 'religion_name_hinduism',
       'religion_name_islam', 'religion_name_judaism', 'religion_name_other']



  'Pclass': 3,  # int
  'Sex': 'M',    # M or F
  'Age': 22,    # int
  'SibSp': 1,  # int
  'Parch': 0,  # int
  'Fare': 7.25    # float
}

def make_prediction(features):
    X = np.array([features['Pclass'], int(features['Sex'] == 'M'), features['Age'],
                  features['SibSp'], features['Parch'], features['Fare']]).reshape(1,-1)
    prob_survived = pipeline.predict_proba(X)[0, 1]

    result = {
        'prediction': int(prob_survived > 0.5),
        'prob_survived': prob_survived
    }
    return result

if __name__ == '__main__':
    print(make_prediction(example))
