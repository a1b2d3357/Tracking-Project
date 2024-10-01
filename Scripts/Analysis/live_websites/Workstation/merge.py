import pandas as pd

csv_with_multiple_columns = 'pixelHistory.csv'  # Wayback CSV
pixel_live_csv = 'pixelHistoryLive.csv'  # Live CSV

df1 = pd.read_csv(csv_with_multiple_columns)
df2 = pd.read_csv(pixel_live_csv)

# Merge the two DataFrames on the 'website' column, keeping all rows from df1
# If there's no match in df2, it will place NaN (which we'll replace with None later)
df_merged = pd.merge(df1, df2[['Website', 'Pixel IDs']], left_on='website', right_on='Website', how='left')

# Drop the duplicate 'Website' column since we already have 'website'
df_merged = df_merged.drop(columns=['Website'])

# Rename 'Pixel IDs' column to 'live' for the output
df_merged = df_merged.rename(columns={'Pixel IDs': 'live'})

# Replace NaN values in 'live' column with None
df_merged['live'] = df_merged['live'].apply(lambda x: None if pd.isna(x) else x)

output_csv = 'pixelHistoryComplete.csv'
df_merged.to_csv(output_csv, index=False)

print(f"New CSV with 'live' column saved as {output_csv}")
