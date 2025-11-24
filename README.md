# ReadIt
**ReadIt** is a smart book recommendation web application designed to help users discover their next favorite read. By leveraging Natural Language Processing (NLP), ReadIt analyzes book descriptions and genres to provide personalized suggestions based on content similarity rather than just popularity.

## What Is Readit?
ReadIt takes a book title and/or a preferred genre as input. It processes this information against a dataset of over 10,000 books to suggest titles that are semantically similar to the user's input.

Unlike simple filter-based systems, ReadIt uses **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity** to understand the nuances of book descriptions, ensuring that recommendations match the feel and theme of the book you liked.

## Features
- **Smart Title Matching:** Accepts partial or approximate book titles, using bigram similarity to guess the user's intended book even if there are typos.

- **Content-Based Filtering:** Analyzes the actual text of book descriptions (sourced from Goodreads) to find narrative similarities.

- **Genre Filtering:** Allows users to filter results by genre (case insensitive) to refine recommendations.

- **Smart Fallbacks:**
    - Prioritizes genre-matching books but expands to similar genres if necessary.
    - Recommends top-rated books within a specific genre if no specific title is provided.

## Tech Stack
**Frontend**: 
- HTML
- CSS
- JavaScript

**Backend**:
- Python (Flask)

**Machine Learning & NLP Libraries:**
- pandas & numpy (Data Processing)
- re (Regular Expressions)
- nltk (Natural Language Toolkit)
- sklearn (Scikit-learn for TF-IDF and Cosine Similarity)

## Dataset
The application uses the **Best Books 10k Multi-Genre Data** sourced from Kaggle.
- Source: [Link to Dataset](https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data)

- Key Attributes: Title, Author, Description, Genres, Average Rating, and Number of Ratings.

**Data Preprocessing:** 
- **Genre Handling:** The original dataset contained genres listed in a single column. For ReadIt, this was preprocessed to separate genres into distinct columns, considering only the top five genres listed for each book.

- **Weighted Rating:** A custom formula was applied to the dataset to calculate a "Weighted Rating." This calculation accounts for the number of ratings a book has received. This ensures that a book with a single 5-star review does not artificially rank higher than a classic book with thousands of 4.8-star reviews.

