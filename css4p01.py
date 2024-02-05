# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:31:30 2024

@author: langa
"""

import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

#Reading the csv file:
file=pd.read_csv("movie_dataset.csv")  
#Printing the csv file:
print(file) 
#converting the csv file to a DataFrame:
df=pd.DataFrame(file)

#Rename the column names that have spaces:
df.rename(columns={'Runtime (Minutes)': 'Runtime_(Minutes)'}, inplace=True)
df.rename(columns={'Revenue (Millions)': 'Revenue_(Millions)'}, inplace=True)

#Summary of the DataFrame:
print(df.info())

#calculate the average of the last two cloumns in the DataFrame:
avg_revenue=df["Revenue_(Millions)"].mean()
avg_metascore=df["Metascore"].mean()

#printing the average revenue of all movies in the dataset:
print("The average revenue of all movies in the dataset: ", avg_revenue) 

#Replace the nan's with the average value:
df["Revenue_(Millions)"].fillna(avg_revenue,inplace=True)
df["Metascore"].fillna(avg_metascore, inplace=True )

#printing the maximum value in column called "Rating":
print("The maximum value in column called 'Rating' is: ", df["Rating"].max())
#Then we are displaying only the row that corresponds to the maximum value in column called Rating:
print("displaying only the row that corresponds to the maximum value in column called Rating: ", df[df["Rating"]==9.0])
highest_rated_movie_row=df[df["Rating"]==9.0]
#selecting only the column called "Title" from the dataframe 'highest_rated_movie_row':
highest_rated_movie=highest_rated_movie_row["Title"]
print("The highest rated movie in the dataset is: ", highest_rated_movie)

#selecting all the rows that corresponds to the year between 2015 and 2017:
selected_rows=df[(df["Year"]>=2015) & (df["Year"]<=2017)]
#printing the rows that corresponds to the year between 2015 and 2017:
print(selected_rows)

#calculating the average revenue of movies from 2015 to 2017 in the dataset:
avg_selected_rows=selected_rows["Revenue_(Millions)"].mean()
#print the average revenue of movies from 2015 to 2017 in the dataset:
print("The average revenue of movies from 2015 to 2017 in the dataset: ", avg_selected_rows)

#selecting only the rows that that corresponds to the year 2016:
select_rows_2016=df[df["Year"]==2016]
#reset the index:
select_rows_2016=select_rows_2016.reset_index(drop=True)
#count the number of movies released on the year 2016:
totalrows_2016=select_rows_2016["Title"].count()
#print the number of movies released on the year 2016:
print("The number of movies released on the year 2016: ", totalrows_2016)
#calculating average rating corresponding to the year 2016:
avg_rating2016=select_rows_2016["Rating"].mean()
#printing the average rating corresponding to the year 2016:
print("The average rating corresponding to the year 2016 is: ", avg_rating2016)
#counting the number of movies released in 2016:
movies2016=select_rows_2016["Title"].count()

#selecting only the rows that that corresponds to the year 2007:
select_rows_2007=df[df["Year"]==2007]
#reset the index:
select_rows_2007=select_rows_2007.reset_index(drop=True)
#calculating average rating corresponding to the year 2007:
avg_rating2007=select_rows_2007["Rating"].mean()
#printing the average rating corresponding to the year 2007:
print("The average rating corresponding to the year 2007 is: ",avg_rating2007)

#selecting only the rows that that corresponds to the year 2006:
select_rows_2006=df[df["Year"]==2006]
#reset the index:
select_rows_2006=select_rows_2006.reset_index(drop=True)
#calculating average rating corresponding to the year 2006:
avg_rating2006=select_rows_2006["Rating"].mean()
#printing the average rating corresponding to the year 2006:
print("The average rating corresponding to the year 2006 is: ", avg_rating2006)
#counting the number of movies released in 2006:
movies2006=select_rows_2006["Title"].count()

#selecting only the rows that that corresponds to the year 2008:
select_rows_2008=df[df["Year"]==2008]
#reset the index:
select_rows_2008=select_rows_2008.reset_index(drop=True)
#calculating average rating corresponding to the year 2008:
avg_rating2008=select_rows_2008["Rating"].mean()
#printing the average rating corresponding to the year 2008:
print("The average rating corresponding to the year 2008 is: ", avg_rating2008)
print("Thus the year with the highest average rating is 2007.")

"""
Answer for Question 8 (Project 1):
Thus the year with the highest average rating is 2007.
"""


#Calculate the percentage increase in number of movies made between 2006 and 2016:
percentage_increase=((movies2016-movies2006)/movies2006)*100
print("The percentage increase in number of movies made between 2006 and 2016 is: ", percentage_increase)


#selecting only the rows that corresponds to the director "Christopher Nolan":
select_director=df[df["Director"]=="Christopher Nolan"]
#reset the index:
select_director=select_director.reset_index(drop=True)
#count the number of movies directed by Christopher Nolan:
totalrows_director=select_director["Title"].count()
#print the number of movies directed by Christopher Nolan:
print("The number of movies directed by Christopher Nolan is: ", totalrows_director)
#finding the median rating of movies directed by Christopher Nolan:
median_rating_Nolan=select_director["Rating"].median()
#printing the median rating of movies directed by Christopher Nolan:
print("The median rating of movies directed by Christopher Nolan is: ", median_rating_Nolan)

#selecting only the rows that corresponds to the movies with a rating of at least 8.0:
select_rating_8=df[df["Rating"]>=8.0]
#reset the index:
select_rating_8=select_rating_8.reset_index(drop=True)
#count the number of movies that have a rating of at least 8.0:
totalrows_rating_8=select_rating_8["Title"].count()
#print the number of movies that have a rating of at least 8.0:
print("The number of movies that have a rating of at least 8.0 is: ", totalrows_rating_8)


#grouping common genres together and counting how many of them are there:
genres=df["Genre"].value_counts()
#counting the number of unique genres in the dataset:
genre_count=genres.count()
#printing the number of unique genres in the dataset:
print("The number of unique genres in the dataset is: ", genre_count)


#Split the 'Actors' column into individual actors and flatten the lists:
all_actors=[actor.strip() for sublist in df['Actors'].str.split(',') for actor in sublist]
actor_counter=Counter(all_actors)

#Find the most common actor:
most_common_actor=actor_counter.most_common(1)[0][0]
#printing the name of the most common actor in all the movies:
print("The name of the most common actor in all the movies is: ", most_common_actor)


#Select specific columns using labels:
selected_columns_labels=df[['Rank', 'Year','Runtime_(Minutes)','Rating','Votes','Revenue_(Millions)','Metascore']]

#Perform a correlation analysis:
correlation_matrix=selected_columns_labels.corr()

#Display the correlation matrix:
print("The correlation of the numerical features is given by: ",correlation_matrix)

"""
Answer for question 12 (Project 1):
1) Votes and Revenue_(Millions): The positive correlation between the votes
and revenues suggests that the higher the number of votes for a movie, the 
higher the revenues, which implies that movies that get more votes generate 
more income.

