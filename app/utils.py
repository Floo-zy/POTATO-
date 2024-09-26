import polars as pl
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Load and process data
def load_and_process_data():
    # Fetch file path from environment or default to 'data' folder
    file_path = os.getenv("DATA_FILE_PATH", "data/tweets_data.tsv")

    df = pl.read_csv(
        file_path, separator="\t", ignore_errors=True, try_parse_dates=True
    )

    # Convert timestamp and extract hour
    df = df.with_columns(pl.col("created_at").dt.hour().alias("hour"))

    return df


# Function to query data
def search_data(df, term):
    # Ensure the column names are valid
    if "text" not in df.columns or "created_at" not in df.columns:
        raise ValueError("The required columns do not exist in the DataFrame.")

    # Filter for tweets that contain the search term
    filtered_df = df.filter(pl.col("text").str.contains(term.lower()))

    # Tweets per day
    tweets_per_day = filtered_df.group_by(
        pl.col("created_at").dt.date().alias("date")
    ).agg(
        pl.col("id").count().alias("tweet_count")  # Adjust column name
    )

    # Unique users
    unique_users = filtered_df["author_id"].unique().len()

    # Average likes
    avg_likes = filtered_df["like_count"].mean()

    # Place IDs (locations)
    place_ids = filtered_df["place_id"].unique()

    # Times of day (Remove redundant aliasing)
    times_of_day = filtered_df.group_by(
        pl.col("created_at").dt.hour().alias("hour")
    ).agg(
        pl.col("id").count().alias("tweet_count")  # Adjust column name
    )

    # User with the most tweets
    most_active_user = (
        filtered_df.group_by("author_handle")
        .agg(pl.col("author_handle").count().alias("count"))
        .sort("count")
        .select("author_handle")[0, 0]
    )

    # Return relevant data
    return {
        "tweets_per_day": tweets_per_day.to_dict(as_series=False),
        "unique_users": unique_users,
        "avg_likes": avg_likes,
        "place_ids": place_ids.to_list(),
        "times_of_day": times_of_day.to_dict(as_series=False),
        "most_active_user": most_active_user,
    }
