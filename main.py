import pygame

WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #sets width and height of game window
pygame.display.set_caption("Typing Test") #setting title of game window

def draw_window():
    WIN.fill((255,255,255))
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
