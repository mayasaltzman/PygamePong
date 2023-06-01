import pygame
import os
import random
import textwrap

pygame.init()

FPS = 60 #frames per second
clock = pygame.time.Clock()

WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #sets width and height of game window
pygame.display.set_caption("Typing Test") #setting title of game window

titleFont = pygame.font.Font('freesansbold.ttf', 32)
textFont = pygame.font.Font('freesansbold.ttf', 20)
white = (255, 255, 255)
black = (0, 0, 0)

title = titleFont.render('Typing Test', True, black, white)
titleRect = title.get_rect()
titleRect.center = (WIDTH/2,30)


def read_file():
    arr = os.listdir() #getting the list of files in the directory
    files = []

    #getting only the text files
    for i in arr:
        if i.endswith(".txt") == True:
            files.append(i)
        
    fileName = random.choice(files) #selecting a random file
    f = open(fileName, "r")

    return f


def draw_window(str):
    WIN.fill((white)) #fill window to be white
    WIN.blit(title, titleRect)

    wrapped_text = textwrap.fill(str, 70)  # Adjust the desired line width as per your needs
    
    # Displaying the wrapped text
    lines = wrapped_text.split('\n')
    y = (HEIGHT // 2 - len(lines) * textFont.get_height() // 2) + 60 #centering the text along the y axis

    for line in lines:
        text = textFont.render(line, True, black)
        textRect = text.get_rect()
        textRect.center = (WIDTH/2, y)
        WIN.blit(text, textRect)
        y += textFont.get_height()
    
    #displaying the text read from the random file
    #text = textFont.render(str, True, black)
    #textRect = text.get_rect()
    #textRect.center = (WIDTH/2, HEIGHT/2)
    #WIN.blit(text,textRect)
    
    pygame.display.update()


def main():
    
    run = True
    clock.tick(FPS)

    #reading random file to avoid infinite file reads
    f = read_file()
    str = f.read()
    
    #window runs until user exits window
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(str)
    pygame.quit()

if __name__ == "__main__":
    main()
