shapes = [
    [[1, 1, 1], [0, 1, 0]], # T
    [[1, 1], [1, 1]],       # O
    [[1, 1, 1, 1]],         # I
    [[1, 1, 0], [0, 1, 1]], # S
    [[0, 1, 1], [1, 1, 0]], # Z
    [[1, 1, 1], [1, 0, 0]], # L
    [[1, 1, 1], [0, 0, 1]]  # J
]

# Colors
colors = [
    (0, 255, 255), # Cyan
    (255, 255, 0), # Yellow
    (0, 0, 255),   # Blue
    (255, 165, 0), # Orange
    (0, 255, 0),   # Green
    (255, 0, 0),   # Red
    (128, 0, 128)  # Purple
]

class Piece:
    def __init__(self, shape, width):
        self.shape = shape
        self.color = colors[shapes.index(shape)]
        self.x = width // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

#    def collision(self, dx, dy, grid):
#        for y, row in enumerate(self.shape):
#            for x, cell in enumerate(row):
#                if cell and (
#                    x + self.x + dx < 0 or
#                    x + self.x + dx >= len(grid[0]) or
#                    y + self.y + dy >= len(grid) or
#                    grid[y + self.y + dy][x + self.x + dx]
#                ):
#                    return True
#        return False
    def collision(self, dx, dy, grid):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:  # Check only filled cells in the shape
                    new_x = x + self.x + dx
                    new_y = y + self.y + dy

                    # Check if the piece is out of bounds
                    if new_x < 0 or new_x >= len(grid[0]) or new_y >= len(grid):
                        return True

                    # Check if the piece collides with existing blocks
                    if new_y >= 0 and grid[new_y][new_x]:
                        return True
        return False


    def lock(self, grid):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    grid[y + self.y][x + self.x] = self.color
