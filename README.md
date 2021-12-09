# Python-and-R-For-DS
Python and R for Data Science course project work repository
Tasks 1 & 2


TASK 1

Project chosen: Art Institute of Chicago API: https://api.artic.edu/docs/#introduction

	We access the /artworks listing endpoint in the API by visiting the following URL: https://api.artic.edu/api/v1/artworks, to see all the published artworks in the collection.

Procedure/Python Code Explanation

	To access the data, we first sent an API request. Next, we converted the response object that we received to a dictionary. 

	First, we explored the dictionary, and realized that there was a key-value pair (key called “data”) that contained, as its value, a list of dictionaries (each dictionary representing a single artwork observation). Once we realized this, we iterated through the list of dictionaries and added each dictionary to a new list. The reason we did this (and did not simply use the original list) was because some key-value items within each dictionary contained a dictionary as their value. To access the information contained in these “nested dictionaries”, we added the information contained in the nested dictionaries to the main dictionary (“main dictionary” referring to the dictionary that represented a single artwork observation). Once we effectively “de-nested” the main dictionary and had all attribute information of an artwork on a single level, we added this main dictionary to the new list. 

	Finally, we converted this list of dictionaries to a dataframe. Then, we created a final dataframe consisting of only the columns we deemed particularly relevant. We then saved the final dataframe as both a .csv and an .xlsx. 

We selected 12 endpoints (columns) in the Artworks Collection data:

title - The name of this resource
thumbnail.alt_text - Alternate text for this work. 
date_start - The year of the period of time associated with the creation of this work.
date_display - Readable, free-text description of the period of time associated with the creation of this work. 
artist_display - Readable description of the creator of this work. Includes artist names, nationality and lifespan dates.
place_of_origin - The location where the creation, design, or production of the work took place, or the original location of the work.
dimensions - The size, shape, scale, and dimensions of the work.
medium_display - The substances or materials used in the creation of a work.
credit_line - Brief statement indicating how the work came into the collection.
department_title - Name of the curatorial department that this work belongs to.
artist_title - Name of the preferred artist/culture associated with this work.
classification_title - The name of the preferred classification term for this work.

TASK 2

	Please reference the individual folders (corresponding to dataset #1 and dataset #2) of Task 2 for a detailed explanation of the contents of each folder. 