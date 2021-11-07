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
        #if the thumbnail dictionary exists
        if eachItem["thumbnail"] != None:
            #for each key in the thumbnail dictionary
            for thumbnailItemKey in eachItem.get("thumbnail"):
                #add each key-value pair in the thumbnail dictionary to the main data dictionary
                eachItem["thumbnail." + thumbnailItemKey] = eachItem.get("thumbnail").get((thumbnailItemKey))
            #remove the thumbnail dictionary from the main dictionary because it's repetitive information
            eachItem.pop("thumbnail")
        #if the color dictionary exists
        if eachItem["color"] != None:
            #for each key in the color dictionary
            for colorItemKey in eachItem.get("color"):
                #add each key-value pair in the color dictionary to the main data dictionary
                eachItem["color." + colorItemKey] = eachItem.get("color").get((colorItemKey))
            #remove the color dictionary from the main dictionary because it's repetitive information
            eachItem.pop("color")
        #add the dictionary to the list we defined above
        listOfArtworks.append(eachItem)

    print("Finished with page: " + str(i))
    
#convert the list of dictionaries to a dataframe        
episodes_dataFrame = pd.DataFrame(data=listOfArtworks)
#convert the dataframe to a csv
episodes_dataFrame.to_csv("artworks.csv")
