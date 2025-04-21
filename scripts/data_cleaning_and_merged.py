import pandas as pd
import os
from IPython.display import display

df = pd.read_csv("./data/raw/area_production_yield_data.csv")
print(df.head())
print(df.columns)

# Step 1: Drop duplicates
df = df.drop_duplicates()

# Step 2: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 3: Handle missing values
# Drop rows missing essential identifiers
df = df.dropna(subset=["state_name", "dist_name", "year"])

# Fill NaNs in crop data with 0 (means no cultivation that year)
crop_cols = [col for col in df.columns if any(keyword in col for keyword in ['area', 'production', 'yield'])]
df[crop_cols] = df[crop_cols].fillna(0)

# Step 4: Convert datatypes
df["year"] = df["year"].astype(int)
df["state_name"] = df["state_name"].str.strip().str.lower()
df["dist_name"] = df["dist_name"].str.strip().str.lower()

# Step 5: (Optional) Filter out zero or unrealistic yields
for col in df.columns:
    if "yield" in col:
        df = df[df[col] >= 0]

# Step 6: Reset index
df = df.reset_index(drop=True)

# Done!
print("Preprocessed data shape:", df.shape)
print(df.head(3))

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# List of crops to keep
crops = ['rice', 'wheat', 'groundnut', 'sunflower', 'soyabean',
         'oilseeds', 'sugarcane', 'cotton', 'fruits_and_vegetables', 'potatoes', 'onion']

# Build list of relevant columns (area, production, yield for each crop)
target_cols = ['state_name', 'dist_name', 'year']
for crop in crops:
    for metric in ['area', 'production', 'yield']:
        col_name = f'{crop}_{metric}_(1000_ha)' if metric == 'area' else \
                   f'{crop}_{metric}_(1000_tons)' if metric == 'production' else \
                   f'{crop}_{metric}_(kg_per_ha)'
        # fix for "fruits and vegetables"
        col_name = col_name.replace('fruits_and_vegetables', 'fruits_and_vegetables')
        # check if column exists in df
        matched_cols = [col for col in df.columns if crop in col and metric in col]
        target_cols += matched_cols

# Drop duplicates and clean data
df = df.drop_duplicates()
df = df[target_cols]
df = df.fillna(0)

# Final check
print("Filtered dataset shape:", df.shape)
print(df.head(3))

df_month_rain = pd.read_csv("./data/raw/monthly_rainfall_data.csv")
# print(df_month_rain.head())
print(df_month_rain.columns)
df_month_rain.head()

import pandas as pd

# Load the dataset
df_month_rain = pd.read_csv("./data/raw/monthly_rainfall_data.csv")

# Make a copy for cleaning
df_clean = df_month_rain.copy()

# Step 1: Clean column names
df_clean.columns = (
    df_clean.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('(', '', regex=False)
    .str.replace(')', '', regex=False)
)

# Step 2: Convert rainfall columns to numeric
rainfall_columns = [col for col in df_clean.columns if 'rainfall' in col]
df_clean[rainfall_columns] = df_clean[rainfall_columns].apply(pd.to_numeric, errors='coerce')

# Step 3: Drop rows with missing rainfall data
df_clean.dropna(subset=rainfall_columns, inplace=True)

# Step 4: Feature Engineering - Monsoon average (June to September)
df_clean['monsoon_avg'] = df_clean[[
    'june_rainfall_millimeters',
    'july_rainfall_millimeters',
    'august_rainfall_millimeters',
    'september_rainfall_millimeters'
]].mean(axis=1)

# View cleaned data
df_clean.head()

import pandas as pd

# Load the data
df_normal_rain = pd.read_csv("./data/raw/normal_rainfall_data.csv")  # Update path as needed

# Step 1: Standardize column names
df_normal_rain.columns = (
    df_normal_rain.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('(', '', regex=False)
    .str.replace(')', '', regex=False)
)

# Step 2: Identify rainfall columns
rainfall_cols = [col for col in df_normal_rain.columns if 'rainfall' in col]

# Step 3: Convert rainfall values to numeric
df_normal_rain[rainfall_cols] = df_normal_rain[rainfall_cols].apply(pd.to_numeric, errors='coerce')

