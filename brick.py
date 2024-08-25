from settings import BRICK_WIDTH, BRICK_HEIGHT, BRICK_OFFSET, pg

class Brick:
    def __init__(self, row, column, color):

        self.rect = pg.Rect((column * BRICK_WIDTH, row * BRICK_HEIGHT + BRICK_OFFSET), (BRICK_WIDTH, BRICK_HEIGHT))
        self.color = color

        match self.color:
            case 'yellow': self.points = 1
            case 'green': self.points = 3
            case 'orange': self.points = 5
            case 'red': self.points = 7

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
