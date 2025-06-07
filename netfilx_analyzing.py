import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# sns.set_theme()
dataset = pd.read_csv("./data/netflix_data/netflix_data.csv")
print(dataset.columns)
# print(dataset["description"])
data_set_1 = dataset.drop(columns=["show_id","type","title","director","cast","country","listed_in","description"])

index = 0
for i in data_set_1["duration"]:
    if "Season" not in str(i) and str(i)!="nan":
        num, mins = i.split(" ")
        data_set_1.loc[index, "duration"] = int(num)
    if "Season" in str(i):
        data_set_1.loc[index, "duration"] = np.nan        
    index +=1

child_list = ["TV-Y", "TV-G", "TV-Y7", "G", "TV-Y7-FV"]
teen_list = ['PG-13', 'TV-14', "PG", "TV-PG"]
adult_list = ['TV-MA', 'R', "NC-17"]
unrated_list = ["NR", "UR"]

index = 0
for rating in data_set_1["rating"]:
    if rating in child_list:
        data_set_1.loc[index, "rating"] = "G"
    elif rating in teen_list:
        data_set_1.loc[index, "rating"] = "PG"
    elif rating in adult_list:
        data_set_1.loc[index, "rating"] = "R"
    elif rating in unrated_list:
        data_set_1.loc[index, "rating"] = "Unrated"

    index +=1

data_set_1 = data_set_1.dropna()

sns.set_theme(style = "darkgrid")
sns.relplot(data=data_set_1,x="release_year", y="duration", hue = "rating", palette="muted", alpha = 1)
plt.show()

dataset = dataset.dropna()
data_set_2 = pd.DataFrame([],
columns=['year', 'amt'])

index = 0
for i in range(data_set_1['release_year'].min(), int(data_set_1['release_year'].max())+1):
    data_set_2.loc[index, "year"] = int(i)
    data_set_2.loc[index, "amt"] = 0
    index += 1

data_set_2["amt"]=pd.to_numeric(data_set_2["amt"])
min_year = data_set_1['release_year'].min()
for year in dataset["release_year"]:
    current_amt = int((data_set_2.loc[int(year)-min_year, "amt"]))
    data_set_2.loc[int(year)-min_year, "amt"] = current_amt + 1
    index += 1

sns.set_theme(style = "darkgrid")
sns.barplot(data=data_set_2, x="year", y="amt", palette="muted", alpha = 1)
plt.xticks(rotation = 90, fontsize = 8)
tick_labels = plt.gca().get_xticklabels()
for i, label in enumerate(tick_labels):
    if i % 2 != 1:
        label.set_visible(False)
plt.show()

tags_list = []
for tags in dataset["listed_in"]:
    tag_list = tags.split(", ")
    for tag in tag_list:
        if tag not in tags_list:
            tags_list.append(tag)

data_set_3 = pd.DataFrame([],
columns=['Number Of Movies'])
for i in range(len(tags_list)):
    data_set_3.loc[i, "Number Of Movies"] = 0

data_set_3.index = tags_list

for tags in dataset["listed_in"]:
    tag_list = tags.split(", ")
    for tag in tag_list:
        data_set_3.at[tag, "Number Of Movies"] = data_set_3.at[tag, "Number Of Movies"]+1
data_set_3=data_set_3.sort_values("Number Of Movies")

sns.set_theme(style = "darkgrid")
sns.barplot(data=data_set_3, x=data_set_3.index, y="Number Of Movies", palette="muted", alpha = 1)
plt.xticks(rotation = 90, fontsize = 7)
plt.show()