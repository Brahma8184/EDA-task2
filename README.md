Exploratory Data Analysis (EDA) Netflix dataset

 Netflix EDA Summary
1.Summary Statistics
- Used `.describe()` to get count, unique values, most frequent values, etc.
- Found that most content is **Movies**, and each title is unique.
 2. Histograms & Boxplots
- Plotted histograms to see the distribution of numeric data (like `release_year`).
- Boxplots helped identify **outliers** or skewed values in numeric columns.
3. Correlation Matrix
- Heatmap showed **low correlation** between numeric features (like `release_year` and `show_id`), which is expected since most data is **categorical**.

 4. **Trends & Patterns
- Most content is Movies (around 70%).
- Number of titles released spiked in recent years (especially 2018–2020).
- Countries like **USA**, **India**, and **UK** contribute the most content.

5. Basic Inferences
- Netflix content is mostly recent.
- There are some duplicate descriptions and missing values in `country`, `cast`, etc.
- Boxplots reveal that some numeric values may need further cleaning or categorization.
