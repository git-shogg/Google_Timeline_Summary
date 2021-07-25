###############################################################################
#                          2. User Inputs                                     #
###############################################################################
start_year, start_month, start_day = 2021, 6, 30
end_year, end_month, end_day = 2021, 7, 25
point_of_interest = (-77.85, 166.64)  # Latitude, Longitude
distance_from_point_of_interest = 0.1
aggregate_by = 'Day'   # This can be 'Year', 'Month', 'Day', 'Hour', 'Second'
weekday_exceptions = ['Saturday','Sunday'] # A list of weekdays that should excluded.

# Reformat the start/end datetimes to epoch times in milliseconds
start_datetime = datetime.datetime(start_year,start_month,start_day).timestamp()*1e3
end_datetime = datetime.datetime(end_year,end_month,end_day).timestamp()*1e3

# Setup the aggregate list
aggregate_options = ['Year','Month','Day','Hour','Second']
aggregate_list = aggregate_options[:aggregate_options.index(aggregate_by)+1]