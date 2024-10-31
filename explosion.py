import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Explosion, self).__init__()
        
        # Load each frame of the explosion animation
        self.frames = [
            pygame.transform.scale(pygame.image.load(f"asteroid_explosions_alternate/asteroid_explosion_{i}.png"), (100, 100))
            for i in range(1,8)
        ]

        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=position)

        # Set the time between frames and the start time of the animation
        self.frame_duration = 50
        self.last_update = pygame.time.get_ticks()

        # Load explosion sound effect
        self.explosion_sound = pygame.mixer.Sound("explosion.wav")
        self.explosion_sound.play()


    def update(self):
        # Check if it's time to update to the next frame
        now = pygame.time.get_ticks()
        if now - self.last_update >= self.frame_duration:
            self.last_update = now
            self.current_frame += 1

            # If all the frames have been displayed, kill the sprite
            if self.current_frame >= len(self.frames):
                self.kill()
            else:
                self.image = self.frames[self.current_frame]

