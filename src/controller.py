import time
import pyautogui
from src.detector import ObstacleDetector

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01

class DinoController:
    def __init__(self):
        self.detector = ObstacleDetector()
        self.running = False
        self.jump_count = 0
        self.duck_count = 0
    
    def configure(self, detection_x, detection_y, detection_w, detection_h,
                  game_x=None, game_y=None, game_w=None, game_h=None):

        self.detector.set_detection_zone(detection_x, detection_y,
                                         detection_w, detection_h)
        if game_x is not None:
            self.detector.set_game_region(game_x, game_y, game_w, game_h)
    
    def jump(self):
        pyautogui.press('space')
        self.jump_count += 1
    
    def duck(self):
        pyautogui.keyDown('down')
        time.sleep(0.3)
        pyautogui.keyUp('down')
        self.duck_count += 1
    
    def start_game(self):
        pyautogui.press('space')
        time.sleep(0.5)
    
    def run(self, duration=None):
        self.running = True
        start_time = time.time()
        
        print("Starting in 3 seconds... Switch to the game window!")
        print("Move mouse to top-left corner to abort.")
        time.sleep(3)
        
        self.start_game()
        print("Game started! Bot is running...")
        
        try:
            while self.running:
                if duration and (time.time() - start_time) > duration:
                    break
                
                if self.detector.has_obstacle():
                    proximity = self.detector.get_obstacle_position()
                    
                    if proximity > 0.3:
                        self.jump()
                        time.sleep(0.05)
                
                time.sleep(0.01)
                
        except pyautogui.FailSafeException:
            print("\nFail-safe triggered! Bot stopped.")
        
        self.running = False
        self.print_stats()
    
    def stop(self):
        self.running = False
    
    def print_stats(self):
        print(f"\n--- Bot Statistics ---")
        print(f"Jumps: {self.jump_count}")
        print(f"Ducks: {self.duck_count}")
        print(f"Total actions: {self.jump_count + self.duck_count}")