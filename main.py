import pygame

pygame.init()

WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #sets width and height of game window
pygame.display.set_caption("Typing Test") #setting title of game window

font = pygame.font.Font('freesansbold.ttf', 32)
white = (255, 255, 255)
black = (0, 0, 0)

text = font.render('Typing Test', True, black, white)
textRect = text.get_rect()
textRect.center = (WIDTH/2,30)


def draw_window():
    WIN.fill((white)) #fill window to be white
    WIN.blit(text, textRect)
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
