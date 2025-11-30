class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # 游戏模式设置
        self.difficulty_modes = {
            'normal': 1.0,
            'hard': 1.3
        }
        self.current_difficulty = 'normal'

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # 根据难度设置基础速度
        difficulty_multiplier = self.difficulty_modes[self.current_difficulty]
        
        self.ship_speed = 1.5 * difficulty_multiplier
        self.bullet_speed = 2.5 * difficulty_multiplier
        self.alien_speed = 1.0 * difficulty_multiplier

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def set_difficulty(self, mode):
        """设置游戏难度"""
        if mode in self.difficulty_modes:
            self.current_difficulty = mode
            self.initialize_dynamic_settings()