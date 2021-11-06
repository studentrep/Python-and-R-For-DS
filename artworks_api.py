#Anika
#Art Institute of Chicago API
#https://api.artic.edu/docs/#quick-start

import requests
import json
import pandas as pd

#will eventually hold a list of dictionaries
#each dictionary in the list will represent an artwork and its associated information
listOfArtworks = []


for i in range(1,101):
    #send a request to get the data
    res = requests.get("https://api.artic.edu/api/v1/artworks" + "?page=" + str(i))

    #convert the response object to a dictionary
    dictRes = res.json()
    
    #for each key-value pair in the data dictionary (the data dictionary is the associated value of the "data" key)
    for eachItem in dictRes.get("data"):
        #add the dictionary to the list we defined above
        listOfArtworks.append(eachItem)

    print("Finished with page: " + str(i))
    
#convert the list of dictionaries to a dataframe        
episodes_dataFrame = pd.DataFrame(data=listOfArtworks)
#convert the dataframe to a csv
episodes_dataFrame.to_csv("artworks.csv")
