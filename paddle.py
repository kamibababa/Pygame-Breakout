from settings import MOV_SPEED, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_ORIGIN, pg

class Paddle:
    def __init__(self) -> None:
        self.rect = pg.Rect(PADDLE_ORIGIN, (PADDLE_WIDTH, PADDLE_HEIGHT))
        self.color = 'white'
        self.movement = [False, False]

    def handle_input(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                self.movement[0] = True
            if event.key == pg.K_d:
                self.movement[1] = True

        elif event.type == pg.KEYUP:
            if event.key == pg.K_a:
                self.movement[0] = False
            if event.key == pg.K_d:
                self.movement[1] = False

    def move(self, screen_rect):
        if self.movement[0]:
            self.rect.x -= MOV_SPEED
        if self.movement[1]:
            self.rect.x += MOV_SPEED

        self.rect.clamp_ip(screen_rect)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)