#Anika
#Jikan API
#https://jikan.docs.apiary.io/#

import requests
import json
import pandas as pd

#send a request to get the data
res = requests.get("https://api.jikan.moe/v3/anime/1/episodes/1")

#ensure that the operation was a successful
print(res.status_code)

#convert the response object to a dictionary
dictRes = res.json()

#check to ensure that the object is a dictionary
print(type(dictRes))

#will eventually hold a list of dictionaries
#each dictionary in the list will represent an episode and its associated information
listOfEpisodes = []

#dictRes is a dictionary containing several key-value pairs
#We need to navigate to the key-value pair that contains (as its value) key-value pairs consisting of each episode and its associated information

#for each key-value pair in the episodes dictionary (the episodes dictionary is the associated value of the "episodes" key)
for eachItem in dictRes.get("episodes"):
        #add the key-value pair to the list we defined above
        listOfEpisodes.append(eachItem)

    
#convert the list of dictionaries to a dataframe        
episodes_dataFrame = pd.DataFrame(data=listOfEpisodes)
#convert the dataframe to a csv
episodes_dataFrame.to_csv("jikan-episodes.csv")
