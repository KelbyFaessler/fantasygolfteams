###############################################################################
# Types to be used in both python and cython code for computing teams
###############################################################################

class Player:
    def __init__(self, name: str='', cost: float=0.0, birdie_avg: float=0.0):
        self.name = name
        self.cost = cost
        self.birdie_avg = birdie_avg

class PlayerPair:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.total_cost = self.player1.cost + self.player2.cost
        self.total_birdie_avg = self.player1.birdie_avg + self.player2.birdie_avg

class PlayerTeam:
    def __init__(self, player1: Player, player2: Player, player3: Player, player4: Player):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.total_cost = ( self.player1.cost + 
                            self.player2.cost + 
                            self.player3.cost + 
                            self.player4.cost)
        self.total_birdie_avg = (self.player1.birdie_avg + 
                                    self.player2.birdie_avg + 
                                    self.player3.birdie_avg + 
                                    self.player4.birdie_avg)  