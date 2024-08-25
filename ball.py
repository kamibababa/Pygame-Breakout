from settings import BALL_SIDE_LENGTH, BALL_ORIGIN, BALL_SPEED, pg

class Ball:
    def __init__(self) -> None:
        
        self.color = 'white'
        self.rect = pg.Rect(BALL_ORIGIN, (BALL_SIDE_LENGTH, BALL_SIDE_LENGTH))
        self.velocity = [0, BALL_SPEED]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def invert_direction(self, axis):
        self.velocity[axis] *= -1