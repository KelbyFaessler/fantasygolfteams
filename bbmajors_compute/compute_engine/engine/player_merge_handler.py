###############################################################################
# Functions to merge player costs data with player stats data into one set of
# player data
###############################################################################

from .compute_types import Player

def merge_player_data(costs_dict, stats_dict):
    player_list = []
    player_not_found_list = []
    for player_key in costs_dict:
        if player_key in stats_dict:
            new_player = Player(player_key, float(costs_dict[player_key]), float(stats_dict[player_key]))
            player_list.append(new_player)
        else:
            player_not_found_list.append(player_key)

    return (player_list, player_not_found_list)

def create_results_dict(results_list):
    pass