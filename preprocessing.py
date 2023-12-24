import pandas as pd
from sklearn.cluster import KMeans

# create dataframe
colors = pd.read_csv('color_names.csv')
# drop columns that won't be used
colors.drop(columns=['Name', 'Hex (24 bit)', 'Hue (degrees)', 'HSL.S (%)','HSL.L (%), HSV.S (%), HSV.V (%)'], inplace=True)
# rename relevant columns for usability
colors.rename(columns={'Red (8 bit)': 'Red', 'Green (8 bit)': 'Green', 'Blue (8 bit)':'Blue'}, inplace=True)
# independent variable will be the rgb values
X = colors[['Red', 'Green', 'Blue']]

# color data will be clustered into simpler, basic color terms
# 11 clusters: red, orange, yellow, green, blue, violet, pink, brown, white, gray, black
centers = [[255, 0, 0], [255, 127, 0], [255, 255, 0], [0, 255, 0], [0, 0, 255], [165, 0, 255], \
           [255, 0, 255], [127, 63, 0], [255, 255, 255], [127, 127, 127], [0, 0, 0]]
# centers = [[218, 34, 79], [228, 125, 44], [255, 255, 0], [0, 255, 0], [0, 0, 255], [165, 0, 255], \
        #    [255, 0, 255], [127, 63, 0], [255, 255, 255], [127, 127, 127], [0, 0, 0]]
namer = KMeans(n_clusters=11, n_init=1, init=centers, random_state=255)
namer.fit(X)
# add these as a column in the dataframe
colors['Name'] = namer.labels_

# this code was used to check what color each of these labels corresponds to for manual naming
min_rgb = colors.groupby(['Name']).min()
mean_rgb = colors.groupby(['Name']).mean()
max_rgb = colors.groupby(['Name']).max()

# 0=red, 1=orange, 2=yellow, 3=green, 4=blue, 5=violet, 6=pink, 7, 