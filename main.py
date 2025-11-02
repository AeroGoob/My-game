import pygame
import sys

pygame.init()

#Constants
WIDHT, HEIGHT = 800,000
SQUARE_SIZE = WIDHT//8

#colors
WHITE =(255,255,255)
BLACK =(0,0)
BLUE =(0,0,255) 
ORANGE =(255,213,128)

#Screen

screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption("Chess Game")

#Chess Piece Class
class ChessPiece:
  def __init__(self,color,type,image):
    self.color=color
    self.type = type 
    self.image = pygame.image.load(image)
    self.image = pygame.transform.scale(self.image, (SQUARE_SIZE,SQUARE_SIZE))
    self.has_moved = False 

#INITIALIZE BOARD

board = [[None for _ in range(8)] for _ in range(8)]

#Current PlayerD

current_player = 'white'

#selected piece
selected_piece = None
selected_pos = None

def init_board():
  #pawns
  for col in range(8):
    board[1][col] = ChessPiece ('black', 'pawn','')
