
class Captain:

    def __init__(self, coord):
        self.coord = coord

    def __str__(self):
        return str(self.coord)

    def can_move(self, new_coord, occ):

        # we list all cases where it will be false and at the end return true if nothing wrong happened

        if new_coord[0] < 0 or new_coord[0] > 4 or new_coord[1] < 0 or new_coord[1] > 4:
            return False
        if self.coord == new_coord:
            return False
        dx = new_coord[0] - self.coord[0]
        dy = new_coord[1] - self.coord[1]
        if dx not in [-1,0,1] or dy not in [-1,0,1]:
                return False

        if new_coord in occ:
            if [(new_coord[0] + dx) % 5, (new_coord[1] + dy) % 5] in occ:
                return False
            if dx * dy != 0:        # diagonal case
                if self.coord[0] + dx in occ or self.coord[1] + dy in occ:
                    return False

        return True

    def generate_possible_moves(self, occ):
        moves = []
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                new_coord = [self.coord[0] + dx, self.coord[1] + dy]
                if self.can_move(new_coord, occ):
                    moves.append(new_coord)
        return moves

    def distance_to(self, pos, occ):  # doesn't use occ
        dx = abs(pos[0] - self.coord[0])
        dy = abs(pos[1] - self.coord[1])
        diag = min(dx, dy)
        return (diag + (dx - diag) + (dy - diag))