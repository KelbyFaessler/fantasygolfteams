# distutils: language = c++
# cython: language_level=3

from libcpp.vector cimport vector

from .compute_cpp cimport CalculateCombinations2
from .compute_cpp cimport Player as PlayerCpp
from .compute_cpp cimport Team as TeamCpp


def CalculateCombinationsCpp(players_list, num_teams):
    cdef vector[PlayerCpp] players_vector
    cdef PlayerCpp newPlayerCpp
    for player in players_list:
        newPlayerCpp.name = player.name.encode("UTF-8")
        newPlayerCpp.cost = player.cost
        newPlayerCpp.birdieAvg = player.birdie_avg
        players_vector.push_back(newPlayerCpp)
    cdef vector[Team] results_vector
    CalculateCombinations2(players_vector, results_vector, num_teams)

    results_list = []
    cdef PlayerCpp playerCpp
    for team in results_vector:
        players = []
        num_players = team.GetNumPlayers()
        for player_index in range(0, num_players):
            playerCpp = team.GetPlayer(player_index)
            players.append({'name': playerCpp.name.decode("UTF-8"), 'cost': playerCpp.cost, 'birdie_avg': playerCpp.birdieAvg})
        results_list.append(players)
    
    return results_list