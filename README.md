# 🦖 Dino Game Automation

Automate the Chrome Dino game using Python. The bot watches the screen and jumps over obstacles automatically.

## How It Works

1. Captures a small region of the screen ahead of the dino
2. Checks for dark pixels (obstacles)
3. Presses spacebar to jump when an obstacle is detected
4. Runs in a continuous loop until stopped

## Installation

```bash
git clone https://github.com/sadrasahranavard/dino-game-automation.git
cd dino-game-automation
python -m venv venv

# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

## Usage

### Open the Game
Go to: https://elgoog.im/t-rex/

### Run the Bot
```bash
python src/gui.py
```
1. Set your detection zone coordinates
2. Click Start
3. Quickly switch to the game window
4. Watch the bot play

## Detection Zone

The detection zone is the screen area the bot monitors for obstacles.

### Finding the Right Zone
1. Open the game and position the window
2. Start with default values (X:350, Y:400, W:150, H:80)
3. If the dino doesn't jump, try adjusting:
   - **X, Y**: Move the zone to where obstacles appear
   - **Width**: Make it wider to detect sooner
   - **Height**: Cover the height of cacti and birds

### Tips
- Keep the zone focused ahead of the dino, not too wide
- Make sure the game window is fully visible
- Different screen resolutions need different coordinates

## Emergency Stop

- Move mouse to **top-left corner** of screen
- Or click the **Stop** button in the GUI

## Project Structure
```
dino-game-automation/
├── src/
│   ├── __init__.py
│   ├── detector.py      # Screen capture & obstacle detection
│   ├── controller.py    # Game control logic
│   └── gui.py           # GUI with controls
├── tests/
│   └── test_detector.py # Unit tests
├── .gitignore
├── README.md
└── requirements.txt
```

## Requirements
- Python 3.7+
- pyautogui
- pillow
- numpy
```