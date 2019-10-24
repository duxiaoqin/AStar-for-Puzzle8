# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 15:25:43 2018

@author: duxiaoqin
Functions:
    (1)A* class for 8 puzzle
"""

from time import *
from random import *
from priorityqueue import PriorityQueue
from stack import Stack
from puzzle8 import *
from puzzle8draw import *
from graphics import *

def Astar(puzzle8, came_from):
    frontier = PriorityQueue()
    cost_so_far = {}
    frontier.enqueue(puzzle8, 0)
    cost_so_far[puzzle8.ToString()] = puzzle8.cost
    came_from[puzzle8.ToString()] = None
    while not frontier.is_empty():
        puzzle8 = frontier.dequeue()
        
        if puzzle8.isGoal():
            return puzzle8
        else:
            moves = puzzle8.getAllMoves()
            for move in moves:
                newpuzzle8 = puzzle8.clone()
                newpuzzle8.move(*move)
                new_cost = newpuzzle8.cost
                if cost_so_far.get(newpuzzle8.ToString()) == None or \
                   new_cost < cost_so_far[newpuzzle8.ToString()]:
                    cost_so_far[newpuzzle8.ToString()] = new_cost
                    priority = new_cost + newpuzzle8.heuristics
                    frontier.enqueue(newpuzzle8, priority)
                    came_from[newpuzzle8.ToString()] = puzzle8
    return None

def main():
    seed()
    came_from = {}
    puzzle8 = Puzzle8()
    found = Astar(puzzle8, came_from)
    if found != None:
        s = Stack()
        s.push(found)
        found = came_from.get(found.ToString())
        while found != None:
            s.push(found)
            found = came_from.get(found.ToString())
        win = GraphWin('A* for 8 Puzzle', 600, 600, autoflush=False)
        puzzle8draw = Puzzle8Draw(win)
    
        while win.checkKey() != 'Escape':
            while not s.is_empty():
                puzzle8draw.draw(s.pop())
                time.sleep(1.25)
        win.close()        
    else:
        print('Path not found!')
            
if __name__ == '__main__':
    main()