2) Rating and Votes: The positive correlation between the rating and the 
votes suggests that movies that are highly rated obtain a high number of 
votes.

3) Runtime_(minutes) and Revenue_(Millions): There is a weak correlation 
between the runtime and the revenues which suggests that longer movies might
not necessarily lead to higher revenues.

4) Year and Revenue_(Millions): The negative correlation between the years 
and revenues suggests that old movies generate less revenues because people 
are no longer buying old movies at the stores and they prefer to watch them 
on tv, for example: dstv.

5) Year and Votes: There is a weak correlation between the years and the 
votes, which might suggest that old movies obtain less votes since the 
audience is always looking forward to something new, which implies that 
people no longer buy old movies and so that means their hardly watched. 
Thus, old movies obtain less votes over the course of time.
    
6) Rating and Revenue_(Millions): There is a weak correlation between the 
ratings and the revenues which suggests that movies that are less rated 
leads to less revenues meaning that if a move is poorly rated then the movie
production makes less income from their sales because this implies that the 
viewers did not like the movie and so it got less ratings thus less income 
was generated from selling the copies of the movie.

Advice:

1) My advice is that directors should focus on movie rating, to be more 
specific they should aim for higher ratings as there is a positive 
correlation between Rating and Revenues. This involves paying attention to 
script quality, acting, and overall production value.

2) Directors should also focus on the runtime of the movies, to be more 
specific they should carefully consider the optimal length of their movies 
to maintain audience engagement. This will help strengthen the correlation 
between the Runtime and the Revenues.
"""

