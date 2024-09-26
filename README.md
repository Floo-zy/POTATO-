# POTATO: The Panel-based Open Term-level Aggregate Twitter Observatory

Welcome to the POTATO project! This prototype web application allows users to analyze tweets from the Lazer Lab’s Twitter Panel. With over a million real U.S. voters linked to their Twitter accounts, POTATO provides insights into various topics by allowing users to search for specific terms within tweets.

## Project Overview

The main goals of this project are:

- Ingest and process tweet data from provided TSV files.
- Implement a RESTful API using Flask for querying the tweet data.
- Create a user-friendly frontend with Streamlit to display the search results.

## Features

- Search for tweets containing a specific term.
- View aggregate data such as:
  - Number of tweets per day
  - Unique users tweeting about the term
  - Average likes on tweets containing the term
  - Locations of tweets (place IDs)
  - Times of day tweets were posted
  - The most active user for the searched term

## Folder Structure

Here's a quick overview of the folder structure:

```
POTATO/
│
├── app/
│   ├── app.py               # Main Flask application file 
│   ├── utils.py             # Data processing and querying functions 
│   └── .env                 # Environment variables configuration 
│
├── data/
│   ├── small_tweets_data.tsv      # Smaller dataset for testing 
│   └── tweets_data.tsv            # Main dataset 
│
├── streamlit_app/
│   └── app.py               # Streamlit application file 
│
├── tests/
│   └── test_app.py          # Unit tests for Flask app 
│
├── requirements.txt          # Project dependencies 
└── README.md                 # Project documentation
```

## Installation

1. **Clone the repository**:

   ```bash
    git clone <repository-url>
    cd <directory_name>
    ```
2. **Create a virtualenv**
    ```py
    py -m venv .venv
    ```

3. **Install requirements.txt**

    ```py
    pip install -r requirements.txt 
    ```

4. **Run the following commands**
    ```py
    python app/app.py
    streamlit run streamlit_app/app.py
    ```

5. **To run tests**
    ```py
    pytest
    ```
