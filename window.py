import os
import sys
import pygame
from pygame.locals import *
import math

# Window size
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# Marker size
MARKER_WIDTH = round(WINDOW_WIDTH * 0.0604838)
MARKER_HEIGHT = round(WINDOW_WIDTH * 0.0604838)

# Base
TOP_LEFT = ( round(WINDOW_WIDTH * 0.0887096), round(WINDOW_HEIGHT * 0.0812807) )
STRIDE_BOARD_X = round(WINDOW_WIDTH * 0.3)
STRIDE_BOARD_Y = round(WINDOW_HEIGHT * 0.3)
STRIDE_X = round(WINDOW_WIDTH * 0.08064512)
STRIDE_Y = round(WINDOW_WIDTH * 0.086206)

SURFACE = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE

class Window:
    def __init__(self, game_grid):
        
        pygame.init()
        self.window  = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ), SURFACE )

        bg = pygame.image.load('images/blank_board.png').convert_alpha()
        self.background_image = pygame.transform.smoothscale(bg, ( WINDOW_WIDTH, WINDOW_HEIGHT ))

        x_marker = pygame.image.load('images/X.png').convert_alpha()
        self.x_marker = pygame.transform.smoothscale(x_marker, ( MARKER_WIDTH, MARKER_HEIGHT ))

        o_marker = pygame.image.load('images/O.png').convert_alpha()
        self.o_marker = pygame.transform.smoothscale(o_marker, ( MARKER_WIDTH, MARKER_HEIGHT ))

        self.update(game_grid)
    
    def update(self, game_grid):
        self.window.fill( (255, 255, 255) )
        self.window.blit( self.background_image, ( 0,0 ) )

        base_x, base_y = TOP_LEFT

        for i in range(9):
            board_base = (base_x + math.floor(i / 3) * STRIDE_BOARD_X, base_y + math.floor(i % 3) * STRIDE_BOARD_Y)
            for j in range(9):
                if game_grid[i][j] == 1:
                    self.window.blit( self.x_marker, self.map_idx_to_pos(board_base, j) )
                if game_grid[i][j] == 2:
                    self.window.blit( self.o_marker, self.map_idx_to_pos(board_base, j) )

        pygame.display.flip()

    def map_idx_to_pos(self, board_base, idx):
        base_x, base_y = board_base
        return (base_x + math.floor(idx / 3) * STRIDE_X, base_y + math.floor(idx % 3) * STRIDE_Y)

    def quit():
        pygame.quit()