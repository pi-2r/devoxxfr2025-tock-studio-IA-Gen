import pandas as pd

# Load the CSV file
df = pd.read_csv('/app/data/documents_csv/horror_movies.csv')

# Set the number of random rows you want to keep
n = 15  # Example value

# Randomly select n rows
df_sampled = df.sample(n=n, random_state=42)  # random_state ensures reproducibility

# Keep only the specified columns
columns_to_keep = ['id', 'title', 'overview']
df_filtered = df_sampled.loc[:, columns_to_keep]

# Map id column to URLs
df_filtered['id'] = df_filtered['id'].map(lambda x: f"https://www.themoviedb.org/movie/{x}")

# Rename columns
df_filtered.rename(columns={'id': 'source', 'overview': 'text', 'title': 'title'}, inplace=True)

# Save the filtered DataFrame to a CSV file
df_filtered.to_csv('data/documents_csv/filtered_horror_movies.csv', index=False, sep='|')
