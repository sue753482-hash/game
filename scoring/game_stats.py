import json
import os

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.ai_game = ai_game
        
        # 直接从文件加载最高分
        self.high_score = self.load_high_score()
        
        # 重置其他统计信息
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """从文件加载当前难度的最高分，如果文件不存在返回0"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            high_score_file = os.path.join(script_dir, 'high_scores.json')
            
            if os.path.exists(high_score_file):
                with open(high_score_file, 'r') as f:
                    data = json.load(f)
                    # 根据当前难度获取对应的最高分
                    high_score = data.get(self.settings.current_difficulty, 0)
                    print(f"从文件读取{self.settings.current_difficulty}难度最高分: {high_score}")
                    return high_score
            else:
                print("最高分文件不存在，使用默认值0")
                return 0
        except Exception as e:
            print(f"读取最高分时出错: {e}")
            return 0

    def save_high_score(self):
        """保存当前难度的最高分到文件"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            high_score_file = os.path.join(script_dir, 'high_scores.json')
            
            # 先读取现有的所有难度最高分
            if os.path.exists(high_score_file):
                with open(high_score_file, 'r') as f:
                    data = json.load(f)
            else:
                data = {}
            
            # 更新当前难度的最高分
            data[self.settings.current_difficulty] = self.high_score
            
            # 保存回文件
            with open(high_score_file, 'w') as f:
                json.dump(data, f)
            print(f"{self.settings.current_difficulty}难度最高分已保存: {self.high_score}")
        except Exception as e:
            print(f"保存最高分时出错: {e}")