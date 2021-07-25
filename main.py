import json
import datetime
import pandas as pd
from geopy import distance

def df_google_timeline_summary(point_of_interest, start_date,end_date=None,distance_from_point_of_interest=0.1, aggregate_by='Day',weekday_exceptions=None):
    '''
    Arguments:
        - point_of_interest (tuple): Latitude and Longitude. Example: (-77.85, 166.64).
        - distance_from_point_of_interest (float): The distance in meters from the point of interest that you would like to include in the timeline summary. Example: 0.1.
        - start_date (str): The start date filter to be applied, formatted 'DD/MM/YYYY'. Example: '10/07/2021'.
        - end_date (str): The end date filter to be applied, formatted 'DD/MM/YYYY'. Defaults to today's date. Example: '25/07/2021'. 
        - aggregate_by (str): The timeframe that should be used for aggregating the timeline history. Options: 'Year','Month','Day','Hour','Second'. 
        - weekday_exceptions (list): Any weekdays you would like to entirely exclude from the timeline summary. Example: ['Saturday', 'Sunday'].
    Returns:
        - Pandas Dataframe (df): A pandas dataframe that aggregates and summarizes the timeline history between two dates for a point of interest (excluding any weekday exceptions).
    '''
    # Exceptions
    aggregate_options = ['Year','Month','Day','Hour','Second']
    if aggregate_by not in aggregate_options:
        raise ValueError("Invalid aggregate_by type. Expected one of: %s" % aggregate_options)

    # User inputs
    start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y')
    if end_date == None:
        end_date = datetime.datetime.today()
    start_year, start_month, start_day = start_date.year, start_date.month, start_date.day
    end_year, end_month, end_day = end_date.year, end_date.month, end_date.day
    
    # Reformat the start/end datetimes to epoch times in milliseconds
    start_datetime = datetime.datetime(start_year,start_month,start_day).timestamp()*1e3
    end_datetime = datetime.datetime(end_year,end_month,end_day).timestamp()*1e3

    # Setup the aggregate list
    aggregate_list = aggregate_options[:aggregate_options.index(aggregate_by)+1]

    # Get the data
    json_file = "Location History.json"
    data = json.load(open(json_file))   # Read the file
    locations = data['locations']

    # Unpack the data
    df_rows = []
    for key in locations:
        timestamp = float(key['timestampMs'])
        latitude = float(key['latitudeE7'])/10000000
        longitude = float(key['longitudeE7'])/10000000
        
        if timestamp >= start_datetime and timestamp <= end_datetime:
            df_rows.append([timestamp,latitude,longitude])

    df = pd.DataFrame(df_rows,columns=['timestamp','latitude','longitude'])

    # Setup Useful Columns
    df['distance'] = df.apply(lambda row: distance.geodesic(point_of_interest, (row.latitude, row.longitude)).km, axis=1)
    df = df[df['distance'] < distance_from_point_of_interest]
    df['datetime'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1)
    df['weekday'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3).strftime('%A'),axis=1)
    df['Year'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1).dt.year
    df['Month'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1).dt.month
    df['Day'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1).dt.day
    df['Hour'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1).dt.year
    df['Minute'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1).dt.year
    df['Second'] = df.apply(lambda row: datetime.datetime.fromtimestamp(row.timestamp/1e3),axis=1).dt.year

    # Remove Weekday Exceptions and Aggregate the Results
    if weekday_exceptions != None:
        df = df[~df.weekday.isin(weekday_exceptions)]
    df = df.groupby(aggregate_list).agg({'timestamp':['count'],'distance':['mean']})
    
    return df

df = df_google_timeline_summary((-27.464032634820306, 153.03057999435137),start_date='01/07/2019',weekday_exceptions=['Saturday'])
print(df)