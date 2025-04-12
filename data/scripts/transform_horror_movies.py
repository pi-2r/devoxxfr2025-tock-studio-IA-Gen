import pandas as pd

# Load the CSV file
df = pd.read_csv('/app/data/documents_csv/horror_movies.csv')

# Define the number of random rows to keep
n = 35  # Example value

# Filter only horror movies
df = df[df['genre_names'].str.contains('Horror', na=False)]

# Randomly select n rows
df_sampled = df.sample(n=n, random_state=42)  # random_state ensures reproducibility

# Keep only the specified columns
columns_to_keep = [
    'title', 'original_title', 'runtime', 'original_language',
    'overview', 'release_date', 'tagline', 'genre_names', 'budget', 'revenue'
]

df_filtered = df_sampled.loc[:, columns_to_keep]

# Create a new 'text' column based on the template
text_template = (
    "### $title\n\n"
    "* Movie title: $title\n"
    "* Original title: $original_title\n"
    "* Runtime (minutes): $runtime\n"
    "* Original language: $original_language\n"
    "* Release date: $release_date\n"
    "* Tagline: $tagline\n"
    "* Genres: $genre_names\n"
    "* Budget: $budget\n"
    "* Revenue: $revenue\n\n"
    "#### Overview of $title\n"
    "$overview\n"
    "\n\n"
)

df_filtered['text'] = df_filtered.apply(lambda row: text_template
                                        .replace('$title', str(row['title']))
                                        .replace('$original_title', str(row['original_title']))
                                        .replace('$runtime', str(row['runtime']))
                                        .replace('$original_language', str(row['original_language']))
                                        .replace('$release_date', str(row['release_date']))
                                        .replace('$tagline', str(row['tagline']))
                                        .replace('$genre_names', str(row['genre_names']))
                                        .replace('$budget', str(row['budget']))
                                        .replace('$revenue', str(row['revenue']))
                                        .replace('$overview', str(row['overview'])), axis=1)

# Rename columns
df_filtered.rename(columns={'title': 'title', 'text': 'text'}, inplace=True)

# Add a source column (as it's required in the final format)
df_filtered['source'] = df_filtered.apply(lambda row: f"https://www.themoviedb.org/movie/{row.name}", axis=1)

# Keep only the specified columns for the final format
columns_to_keep = ['source', 'title', 'text']
df_filtered = df_filtered.loc[:, columns_to_keep]

# Save the filtered DataFrame to a CSV file
df_filtered.to_csv('data/documents_csv/filtered_horror_movies.csv', index=False, sep='|')
