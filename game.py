import pygame                   
from sys import exit            
 
pygame.init()

def display_score():
    score=int(pygame.time.get_ticks()/100)-start_time
    score1=font1.render(f'Score:{score}',False,(64,64,64))
    score_rect=score1.get_rect(center=(400,50))
    screen.blit(score1,score_rect) 

screen = pygame.display.set_mode((800,400)) 
pygame.display.set_caption('Pixle Runner') 
clock=pygame.time.Clock() 
font1=pygame.font.Font('Python/Projects/game/font/Pixeltype.ttf',50)

sky=pygame.image.load('Python/Projects/game/graphics/Sky.png').convert_alpha()
ground=pygame.image.load('Python/Projects/game/graphics/ground.png').convert_alpha()

start_time=0

snail_surf= pygame.image.load('Python/Projects/game/graphics/snail/snail1.png').convert_alpha()
snail_x_pos=600
snail_rect=snail_surf.get_rect(midbottom=(snail_x_pos,300))

player_surf=pygame.image.load('Python/Projects/game/graphics/player/player_walk_1.png').convert_alpha()
player_rect=player_surf.get_rect(midbottom=(80,300))
player_gravity=0

player_stand=pygame.image.load('Python/Projects/game/graphics/player/player_stand.png').convert_alpha()
player_stand=pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect=player_stand.get_rect(center=(400,200))

game_active=False

while True:   
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active==True:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom>=300:
                       player_gravity=-11

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and player_rect.bottom>=300:
                    player_gravity=-11
        
        else:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_active=True
                snail_rect.left=800
                start_time=int(pygame.time.get_ticks()/100)       
                

    if game_active:
        screen.blit(sky,(0,0))
        screen.blit(ground,(0,300))

        snail_rect.x -= 4
        if snail_rect.right==0:
                snail_rect.left=800

        player_gravity+=.45
        player_rect.y+=player_gravity
        if player_rect.bottom>=300:
                player_rect.bottom=300
        
        screen.blit(snail_surf,snail_rect)
        screen.blit(player_surf,player_rect)

        display_score() 

        if snail_rect.colliderect(player_rect):
            game_active=False

    else:
         screen.fill((94,129,162)) 
         screen.blit(player_stand,player_stand_rect)       

    pygame.display.update()
    clock.tick(60)