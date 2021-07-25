###############################################################################
#                          5. Setup Useful Columns                            #
###############################################################################
df['distance'] = df.apply(lambda row: distance.geodesic(point_of_interest, (row.latitude, row.longitude)).km, axis=1)   # https://stackoverflow.com/questions/51425127/pandas-go-through-2-columns-latitude-and-longitude-and-find-the-distance-bet/57106028
df = df[df['distance'] < distance_from_point_of_interest]
df['datetime'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1)
df['weekday'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3).strftime('%A'),axis=1)
df['Year'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1).dt.year
df['Month'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1).dt.month
df['Day'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1).dt.day
df['Hour'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1).dt.year
df['Minute'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1).dt.year
df['Second'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1).dt.year