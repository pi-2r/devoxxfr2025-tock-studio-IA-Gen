import pandas as pd

# Load the CSV file
df = pd.read_csv('/app/data/documents_csv/imdb_movies.csv')

# Set the number of random rows you want to keep
n = 20  # Example value or 5050 with all the movies

# Randomly select n rows
df_sampled = df.sample(n=n, random_state=42)  # random_state ensures reproducibility

# Keep only the specified columns
columns_to_keep = ['url', 'title', 'resume' ]
df_filtered = df_sampled[columns_to_keep].copy()

# Rename columns
df_filtered.rename(columns={'url': 'source', 'title': 'title', 'resume': 'text'}, inplace=True)

# Save the filtered DataFrame to a CSV file, excluding rows with empty 'resume'
df_filtered[df_filtered['text'].notna()].to_csv('data/documents_csv/filtered_imdb_movies.csv', index=False, sep='|')
