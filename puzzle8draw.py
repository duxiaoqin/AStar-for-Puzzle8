# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:31:40 2018

@author: duxiaoqin
Functions:
    (1)Puzzle8Draw class;
"""

from graphics import *
from puzzle8 import *

class Puzzle8Draw:
    WIDTH = 5.0
    HEIGHT = 5.0
    START = 1.0
    END = 4.0
    
    def __init__(self, win):
        self.win = win
        self.win.setCoords(0.0, 0.0, Puzzle8Draw.WIDTH, Puzzle8Draw.HEIGHT)
        
        self.lines = []
        for offset in range(4):
            l = Line(Point(Puzzle8Draw.START, Puzzle8Draw.START+offset), \
                     Point(Puzzle8Draw.END, Puzzle8Draw.START+offset))
            l.setWidth(3)
            self.lines.append(l)
            l = Line(Point(Puzzle8Draw.START+offset, Puzzle8Draw.START), \
                     Point(Puzzle8Draw.START+offset, Puzzle8Draw.END))
            l.setWidth(3)
            self.lines.append(l)
        
        self.items = Puzzle8.ITEMS[:]
        self.stones = []
        for item in self.items:
            text = Text(Point(0, 0), item)
            text.setSize(36)
            text.setStyle('bold')
            text.setOutline('red')
            self.stones.append(text)
            
        self.text = Text(Point(2.5, 0.5), '8 Puzzle')
        self.text.setTextColor('red')
        
    def draw_lines(self):
        for l in self.lines:
            l.undraw()
        for l in self.lines:
            l.draw(self.win)
            
    def draw_puzzle8(self, puzzle8):
        self.text.undraw()
        self.text.draw(self.win)

        for i in range(len(self.stones)):
            self.stones[i].undraw()
            
        for row in range(puzzle8.numRows()):
            for col in range(puzzle8.numCols()):
                item = puzzle8[row, col]
                index = self.items.index(item)
                self.stones[index].anchor = \
                     Point(Puzzle8Draw.START+1/2+col, \
                           Puzzle8Draw.END-1/2-row)
                
        for i in range(len(self.stones)):
            self.stones[i].draw(self.win)
                    
    def draw(self, puzzle8):
        self.draw_lines()
        self.draw_puzzle8(puzzle8)    
        self.win.update()
            
def main():
    win = GraphWin('8 Puzzle Draw', 600, 600, autoflush=False)
    puzzle8 = Puzzle8()
    puzzle8.print()
    puzzle8draw = Puzzle8Draw(win)

    while win.checkKey() != 'Escape':
        puzzle8draw.draw(puzzle8)
    win.close()
    
if __name__ == '__main__':
    main()