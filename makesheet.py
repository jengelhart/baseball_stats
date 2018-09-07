import json
import csv
import pandas

with open('lineups.json') as a:
    lineups = json.load(a)

stats = pandas.read_csv('FanGraphs Leaderboard.csv')

with open('offense.csv', 'w', newline='') as csvfile:
    fw = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    fw.writerow(['team', 'name', 'PA', 'BsR', 'wOBA'])

    for game in lineups:
        away_team = game['away-team']
        for player in game['away-lineup']:
            player_stats = stats.loc[stats['Name'].str.contains(player)]
            if not player_stats.empty:
                fw.writerow([away_team, player, 600, player_stats.iloc[0]['BsR'], player_stats.iloc[0]['wOBA']])
            else:
                fw.writerow([away_team, player, 600])
        home_team = game['home-team']
        for player in game['home-lineup']:
            player_stats = stats.loc[stats['Name'].str.contains(player)]
            if not player_stats.empty:
                fw.writerow([home_team, player, 600, player_stats.iloc[0]['BsR'], player_stats.iloc[0]['wOBA']])
            else:
                fw.writerow([home_team, player, 600])