Setup
1. Get your location history from Google Takeout (https://takeout.google.com/). 
    1.a. Navigate to Google Takeout webpage.
    1.b. Navigate to New Export. 
    1.c. Deselect all exports.
    1.d. Find and select the "Location History".
    1.e. Scroll to the bottom of the screen and select "Next Step".
    1.f. Click "Create Export".
2. Now that you've downloaded your takeout file copy and paste it into the same location as this script. Unzip it and copy and paste the "Location History.json" file into the same folder directory as the main.py.

An example of how this function could be used is as follows:

Find all of the times you have been within 10,000 kms of the Sydney Opera house since the 1st of July 2021 according to your Google Timeline Data.

df = df_google_timeline_summary((-33.85538908610386, 151.21570005901881),start_date='01/07/2021',distance_from_point_of_interest=10000)