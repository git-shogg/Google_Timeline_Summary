###############################################################################
#          6. Remove Weekday Exceptions and Aggregate the Results             #
###############################################################################
if weekday_exceptions != None:
    df = df[~df.weekday.isin(weekday_exceptions)]
df = df.groupby(aggregate_list).agg({'timestamp':['count'],'distance':['mean']}) 