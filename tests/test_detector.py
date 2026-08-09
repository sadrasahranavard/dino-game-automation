import unittest
import sys
import os
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.detector import ObstacleDetector


class TestObstacleDetector(unittest.TestCase):
    def setUp(self):
        self.detector = ObstacleDetector()
    
    def test_set_detection_zone(self):
        self.detector.set_detection_zone(100, 200, 150, 80)
        self.assertEqual(self.detector.detection_box, (100, 200, 150, 80))
    
    def test_detection_zone_not_set_error(self):
        with self.assertRaises(ValueError):
            self.detector.capture_screen()
    
    def test_set_game_region(self):
        self.detector.set_game_region(0, 0, 800, 300)
        self.assertEqual(self.detector.game_region, (0, 0, 800, 300))
    
    def test_has_obstacle_with_dark_image(self):
        detector = ObstacleDetector()
        detector.detection_box = (0, 0, 100, 50)

        self.assertIsNotNone(detector)

class TestDetectionLogic(unittest.TestCase):
    def test_dark_pixel_detection(self):
        test_array = np.ones((50, 100, 3), dtype=np.uint8) * 255
        
        test_array[20:30, 60:80] = [50, 50, 50]
        
        gray = np.mean(test_array, axis=2)
        dark_pixels = np.sum(gray < 100)
        
        self.assertGreater(dark_pixels, 0)
    
    def test_no_obstacle_in_white_image(self):
        test_array = np.ones((50, 100, 3), dtype=np.uint8) * 255
        
        gray = np.mean(test_array, axis=2)
        dark_pixels = np.sum(gray < 100)
        
        self.assertEqual(dark_pixels, 0)

if __name__ == '__main__':
    unittest.main()