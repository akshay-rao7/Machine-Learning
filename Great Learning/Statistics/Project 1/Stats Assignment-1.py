#!/usr/bin/env python
# coding: utf-8

# # Read the data set and replace dashes with 0 to make sure you can perform arithmetic operations on the data. (5 points)

# In[1]:


import numpy as np #import library numpy as np
import pandas as pd #import library pandas as pd
import warnings #importing warnongs library to ignore
warnings.filterwarnings("ignore") #ignore any warnings
df = pd.read_csv("Laliga.csv") #importing file
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header
df = df.replace('-', 0) #replace the '-' values with 0
df #print the dataframe


# # Print all the teams which have started playing between 1930-1980. Use “Debut” column (5 points)

# In[345]:


df["Debut"] = df["Debut"].astype(str) #convert Debut column to string
df["Debut"] = df['Debut'].str[:4] #extract only the first 4 characters of Debut
df["Debut"] = df["Debut"].astype(int) #Convert to int
df1 = df[(df.Debut >= 1930) & (df.Debut <= 1980)] #get the Teams started playing between 1930 and 1980
print(df1['Team'].unique()) #printing the teams


# # Print the list of teams which came Top 5 in terms of points (2.5 points)

# In[4]:


df['Points'].astype(str).astype(int).sort_values #Sorting teams in ascending 
df.iloc[:,1].head(5) #Picking and displaying the first 5 rows of Teams


# # Write a function with name “Goal_diff_count” which should return all the teams with their Goal Differences. Using the same function, find the team which has maximum and minimum goal difference. (5 points)
# Goal_diff_count = GoalsFor - GoalsAgainst

# In[331]:


df["GoalsFor"] = df["GoalsFor"].astype(int) #conver into int
df["GoalsAgainst"] = df["GoalsAgainst"].astype(int) #conver into int
df["Goal_diff_count"] = df["GoalsFor"] - df["GoalsAgainst"] #Goal_diff_count = GoalsFor - GoalsAgainst
df#display df


# # Create a new column with the name “Winning Percent” and append it to the data set (5 points)
# 
# Percentage of Winning = (GamesWon / GamesPlayed)*100
# 
# If there are any numerical error, replace it with 0%
# 
# Print the top 5 teams which have the highest Winning percentage

# In[332]:


df["GamesWon"] = df["GamesWon"].astype(int) #convert into int
df["GamesPlayed"] = df["GamesPlayed"].astype(int)#convert into int
df["WinningPercentage"]= (df.GamesWon / df.GamesPlayed)*100 #calculate and add new column
df #display df


# # Group teams based on their “Best position” and print the sum of their points for all positions (7.5 points)
# 
# Eg: Best Position  Points 
# 
#   1 25000
# 
# 2  7000 

# In[380]:


df2 = df[['BestPosition', 'Points']]  #Create a second dataframe with name df2 consisting of 2 rows - BestPosition and Points
df2["BestPosition"] = df2["BestPosition"].astype(int)#Converting to integer type
df2["Points"] = df2["Points"].astype(int))#Converting to integer type
df2.groupby("BestPosition").sum() #Grouping by sum


# In[ ]:


#End of Assignment

