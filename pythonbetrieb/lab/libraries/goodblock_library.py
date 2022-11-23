import random
import block_library
class Goodblock(block_library.Block):
    def update(self):
        self.rect.x += random.randrange(-3,4)
        self.rect.y += random.randrange(-3,4)