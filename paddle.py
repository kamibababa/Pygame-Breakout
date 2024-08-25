from settings import MOV_SPEED, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_ORIGIN, pg



class Paddle:
    def __init__(self) -> None:
        
        self.rect = pg.Rect(PADDLE_ORIGIN, (PADDLE_WIDTH, PADDLE_HEIGHT))
        self.color = 'white'

    def handle_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x -= MOV_SPEED
        if keys[pg.K_d]:
            self.rect.x += MOV_SPEED

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)