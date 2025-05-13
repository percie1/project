import pandas as pd
df = pd.read_csv('sample_submission.csv')
print(df.head())

import pandas as pd

# Sample data
data = {
    'date': ['2020-03-15', '2020-03-16', '2020-03-17'],
    'cases': [10, 15, 20]
}

df = pd.DataFrame(data)

# Convert the 'date' column to datetime type
df['date'] = pd.to_datetime(df['date'])

# Check the result
print(df.info())


# Group by date and sum cases for all countries
global_trend = df.groupby('date')['new_cases'].sum()

# Plot the trend
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 5))
global_trend.plot()
plt.title("Global Daily New COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.grid(True)
plt.show()


# Filter latest date
latest = df[df['date'] == df['date'].max()]

# Calculate per 100k deaths
latest['deaths_per_100k'] = latest['total_deaths_per_million'] / 10

# Sort and get top 10 countries
top_death_rates = latest[['location', 'deaths_per_100k']].sort_values(by='deaths_per_100k', ascending=False).head(10)

print(top_death_rates)

# Again, take latest date
latest = df[df['date'] == df['date'].max()]

# Drop rows with no continent info
latest = latest[latest['continent'].notna()]

# Group by continent and get the average vaccination rate
continent_vax = latest.groupby('continent')['people_fully_vaccinated_per_hundred'].mean().sort_values(ascending=False)

print(continent_vax)

continent_vax.plot(kind='bar', color='skyblue')
plt.title("Average Vaccination Rate by Continent")
plt.ylabel("People Fully Vaccinated per 100 People")
plt.xlabel("Continent")
plt.grid(axis='y')
plt.show()

df = pd.read_csv("owid-covid-data.csv")
df['date'] = pd.to_datetime(df['date'])
df = df[df['date'] >= '2020-01-01']
df = df[df['continent'].notna()]  # Remove aggregates like 'World'

import seaborn as sns
import matplotlib.pyplot as plt

top10 = df[df['date'] == '2023-12-31'].sort_values('total_cases', ascending=False).head(10)
sns.barplot(x='total_cases', y='location', data=top10)
plt.title('Top 10 Countries by Total COVID-19 Cases (2023)')
plt.show()
