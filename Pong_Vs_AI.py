import pygame
from pygame.locals import *
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class ball(object):
    def __init__(self, surface):
        self.surface = surface

        self.x_axis = int (surface[0] * 0.5)
        self.y_axis = int (surface[0] * 0.5)

        self.radi = 5
        self.size = 5

        self.rect = pygame.Rect(self.x_axis-self.radi, self.y_axis-self.radi, self.radi * 2, self.radi * 2)
        self.color = GREEN
        self.rng_direc = [-1, 1]
        self.direc = [random.choice(self.rng_direc), random.choice(self.rng_direc)]

        self.x_speed = 1
        self.y_speed = 1

        self.hit_top = False
        self.hit_bottom = False
        self.hit_left = False
        self.hit_right = False

    def reset_court(self, surface):
        self.x_axis = int (surface[0] * 0.5)
        self.y_axis = int (surface[1] * 0.5)
        self.direc = [random.choice(self.rng_direc), random.choice(self.rng_direc)]
        self.hit_top = False
        self.hit_bottom = False
        self.hit_left = False
        self.hit_right = False
    
    def update(self, player_middle, player_top, player_bottom, AI_middle, AI_top, AI_bottom):
        self.x_axis += self.direc[0] * self.x_speed
        self.y_axis += self.direc[1] * self.y_speed
        self.rect.center = (self.x_axis, self.y_axis)
        
        if self.rect.right >= self.surface[0] - 1:
            self.hit_right = True
        elif self.rect.left <= 0:
            self.hit_left = True
        elif self.rect.top < 2:
            self.hit_top = True
        elif self.rect.bottom > self.surface[1] - 2:
            self.hit_bottom = True
        
        #collisions and sounds bites
        if self.rect.colliderect(player_middle.rect):
            pygame.mixer_music.load('hit.wav')
            pygame.mixer_music.play(0)
            self.direc[0] = -1
        if self.rect.colliderect(player_top.rect):
            pygame.mixer_music.load('hit.wav')
            pygame.mixer_music.play(0)
            self.direc[1] = 1
        if self.rect.colliderect(player_bottom.rect):
            pygame.mixer_music.load('hit.wav')
            pygame.mixer_music.play(0)
            self.direc[1] = -1
####
        if self.rect.colliderect(AI_middle.rect):
            pygame.mixer_music.load('hit.wav')
            pygame.mixer_music.play(0)
            self.direc[0] = 1
        if self.rect.colliderect(AI_top.rect):
            pygame.mixer_music.load('hit.wav')
            pygame.mixer_music.play(0)
            self.direc[1] = 1
        if self.rect.colliderect(AI_bottom.rect):
            pygame.mixer_music.load('hit.wav')
            pygame.mixer_music.play(0)
            self.direc[1] = -1
    def render(self, surface):
        pygame.draw.circle(surface,self.color, self.rect.center, self.radi, 0)
        pygame.draw.circle(surface,GREEN, self.rect.center, self.radi, 1)

class AI_paddle_middle(object):
    def __init__(self, surface):
        self.surface = surface
        self.x_axis = 5
        self.y_axis = int (surface[1] * 0.5)

        self.heigth = 100
        self.width = 10

        self.rect = pygame.Rect(0, self.y_axis- int(self.heigth * 0.5), self.width, self.heigth)

        self.color = RED
        self.speed = .5
    def update(self, pong):
        if pong.rect.top < self.rect.top:
            self.y_axis -= self.speed
        elif pong.rect.bottom > self.rect.bottom:
            self.y_axis += self.speed
        self.rect.center = (self.x_axis, self.y_axis)
    
    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)
        pygame.draw.rect(surface,RED,self.rect, 1)

class AI_paddle_top(object):
    def __init__(self, surface):
        self.surface = surface
        self.y_axis = 5
        self.x_axis = int (surface[0] * 0.1)

        self.height = 10
        self.width = 100

        self.rect = pygame.Rect(self.x_axis - int(self.width * 0.5), 0, self.width, self.height)

        self.color = RED
        self.speed = .5
    def update(self, pong):
        if pong.rect.left < self.rect.left:
            self.x_axis -= self.speed
        elif pong.rect.right > self.rect.right:
            self.x_axis += self.speed

        if self.x_axis > 280:
            self.x_axis = 280

        self.rect.center = (self.x_axis, self.y_axis)
    
    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)
        pygame.draw.rect(surface,RED,self.rect, 1)
        
class AI_paddle_bottom(object):
    def __init__(self, surface):
        self.surface = surface
        self.x_axis = int (surface[0] * 0.1)
        self.y_axis = 475
        self.height = 10
        self.width = 100
        self.rect = pygame.Rect(self.x_axis - int(self.width * 0.5), 0, self.width, self.height)
        self.color = RED
        self.speed = .5
    def update(self, pong):
        if pong.rect.left < self.rect.left:
            self.x_axis -= self.speed
        elif pong.rect.right > self.rect.right:
            self.x_axis += self.speed
        if self.x_axis > 280:
            self.x_axis = 280
        self.rect.center = (self.x_axis, self.y_axis)
    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)
        pygame.draw.rect(surface, RED,self.rect, 1)

