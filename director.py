from constants import screen_height, screen_width,accent_color,basic_font,screen,luigi_sound,mario_sound
import pygame

class GameManager:
	def __init__(self,ball_group,paddle_group):
		self.player_score = 0
		self.opponent_score = 0
		self.ball_group = ball_group
		self.paddle_group = paddle_group

	def run_game(self):
		# Drawing the game objects
		self.paddle_group.draw(screen)
		self.ball_group.draw(screen)

		# Updating the game objects
		self.paddle_group.update(self.ball_group)
		self.ball_group.update()
		self.reset_ball()
		self.draw_score()

	def reset_ball(self):
		if self.ball_group.sprite.rect.right >= screen_width:
			pygame.mixer.Sound.play(luigi_sound)
			self.opponent_score += 1
			self.ball_group.sprite.reset_ball()
		if self.ball_group.sprite.rect.left <= 0:
			pygame.mixer.Sound.play(mario_sound)
			self.player_score += 1
			self.ball_group.sprite.reset_ball()

	def draw_score(self):
		player_score = basic_font.render(str(self.player_score),True,accent_color)
		opponent_score = basic_font.render(str(self.opponent_score),True,accent_color)

		player_score_rect = player_score.get_rect(midleft = (screen_width / 2 + 40,screen_height/2))
		opponent_score_rect = opponent_score.get_rect(midright = (screen_width / 2 - 40,screen_height/2))

		screen.blit(player_score,player_score_rect)
		screen.blit(opponent_score,opponent_score_rect)