import sys
import random
import time

import pygame


from go import five_in_a_row
from go import occupied
from go import generate_map
from go import alter_map


class gameboard:
    """ A class that draw a checker board in memory """

   # length = 0
   # width = 0
   # board = ([0])

    def __init__(self):
        self.length = 640
        self.width = 640
        pygame.init()
        self.screen = pygame.display.set_mode((self.length, self.width))
        pygame.display.set_caption("Five In a Row")
        self.draw_lines(12, 12)
        pygame.draw.line(self.screen, (0, 0, 0), (30,20), (600, 600), 1)
        self.board = generate_map(12, 12)

    def draw_lines(self, row, col):
        c = pygame.Color(0, 0, 0)
        w = 1
        #print("here1")
        for r in range(row + 1):
            point_1 = (20, 20 + r * ((self.length - 40) / row))
            point_2 = (self.length - 20, 20 + r * ((self.length - 40) / row))
            pygame.draw.line(self.screen, c, point_1, point_2, w)
           # print("here...")

        print("here3")
        for c in range(col + 1):
            point_1 = (20 + c * ((self.length - 40) / col), 20)
            point_2 = (20 + c * ((self.length - 40) / col), self.length - 20)
            pygame.draw.line(self.screen, c, point_1, point_2, w)
            #print("here123")

    def space_clicked(self):
        got = True
        while got:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    point = event.pos
                    got = False
        #print(point.getX)
        coordinate = ((point.X-20)/50, (point.Y-20)/50)
        return coordinate

    def take_turn(self, player):
        position = self.space_clicked()
        while (occupied(self.board, position.X, position.Y)==True):
            #create message to let them click again
            position = self.space_clicked()
        alter_map(self.board, position.X, position.Y, player)
        self.draw_point(self, player, position)


    def draw_point(self, player, position):
        if player == 1:
            color = 255, 255, 255
        else:
            color = 0, 0, 0

        center = (20 + position.X * ((self.width - 40) / 12) + 25, 20 + position.Y * ((self.length - 40) / 12) + 25)
        pygame.draw.circle(self, color, center, 20)

    def game_over(self):
        if five_in_a_row(self.board, 1) == True or five_in_a_row(self.board, 2) == True:
            return True
        else:
            return False


if __name__ == "__main__":
    gb = gameboard()
    while gb.game_over() == False:
        gb.take_turn(1)
        gb.take_turn(2)

