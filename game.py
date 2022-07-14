import pygame, sys

from director import GameManager
from objects.player import Player
from objects.ball import Ball
from objects.opponent import Opponent
from constants import screen_height, screen_width,accent_color,bg_color,screen,middle_strip,clock



# Game objects
player = Player('./multimedia/Paddle.png',screen_width - 20,screen_height/2,5)
opponent = Opponent('./multimedia/Paddle.png',20,screen_width/2,5)
paddle_group = pygame.sprite.Group()
paddle_group.add(player)
paddle_group.add(opponent)

ball = Ball('./multimedia/Ball.png',screen_width/2,screen_height/2,4,4,paddle_group)
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)

game_manager = GameManager(ball_sprite,paddle_group)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player.movement -= player.speed
			if event.key == pygame.K_DOWN:
				player.movement += player.speed
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player.movement += player.speed
			if event.key == pygame.K_DOWN:
				player.movement -= player.speed
	
	# Background Stuff
	screen.fill(bg_color)
	pygame.draw.rect(screen,accent_color,middle_strip)
	
	# Run the game
	game_manager.run_game()

	# Rendering
	pygame.display.flip()
	clock.tick(120)