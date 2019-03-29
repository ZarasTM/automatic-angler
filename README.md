# Automatic angler
Bot that automatcally catches fishes in "Gone Fishing" browser game

# Conspect
[Installation of needed components](README.md#Installation-of-needed-components) \
[Running bot](README.md#Running-bot) \
[Todo](README.md#Todo)

# Installation of needed components

To run this bot you will need Python along with given libraries:
  * pynput
  * Pillow (PIL)

To install libraries you can run **install.sh** for Linux distibutions or **install.cmd** for Windows (you need to have python and pip installed for it to work).

# Running bot

To run bot follow steps below:
  1. Enter the game, make sure that no in game popups are present and get ready to turn it to full screen mode *(Full screen mode is toggled by clicking rectangle in top-right side of game window)*
  2. Run **main.py** using command `python main.py` or by double clicking **main.py** *(Now you have 5 sec to do step 3.)*
  3. Turn game into full screen mode and wait for bot to start
  4. If you want to stop catching:
      1. Exit full screen mode
      2. Press `Ctrl+C` in console to interrupt program execution
      
# Todo
  * There is problem where sometimes fish can get away and bot doesn't know what to do then
  * It would be nice to have bot start on key press and stop on key press
  * Option to pause bot would be nice to have
  * ...
