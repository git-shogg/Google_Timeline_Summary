# Google Timeline Summary
## Overview:
The python function (in the main.py file) enables you to summarize your GPS location in relation to a point of interest for a given timeframe. 

## Setup:
1. Navigate [Google Takeout](https://takeout.google.com).
2. Deselect all of the data.

    ![google takeout](https://miro.medium.com/max/2160/1*G-OwQVIPMJtxYVfZxu03xA.png)
3. Scroll down until you find the "Location History". Select this data.
    ![location history](https://miro.medium.com/max/553/1*31avyKZtERYQePTiZHM7ow.png)
4. Scroll to the bottom of the webpage, click "Next Step".
5. Setup your delivery method, I just used Google's recommendation.
6. Wait for your download to be made available.
7. Once the download is available. Download it.
8. Open the zipped folder and extract the "Location History.json" file, place in the same working directory as the main.py.
9. You're ready to go!

## Quick Start:
Find all of the times you have been within 100 meters of the Sydney Opera house since the 1st of July 2021.

```
df = df_google_timeline_summary((-33.85538908610386, 151.21570005901881),start_date='01/07/2021',distance_from_point_of_interest=0.1)
```
## Author:
Stephen Hogg