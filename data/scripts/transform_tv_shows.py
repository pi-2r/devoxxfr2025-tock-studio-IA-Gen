import pandas as pd

# Load the CSV file
df = pd.read_csv('/app/data/documents_csv/TMDB_tv_dataset_v3.csv')

# Set the number of random rows you want to keep
n = 35  # Example value

# Filter only rows that contain "Sci-Fi" in the genres, "netflix" or "hbo" in the networks, and have a vote_average over 8
df = df[df['genres'].str.contains('Sci-Fi', na=False) & df['networks'].str.contains('netflix|hbo', case=False, na=False) & (df['vote_average'] > 8)]
# Randomly select n rows
df_sampled = df.sample(n=n, random_state=42)  # random_state ensures reproducibility

# Keep only the specified columns
columns_to_keep = [
    'name', 'number_of_seasons', 'number_of_episodes', 'original_language',
    'overview', 'first_air_date', 'last_air_date', 'homepage', 'created_by', 'genres', 'networks'
]
df_filtered = df_sampled.loc[:, columns_to_keep]

# Create a new column 'text' based on the template
text_template = (
    "### $name\n\n"
    "* TV Show name : $name\n"
    "* Number of seasons  : $number_of_seasons\n"
    "* Number of episodes : $number_of_episodes\n"
    "* Original language : $original_language\n"
    "* First diffusion / Air date : $first_air_date\n"
    "* Last diffusion / Air date : $last_air_date\n"
    "* Show created by : $created_by\n"
    "* Genres : $genres\n\n"
    "#### Overview of $name\n"
    "$overview\n"
    "\n\n"
)

df_filtered['text'] = df_filtered.apply(lambda row: text_template
    .replace('$name', str(row['name']))
    .replace('$number_of_seasons', str(row['number_of_seasons']))
    .replace('$number_of_episodes', str(row['number_of_episodes']))
    .replace('$original_language', str(row['original_language']))
    .replace('$first_air_date', str(row['first_air_date']))
    .replace('$last_air_date', str(row['last_air_date']))
    .replace('$created_by', str(row['created_by']))
    .replace('$genres', str(row['genres']))
    .replace('$overview', str(row['overview'])), axis=1)

# Rename columns
df_filtered.rename(columns={'homepage': 'source', 'text': 'text', 'name': 'title'}, inplace=True)

# Keep only the specified columns
columns_to_keep = ['source', 'title', 'text']
df_filtered = df_filtered.loc[:, columns_to_keep]

# Save the filtered DataFrame to a CSV file
df_filtered.to_csv('data/documents_csv/filtered_tv_series.csv', index=False, sep='|')
