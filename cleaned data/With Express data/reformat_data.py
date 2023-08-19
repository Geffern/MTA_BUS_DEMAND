# importing libraries
import pandas as pd

# creating a function to reformat the csv file
def reformat(column_name):
    # reading the csv file and putting it into a dataframe
    filename = 'Average Weekday Ridership.csv'
    file = pd.read_csv(filename, usecols=['Route', column_name]) # only using the selected columns
    df = pd.DataFrame(file)
    
    
    # inserting the year column
    year_list = []
    for i in range(len(df)):
        year_list.append(column_name)
    df.insert(0, 'Year', year_list)
    
    
    # creating a dictionary 
    borough = {'B': 'Brooklyn', 
               'Bx': 'Bronx',
               'M': 'Manhatten',
               'Q': 'Queens',
               'S': 'Staten Island',
               'X': 'Express'}
    
    # creating a list to add as a column
    borough_list = []
    
    # matching the route with the borough
    for route in df['Route']:
        for key in borough:
            if route[0] == key:
                #print(route)
                borough_list.append(borough[key])
                
    # inserting the borough column
    df.insert(2, 'Borough', borough_list)
    
    # renaming the column as average ridership
    df = df.rename(columns= {column_name: 'Avg. Ridership'})
    
    # returning the dataframe created
    return df


# creating a list to refomat each year
years = ['2016', '2017', '2018', '2019', '2020']

# creating a list to put each dataframe into
dataframes = []

# adding each dataframe into the list
for year in years:
    dataframes.append(reformat(year))
    
# combining all the dataframes into one
df = pd.concat(dataframes, ignore_index = True)

print(df)

# putting the dataframe into a csv file
df.to_csv('2nd Format.csv', index = False)
    
    


