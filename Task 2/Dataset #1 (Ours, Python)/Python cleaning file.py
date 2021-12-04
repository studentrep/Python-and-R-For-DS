#Task 2
#Art Institute of Chicago API
#https://api.artic.edu/docs/#quick-start

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

#Cverview of variables in the dataset and each variable's data type
df.info()

#Change the type of the id variable to string (called object in pandas)
df['id'] = df['id'].astype('object')

#Get an overview of the number of missing variables in the dataset
missingno.bar(df)

#Replace blank cells with nan value to indicate missing
print(df.replace(r'^\s*$', np.nan, regex=True))

#Grouping by painting place of origin

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

#Group by classification and get the count (the number of each classification type) associated with each classification type
#This can be used to see the frequency of each classification type
byClassification = df.groupby('classification_title', as_index=False)['id'].count()
byClassification = byClassification.rename({'id': 'count'}, axis='columns')

#Shows a Pie chart for the different classifications 
figclass = px.pie(byClassification, values='count', names='classification_title', title='Different classifications')
figclass.update_traces(textposition='inside')
figclass.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
figclass.show()


#Create new column in our dataframe to see how long it took to create each art piece
#this helps to create a visual that has time_to_create on the y axis, start_date on the x axis
#and maybe we can do a scatter plot (? I think it is called) where each point is color-coded by classification_type
df["time_to_create"] = df["date_end"] - df["date_start"] 

#A dataframe that is grouped by artist
byArtist = df.groupby('artist_title', as_index=False)['id'].count()
byArtist = byArtist.rename({'id': 'count'}, axis='columns')

#Sort the above dataframe to get the top 10 artists 
byArtist = byArtist.sort_values(by = 'count', ascending= False)
#grab the top 10 artists ("top ten" meaning the top 10 artists who have the most artworks in the dataset)
top10Artist = byArtist[0:10]

#See which countries are represented the most in the modern art department
#Maybe a visualization can be created out of this

#We filter the dataset and include only those observations that have "modern art" as the value in their department_title column
modernArt = df[df["department_title"] == "Modern Art"]

#This is just to check how many observations there are that meet the above condition
print(len(modernArt["department_title"]))

#Generates a treemap that reflects the frequency of place_of_origin
#You can keep it or do something else, I don't mind either way
#If you keep it, can we add percentages to it?
fig = px.treemap(locationGrouping, path= ["place_of_origin"], values='count',branchvalues = "total")
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()

#Another treemap that reflects frequency by classification title
#again, you can keep this or toss it, either works for me
fig = px.treemap(byClassification, path= ["classification_title"], values='count',branchvalues = "total")
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()

#Please keep these here for now
#fig = px.treemap(new["place_of_origin"])
#fig.show()
#df["artist_display"] = df.artist_display.str.split('\\n', expand=True)[0]
