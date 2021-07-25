###############################################################################
#                          4. Unpack the Data                                 #
###############################################################################
df_rows = []
for key in locations:
    timestamp = float(key['timestampMs'])
    latitude = float(key['latitudeE7'])/10000000
    longitude = float(key['longitudeE7'])/10000000
    
    if timestamp >= start_datetime and timestamp <= end_datetime:
        df_rows.append([timestamp,latitude,longitude])

df = pd.DataFrame(df_rows,columns=['timestamp','latitude','longitude'])