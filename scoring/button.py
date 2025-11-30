import pygame.font


class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg, x_offset=0, y_offset=0, width=200, height=50):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = width, height
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx + x_offset
        self.rect.centery = self.screen_rect.centery + y_offset
        
        # 根据按钮文字设置颜色
        if "Hard" in msg:
            self.button_color = (135, 0, 0)  # 困难模式用红色
        elif "Exit" in msg:
            self.button_color = (100, 100, 100)  # 退出按钮用灰色
        elif "Menu" in msg:
            self.button_color = (0, 100, 200)  # 返回菜单用蓝色
        elif "Resume" in msg:
            self.button_color = (0, 135, 0)  # 继续游戏用绿色

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)