from Player import Player
import random
from winsound import *
from copy import copy, deepcopy
import itertools

#sound_push = lambda: PlaySound(r'C:\Users\kael chiche the bada\PycharmProjects\Game_with_Val\game extra\sounds\YEET', SND_ASYNC)

class Game:

    def __init__(self,sound=None, player1_init = Player(None, [0,2], [0,0], [0,4], [0,1], [0,3]), player2_init = Player(None, [4,2], [4,0], [4,4], [4,1], [4,3])):
        self.sound = sound
        self.score = 0
        self.turn = int(random.random()*2+1)
        self.player1 = player1_init
        self.player2 = player2_init
        print("player "+ str(self.turn) +" it's your turn !")
        print(self.to_GUI())

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result

    def __str__(self):
        return "score = " + str(self.score) + "\nplayer1 = " + str(self.player1)  + "\nplayer2 = " + str(self.player2)

    def same_cards(self):
        same = 0
        for pos in self.player1.goal:
            if pos in self.player2.goal:
                same += 1
        return same

    def pion_to_string(self, pion):
        if pion == self.player1.captain:
            return "player 1 capain"
        if pion == self.player1.pyramid1 or pion == self.player1.pyramid2:
            return "player 1 pyramid"
        if pion == self.player1.pilot1 or pion == self.player1.pilot2:
            return "player 1 pilot"
        if pion == self.player2.captain:
            return "player 2 capain"
        if pion == self.player2.pyramid1 or pion == self.player2.pyramid2:
            return "player 2 pyramid"
        if pion == self.player2.pilot1 or pion == self.player2.pilot2:
            return "player 2 pilot"

    def who_there(self, coord): # return a who is at this location or None if nothing is there
        if(self.player1.captain.coord == coord):
            return self.player1.captain
        elif (self.player1.pyramid1.coord == coord):
            return self.player1.pyramid1
        elif (self.player1.pyramid2.coord == coord):
            return self.player1.pyramid2
        elif (self.player1.pilot1.coord == coord):
            return self.player1.pilot1
        elif (self.player1.pilot2.coord == coord):
            return self.player1.pilot2
        elif (self.player2.captain.coord == coord):
            return self.player2.captain
        elif (self.player2.pyramid1.coord == coord):
            return self.player2.pyramid1
        elif (self.player2.pyramid2.coord == coord):
            return self.player2.pyramid2
        elif (self.player2.pilot1.coord == coord):
            return self.player2.pilot1
        elif (self.player2.pilot2.coord == coord):
            return self.player2.pilot2

    def is_right_turn(self, pion):
        if self.turn == 1 and pion in [self.player1.captain, self.player1.pilot1, self.player1.pilot2, self.player1.pyramid1, self.player1.pyramid2]:
                return True
        if self.turn == 2 and pion in [self.player2.captain, self.player2.pilot1, self.player2.pilot2, self.player2.pyramid1, self.player2.pyramid2]:
                return True
        return False

    def move(self, pion, location):
        if not self.is_right_turn(pion):
            print("not your turn !")
            return None
        occ = self.get_occupied()
        if pion == self.player1.captain or pion == self.player2.captain:    # if pion is a captain
            if pion.can_move(location, occ):
                if location in occ:
                    if self.sound != None:
                        self.sound.play_push()
                    other_pion = self.who_there(location)
                    dx = location[0] - pion.coord[0]
                    dy = location[1] - pion.coord[1]
                    other_pion.coord = [(location[0] + dx) % 5, (location[1] + dy) %5]
                else:
                    if self.sound != None:
                        self.sound.play_move()
                pion.coord = location
            else:
                print("this move is not possible")
                print(self.to_GUI())
                print(location)
                return False
        else:                                    # if pion is not a captain
            if pion.can_move(location, occ):
                pion.coord = location
                if self.sound != None:
                    self.sound.play_move()
            else:
                print("this move is not possible")
                print(self.to_GUI())
                print(location)
                return False
        self.change_turn()
        #print(self.to_GUI())

    def change_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
        #print("player " + str(self.turn) + " it's your turn !")
        score=+1

    def get_occupied(self): # return list of occupied coordinates
        occ = [self.player1.captain.coord,self.player1.pilot1.coord,self.player1.pilot2.coord,self.player1.pyramid1.coord,self.player1.pyramid2.coord,self.player2.captain.coord,self.player2.pilot1.coord,self.player2.pilot2.coord,self.player2.pyramid1.coord,self.player2.pyramid2.coord]
        return occ

    def to_GUI(self):
        return {'player1_captain': self.player1.captain.coord, 'player1_pyramid1': self.player1.pyramid1.coord, 'player1_pyramid2': self.player1.pyramid2.coord, 'player1_pilot1': self.player1.pilot1.coord, 'player1_pilot2': self.player1.pilot2.coord,
                'player2_captain': self.player2.captain.coord, 'player2_pyramid1': self.player2.pyramid1.coord, 'player2_pyramid2': self.player2.pyramid2.coord, 'player2_pilot1': self.player2.pilot1.coord, 'player2_pilot2': self.player2.pilot2.coord}

    #def generate_card():

    def clicking_player1_captain():
        print("clicked payer1 captain")

    def winner(self):  # return 1 for player1, 2 for player 2, None or 0 for both
        winner1 = self.player1.winner()
        #winner1 = True
        winner2 = self.player2.winner()
        #winner2 = True
        if winner1 and winner2:
            return 0
        if winner1:
            return 1
        if winner2:
            return 2
        return None


    def get_state(self): # an np array of shape (10,1)
        return np.array(self.player1.get_state() + self.player2.get_state()).reshape(1,10)

    def distance_to_goal(self, player):
        distance = 800
        pions = list(player.get_all_pions().values())
        goal_permutations = tuple(itertools.permutations(player.goal))
        occ = self.get_occupied()
        for goal in goal_permutations:
            distance_temp = 0
            for i in range(5):
                add_to_distance_temp = pions[i].distance_to(goal[i], occ)
                distance_temp += add_to_distance_temp
            if distance_temp < distance:
                distance = distance_temp
                goal_temp = tuple(goal)
        return distance, goal_temp

    def num_moves_to(self, player, goal_ordered, distance): # garbage for now
        pions = list(player.get_all_pions.values())
        occ = self.get_occupied()
        num = 0
        for i in range(5):
            pion = pions[i]
            pion_str = self.game.player2.get_pion_str(pion)
            possible_moves = pion.generate_possible_moves(occ)

            for move in possible_moves:
                game_temp = deepcopy(self.game)
                game_temp.sound = None
                game_temp.turn = 2

            add_to_num = pion[i].num_moves_to(goal[i], occ)
            num += add_to_num
        return num

