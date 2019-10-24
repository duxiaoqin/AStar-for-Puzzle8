# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:37:54 2018

@author: duxiaoqin
Functions:
    (1)Puzzle8 class;
"""

from random import *
from myarray2d import Array2D

class Puzzle8:
    
    HEIGHT = 3
    WIDTH = 3
    ITEMS = [' ', '1', '2', '3', '4', '5', '6', '7', '8']
    GOAL = Array2D(HEIGHT, WIDTH)
    for row in range(HEIGHT):
        for col in range(WIDTH):
            GOAL[row, col] = ITEMS[row*WIDTH+col]
            
    def __init__(self, clone=False):
        self.__puzzle8 = Array2D(Puzzle8.HEIGHT, Puzzle8.WIDTH)
        self.__cost_so_far = 0
        self.__inversions = 0
        
        if (clone == False):
            self._genRandomItems()
            self._calcInversions()
            while self.__inversions % 2 != 0:
                self._genRandomItems()
                self._calcInversions()
            self.__heuristics = self._calcHeuristics()
        
    def _genRandomItems(self):
        items = Puzzle8.ITEMS[:]
        for row in range(Puzzle8.HEIGHT):
            for col in range(Puzzle8.WIDTH):
                index = randint(0, len(items)-1)
                item = items[index]
                self[row, col] = item
                if item == ' ':
                    self.__space = (row, col)
                items.remove(item)
                
    def _calcInversions(self):
        def merge_sort(items):
            if len(items) <= 1:
                return items
            pos = len(items) // 2
            half1 = items[:pos]
            half2 = items[pos:]
            left = merge_sort(half1)
            right = merge_sort(half2)
            return merge(left, right)
        
        def merge(left, right):
            list = []
            while len(left) > 0 and len(right) > 0:
                item1 = left[0]
                item2 = right[0]
                if item1 <= item2:
                    list.append(left.pop(0))
                else:
                    self.__inversions += len(left)
                    list.append(right.pop(0))
            list.extend(left)
            list.extend(right)
            return list

        self.__inversions = 0
        items = [int(self[row, col]) \
                     for row in range(Puzzle8.HEIGHT) \
                         for col in range(Puzzle8.WIDTH) \
                             if self[row, col] != ' ']
        merge_sort(items)

    def clone(self):
        new = Puzzle8(clone=True)
        for row in range(Puzzle8.HEIGHT):
            for col in range(Puzzle8.WIDTH):
                new[row, col] = self[row, col]
        new.__cost_so_far = self.__cost_so_far
        new.__heuristics = self.__heuristics
        new.__space = self.__space
        return new
    
    def isGoal(self):
        for row in range(Puzzle8.HEIGHT):
            for col in range(Puzzle8.WIDTH):
                if self[row, col] != Puzzle8.GOAL[row, col]:
                    return False
        return True
    
    def __lt__(self, other):#for PriorityQueue
        return self.heuristics < other.heuristics
    
    def _calcHeuristics(self):
        heuristics = 0
        for row in range(Puzzle8.HEIGHT):
            for col in range(Puzzle8.WIDTH):
                item = self[row, col]
                if item != ' ':
                    index = Puzzle8.ITEMS.index(item)
                    row1 = index // Puzzle8.WIDTH
                    col1 = index % Puzzle8.WIDTH
                    heuristics += abs(row1-row) + abs(col1-col)
        return heuristics
                
    def __getitem__(self, ndxTuple):
        return self.__puzzle8.__getitem__(ndxTuple)
    
    def __setitem__(self, ndxTuple, value):
        self.__puzzle8.__setitem__(ndxTuple, value)
        
    def numRows(self):
        return self.__puzzle8.numRows()
    
    def numCols(self):
        return self.__puzzle8.numCols()
    
    def getAllMoves(self):
        row = self.__space[0]
        col = self.__space[1]
        moves = []
        offsets = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        for x, y in offsets:
            x = col + x
            y = row + y
            if x < 0 or x > Puzzle8.WIDTH-1 or \
               y < 0 or y > Puzzle8.HEIGHT-1:
                continue
            moves.append((y, x))
        return moves
    
    def move(self, row, col):
        self[self.__space[0], self.__space[1]] = self[row, col]
        self[row, col] = ' '
        self.__space = (row, col)
        self.__cost_so_far += 1
        self.__heuristics = self._calcHeuristics()
        
    @property
    def cost(self):
        return self.__cost_so_far
    
    @property
    def heuristics(self):
        return self.__heuristics
    
    def ToString(self):
        items = [self[row, col] for row in range(Puzzle8.HEIGHT) \
                                    for col in range(Puzzle8.WIDTH)]
        return ''.join(items)

    def print(self):
        for row in range(Puzzle8.HEIGHT):
            for col in range(Puzzle8.WIDTH):
                print(self[row, col], end=' ')
            print()
    
def main():
    seed()
    puzzle8 = Puzzle8()
    puzzle8.print()
    Puzzle8.GOAL.print()
    print('cost=', puzzle8.cost)
    print('heuristics=', puzzle8.heuristics)
    for i in range(3):
        moves = puzzle8.getAllMoves()
        print(moves)
        puzzle8.move(*moves[randint(0, len(moves)-1)])
        print('cost=', puzzle8.cost)
        print('heuristics=', puzzle8.heuristics)
        puzzle8.print()
    
    print()
    
    new = puzzle8.clone()
    new.print()
    print('cost=', new.cost)
    print('heuristics=', new.heuristics)
    for i in range(3):
        moves = new.getAllMoves()
        print(moves)
        new.move(*moves[randint(0, len(moves)-1)])
        print('cost=', new.cost)
        print('heuristics=', new.heuristics)
        new.print()
    
if __name__ == '__main__':
    main()