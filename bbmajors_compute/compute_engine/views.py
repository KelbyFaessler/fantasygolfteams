from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .forms import TeamForm

from .engine.player_costs_handler import create_costs_dict
from .engine.player_stats_handler import create_stats_dict
from .engine.player_merge_handler import merge_player_data, create_results_dict

# Cython modules
from .engine.compute_cpp import CalculateCombinationsCpp

@login_required
def players(request):
    """
    page where player information is input so best teams
    can be calculated
    """
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('teams')
    else:
        form = TeamForm()

    return render(
        request,
        'teams.html',
        context={'form': form}
    )

@login_required
def teams(request):
    """
    page where best teams are calculated
    """
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('teams')

    return render(
        request,
        'teams.html',
        context={}
    )

def calculate_teams(request):
    #extract num_teams and players from request
    num_teams = request.POST.get('num_teams', 10)
    players_raw = request.POST.get('players', '')

    results_list = []
    players_not_found = []

    if (players_raw):
        #call calculation functions
        player_costs = create_costs_dict(players_raw)
        # for player in player_costs:
        #     print(f"{player} {player_costs[player]}")

        player_stats = create_stats_dict()
        #TODO: remove print statement
        # for player in player_stats:
        #     print(f"{player}: {player_stats[player]}")

        players = []
        
        players, players_not_found = merge_player_data(player_costs, player_stats)
        #for player in players:
        #    print(f"{player}")
        results_list = CalculateCombinationsCpp(players, int(num_teams))
        if not results_list:
            print("results list empty")
        for team in results_list:
            print(team)
        #results_dict = create_results_dict(results_list)
        

    #return data to requestor
    data = {
        'num_teams': num_teams
    }

    #if results_dict:
    #    data['teams'] = results_dict
    if results_list:
        data['teams'] = results_list
        
    if players_not_found:
        data['players_not_found'] = players_not_found

    return JsonResponse(data)