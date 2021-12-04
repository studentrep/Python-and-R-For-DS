#CODE OF PREVIOUS TASK1
#Art Institute of Chicago API
#https://api.artic.edu/docs/#quick-start

import requests
import json
import pandas as pd
from openpyxl.workbook import workbook

#will eventually hold a list of dictionaries
#each dictionary in the list will represent an artwork and its associated information
listOfArtworks = []


for i in range(1,101):
    #send a request to get the data
    res = requests.get("https://api.artic.edu/api/v1/artworks" + "?page=" + str(i))

    #convert the response object to a dictionary
    dictRes = res.json()

    #The dictionary response object contains several key-value pairs
    #the key-value pair of interest to us is the one having the key "data"
    #The value of this key contains a list of dictionaries, each dictionary representing one artwork observation

    #We need to iterate through each dictionary item in the list and add each to a new list
    #The reason we do this is because some key-value items in each dictionary have a dictionary as their value
    #In order to access the values in this nested dictionary, we need to add the key-value pairs of these nested dictionaries to
    #each dictionary item (each representing one artwork observation) in the original list
    for eachItem in dictRes.get("data"):
        #in each dictionary item (eachItem), there is a key "thumbnail" that has a dictionary as its value
        #first, we check to see if the thumbnail dictionary exists
        if eachItem["thumbnail"] != None:
            #if it exists, for each key in the thumbnail dictionary
            for thumbnailItemKey in eachItem.get("thumbnail"):
                #add each key-value pair in the thumbnail dictionary to the main data dictionary (eachItem)
                eachItem["thumbnail." + thumbnailItemKey] = eachItem.get("thumbnail").get((thumbnailItemKey))
            #remove the thumbnail dictionary from the main dictionary because it's repetitive information
            eachItem.pop("thumbnail")
        #in each dictionary item (eachItem), there is a key "color" that has a dictionary as its value
        #first, we check to see if the color dictionary exists
        if eachItem["color"] != None:
            #if it exists, for each key in the color dictionary
            for colorItemKey in eachItem.get("color"):
                #add each key-value pair in the color dictionary to the main data dictionary (eachItem)
                eachItem["color." + colorItemKey] = eachItem.get("color").get((colorItemKey))
            #remove the color dictionary from the main dictionary because it's repetitive information
            eachItem.pop("color")
        #add the main dictionary (eachitem) to the list we defined above
        listOfArtworks.append(eachItem)

    #to provide updates on how the code is progressing
    print("Finished with page: " + str(i))
    
#convert the list of dictionaries to a dataframe        
arts_dataFrame = pd.DataFrame(data=listOfArtworks)

#make a more concise database with the columns that we perceive as important 
final_dataFrame= arts_dataFrame[["id", "title", "thumbnail.alt_text", "date_start", "date_end", "date_display", "artist_display", "place_of_origin", "dimensions", "medium_display", "credit_line", "department_title", "artist_title", "classification_title"]]

#convert the dataframe to a csv
final_dataFrame.to_csv("artworks.csv")

#convert the dataframe to an xlsx
final_dataFrame.to_excel("artworks.xlsx")




#CODE TASK2 

#Mathieu 

#Visualization 

import matplotlib.pyplot as plt
import numpy as np

#Create new dataframe for all the types of classifications and count for the classifications the frequency
Clasdf = final_dataFrame["classification_title"]
Clascount = Clasdf.value_counts()
#Plot the first 5, most frequent classifications
plt.plot(Clascount[:5])

#Create new dataframe for all the types of origins and count for the place of origin the frequency
Origin = final_dataFrame["place_of_origin"]
Origincount = Origin.value_counts()
#Plot the first 5, most frequent classifications
plt.plot(Origincount[:5])

#Create new dataframe for all the types of departmens and count for the departmens the frequency
Departmentdf = final_dataFrame["department_title"]
Departmentcount = Departmentdf.value_counts()
#Plot the first 5, most frequent classifications
plt.plot(Departmentcount[:5])

#Create new dataframe for all the types of artists and count for the artists the frequency
Artistdf = final_dataFrame["artist_display"]
Artistcount = Artistdf.value_counts()
#Plot the first 5, most frequent classifications
plt.plot(Artistcount[:5])

#Create new dataframe to see how long it took for each artpiece to create it
Lengthdf = final_dataFrame["date_end"] - final_dataFrame["date_start"] 
Lengthcount = Lengthdf.value_counts()
plt.plot(Lengthcount[:10])
plt.xlabel("Amount of years it took to make the art piece")
plt.ylabel("Amount of art pieces")
