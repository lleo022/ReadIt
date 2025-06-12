import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ------------ Book Recommendation Code ------------ #
df = pd.read_pickle("data/books.pkl")

def recommend(title="", genre=""):
    # important variables
    GENRE_SIMILARITY_THRESHOLD = 0.2
    FULL_SIMILARITY_THRESHOLD = 0.1
    MAX_RECOMMENDATIONS = 5
    # normalize user inputs
    title = title.lower()
    genre = genre.lower()
    
    # Filter by genre, else use all the data
    if genre.strip():
        temp = df[
            (df['Genre1'].str.lower() == genre) |
            (df['Genre2'].str.lower() == genre) |
            (df['Genre3'].str.lower() == genre) |
            (df['Genre4'].str.lower() == genre) |
            (df['Genre5'].str.lower() == genre)
        ].reset_index(drop=True)
    else:
        temp = df.copy()

    # Recommend top 5 books by weighted rating if title is empty
    if not title.strip():
        rec = temp.sort_values(by='Weighted Rating', ascending=False).head(5)
        return rec.to_dict(orient="records")

    matchTitle = None
    genreTitles = temp["Title"].str.lower()
    # Exact match in genre-filtered data
    if title in genreTitles.values:
        matchTitle = temp.loc[genreTitles == title, 'Title'].values[0]
    # Bigram match for similar titles in genre-filtered data
    elif not temp.empty:
        print(title)
        similarTitle = TfidfVectorizer(ngram_range=(2, 2), stop_words='english')
        titleMatrix = similarTitle.fit_transform(temp['Title'])
        userVec = similarTitle.transform([title])
        simScores = cosine_similarity(userVec, titleMatrix).flatten()
        bestID = np.argmax(simScores)
        if simScores[bestID] > GENRE_SIMILARITY_THRESHOLD: # prevents clearly wrong matches
            matchTitle = temp.iloc[bestID]['Title']
            # Assuming you meant {matchTitle}
    # if genre-filtered match fails, expand search to larger dataset
    if matchTitle is None:
        allTitles = df['Title'].str.lower()
        # Exact title match
        if title in allTitles.values:
            matchTitle = df.loc[allTitles[allTitles == title].index[0], 'Title']
        # Bigram match for similar titles 
        else:
            similarTitle = TfidfVectorizer(ngram_range=(2, 2), stop_words='english')
            titleMatrix = similarTitle.fit_transform(df['Title'])
            userVec = similarTitle.transform([title])
            simScores = cosine_similarity(userVec, titleMatrix).flatten()
            bestID = np.argmax(simScores)
            if simScores[bestID] > FULL_SIMILARITY_THRESHOLD:
                matchTitle = df.iloc[bestID]['Title']
                # Assuming you meant {matchTitle}
                # get genres of matchTitle to apply to new temp
                matchedRow = df[df['Title'] == matchTitle].iloc[0]
                matchedGenres = [matchedRow[f'Genre{i}'] for i in range(1, 6)]
                temp = df[df[[f'Genre{i}' for i in range(1, 6)]].isin(matchedGenres).any(axis=1)].reset_index(drop=True)
            else:
                return None
  
    # use trigrams to analyze book similarity from description
    indices = pd.Series(temp.index, index=temp['Title'])
    tf = TfidfVectorizer(ngram_range=(3, 3), stop_words='english')
    tfidf_matrix = tf.fit_transform(temp['Description'])
    sg = cosine_similarity(tfidf_matrix, tfidf_matrix)
    idx = indices[matchTitle]
    sig = list(enumerate(sg[idx]))
    sig = [x for x in sig if x[0] != idx]  # remove self-match explicitly
    sig = sorted(sig, key=lambda x: x[1], reverse=True)[:MAX_RECOMMENDATIONS]
    book_indices = [i[0] for i in sig]
    rec = temp.iloc[book_indices]
    
    return rec.to_dict(orient="records")

