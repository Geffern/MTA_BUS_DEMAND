# importing libraries
import pandas as pd

# initializing the name of the file and the columns we want to include
filename = 'NYCT Bus Tables - Average Weekday' + '.csv'
cols = ['Route', '2016', '2017', '2018', '2019', '2020']

# reading the csv file and putting it into a data frame
file = pd.read_csv(filename, header = 1, usecols = cols)
df = pd.DataFrame(file)
#print(df)

# removing the empty rows
df = df.dropna()


# finding the rows we want to remove
words_to_remove = ['Local', 'Total', 'Exp']
rows_to_remove = [] # creating a list to put the names of the rows I want to remove

for route in df['Route']:
    for word in words_to_remove:
        if word in route:
            rows_to_remove.append(route)
#print(rows_to_remove)


# finding the index of the rows we want to remove
for row in rows_to_remove:
    #print(df.loc[df['Route'] == index].index)
    filter_mask = df.loc[df['Route'] == row].index
    df = df.drop(filter_mask)   # dropping the rows

print(df)

# putting the dataframe into a csv file
df.to_csv('Average Weekday Ridership.csv', index = False)