##import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=pd.read_csv("mymoviedb.csv",lineterminator= "\n")
data.info()
print(data.head(10))
print(data["Genre"].head())#to print genre of first 5 movies
print(data.duplicated().sum())#to check any duplicated value is presnt or not
sns.displot(data["Vote_Average"],kde=True)
plt.show()
#to change the category of release date and convert int years only
data["Release_Date"]=pd.to_datetime(data["Release_Date"])
print(data["Release_Date"].dtypes)
data["Release_Date"]=data["Release_Date"].dt.year
print(data["Release_Date"].dtypes)
print(data.head(10))
#to remove useless columns
data.drop(["Poster_Url","Original_Language","Overview"],axis=1,inplace=True)
print(data.head(10))

#making a fuction to categorize column
def categorize_col(df,col,labels):

    edges=[data[col].describe()["min"],
           data[col].describe()["25%"],
           data[col].describe()["50%"],
           data[col].describe()["75%"],
           data[col].describe()["max"]]
    data[col]=pd.cut(data[col],edges,labels=labels,duplicates="drop")
    return data

labels=["Not_Popualr","Below_Avg","Average","popular"]
categorize_col(data,"Vote_Average",labels)
print(data.head(15))
print(data["Vote_Average"].head(15))

#TO SPLIT THE GENRE
data["Genre"]=data["Genre"].str.split(", ")
data=data.explode("Genre").reset_index(drop=True)

print(data.head(20))
print(data.duplicated().sum())
data["Genre"]=data["Genre"].astype("category")
print(data["Genre"].dtypes)
print(data.describe())
# preprocessing of data completed

# most frequent genre on netflix is drama

sns.set_style("darkgrid")
sns.catplot(x="Genre",data=data,kind="count",palette="gist_earth",
            order=data["Genre"].value_counts().index)
plt.title("Genre column  distribution")
plt.show()

#genre with highest votes
sns.set_style("darkgrid")
sns.catplot(x="Vote_Average",data=data,kind="count",palette="gist_rainbow",
order=data["Vote_Average"].value_counts().index,legend=True)
plt.title("Genre column  distribution")
plt.show()

#movie with max poplularity
print(data[data["Popularity"]==data["Popularity"].max()])

#genre ith minimum popularity

print(data[data["Popularity"]==data["Popularity"].min()])
#genre with maximum vote count

print(data[data["Vote_Count"]==data["Vote_Count"].max()])

sns.set_style("darkgrid")
sns.displot(data["Release_Date"],palette="ocean")
plt.show()