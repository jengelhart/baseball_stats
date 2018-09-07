To use this program:
1) Make  sure scrapy is installed:
    pip3 install scrapy
2) Download "FanGraphs Leaderboard.csv", and place it in the same directory as the python source files:
    https://www.fangraphs.com/projections.aspx?pos=all&stats=bat&type=steamer600u&team=0&lg=all&players=0
3) Generate today's lineup:
    a) delete any previously generated json files
    b) scrapy runspider lineups.py -o lineups.json
4) Generate a spreadsheet with selected metrics by player
    python makesheet.py
