from settings import BALL_SIDE_LENGTH, BALL_ORIGIN, BALL_SPEED, pg

class Ball:
    def __init__(self) -> None:
        
        self.color = 'white'
        self.rect = pg.Rect(BALL_ORIGIN, (BALL_SIDE_LENGTH, BALL_SIDE_LENGTH))
        self.velocity = [BALL_SPEED, BALL_SPEED]

    def update(self, entities, screen_rect):
        self.rect.x += min(self.velocity[0], BALL_SPEED)
        self.rect.y += min(self.velocity[1], BALL_SPEED)

        if (self.rect.left <= screen_rect.left) or (self.rect.right >= screen_rect.right):
            self.invert_direction(0) # Left or right wall

        if (self.rect.top <= screen_rect.top):
            self.invert_direction(1) # Top wall

        for entity in entities: # Bricks and paddle
            if self.rect.colliderect(entity.rect):

                self.color = entity.color

                if self.rect.bottom > entity.rect.top and self.rect.top < entity.rect.bottom:
                    self.invert_direction(1)
                elif self.rect.right > entity.rect.left and self.rect.left < entity.rect.right:
                    self.invert_direction(0)

        self.rect.clamp_ip(screen_rect)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)

    def invert_direction(self, axis):
        self.velocity[axis] *= -1