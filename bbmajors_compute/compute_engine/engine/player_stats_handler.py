###############################################################################
# Functions to parse pga tour website, find birdie average for each player, and
# put into dictionary of player stats
###############################################################################

from urllib.request import urlopen 
import re
from bs4 import BeautifulSoup as bsoup

#Birdie Percentage Stat
STATS_URL = "http://www.pgatour.com/stats/stat.352.html"

# Assumptions:
#     -Correct place on pga tour website to get birdie avg stat is STATS_URL
def create_stats_dict():
    #read birdie stats from pgatour.com
    html = urlopen(STATS_URL)
    #use BeautifulSoup library to parse html
    soup = bsoup(html, features="html.parser")
    player_rows = soup.findAll('tr', {"id" : re.compile("playerStatsRow(.*)")})

    stats_dict = create_stats_dict_from_html(player_rows)
        
    return stats_dict

def create_stats_dict_from_html(player_rows):
    stats_dict = {}
    for player_row in player_rows:
        cells = player_row.findAll('td')
        player_name = cells[2].text
        player_name = player_name.replace("&nbsp;", " ")
        player_name = player_name.replace(".", "")
        player_name = player_name.replace("\n", "")
        if player_name[-4:] == " III":
            player_name = player_name.replace(" III", "")
        birdie_pct_str = cells[4].text
        if player_name in stats_dict:
            #duplicate
            pass
        stats_dict[player_name] = birdie_pct_str
        
    return stats_dict