# Step 4: Drop rows with missing rainfall values
df_normal_rain.dropna(subset=rainfall_cols, inplace=True)

# Step 5: Compute average monsoon rainfall (June–September)
df_normal_rain['monsoon_avg'] = df_normal_rain[[
    'june_normal_rainfall_millimeters',
    'july_normal_rainfall_millimeters',
    'august_normal_rainfall_millimeters',
    'september_normal_rainfall_millimeters'
]].mean(axis=1)

# Final preview
print(df_normal_rain[['dist_name', 'monsoon_avg']].head())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Define crops
crops = [
    'rice', 'wheat', 'groundnut', 'sunflower', 'soyabean',
    'oilseeds', 'sugarcane', 'cotton', 'fruits_and_vegetables',
    'potatoes', 'onion'
]

# Select relevant columns
target_cols = ['state_name', 'dist_name', 'year']
for crop in crops:
    for suffix in ['area_(1000_ha)', 'production_(1000_tons)', 'yield_(kg_per_ha)']:
        col = f"{crop}_{suffix}"
        if col in df.columns:
            target_cols.append(col)

filtered_df = df[target_cols].drop_duplicates().fillna(0)

# Set style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Melt wide to long format for yield columns
yield_cols = [col for col in filtered_df.columns if '_yield_' in col]
melted_df = filtered_df.melt(
    id_vars=['state_name', 'dist_name', 'year'],
    value_vars=yield_cols,
    var_name='crop_yield_type',
    value_name='yield_kg_per_ha'
)

# Extract crop name from column
melted_df['crop'] = melted_df['crop_yield_type'].str.extract(
    r'(rice|wheat|groundnut|sunflower|soyabean|oilseeds|sugarcane|cotton|fruits_and_vegetables|potatoes|onion)'
)

# Group and average
avg_yield_by_crop_year = melted_df.groupby(['crop', 'year'])['yield_kg_per_ha'].mean().reset_index()

