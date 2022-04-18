    # ---------------------   Imports   ----------------------------#
import pygame
import sys

    # ---------------------   Constants   ----------------------------#

# Screen Display Constraints
WIDTH, HEIGHT = 448, 596
CENTER_WIDTH = WIDTH//2
CENTER_HEIGHT = HEIGHT//2
Frames_Speed = 75

# Color Constraints
COLOR = (10,10,30)

#Font Constraints
FONT = 'arial'
FONT_SIZE = 20
FONT_COLOR = (255, 200, 200)

# Protagonist Player Constraints


# Enemy Player Constraints


    #---------------------  Initializers  -----------------------------#

pygame.init()
vect = pygame.math.Vector2

class App:

    #------------------------- Constructor -------------------------#
    def __init__(self):
        self.visualscreen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.timer = pygame.time.Clock()
        self.running = True
        self.run_state = "Start"


    # ---------------------- Start Functions ----------------------#

    def start(self):
        while self.running:
            if self.run_state == "Start":
                self.opening_update()
                self.opening_display()
                self.opening_state_check()
            self.timer.tick(Frames_Speed)
        pygame.quit()
        sys.exit()

    def display_title_text(self, opening_message,font_color, font_size, font_type):
        self.text_font = pygame.font.SysFont(font_type, font_size)
        self.text_render = self.text_font.render(opening_message, False, font_color)
        self.text_rect = self.text_render.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        #self.text_position = (opening_display_text_position_width, opening_display_text_position_height)
        self.visualscreen.blit(self.text_render, self.text_rect)

    def display_printer(self, opening_message, opening_display_text_position_width, opening_display_text_position_height,
                          font_color, font_size, font_type):
         self.text_font = pygame.font.SysFont(font_type, font_size)
         self.text_render = self.text_font.render(opening_message, False, font_color)
        #text_rect = self.text_render.get_rect(center=(WIDTH // 2, HEIGHT // 2))
         self.text_position = (opening_display_text_position_width, opening_display_text_position_height)
         self.visualscreen.blit(self.text_render, self.text_position)

    def display_image_printer(self):
        self.image = pygame.image.load(r"C:pacman_title_image.jpg")
        self.visualscreen.blit(self.image, self.text_position)

    def opening_update(self):
        pass

    def opening_display(self):
        self.visualscreen.fill(COLOR)
        self.display_title_text("WELCOME TO PACMAN 2022!", (255, 200, 200), 20, 'arial')
        self.display_printer("Press Return to Play!", 135, 320, (255, 255, 250), 20, 'arial')
        self.display_printer("HIGH SCORE", 0, 0, (255, 255, 250), 20, 'arial')

        pygame.display.update()

    def opening_state_check(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.run_state = "In Play"
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    #------------------------- Calls ----------------------------#

app = App()
app.start()