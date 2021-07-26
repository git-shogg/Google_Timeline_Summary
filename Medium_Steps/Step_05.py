###############################################################################
#                          5. Setup Useful Columns                            #
###############################################################################
# Determine the distance of each GPS coordinate from your point of interest.
distances_list = []
for lat, long in zip(df['latitude'],df['longitude']):
    distances_list.append(distance.geodesic(point_of_interest,(lat,long)).km)
df['distance'] = distances_list
df = df[df['distance'] < distance_from_point_of_interest]

# Breakdown the timestamp (which was an epoch ms timestamp) to some useful time based columns.
df['timestamp'] = df['timestamp']/1000
df['datetime'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp),axis=1)
df['weekday'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp).strftime('%A'),axis=1)
df['Year'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp),axis=1).dt.year
df['Month'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp),axis=1).dt.month
df['Day'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp),axis=1).dt.day
df['Hour'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp),axis=1).dt.year
df['Minute'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp),axis=1).dt.year
df['Second'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp),axis=1).dt.year