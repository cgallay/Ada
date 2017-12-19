from sklearn.feature_extraction import DictVectorizer
import pandas as pd
import numpy as np



def get_LDA_vectorizer_features(df):
    vectorizer = DictVectorizer()
    X_dict = get_LDA_features_dict(df)
    X = vectorizer.fit_transform(X_dict)
    return vectorizer, X

def get_LDA_features_dict(df):
    df["artist_terms_weight_"] = df["artist_terms_weight"] * 100
    X_dict = df[["artist_terms", "artist_terms_weight_"]].apply(lambda x: dict(zip(np.array(x["artist_terms"]), np.array(x["artist_terms_weight_"]))), axis=1)
    return X_dict

def get_LDA_features(df, vectorizer):
    X_dict = get_LDA_features_dict(df)
    return vectorizer.transform(X_dict)
    
def show_top_topic(LDA, vectorizer, top):
    components_norm = LDA.components_ / LDA.components_.sum(axis=1)[:, np.newaxis]
    res = sorted(zip(np.max(components_norm, axis=0), np.argmax(components_norm, axis=0), vectorizer.get_feature_names()), reverse=True)
    d = [np.array(res)[np.array(res)[:, 1].astype(int) == i][:top][:, 2].tolist() for i in range(LDA.n_components)]
    p = pd.DataFrame(d)
    return p.set_index(pd.Series(["Topic "+str(i) for i in range(LDA.n_components)]))

features = ['X_mean', 'X_std', 'X_skew', 'X_kurtosis', 'X_median']
def get_features(df):
    """ Return features based on the content of the song
    """
    all = []
    for f in features:
        all.append(np.array(df[f].tolist()))
        
    return np.concatenate(all, axis=1)