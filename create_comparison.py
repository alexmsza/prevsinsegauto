import pandas as pd

# Read original data
path_file = 'https://raw.githubusercontent.com/MathMachado/DSWP/refs/heads/master/Dataframes/Car_Insurance_Claim.csv'
df_original = pd.read_csv(path_file)

# Read cleaned data
df_cleaned = pd.read_csv('cleaned_data.csv')

# Create a comparison of the first 5 rows
original_head = df_original.head().to_html(classes='table table-striped', index=False)
cleaned_head = df_cleaned.head().to_html(classes='table table-striped', index=False)

# Create the html content
html_content = f"""
<div class="card">
    <h2>Dados Originais</h2>
    {original_head}
</div>
<div class="card">
    <h2>Dados Alterados</h2>
    {cleaned_head}
</div>
"""

# Save the html content to a file
with open('comparison.html', 'w') as f:
    f.write(html_content)