# Plot
plt.figure(figsize=(14, 7))
sns.lineplot(data=avg_yield_by_crop_year, x='year', y='yield_kg_per_ha', hue='crop', marker='o')
plt.title('Average Yield per Crop Over Time (kg/ha)')
plt.xlabel('Year')
plt.ylabel('Yield (kg per ha)')
plt.legend(title='Crop', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Crop categories
yield_cols = [col for col in filtered_df.columns if '_yield_' in col]
area_cols = [col for col in filtered_df.columns if '_area_' in col]
prod_cols = [col for col in filtered_df.columns if '_production_' in col]

# Basic descriptive statistics
print("=== Yield (kg/ha) ===")
display(filtered_df[yield_cols].describe())

print("\n=== Area (1000 ha) ===")
display(filtered_df[area_cols].describe())

print("\n=== Production (1000 tons) ===")
display(filtered_df[prod_cols].describe())

# Step 1: Ensure consistent lowercase and strip spaces
df_clean['dist_name'] = df_clean['dist_name'].str.strip().str.lower()
df_normal_rain['dist_name'] = df_normal_rain['dist_name'].str.strip().str.lower()
filtered_df['dist_name'] = filtered_df['dist_name'].str.strip().str.lower()

# Step 2: Merge crop dataset with monthly rainfall on district name and year
merged_df = pd.merge(
    filtered_df, 
    df_clean[['dist_name', 'year', 'monsoon_avg']], 
    on=['dist_name', 'year'], 
    how='inner'
)

# Step 3: Merge with normal rainfall data on district name
final_df = pd.merge(
    merged_df, 
    df_normal_rain[['dist_name', 'monsoon_avg']].rename(columns={'monsoon_avg': 'normal_monsoon_avg'}), 
    on='dist_name', 
    how='inner'
)

# Step 4: Calculate deviation from normal rainfall
final_df['rainfall_deviation'] = final_df['monsoon_avg'] - final_df['normal_monsoon_avg']

# Final Output Check
print("Final Merged DataFrame Shape:", final_df.shape)
print(final_df[['state_name', 'dist_name', 'year', 'monsoon_avg', 'normal_monsoon_avg', 'rainfall_deviation']].head())

# Create the directory if it doesn't exist
os.makedirs("data/cleaned", exist_ok=True)

# Optional: Save for future
final_df.to_csv("data/cleaned/final_crop_rainfall_merged.csv", index=False)
final_df.to_csv("data/cleaned/merged_dataset.csv", index=False)

import seaborn as sns
import matplotlib.pyplot as plt

# Choose a crop to visualize
crop_yield_col = 'rice_yield_(kg_per_ha)'

# Filter data to remove zeros (if needed)
plot_df = final_df[final_df[crop_yield_col] > 0]

# Scatter plot with regression line
plt.figure(figsize=(10, 6))
sns.regplot(
    data=plot_df,
    x='rainfall_deviation',
    y=crop_yield_col,
    scatter_kws={'alpha':0.5},
    line_kws={'color':'red'}
)
plt.title(f'{crop_yield_col.replace("_", " ").title()} vs Rainfall Deviation')
plt.xlabel('Rainfall Deviation (mm)')
plt.ylabel('Crop Yield (kg/ha)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Get all yield columns
yield_cols = [col for col in final_df.columns if '_yield_' in col]

# Create a correlation DataFrame
cor_df = final_df[yield_cols + ['rainfall_deviation']].corr()

# Show correlation of rainfall deviation with all yields
print(cor_df['rainfall_deviation'].sort_values(ascending=False))

from sklearn.linear_model import LinearRegression
import numpy as np

# Drop NaNs
reg_df = plot_df[[crop_yield_col, 'rainfall_deviation']].dropna()

X = reg_df['rainfall_deviation'].values.reshape(-1, 1)
y = reg_df[crop_yield_col].values

model = LinearRegression()
model.fit(X, y)

print("Regression Coefficient (slope):", model.coef_[0])
print("Intercept:", model.intercept_)
print(f"R-squared: {model.score(X, y):.3f}")

# Standardize key columns
filtered_df['dist_name'] = filtered_df['dist_name'].str.lower().str.strip()
df_clean['dist_name'] = df_clean['dist_name'].str.lower().str.strip()
df_normal_rain['dist_name'] = df_normal_rain['dist_name'].str.lower().str.strip()

filtered_df['year'] = filtered_df['year'].astype(int)
df_clean['year'] = df_clean['year'].astype(int)

merged_df = pd.merge(filtered_df, df_clean[['dist_name', 'year', 'monsoon_avg']],
                     on=['dist_name', 'year'], how='inner')

final_df = pd.merge(merged_df, df_normal_rain[['dist_name', 'monsoon_avg']],
                    on='dist_name', how='inner', suffixes=('_actual', '_normal'))

final_df['rainfall_deviation_%'] = (
    (final_df['monsoon_avg_actual'] - final_df['monsoon_avg_normal']) / final_df['monsoon_avg_normal']
) * 100

def plot_rainfall_vs_yield(df, crop_name):
    # Generate column name
    yield_col = f'{crop_name}_yield_(kg_per_ha)'
    
    # Check if yield column exists
    if yield_col not in df.columns:
        print(f"Yield data for {crop_name} not found!")
        return

    # Filter and drop NA
    crop_df = df[['dist_name', 'year', 'rainfall_deviation_%', yield_col]].dropna()

    # Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=crop_df, x='rainfall_deviation_%', y=yield_col)
    sns.regplot(data=crop_df, x='rainfall_deviation_%', y=yield_col, scatter=False, color='red')
    plt.title(f'Rainfall Deviation vs. {crop_name.capitalize()} Yield')
    plt.xlabel('Rainfall Deviation (%)')
    plt.ylabel(f'{crop_name.capitalize()} Yield (kg/ha)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Correlation
    correlation = crop_df['rainfall_deviation_%'].corr(crop_df[yield_col])
    print(f"Correlation between rainfall deviation and {crop_name} yield: {correlation:.2f}")

crops = [
    'rice', 'wheat', 'groundnut', 'sunflower', 'soyabean',
    'oilseeds', 'sugarcane', 'cotton', 'fruits_and_vegetables',
    'potatoes', 'onion'
]

for crop in crops:
    print(f"\n Analyzing: {crop.upper()}")
    plot_rainfall_vs_yield(final_df, crop)
