from Captain import Captain
from Pyramid import Pyramid
from Pilot import Pilot

class Player:

    def __init__(self, goal, captain_coord, pyramid1_coord, pyramid2_coord, pilot1_coord, pilot2_coord):
        self.goal = goal
        self.captain = Captain(captain_coord)
        self.pyramid1 = Pyramid(pyramid1_coord)
        self.pyramid2 = Pyramid(pyramid2_coord)
        self.pilot1 = Pilot(pilot1_coord)
        self.pilot2 = Pilot(pilot2_coord)

    def __str__(self):
        return "Goal: " + str(self.goal) + ", captain, pyramid1, pyramid2, pilot1, pilot2: " + str(self.captain) + str(self.pyramid1) +str(self.pyramid2) +str(self.pilot1) +str(self.pilot2)

    def winner(self):
        current = [self.captain.coord, self.pyramid1.coord, self.pyramid2.coord, self.pilot1.coord, self.pilot2.coord]
        for x in self.goal:
            if x not in current:
                return False
        return True

    def get_pion(self, pion_str):
        d = {'captain': self.captain, 'pyramid1': self.pyramid1, 'pyramid2': self.pyramid2, 'pilot1': self.pilot1,
             'pilot2': self.pilot2}
        return d[pion_str]

    def get_pion_str(self, pion):
        d = {'captain': self.captain, 'pyramid1': self.pyramid1, 'pyramid2': self.pyramid2, 'pilot1': self.pilot1,
             'pilot2': self.pilot2}
        for key in d:
            if d[key] == pion:
                return key
        return None

    def get_all_pions(self):
        d = {'captain': self.captain, 'pyramid1': self.pyramid1, 'pyramid2': self.pyramid2, 'pilot1': self.pilot1,
             'pilot2': self.pilot2}
        return d

    def get_occupying(self):
        occ = [self.captain.coord, self.pyramid1.coord, self.pyramid2.coord, self.pilot1.coord, self.pilot2.coord]
        return occ

    def get_state(self):  # shape (5,) [x,y] <-> x*5+y
        x = [self.coord_to_number(self.captain.coord), self.coord_to_number(self.pyramid1.coord),
             self.coord_to_number(self.pyramid2.coord),
             self.coord_to_number(self.pilot1.coord), self.coord_to_number(self.pilot2.coord)]
        return x

    def coord_to_number(self, coord):
        [x, y] = coord
        return x * 5 + y

    def number_to_coord(self, m):
        return [int(m / 5), m % 5]