import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
df = pd.read_csv('netflix_titles-task2.csv')
print(df.head())
print("\nSummary Statistics:")
print(df.describe(include='all'))
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
print("\nNumeric Columns:", numeric_cols)
df[numeric_cols].hist(figsize=(12, 6), bins=30)
plt.tight_layout()
plt.show()
for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()
plt.figure(figsize=(10, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
if len(numeric_cols) <= 5:
    sns.pairplot(df[numeric_cols].dropna())
    plt.show()
plt.figure(figsize=(12, 6))
top_years = df['release_year'].value_counts().index[:20]
sns.countplot(data=df, x='release_year', order=top_years)
plt.xticks(rotation=45)
plt.title('Count of Netflix Titles by Release Year')
plt.show()
sns.countplot(data=df, x='type')
plt.title('Content Type Distribution')
plt.show()
