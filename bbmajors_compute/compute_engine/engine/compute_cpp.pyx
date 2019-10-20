# distutils: language = c++
# cython: language_level=3

from libcpp.vector cimport vector

from .compute_cpp cimport CalculateCombinations2
from .compute_cpp cimport Player as PlayerCpp
from .compute_cpp cimport Team as TeamCpp

#from compute_types import Player as PlayerPy
#from compute_types import PlayerTeam as PlayerTeamPy
#from compute import Player as PlayerPy
#from compute import PlayerTeam as PlayerTeamPy

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

    #For now, print results
    #print("==================================== RESULTS ===================================")
    #for team in results_vector:
    #    print(f"Team birdie avg: {team.GetBirdieAvg()}")
    #    print(f"Team cost: {team.GetCost()}")
    #    print(f"Player: {team.GetPlayer1()}")
    #    print(f"Player: {team.GetPlayer2()}")
    #    print(f"Player: {team.GetPlayer3()}")
    #    print(f"Player: {team.GetPlayer4()}")
    #    print("--------------------------------------------")

    results_list = []
    cdef PlayerCpp player1Cpp
    cdef PlayerCpp player2Cpp
    cdef PlayerCpp player3Cpp
    cdef PlayerCpp player4Cpp
    for team in results_vector:
        players = []
        player1Cpp = team.GetPlayer1()
        players.append({'name': player1Cpp.name.decode("UTF-8"), 'cost': player1Cpp.cost, 'birdie_avg': player1Cpp.birdieAvg})
        #player1 = PlayerPy(player1Cpp.name, player1Cpp.cost, player1Cpp.birdieAvg)
        player2Cpp = team.GetPlayer2()
        players.append({'name': player2Cpp.name.decode("UTF-8"), 'cost': player2Cpp.cost, 'birdie_avg': player2Cpp.birdieAvg})
        #player2 = PlayerPy(player2Cpp.name, player2Cpp.cost, player2Cpp.birdieAvg)
        player3Cpp = team.GetPlayer3()
        players.append({'name': player3Cpp.name.decode("UTF-8"), 'cost': player3Cpp.cost, 'birdie_avg': player3Cpp.birdieAvg})
        #player3 = PlayerPy(player3Cpp.name, player3Cpp.cost, player3Cpp.birdieAvg)
        player4Cpp = team.GetPlayer4()
        players.append({'name': player4Cpp.name.decode("UTF-8"), 'cost': player4Cpp.cost, 'birdie_avg': player4Cpp.birdieAvg})
        #player4 = PlayerPy(player4Cpp.name, player4Cpp.cost, player4Cpp.birdieAvg)
        #results_list.append(PlayerTeamPy(player1, player2, player3, player4))
        results_list.append(players)
    
    return results_list