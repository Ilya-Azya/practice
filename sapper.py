import random


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

    def set_around_mines(self, count):
        self.around_mines = count

    def get_around_mines(self):
        return self.around_mines

    def set_mine(self, mine):
        self.mine = mine

    def get_mine(self):
        return self.mine

    def open(self):
        self.fl_open = True

    def is_open(self):
        return self.fl_open


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.field = [[Cell() for _ in range(N)] for _ in range(N)]
        self.init()

    def init(self):
        for row in self.field:
            for cell in row:
                cell.set_mine(False)
                cell.set_around_mines(0)
                cell.fl_open = False
        coords = [(i, j) for i in range(self.N) for j in range(self.N)]
        mines = random.sample(coords, self.M)
        for i, j in mines:
            self.field[i][j].set_mine(True)
        for i in range(self.N):
            for j in range(self.N):
                if self.field[i][j].get_mine():
                    continue
                count = 0
                for si in (-1, 0, 1):
                    for sj in (-1, 0, 1):
                        ni, nj = i + si, j + sj
                        if 0 <= ni < self.N and 0 <= nj < self.N:
                            if self.field[ni][nj].get_mine():
                                count += 1
                self.field[i][j].set_around_mines(count)

    def show(self):
        for i in range(self.N):
            row_field = []
            for j in range(self.N):
                cell = self.field[i][j]
                if not cell.is_open():
                    row_field.append('#')
                elif cell.get_mine():
                    row_field.append('*')
                else:
                    row_field.append(str(cell.get_around_mines()))
            print(' '.join(row_field))
