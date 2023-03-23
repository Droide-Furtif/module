import pygame


class App:
    def __init__(self):
        self.background_color = "#F0FFF9"
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Module')
        self.clock = pygame.time.Clock()
        self.running = True
        self.FPS = 30
        self.start()

        self.meta_update()

    def start(self):
        pass

    def meta_update(self):
        while self.running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.update()
            self.before_draw()
            self.draw()
            self.after_draw()
        self.close()
        self.quit()

    def update(self):
        pass

    def before_draw(self):
        self.screen.fill(self.background_color)

    def draw(self):
        pass

    def after_draw(self):
        pygame.display.flip()

    def close(self):
        pass

    def quit(self):
        print("Quitting")

    def set_fps(self, fps):
        self.FPS = fps

    def set_background_color(self, bg_color):
        self.background_color = bg_color