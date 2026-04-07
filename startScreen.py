import pygame
import os

pygame.init()

font = pygame.font.Font('fonts/Vera.ttf', 40)
width = 1080
height = 600
clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode([width, height]) #sets screen size
pygame.display.set_caption("software engineering project")
current_dir = os.getcwd()

#load images
pitch_btn = pygame.image.load(os.path.join(current_dir, 'img', 'pitch_btn.png')).convert_alpha()
rhythm_btn = pygame.image.load(os.path.join(current_dir, 'img', 'rhythm_btn.png')).convert_alpha()
select = pygame.image.load(os.path.join(current_dir, 'img', 'select.png')).convert_alpha()
logo = pygame.image.load(os.path.join(current_dir, 'img', 'logo.png')).convert_alpha()

#resize images
home_btn_normal_size = (325, 200)
home_btn_hover_size = (358, 220)
pitch_btn_normal = pygame.transform.smoothscale(pitch_btn, home_btn_normal_size)
pitch_btn_hover = pygame.transform.smoothscale(pitch_btn, home_btn_hover_size)
rhythm_btn = pygame.transform.scale(rhythm_btn, (325, 200))
select = pygame.transform.scale(select, (170, 50))
logo = pygame.transform.scale(logo, (460, 150))

#text_surface = font.render('Hello, Pygame!', True, (255, 255, 255)) # text, true, text colour

def pitchBtn():
    global pitch_btn
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    pitch_btn_rect = pygame.Rect(600, 300, 325, 200) #creates rectangle at (600, 300) with dimensions 325x200px
    if pitch_btn_rect.collidepoint(mouse_pos):
        image = pitch_btn_hover
        draw_pos = (583, 290)
    else:
        image = pitch_btn_normal
        draw_pos = (600, 300)

    screen.blit(image, draw_pos)

    if pitch_btn_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
        screen.fill((0, 0, 0))
        pygame.display.update()

# Main loop
run = True
while run:
    screen.fill((255, 255, 255))
    screen.blit(logo, (315, 50))
    pitchBtn()
    screen.blit(rhythm_btn, (150, 300))
    screen.blit(select, (450, 200))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    #screen.fill((0, 50, 0)) # Fill screen with black



    pygame.display.update()




pygame.quit()