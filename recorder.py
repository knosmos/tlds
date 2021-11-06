import pygame, sys, copy
from pygame.locals import *

# create window
pygame.init()
screen = pygame.display.set_mode((200, 400))
pygame.display.set_caption("Gcode Converter Recorder")

points = []
recording = False

clock = pygame.time.Clock()

while True:
    screen.fill((255,255,255))
    if recording:
        points.append(list(pygame.mouse.get_pos()))
    if (len(points) >= 2):
        pygame.draw.lines(screen, (0,0,0), False, points, width = 2)
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == MOUSEBUTTONDOWN:
            recording = True
            points = []
        if e.type == MOUSEBUTTONUP:
            recording = False
            # normalize
            res = copy.deepcopy(points)
            for i in range(len(res)):
                res[i][0] /= 200
                res[i][1] /= 200
            print(res)
            with open(f"digits/{sys.argv[1]}.txt", "w") as f:
                f.write("\n".join(map(lambda i:f"{i[0]} {i[1]}",res)))
            pygame.quit()
            sys.exit()
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(20)