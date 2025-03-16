# Mario Kart Leaderboard Merger

This project utilizes Python to merge and sort region-based leaderboard CSV files for Mario Kart. The leaderboard information was gathered from https://www.mkleaderboards.com/. The script reads manually created CSV files containing player rankings and times, merges them into a single leaderboard, and outputs a new CSV file with the merged data. The merged leaderboard is sorted by time, with the fastest times ranked at the top. The program supports multiple input files and allows for flexible handling of leaderboard data from various regions.

The base file, **leaderboardRanker.py**, does not allow for user input; instead, it reads the American and European leaderboard files that come with the project. The second version of the file, **leaderboardRanker2.py**, allows the user to provide the paths to the leaderboard files they'd like to use. (NOTE: The files must follow the same template as the exemplary files: **AmericaTop10Leaderboard.csv** and **EuropeTop10Leaderboard.csv**.)

## Python Script Usage Instructions
leaderboardRanker.py (**WITHOUT** user input):
  1. Place the script **leaderboardRanker.py** in a folder with the **AmericaTop10Leaderboard.csv** and **EuropeTop10Leaderboard.csv** files.
  2. Ensure the CSV files follow the correct format, with columns labeled "Player" and "Time."
  3. Run the script.
  4. The script will read the CSV files and merge them based on time.
  5. A new CSV file, **mergedLeaderboard.csv**, will be generated in the same folder, containing the merged and sorted leaderboard.
  6. The merged leaderboard will be printed in the console, with the rankings displayed from fastest to slowest time.

leaderboardRanker2.py (**WITH** user input)
  1. Place the script **leaderboardRanker2.py** in a folder with the leaderboard CSV files you want to merge.
  2. Run the script.
  3. You will be prompted to enter the file paths for two region-based leaderboard CSV files.
  4. **Ensure the CSV files follow the correct format, with columns labeled "Player" and "Time."**
  5. The script will read the CSV files, merge them based on time, and generate a new leaderboard.
  6. The merged leaderboard will be printed in the console, sorted from fastest to slowest time.
  7. A new CSV file, **mergedleaderboard.csv**, will be created in the same folder, containing the merged leaderboard data.

## Prerequisites

Make sure you have the following library installed:

- [Pandas](https://pypi.org/project/pandas/)

You can install it using:

    pip install pandas

<br></br>
