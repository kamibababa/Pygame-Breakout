from settings import BALL_SIDE_LENGTH, BALL_ORIGIN, BALL_SPEED, pg

class Ball:
    def __init__(self) -> None:
        
        self.color = 'white'
        self.rect = pg.Rect(BALL_ORIGIN, (BALL_SIDE_LENGTH, BALL_SIDE_LENGTH))
        self.velocity = [BALL_SPEED, BALL_SPEED]

    def update(self, game):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Check for collision with screen boundaries
        if self.rect.left <= game.screen_rect.left or self.rect.right >= game.screen_rect.right:
            self.invert_direction(0)  # Left or right wall

        if self.rect.top <= game.screen_rect.top:
            self.invert_direction(1)  # Top wall

        # Check for collision with entities (bricks and paddle)
        for entity in game.bricks + [game.paddle]:
            if self.rect.colliderect(entity.rect):
                self.color = entity.color

                # Determine the side of the collision
                if (self.rect.bottom >= entity.rect.top and self.rect.top < entity.rect.top) or (self.rect.top <= entity.rect.bottom and self.rect.bottom > entity.rect.bottom): 
                    self.rect.bottom = entity.rect.top  # Adjust position to avoid sticking
                    self.invert_direction(1)  # Invert vertical direction
                elif (self.rect.right >= entity.rect.left and self.rect.left < entity.rect.left) or (self.rect.left <= entity.rect.right and self.rect.right > entity.rect.right):
                    self.rect.right = entity.rect.left  # Adjust position to avoid sticking
                    self.invert_direction(0)  # Invert horizontal direction

                # Delete the entity if it's a brick
                if entity in game.bricks:
                    game.bricks.remove(entity)
                    game.score += entity.points

                break # Break the loop if a collision is detected because the ball can only collide with one entity at a time

        # Ensure the ball stays within the screen boundaries
        self.rect.clamp_ip(game.screen_rect)


    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)

    def invert_direction(self, axis):
        self.velocity[axis] *= -1