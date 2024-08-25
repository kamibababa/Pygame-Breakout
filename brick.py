from settings import BRICK_WIDTH, BRICK_HEIGHT, \
                BRICK_OFFSET, RECT_SHRINK_FACTOR, \
                pg

class Brick:
    def __init__(self, row, column, color):

        self.rect = pg.Rect((column * BRICK_WIDTH, row * BRICK_HEIGHT + BRICK_OFFSET), (BRICK_WIDTH, BRICK_HEIGHT))
        self.color = color

        match self.color:
            case 'yellow': self.points = 1
            case 'green': self.points = 3
            case 'orange': self.points = 5
            case 'red': self.points = 7

        # Calculate the new dimensions for the smaller rectangle
        new_width = int(self.rect.width * RECT_SHRINK_FACTOR)
        new_height = int(self.rect.height * RECT_SHRINK_FACTOR)
        
        # Calculate the position to center the smaller rectangle within the original rectangle
        new_x = self.rect.x + (self.rect.width - new_width) // 2
        new_y = self.rect.y + (self.rect.height - new_height) // 2
        
        # Create the new smaller rectangle
        self.smaller_rect = pg.Rect(new_x, new_y, new_width, new_height)

    def draw(self, screen):
        # Draw the smaller rectangle
        pg.draw.rect(screen, self.color, self.smaller_rect)
