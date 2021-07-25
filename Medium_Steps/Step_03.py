###############################################################################
#                          3. Get Data                                        #
###############################################################################
json_file = "Location History.json"
data = json.load(open(json_file))   # Read the file
locations = data['locations']