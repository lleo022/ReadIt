# ReadIt

## What Is Readit?
ReadIt is a book recommendation webapp. It takes in a book title and/or genre as input and using that information, suggests possible books that the user may enjoy. It uses Natural Language Processing (NLP) techniques such as TF-IDF and cosine similarity to suggest similar books from a large dataset sourced from Kaggle. 

## Features
- Accepts partial or approximate book titles using bigram similarity to guess the user's meaning
- Filters by genre (case insensitive)
- Analyzes books based on the similarity of their descriptions (based on data from Goodreads)
- Recommends top-rated books by genre if no title is provided
- Prioritizes genre-matching books, but expands to similar genres if needed

## Tech Stack
- Frontend: HTML, CSS
- Backend: Python (Flask)
- Libraries
  - pandas
  - numpy
  - re
  - nltk
  - sklearn

## Dataset
[Link to Dataset Used](https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data)

Columns: Title, Author, Description, Genre1, ..., Genre 5, Avg Rating, Num Ratings, Weighted Rating

The original dataset contained all the genres as one list in a column, but I narrowed it down to have one genre per column and only consider the top five genres listed. 
