import pandas as pd

# Load the CSV file
df = pd.read_csv('/app/data/documents_csv/imdb_movies.csv')

# Define the number of random rows to keep
n = 1000  # Example value or 5050 with all the movies

# Filter entries without a synopsis or with an empty synopsis
df = df[df['resume'].notna() & (df['resume'] != '')]

# Randomly select n rows
df_sampled = df.sample(n=min(n, len(df)), random_state=42)  # random_state ensures reproducibility

# Keep only the specified columns
columns_to_keep = [
    'title', 'year', 'time', 'resume', 'metascore', 'url'
]

df_filtered = df_sampled.loc[:, columns_to_keep]

# Create a new 'text' column based on the template
text_template = (
    "### $title\n\n"
    "* Movie title: $title\n"
    "* Release year: $year\n"
    "* Duration: $time\n"
    "* Metascore: $metascore\n\n"
    "#### Synopsis of $title\n"
    "$resume\n"
    "\n\n"
)

df_filtered['text'] = df_filtered.apply(lambda row: text_template
                                        .replace('$title', str(row['title']))
                                        .replace('$year', str(row['year']))
                                        .replace('$time', str(row['time']) if pd.notna(row['time']) else "Not specified")
                                        .replace('$metascore', str(row['metascore']) if pd.notna(row['metascore']) else "Not available")
                                        .replace('$resume', str(row['resume'])), axis=1)

# Rename columns
df_filtered.rename(columns={'url': 'source', 'text': 'text', 'title': 'title'}, inplace=True)

# Keep only the specified columns for the final result
final_columns = ['source', 'title', 'text']
df_filtered = df_filtered.loc[:, final_columns]

# Check if the DataFrame is not empty before saving
if not df_filtered.empty:
    # Save the filtered DataFrame to a CSV file
    df_filtered.to_csv('data/documents_csv/filtered_imdb_movies.csv', index=False, sep='|')
    print(f"CSV file created with {len(df_filtered)} movies.")
else:
    print("No movies with a synopsis were found. No CSV file was created.")
