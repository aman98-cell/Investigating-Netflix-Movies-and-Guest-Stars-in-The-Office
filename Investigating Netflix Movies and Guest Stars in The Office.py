#!/usr/bin/env python
# coding: utf-8

# ### Task 1 : Create two new lists
# 1. years, this list containg the years from the year 2011 to 2020
# 2. durations, this list is having the data of the movie length
# after that there is a dictionary of the name movie_dict which is having years as keys and durations as values

# In[ ]:


#Create the years and durations lists

years = []
for i in range(2011,2021):
    years.append(i)
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93,90]

movie_dict = {'years': years, 'durations': durations}
#Print the dictionary
print(years)


# ### Task 2 : Creating a DataFrame from a dictionary
# To convert our dictionary movie_dict to a pandas DataFrame, we will first need to import the library under its usual alias. 

# In[ ]:


#Import pandas under its usual alias
import pandas as pd

#Create a DataFrame from the dictionary
#method of creating the data frame from dictionary with the name durations_df

durations_df = pd.DataFrame(movie_dict)

#Print the DataFrame
durations_df


# ### Task 3 : A visual inspection of our data using matplotlib

# In[ ]:


#Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt
fig = plt.figure()

#Draw a line plot of release_years and durations
#plotting the line plot using plt.plot(years,durations) years on x axis and durations on y axis
plt.plot(years,durations)

#Create a title using plt.title("title name")
plt.title("Netflix Movie Durations 2011-2020")

#Show the plot using plt.show()
plt.show()


# ### Task 4 : Loading the rest of the data from a CSV

# #Read in the CSV as a DataFrame
# #importing the data from a csv file using pd.read_csv("")
# netflix_df = pd.read_csv("datasets/netflix_data.csv")
# 
# #Print the first five rows of the DataFrame using square brackets for accessing the rows
# netflix_df[0:5]

# ### Task 5 : Filtering for movies!

# In[ ]:


#Subset the DataFrame for type "Movie"
#filtering out the rows which having "type" as "Movie" and saving the data into the new data frame netflix_df_movies_only
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

#Select only the columns of interest
#Selecting the columns of interests
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]

#Print the first five rows of the new DataFrame
netflix_movies_col_subset[0:5]


# ### Task 6 : Creating a scatter plot

# In[ ]:


#Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))

#Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset['release_year'],netflix_movies_col_subset['duration'])

#Providing the title using the below method
plt.title("Movie Duration by Year of Release")

#Show the plot
plt.show()


# ### Task 7 : Digging deeper

# In[ ]:


# Filter for durations shorter than 60 minutes by creating new dataframe short_movies
short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] <60]

# Print the first 20 rows of short_movies
short_movies[0:20]


# ### Task 8 : Marking non-feature films
# 
# Interesting! It looks as though many of the films that are under 60 minutes fall into genres such as "Children", "Stand-Up", and "Documentaries". This is a logical result, as these types of films are probably often shorter than 90 minute Hollywood blockbuster

# In[ ]:


# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for lab,row in netflix_movies_col_subset.iterrows() :
    if row['genre'] == "Children" :
        colors.append("red")
    elif row['genre'] == "Documentaries":
        colors.append("blue")
    elif row['genre'] == "Stand-Up" :
        colors.append("green")
    else:
        colors.append("black")
        
# Inspect the first 10 values in your list        
colors[0:10]


# ### Task 9 : Plotting with color!
# 

# In[ ]:


# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], c=colors)


# Create a title and axis labels
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Show the plot
plt.show()


# In[ ]:




