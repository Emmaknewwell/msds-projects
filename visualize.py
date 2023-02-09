import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file into a Pandas DataFrame
df = pd.read_csv("covid19_data.csv")

print(df.head())

print("Number of missing values:", df.isna().sum().sum())
print("Number of duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()  # drop duplicate rows

print(df.head())

df.to_csv("cleaned_data.csv", index=False)


def visualize_deaths_vs_hospitalizations(df):
    deaths = df['Deaths']
    hospitalizations = df['Hospitalizations']

    plt.scatter(hospitalizations, deaths)
    plt.xlabel("Hospitalizations")
    plt.ylabel("Deaths")
    plt.title("Relationship between Deaths and Hospitalizations in each District")
    plt.show()

# Plot the number of confirmed cases, hospitalizations, and deaths for each district
df.plot(x="District Name", y=["Confirmed Cases", "Hospitalizations", "Deaths"], kind="bar")
plt.title("COVID-19 data for districts in Uganda")
plt.xlabel("District Name")
plt.ylabel("Number of cases")
plt.show()

visualize_deaths_vs_hospitalizations(df)

# Generate a bar graph

def plot_bar_graph(dataframe, x_col, y_col, title, xlabel, ylabel):
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_axes([0,0,1,1])
    ax.bar(dataframe[x_col], dataframe[y_col], color='purple')
    ax.set_title(title  )
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()
    plt.savefig("visuals/bar_graph.png")
    plt.close()

def save_heat_map(df):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax = sns.heatmap(df.corr(), annot=True)
    plt.savefig("visuals/heat_map.png")
    plt.close()

df = pd.read_csv("cleaned_data.csv")
plot_bar_graph(df, "District Name", "Deaths", "Deaths in Different Districts", "Districts", "Deaths")

# Implementation of a heat map

save_heat_map(df)