class Player_paddle_middle(object):
    def __init__(self, surface):
        self.surface = surface
        self.x_axis = surface[0] - 5
        self.y_axis = int(surface[1] * 0.5)
        self.height = 100
        self.width = 10
        self.rect = pygame.Rect(0,self.y_axis - int (self.height * 0.5), self.width, self.height)
        self.color = BLUE
        self.speed = 4
        self.direc = 0
    def update(self):
        self.y_axis += self.direc * self.speed
        self.rect.center = (self.x_axis, self.y_axis)
        #keeps you in bounds
        if self.rect.top < self.rect.top:
            self.x_axis -= self.speed
        elif self.rect.bottom > self.rect.bottom:
            self.x_axis += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.surface[1] - 1:
            self.rect.bottom = self.surface[1] -1
    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)
        pygame.draw.rect(surface, BLUE, self.rect, 1)

class Player_paddle_bottom(object):
    def __init__(self, surface):
        self.surface = surface
        self.x_axis = int (surface[0] * 0.5)
        self.y_axis = surface[1] - 5
        self.height = 10
        self.width = 100
        self.rect = pygame.Rect(self.y_axis - int(self.height * 0.5), 0, self.width, self.height)
        self.color = BLUE
        self.speed = 4
        self. direc = 0
    def update(self):
        self.x_axis += self.direc * self.speed
        self.rect.center = (self.x_axis, self.y_axis)
        if self.rect.left < self.rect.left:
            self.x_axis -= self.speed
        elif self.rect.right > self.rect.right:
            self.x_axis += self.speed
        if self.x_axis < 390:
            self.x_axis =390
        if self.x_axis > 590:
            self.x_axis = 590
    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)
        pygame.draw.rect(surface, BLUE, self.rect, 1)

class Player_paddle_top(object):
    def __init__(self, surface):
        self.surface = surface
        self.x_axis = int (surface[0] * 0.5)
        self.y_axis = surface[1] - 475
        self.height = 10
        self.width = 100
        self.rect = pygame.Rect(self.y_axis - int (self.height * 0.5),0, self.width, self.height)
        self.color = BLUE
        self.speed = 4
        self. direc = 0
    def update(self):
        self.x_axis += self.direc * self.speed
        self.rect.center = (self. x_axis, self.y_axis)
        if self. rect.left < self.rect.left:
            self.x_axis -= self.speed
        elif self.rect.right > self.rect.right:
            self.x_axis += self.speed
        if self.x_axis < 390:
            self.x_axis += self.speed
        if self.x_axis > 590:
            self.x_axis = 590
    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)
        pygame.draw.rect(surface, BLUE, self.rect, 1)

