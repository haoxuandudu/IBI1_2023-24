# First, import the necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir ("C:/Users/17732/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 7")

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# show the fourth column (the DALYs) from every 10th row, starting from the first row, for the first 100 rows
data = dalys_data.iloc[0:100:10, 3]
print(data)

# Use loc function to use column names
dalys_data.loc[2:4,"Year"]
# if the location is unknown
is_afghanistan=dalys_data['Entity']=='Afghanistan'
afghanistan_days=dalys_data.loc[is_afghanistan,'DALYs']
# if the location is known
print(afghanistan_days)

is_china=dalys_data['Entity']=='China'
china_days=dalys_data.loc[is_china,'DALYs']

# Create a separate DataFrame with only China's data
china_data = dalys_data[dalys_data['Entity'] == 'China']

# Extract the 'Year' and 'DALYs' columns from the china_data DataFrame
years, dalys = china_data['Year'].values, china_data['DALYs'].values

# mean DALYs for China 
mean_dalys_china = np.mean(dalys)

dalys_2019 = dalys[years == 2019]

#Comparison
comparison = mean_dalys_china > dalys_2019[0]

# plot the data for China
plt.plot(china_data.Year, china_data.DALYs, 'b+')
plt.xticks(china_data.Year,rotation=-90)
plt.show()
plt.clf

import matplotlib.pyplot as plt
import pandas as pd

# Assuming 'dalys_data' is a pandas DataFrame with the data provided earlier
# And that it has been loaded correctly into your Python environment

# Filter the data to include only the rows for the year 2019
data_2019 = dalys_data[dalys_data['Year'] == 2019]

# Extract the 'Entity' and 'DALYs' columns
entities_2019 = data_2019['Entity'].tolist()
dalys_2019 = data_2019['DALYs'].tolist()

# Create a boxplot using matplotlib
plt.boxplot(dalys_2019, vert=True)

# Set the title and labels for the x and y axes
plt.title('Boxplot of DALYs across Countries in 2019')
plt.xlabel('Country')
plt.ylabel('DALYs')

# Display the boxplot
plt.show()
plt.clf