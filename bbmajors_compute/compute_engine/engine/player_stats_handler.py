###############################################################################
# Functions to parse pga tour website, find birdie average for each player, and
# put into dictionary of player stats
###############################################################################

import requests
import requests_cache
import re
from bs4 import BeautifulSoup as bsoup

#Birdie Percentage Stat
STATS_URL = "http://www.pgatour.com/stats/stat.352.html"

#Url made by ajax call on page after selecting stat year in dropdown menu
#Url is split in half to allow string concatenation with the desired year in the middle
YEAR_URL_FIRST_HALF = "https://www.pgatour.com/stats/stat/jcr:content/mainParsys/details.352.y"
YEAR_URL_SECOND_HALF = ".scontent.html"

class PlayerStats:
    def __init__(self, rounds, birdie_avg):
        self.rounds = rounds
        self.birdie_avg = birdie_avg

def find_current_year(soup):
    season_elems = soup.find_all('div', class_='season')
    for season_elem in season_elems:
        for elem in season_elem.descendants:
            if elem.name == 'option' and 'selected' in elem.attrs:
                return elem.text

def get_players_from_html(soup, players_each_year, year):
    #use BeautifulSoup library to parse html
    player_rows = soup.findAll('tr', {"id" : re.compile("playerStatsRow(.*)")})
    players_each_year[year] = player_rows

# Assumptions:
#     -Correct place on pga tour website to get birdie avg stat is STATS_URL
def create_stats_dict():
    requests_cache.install_cache(expire_after=86400)

    html = requests.get(STATS_URL)
    soup_current_year = bsoup(html.text, features="html.parser")
    current_year = find_current_year(soup_current_year) 
    current_year_int = int(current_year)
    html_year_minus_1 = requests.get(YEAR_URL_FIRST_HALF + str(current_year_int - 1) + YEAR_URL_SECOND_HALF)
    html_year_minus_2 = requests.get(YEAR_URL_FIRST_HALF + str(current_year_int - 2) + YEAR_URL_SECOND_HALF)

    stats_dict = {}
    players_each_year = {}

    get_players_from_html(soup_current_year, players_each_year, current_year_int)
    soup_year_minus_1 = bsoup(html_year_minus_1.text, features="html.parser")
    get_players_from_html(soup_year_minus_1, players_each_year, current_year_int - 1)
    soup_year_minus_2 = bsoup(html_year_minus_2.text, features="html.parser")
    get_players_from_html(soup_year_minus_2, players_each_year, current_year_int - 2)

    for year, players in players_each_year.items():
        for player_row in players:
            cells = player_row.findAll('td')
            player_name = cells[2].text
            player_name = player_name.replace("&nbsp;", " ")
            player_name = player_name.replace(".", "")
            player_name = player_name.replace("\n", "")
            if player_name[-4:] == " III":
                player_name = player_name.replace(" III", "")

            if player_name not in stats_dict:
                stats_dict[player_name] = {}

            birdie_pct_current_str = cells[4].text
            player_num_rounds_str = cells[3].text

            stats_dict[player_name][year] = PlayerStats(int(player_num_rounds_str), float(birdie_pct_current_str))

               
    # Calculate weighted averages for birdie %'s and store in birdie_dict indexed by player name.
    # This will ultimately be what is returned
    birdie_dict = {}
    for player_name, stats_per_year_dict in stats_dict.items():
        num_years_of_stats = 3   # based on stats recorded above
        birdie_pct = 0.0
        enough_current_year_rounds = False
        if current_year_int in stats_per_year_dict and stats_per_year_dict[current_year_int].rounds >= 35:
            enough_current_year_rounds = True
        if len(stats_per_year_dict) == num_years_of_stats:
            # Check if there are enough rounds played by this player in current year to use significant
            # weight for current year's stats. If not, reduce weight of current year's stats
            if enough_current_year_rounds:
                birdie_pct = (0.35 * stats_per_year_dict[current_year_int].birdie_avg +
                              0.45 * stats_per_year_dict[current_year_int - 1].birdie_avg +
                              0.20 * stats_per_year_dict[current_year_int - 2].birdie_avg)
            else:
                birdie_pct = (0.20 * stats_per_year_dict[current_year_int].birdie_avg +
                              0.60 * stats_per_year_dict[current_year_int - 1].birdie_avg +
                              0.20 * stats_per_year_dict[current_year_int - 2].birdie_avg)
        else:
            # Don't have full 3 years of stats for player. Determine which stats are available and use them
            if (current_year_int in stats_per_year_dict) and ((current_year_int - 1) in stats_per_year_dict):
                if enough_current_year_rounds:
                    birdie_pct = (0.40 * stats_per_year_dict[current_year_int].birdie_avg +
                                  0.60 * stats_per_year_dict[current_year_int - 1].birdie_avg)
                else:
                    birdie_pct = (0.20 * stats_per_year_dict[current_year_int].birdie_avg +
                                  0.80 * stats_per_year_dict[current_year_int - 1].birdie_avg)
            elif (current_year_int in stats_per_year_dict) and ((current_year_int -2) in stats_per_year_dict):
                if enough_current_year_rounds:
                    birdie_pct = (0.40 * stats_per_year_dict[current_year_int].birdie_avg +
                                  0.60 * stats_per_year_dict[current_year_int - 2].birdie_avg)
                else:
                    birdie_pct = (0.20 * stats_per_year_dict[current_year_int].birdie_avg +
                                  0.80 * stats_per_year_dict[current_year_int - 2].birdie_avg)
            elif ((current_year_int - 1) in stats_per_year_dict) and ((current_year_int - 2) in stats_per_year_dict):
                birdie_pct = (0.80 * stats_per_year_dict[current_year_int - 1].birdie_avg +
                              0.20 * stats_per_year_dict[current_year_int - 2].birdie_avg)
            elif current_year_int in stats_per_year_dict:
                if enough_current_year_rounds:
                    birdie_pct = stats_per_year_dict[current_year_int].birdie_avg
                else:
                    birdie_pct = 0.0
            elif (current_year_int - 1) in stats_per_year_dict:
                birdie_pct = stats_per_year_dict[current_year_int - 1].birdie_avg
            elif (current_year_int - 2) in stats_per_year_dict:
                birdie_pct = stats_per_year_dict[current_year_int - 2].birdie_avg

        birdie_dict[player_name] = str(birdie_pct)
       
    return birdie_dict
