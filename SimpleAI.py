# Simple (non deep) Q-learning
# the AI is player 2 / RED

# State space = { captain: coord, pilot1 : coord, ..., pyramid2: coord, other_player: coords }

import time
#import numpy as np
from Game import Game
from Player import Player
from copy import copy, deepcopy

class SimpleAI():

    def __init__(self, game):
        self.game = game
        #self.game.distance_to_goal(self.game.player2)

    def compute_moves(self, game, num):
        #pion_optimum = game.player2.captain
        #move_optimum = -1
        #distance_optimum = 300

        all_of_them = []

        pions = list(game.player2.get_all_pions().values())
        occ = game.get_occupied()
        for i in range(len(pions)):
            pion_str = game.player2.get_pion_str(pions[i])
            possible_moves = tuple(pions[i].generate_possible_moves(occ))
            for j in range(len(possible_moves)):
                game_temp = deepcopy(game)
                game_temp.sound = None
                game_temp.turn = 2
                pion_temp = game_temp.player2.get_pion(pion_str)
                game_temp.move(pion_temp, list(possible_moves[j]))
                distance, goal = game_temp.distance_to_goal(game_temp.player2)
                all_of_them.append([distance, pion_str, tuple(possible_moves[j]), tuple(goal)])
                del(game_temp)
                del(pion_temp)

        all_of_them.sort()
        [distance0, pion_str0,move0,goal0] = all_of_them[0]
        if num == 1:
            if distance0 == 0:
                return 19/20
            return distance0
        if distance0 == 0:
            return 1/num
        else:
            for i in range(min(num, len(all_of_them))):
                #[distance, pion_str, move, goal] = all_of_them[i]
                game_temp = deepcopy(game)
                game_temp.sound = None
                game_temp.turn = 2
                pion_temp = game_temp.player2.get_pion(all_of_them[i][1])
                ok = game_temp.move(pion_temp, list(all_of_them[i][2])) # wants to move where it already is
                all_of_them[i][0] = self.compute_moves(game_temp, int(num / 2))
                del (game_temp)
                del (pion_temp)

            all_of_them.sort()
            return all_of_them[0][0]


    def compute_optimal_moves_initial(self, num):
        #pion_optimum = self.game.player2.captain
        #move_optimum = -1
        #distance_optimum = 300

        all_of_them = []

        pions = list(self.game.player2.get_all_pions().values())
        occ = self.game.get_occupied()
        for i in range(len(pions)):
            pion_str = self.game.player2.get_pion_str(pions[i])
            possible_moves = pions[i].generate_possible_moves(occ)
            for move in possible_moves:
                game_temp = deepcopy(self.game)
                #print(game_temp.to_GUI())
                game_temp.sound = None
                game_temp.turn = 2
                pion_temp = game_temp.player2.get_pion(pion_str)
                game_temp.move(pion_temp, list(move))
                distance, goal = game_temp.distance_to_goal(game_temp.player2)
                #distance = self.compute_moves(game_temp, num/2)
                all_of_them.append([distance, pion_str, tuple(move), tuple(goal)])
                #print('[dis, pion, move] = ' + str([distance, pion_str, move]))
                del (game_temp)
                del (pion_temp)


        all_of_them.sort()

        best = all_of_them[0]
        if best[0] == 0 or num == 1:
            return best
        else:
            for i in range(min(num, len(all_of_them))):
                #[distance, pion_str, move, goal] = all_of_them[i]
                game_temp = deepcopy(self.game)
                game_temp.sound = None
                game_temp.turn = 2
                pion_temp = game_temp.player2.get_pion(all_of_them[i][1])
                game_temp.move(pion_temp, list(all_of_them[i][2]))
                all_of_them[i][0] = self.compute_moves(game_temp, int(num / 2))
                del (game_temp)
                del (pion_temp)


            all_of_them.sort()
            return all_of_them[0]

    def make_a_move(self):

        best = self.compute_optimal_moves_initial(4)
        [distance_optimum, pion_optimum_str, move_optimum, goal_optimum] = best

        # want to look 4 moves ahead best 8,4,2,1


        pion_optimum = self.game.player2.get_pion(pion_optimum_str)
        print("moving " + pion_optimum_str + ' to ' + str(move_optimum))
        print('optimum distance = '+str(distance_optimum))

        self.game.move(pion_optimum, list(move_optimum))

        pions = list(self.game.player2.get_all_pions().values())
        print("goal = " + str(goal_optimum))
        for i in range(len(pions)):
            print("distance pion " + str(i) + ' = ' + str(pions[i].distance_to(goal_optimum[i], self.game.get_occupied())))