def main():
    Player_score = 0
    AI_score = 0
    Player_games = 0
    AI_games = 0
    pygame.init()
    surface = (640,480)
    screen = pygame.display.set_mode(surface)
    pong = ball(surface)
    AI_Paddle_top = AI_paddle_top(surface)
    AI_Paddle_middle = AI_paddle_middle(surface)
    AI_Paddle_bottom = AI_paddle_bottom(surface)
    Player_Paddle_top = Player_paddle_top(surface)
    Player_Paddle_middle = Player_paddle_middle(surface)
    Player_Paddle_bottom = Player_paddle_bottom(surface)
    quit_game = False

    while not quit_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game = True
            
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    Player_Paddle_middle.direc = -1
                elif event.key == K_DOWN:
                    Player_Paddle_middle.direc = 1
            if event.type == KEYUP:
                if event.key == K_UP and Player_Paddle_middle.direc == -1:
                    Player_Paddle_middle.direc = 0
                elif event.key == K_DOWN and Player_Paddle_middle.direc == 1:
                    Player_paddle_middle.direc = 0
            
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    Player_Paddle_top.direc = -1
                    Player_Paddle_bottom.direc = -1
                elif event.key == K_RIGHT:
                    Player_Paddle_top.direc = 1
                    Player_Paddle_bottom.direc =1
            if event.type == KEYUP:
                if event.key == K_LEFT and Player_Paddle_top.direc == -1 and Player_Paddle_bottom.direc == -1:
                    Player_Paddle_bottom.direc = 0
                    Player_Paddle_top.direc = 0
                elif event.key == K_RIGHT and Player_Paddle_top.direc == 1 and Player_Paddle_bottom.direc == 1:
                    Player_Paddle_top.direc = 0
                    Player_Paddle_bottom .direc = 0
        AI_Paddle_top.update(pong)
        AI_Paddle_middle.update(pong)
        AI_Paddle_bottom.update(pong)
        Player_Paddle_top.update()
        Player_Paddle_middle.update()
        Player_Paddle_bottom.update()
        pong.update(Player_Paddle_middle, Player_Paddle_top, Player_Paddle_bottom, AI_Paddle_middle, AI_Paddle_top, AI_Paddle_bottom)

        if pong.hit_left:
            pygame.mixer_music.load('round_won.wav')
            pygame.mixer_music.play(0)
            Player_score += 1
            if Player_score == 11:
                Player_games += 1
                Player_score = 0
            pong.update(Player_Paddle_middle, Player_Paddle_bottom, Player_Paddle_top, AI_paddle_bottom, AI_Paddle_middle, AI_Paddle_top)
            pong.reset(screen)
        elif pong.hit_right:
            pygame.mixer_music.load('round_lost.wav')
            pygame.mixer_music.play(0)
            AI_score += 1
            if AI_score == 11:
                AI_games += 1
                AI_score = 0
            pong.update(Player_Paddle_middle, Player_Paddle_bottom, Player_Paddle_top, AI_Paddle_bottom, AI_Paddle_middle, AI_Paddle_top)
            pong.reset(screen)
        elif pong.hit_top and pong.x_axis > 332:
            pygame.mixer_music.load('round_lost.wav')
            pygame.mixer_music.play(0)
            Player_score += 1
            if Player_score == 11:
                Player_games += 1
                Player_score = 0
            pong.update(Player_Paddle_middle, Player_Paddle_bottom, Player_Paddle_top, AI_Paddle_bottom, AI_Paddle_middle, AI_Paddle_top)
            pong.reset_court(screen)
        elif pong.hit_bottom and pong.x_axis < 332:
            pygame.mixer_music.load('round_won.wav')
            pygame.mixer_music.play(0)
            Player_score += 1
            if AI_score == 11:
                AI_games += 1
                AI_score = 0
            pong.update(Player_Paddle_middle, Player_Paddle_bottom, Player_Paddle_top, AI_Paddle_bottom, AI_Paddle_middle, AI_Paddle_top)
            pong.reset_court(surface)
        elif pong.hit_bottom and pong.x_axis > 332:
            pygame.mixer_music.load('round_lost.wav')
            pygame.mixer_music.play(0)
            Player_score += 1
            if Player_score == 11:
                Player_games += 1
                Player_score = 0
            pong.update(Player_Paddle_middle, Player_Paddle_bottom, Player_Paddle_top, AI_Paddle_bottom, AI_Paddle_middle, AI_Paddle_top)
            pong.reset(surface)
        elif pong.hit_bottom and pong.x_axis < 332:
            pygame.mixer_music.load('round_lost.wav')
            pygame.mixer_music.play(0)
            AI_score += 1
            if AI_score == 11:
                AI_score += 1
                AI_score = 0
            pong.update(Player_Paddle_middle, Player_Paddle_bottom, Player_Paddle_top, AI_Paddle_bottom, AI_Paddle_middle, AI_Paddle_top)
            pong.reset(surface)

        if Player_games == 3 and AI_games < 3:
            print ("YOU WIN!!!!")
            AI_games = 0
            Player_games = 0
            AI_score = 0
            Player_score = 0
            pygame.mixer_music.load('game_won.wav')
            pygame.mixer_music.play(0)
            answer = input("Do you want to play again? Y or N")
            print (answer)
            if answer == 'Y':
                pong.reset(surface)
            if answer == 'N':
                quit_game = True
       
        if AI_games == 3 and Player_games < 3:
            print ("you lose :'(")
            AI_games = 0
            Player_games = 0
            AI_score = 0
            Player_score = 0
            pygame.mixer_music.load('game_lost.wav')
            pygame.mixer_music.play(0)
            answer = input("Do you want to play again? Y or N")
            print (answer)
            if answer == 'Y':
                pong.reset(surface)
            if answer == 'N':
                quit_game = True
        screen.fill((100,100,100))
        pygame.draw.line(screen,(255, 255, 255), (332, 0),(332, 480), 3)
        AI_Paddle_middle.render(screen)
        AI_Paddle_bottom.render(screen)
        AI_Paddle_top.render(screen)
        Player_Paddle_top.render(screen)
        Player_Paddle_middle.render(screen)
        Player_Paddle_bottom.render(screen)
        pong.render(screen)

        font = pygame.font.SysFont(None, 50)
        screen_text = font.render("AI", True, (255, 255, 255))
        screen.blit(screen_text,(166, 240))
        fontPlayer = pygame.font.SysFont(None, 50)
        screen_Playertext = fontPlayer.render("Player", True, (255, 255, 255))
        screen.blit(screen_Playertext, (400, 240))

        fontAIScore = pygame.font.SysFont(None, 25)
        screen_text_AIscore = fontAIScore.render("AI Score: " + str(AI_score), True, (255, 255, 255))
        screen.blit(screen_text_AIscore, (166, 100))

        fontPlayerScore = pygame.font.SysFont(None, 25)
        screen_text_playerscore = fontPlayerScore.render("Player Score:" + str(Player_score), True, (255, 255, 255))
        screen.blit(screen_text_playerscore, (400, 100))

        fontAIGames = pygame.font.SysFont(None, 25)
        screen_text_AIgames = fontAIGames.render("AI Games: " + str(AI_games), True, (255, 255, 255))
        screen.blit(screen_text_AIgames, (166, 50))

        fontPlayerGames = pygame.font.SysFont(None, 25)
        screen_text_playergames = fontPlayerGames.render("Player Games: " + str(Player_games), True, (255, 255, 255))
        screen.blit(screen_text_playergames, (400, 50))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()