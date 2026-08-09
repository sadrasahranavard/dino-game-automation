#Analyzes screen pixels to detect obstacles
import pyautogui
import numpy as np
from PIL import Image

class ObstacleDetector:   
    def __init__(self, detection_box=None):
        self.detection_box = detection_box
        self.game_region = None
    
    def set_detection_zone(self, x, y, width, height):
        self.detection_box = (x, y, width, height)
    
    def set_game_region(self, x, y, width, height):
        self.game_region = (x, y, width, height)
    
    def capture_screen(self):
        if self.detection_box is None:
            raise ValueError("Detection zone not set. Call set_detection_zone() first.")
        
        x, y, width, height = self.detection_box
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        return screenshot
    
    def has_obstacle(self):
        screenshot = self.capture_screen()
        img_array = np.array(screenshot)
        
        if len(img_array.shape) == 3:
            gray = np.mean(img_array, axis=2)
        else:
            gray = img_array

        dark_pixels = np.sum(gray < 100)

        return dark_pixels > 50
    
    def get_obstacle_position(self):
        screenshot = self.capture_screen()
        img_array = np.array(screenshot)
        
        if len(img_array.shape) == 3:
            gray = np.mean(img_array, axis=2)
        else:
            gray = img_array
        
        dark_pixels = np.where(gray < 100)
        
        if len(dark_pixels[1]) == 0:
            return 0.0
        
        rightmost = np.max(dark_pixels[1])
        proximity = rightmost / gray.shape[1]
        
        return proximity
    
    def show_detection_zone(self):
        screenshot = self.capture_screen()
        screenshot.show()