import re
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\temp\rus_hh_ru.csv', sep=',')
df = df.drop_duplicates()

# Define regular expressions for each keyword
sql_regex = re.compile(r'sql', re.IGNORECASE)
php_regex = re.compile(r'php', re.IGNORECASE)
java_regex = re.compile(r'java', re.IGNORECASE)
csharp_regex = re.compile(r'c\#|с\#', re.IGNORECASE)
cpp_regex = re.compile(r'c\+\+|с\+\+', re.IGNORECASE)
oneC_regex = re.compile(r'1c|1с', re.IGNORECASE)
packer_regex = re.compile(r'фасовщик', re.IGNORECASE)
javascript_regex = re.compile(r'javascript', re.IGNORECASE)
javaspring_regex = re.compile(r'spring', re.IGNORECASE)
erp_regex = re.compile(r'erp', re.IGNORECASE)
flutter_regex = re.compile(r'flutter', re.IGNORECASE)
bi_regex = re.compile(r' bi ', re.IGNORECASE)
kotlin_regex = re.compile(r'kotlin', re.IGNORECASE)
typescript_regex = re.compile(r'typescript', re.IGNORECASE)
html_regex = re.compile(r'html', re.IGNORECASE)
wordpress_regex = re.compile(r'wordpress', re.IGNORECASE)
python_regex = re.compile(r'python', re.IGNORECASE)
ruby_regex = re.compile(r'ruby', re.IGNORECASE)
rust_regex = re.compile(r'rust', re.IGNORECASE)


# Apply replacements using the regular expressions
for i in range(df.shape[0]):
    df.loc[df['Job'].astype(str).str.contains(sql_regex) |
           df['Description'].astype(str).str.contains(sql_regex), 'Job'] = 'SQL'
    df.loc[df['Job'].astype(str).str.contains(php_regex) |
           df['Description'].astype(str).str.contains(php_regex), 'Job'] = 'PHP'
    df.loc[df['Job'].astype(str).str.contains(java_regex) |
           df['Description'].astype(str).str.contains(java_regex) |
           df['Job'].astype(str).str.contains(javaspring_regex), 'Job'] = 'Java'
    df.loc[df['Job'].astype(str).str.contains(csharp_regex) |
           df['Description'].astype(str).str.contains(csharp_regex), 'Job'] = 'C#'
    df.loc[df['Job'].astype(str).str.contains(cpp_regex) |
           df['Description'].astype(str).str.contains(cpp_regex), 'Job'] = 'C++'
    df.loc[df['Job'].astype(str).str.contains(oneC_regex) |
           df['Description'].astype(str).str.contains(oneC_regex), 'Job'] = '1C'
    df.loc[df['Job'].astype(str).str.contains(javascript_regex) |
           df['Description'].astype(str).str.contains(javascript_regex), 'Job'] = 'JavaScript'
    df.loc[df['Job'].astype(str).str.contains(erp_regex) |
           df['Description'].astype(str).str.contains(erp_regex), 'Job'] = 'ERP'
    df.loc[df['Job'].astype(str).str.contains(flutter_regex) |
           df['Description'].astype(str).str.contains(flutter_regex), 'Job'] = 'Flutter'
    df.loc[df['Job'].astype(str).str.contains(bi_regex) |
           df['Description'].astype(str).str.contains(bi_regex), 'Job'] = 'BI'
    df.loc[df['Job'].astype(str).str.contains(kotlin_regex) |
           df['Description'].astype(str).str.contains(kotlin_regex), 'Job'] = 'Kotlin'
    df.loc[df['Job'].astype(str).str.contains(typescript_regex) |
           df['Description'].astype(str).str.contains(typescript_regex), 'Job'] = 'TypeScript'
    df.loc[df['Job'].astype(str).str.contains(html_regex) |
           df['Description'].astype(str).str.contains(html_regex), 'Job'] = 'HTML'
    df.loc[df['Job'].astype(str).str.contains(wordpress_regex) |
           df['Description'].astype(str).str.contains(wordpress_regex), 'Job'] = 'WordPress'
    df.loc[df['Job'].astype(str).str.contains(python_regex) |
           df['Description'].astype(str).str.contains(python_regex), 'Job'] = 'Python'
    df.loc[df['Job'].astype(str).str.contains(ruby_regex) |
           df['Description'].astype(str).str.contains(ruby_regex), 'Job'] = 'Ruby'
    df.loc[df['Job'].astype(str).str.contains(rust_regex) |
           df['Description'].astype(str).str.contains(rust_regex), 'Job'] = 'Rust'


# Drop rows containing 'Фасовщик' (case-insensitive)
df = df[~(df['Job'].astype(str).str.contains(packer_regex) | df['Description'].astype(str).str.contains(packer_regex))]

# Print the frequency of the top 10 job titles
print(df['Job'].value_counts(normalize=True).head(n=10) * 100)

# Plot job popularity
job_counts = df['Job'].value_counts().head(n=6)
job_counts.plot(kind='bar', figsize=(8, 6))
plt.xlabel('Язык', fontsize=12)
plt.ylabel('Количество', fontsize=12)
plt.title('Популярность языков', fontsize=16)

# Rotate x-axis tick labels
plt.xticks(rotation=45)

plt.show()
