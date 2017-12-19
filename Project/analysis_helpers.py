from sklearn.feature_extraction import DictVectorizer
import pandas as pd
import numpy as np



def get_LDA_vectorizer_features(df):
    vectorizer = DictVectorizer()
    df["artist_terms_weight_"] = df["artist_terms_weight"] * 100
    X_dict = df[["artist_terms", "artist_terms_weight_"]].apply(lambda x: dict(zip(np.array(x["artist_terms"]), np.array(x["artist_terms_weight_"]))), axis=1)
    X = vectorizer.fit_transform(X_dict)
    return vectorizer, X

def show_top_topic(LDA, vectorizer, top):
    components_norm = LDA.components_ / LDA.components_.sum(axis=1)[:, np.newaxis]
    res = sorted(zip(np.max(components_norm, axis=0), np.argmax(components_norm, axis=0), vectorizer.get_feature_names()), reverse=True)
    d = [np.array(res)[np.array(res)[:, 1].astype(int) == i][:top][:, 2].tolist() for i in range(LDA.n_components)]
    p = pd.DataFrame(d)
    return p.set_index(pd.Series(["Topic "+str(i) for i in range(LDA.n_components)]))