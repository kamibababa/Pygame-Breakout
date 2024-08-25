from settings import ROWS, COLUMNS, pg
from brick import Brick
from paddle import Paddle
from ball import Ball

class Game:
    def __init__(self) -> None:
        
        pg.init()
        self.final_screen = pg.display.set_mode((1200, 800), pg.RESIZABLE)
        self.screen = self.final_screen.copy()
        pg.mouse.set_visible(False)
        pg.display.set_caption("Breakout")
        self.clock = pg.time.Clock()

        self.bricks = self.gen_bricks()
        self.paddle = Paddle()
        self.ball = Ball()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()

            self.clock.tick(60)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                quit()

        self.paddle.handle_input() # Move paddle

    def update(self):
        self.ball.update()

    def render(self):
        self.screen.fill((0, 0, 0))

        [brick.draw(self.screen) for brick in self.bricks]
        self.paddle.draw(self.screen)


        self.final_screen.blit(pg.transform.scale(self.screen, self.final_screen.get_rect().size), (0, 0))
        pg.display.flip()

    def gen_bricks(self):
        bricks = []
        for row in range(ROWS):
            for column in range(COLUMNS):
                color = 'red'
                if row > 1:
                    color = 'orange'
                if row > 3:
                    color = 'green'
                if row > 5:
                    color = 'yellow'
                bricks.append(Brick(row, column, color))
        print(len(bricks))
        return bricks

if __name__ == "__main__":
    Game().run()