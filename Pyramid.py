class Pyramid:

    def __init__(self, coord):
        self.coord = coord

    def __str__(self):
        return str(self.coord)

    def can_move(self, new_coord, occ):
        if new_coord[0] < 0 or new_coord[0] > 4 or new_coord[1] < 0 or new_coord[1] > 4:
            return False
        if new_coord in occ:
            return False
        if self.coord != new_coord:
            dx = new_coord[0] - self.coord[0]
            dy = new_coord[1] - self.coord[1]
            if dx in [1,2,-1,-2] and dy == 0 or dx == 0 and dy in [1,2,-1,-2]:
                return True
        else:
            return False

    def generate_possible_moves(self, occ):
        moves = []
        for dx in [-1, 1]:
            new_coord = [self.coord[0] + dx, self.coord[1]]
            if new_coord[0] >= 0 and new_coord[0] <= 4 and new_coord[1] >= 0 and new_coord[
                1] <= 4 and new_coord not in occ:
                moves.append(new_coord)
        for dx in [-2, 2]:
            new_coord = [self.coord[0] + dx, self.coord[1]]
            on_the_way = [self.coord[0] + dx / 2, self.coord[1]]
            if new_coord[0] >= 0 and new_coord[0] <= 4 and new_coord[1] >= 0 and new_coord[
                1] <= 4 and new_coord not in occ and on_the_way not in occ:
                moves.append(new_coord)
        for dy in [-1, 1]:
            new_coord = [self.coord[0], self.coord[1] + dy]
            if new_coord[0] >= 0 and new_coord[0] <= 4 and new_coord[1] >= 0 and new_coord[
                1] <= 4 and new_coord not in occ:
                moves.append(new_coord)
        for dy in [-2, 2]:
            new_coord = [self.coord[0], self.coord[1] + dy]
            on_the_way = [self.coord[0], self.coord[1] + dy / 2]
            if new_coord[0] >= 0 and new_coord[0] <= 4 and new_coord[1] >= 0 and new_coord[
                1] <= 4 and new_coord not in occ and on_the_way not in occ:
                moves.append(new_coord)
        return moves

    def distance_to(self, pos, occ):
        pos = list(pos)
        if pos == self.coord:
            return 0
        x = self.coord[0]
        y = self.coord[1]
        dx = pos[0] - x
        dy = pos[1] - y
        d = int(abs(dx / 2)) + (dx % 2) + int(abs(dy / 2)) + (dy % 2)
        # add bad points if going towards and occupied spot
        if pos in occ and pos != [x, y]:
            d += 5
        # add bad points if there is something on the way
        for i in range(abs(dx) + 1):
            for j in range(abs(dy) + 1):
                p = [x + i*sign(dx), y + j*sign(dy)]
                if p != [x, y] and p in occ:
                    d += 2
        return d

def sign(z):
    if z >= 0:
        return 1
    else:
        return -1