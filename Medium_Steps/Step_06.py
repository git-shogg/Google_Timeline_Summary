###############################################################################
#          6. Remove Weekday Exceptions and Aggregate the Results             #
###############################################################################
# Remove Weekday Exceptions
if weekday_exceptions != None:
    df = df[~df.weekday.isin(weekday_exceptions)]

# Aggregate the Results
df = df.groupby(aggregate_list).agg({'timestamp':['count'],'distance':['mean']})