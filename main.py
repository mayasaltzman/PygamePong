import pygame
import os
import random

pygame.init()

WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #sets width and height of game window
pygame.display.set_caption("Typing Test") #setting title of game window

titleFont = pygame.font.Font('freesansbold.ttf', 32)
textFont = pygame.font.Font('freesansbold.ttf', 12)
white = (255, 255, 255)
black = (0, 0, 0)

title = titleFont.render('Typing Test', True, black, white)
titleRect = title.get_rect()
titleRect.center = (WIDTH/2,30)

def display_text():
    arr = os.listdir() #getting the list of files in the directory
    files = []

    #getting only the text files
    for i in arr:
        if i.endswith(".txt") == True:
            files.append(i)
        
    fileName = random.choice(files) #selecting a random file2
    f = open(fileName, "r") 

    #displaying the text read from the random file
    text = textFont.render(f.read(), True, black, white)
    textRect = text.get_rect()
    textRect.center = (WIDTH/2, HEIGHT/2)
    WIN.blit(text,textRect)
    
def draw_window():
    WIN.fill((white)) #fill window to be white
    WIN.blit(title, titleRect)
    display_text()
    pygame.display.update()


def main():
    run = True
    
    #window runs until user exits window
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()
