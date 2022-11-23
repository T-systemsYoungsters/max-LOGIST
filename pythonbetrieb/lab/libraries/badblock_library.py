import block_library
class BadBlock(block_library.Block):
    def update(self):
        self.rect.y += 1
        if self.rect.y > 750:
            self.rect.y = -30