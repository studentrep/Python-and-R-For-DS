#Task 2
#Art Institute of Chicago API
#https://api.artic.edu/docs/#quick-start

#!!!
#Run the following line of code if you have issues using plotly in Google Colab
#!pip install --upgrade plotly

import requests
import json
import pandas as pd
from openpyxl.workbook import workbook
import missingno
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


#Read in the csv file
#note: this is the csv file which includes the end date
df = pd.read_csv('artworks.csv')

#Overview of variables in the dataset and each variable's data type
df.info()

#Change the type of the id variable to string (called object in pandas)
df['id'] = df['id'].astype('object')

#Get an overview of the number of missing variables in the dataset
missingno.bar(df)

#Replace blank cells with nan value to indicate missing
print(df.replace(r'^\s*$', np.nan, regex=True))

###Grouping by painting place of origin

#Some place_of_origin values are at the city level instead of at the country level
#Here, I'm just cleaning up the place_of_origin column so that we can have all place of origin values at the country level
df['place_of_origin'] = df['place_of_origin'].str.replace('New York City|Abiquiu|Chicago|American|Lake George|New Mexico|Saint Louis|Wichita|Corona|Providence|Loch Vale|Penland|New York','United States')
df['place_of_origin'] = df['place_of_origin'].str.replace('Corfu','Greece')
df['place_of_origin'] = df['place_of_origin'].str.replace('London','England')
df['place_of_origin'] = df['place_of_origin'].str.replace('Frascati|Venice|Sicily','Italy')
df['place_of_origin'] = df['place_of_origin'].str.replace('Flanders','Belgium')
df['place_of_origin'] = df['place_of_origin'].str.replace('Petén','Guatemala')
df['place_of_origin'] = df['place_of_origin'].str.replace('Paris|Vallauris','France')

#Group by location and get the count (the number of artworks) associated with each location
#This dataframe can be used for the # of artworks per country visualization
locationGrouping = df.groupby('place_of_origin', as_index=False)['id'].count()
locationGrouping = locationGrouping.rename({'id': 'count'}, axis='columns')

#Generates a treemap that reflects the frequency of place_of_origin
fig = px.treemap(locationGrouping, path= ["place_of_origin"], values='count',branchvalues = "total")
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()

#Group by classification and get the count (the number of each classification type) associated with each classification type
#This can be used to see the frequency of each classification type
byClassification = df.groupby('classification_title', as_index=False)['id'].count()
byClassification = byClassification.rename({'id': 'count'}, axis='columns')

#Shows a pie chart for the different classifications 
figclass = px.pie(byClassification, values='count', names='classification_title', title='Different classifications')
figclass.update_traces(textposition='inside')
figclass.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
figclass.show()

#Another treemap that reflects frequency by classification title
fig = px.treemap(byClassification, path= ["classification_title"], values='count',branchvalues = "total")
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()

#A dataframe that is grouped by artist
byArtist = df.groupby('artist_title', as_index=False)['id'].count()
byArtist = byArtist.rename({'id': 'count'}, axis='columns')

#Sort the above dataframe to get the top 10 artists 
byArtist = byArtist.sort_values(by = 'count', ascending= False)
#Grab the top 10 artists ("top ten" meaning the top 10 artists who have the most artworks in the dataset)
top10Artist = byArtist[0:10]

#Bar chart of top 10 artists (having the greatest # of art pieces in the dataset)
fig = px.bar(top10Artist, y='count', x='artist_title', text='count')
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', title_text = "Top 10 artist with most artworks in dataset", xaxis_title = "Name of the artist", yaxis_title ="Amount of art pieces in dataset")
fig.show()

#We filter the dataset and include only those observations that have "modern art" as the value in their department_title column
modernArt = df[df["department_title"] == "Modern Art"]

#See which countries are represented the most in the modern art department
#Maybe a visualization can be created out of this
#Countries represented in the modern art department
#Group the modernArt by country
modernArtbycountry = modernArt.groupby('place_of_origin', as_index=False)['id'].count()
modernArtbycountry = modernArtbycountry.rename({'id': 'count'}, axis='columns')
#Make a pie chart to represent the countries and their respective share of modernart
fig = px.pie(modernArtbycountry, values='count', names='place_of_origin')
fig.show()

#This is just to check how many observations there are that meet the above condition
print(len(modernArt["department_title"]))

#Create new column in our dataframe to see how long it took to create each art piece
#this helps to create a visual that has time_to_create on the y axis, start_date on the x axis
df["time_to_create"] = df["date_end"] - df["date_start"] 

#To be able to do the next scatter plot we need to install a new package called seaborn
import seaborn as sns
%matplotlib inline

#Check which countries have a significant amount of art pieces, label the insignifcant countries as other countries
#Otherwise we would have too many countries in the scatter plot; which would make it too chaotic
df["place_of_origin"].value_counts()
df.loc[df["place_of_origin"] == "Greece","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Sweden","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Colombia","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Mozambique","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Switzerland","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Russia","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Egypt","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Mali","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Finland","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Jersey","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Ireland","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Guatemala","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Morocco","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "England","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Belgium","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Germany","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "Netherlands","place_of_origin"] = "Other countries"
df.loc[df["place_of_origin"] == "China","place_of_origin"] = "Other country"
df["place_of_origin"][:30]

#We want to set the size bigger, to be able to see more details 
sns.set(rc={'figure.figsize':(14,10)})
#Plot the data with on the x-axis the start of the art piece, y-axis the length it took to complete, and in color you can see the
#most important countries in terms of # of art pieces delivered
g =sns.scatterplot(x="date_start", y="time_to_create",
              hue="place_of_origin",
              data=df);

#Set the scale because outliers bias the plot 
g.set(ylim = (0,90))
g.set(xlim = (1500,2020))


#Please keep these here for now
#fig = px.treemap(new["place_of_origin"])
#fig.show()
#df["artist_display"] = df.artist_display.str.split('\\n', expand=True)[0]
