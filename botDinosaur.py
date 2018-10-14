import platform
import pyautogui as gui
import numpy as np
import sys

if platform.system() == 'Linux':
    import pyscreenshot as ImageGrab
    from PIL import ImageOps
else:
    from PIL import ImageGrab, ImageOps

class botDinosaur:
    def __init__(self):
        self.replayBtn = (485, 385)
        self.topRightDino = (255, 379)
        self.xDistanceToObstacleCloser = 325  # Diferencia aplicada
        self.yDistanceToObstacleCloser = 369  # Diferencia aplicada
        self.xDistanceToObstacle = 378  # Diferencia aplicada
        self.yDistanceToObstacle = 404  # Diferencia aplicada

    def restartGame(self):
        gui.click(x = self.replayBtn[0], y = self.replayBtn[1])

    def dinoJump(self):
        gui.keyDown(key = 'space')
        gui.keyUp(key = 'space')

    def obstacleDetection(self):
        bbox = (self.xDistanceToObstacleCloser, 
                self.yDistanceToObstacleCloser,
                self.xDistanceToObstacle,
                self.yDistanceToObstacle)

        anilizeRGB = ImageGrab.grab(bbox = bbox)
        analizeGray = ImageOps.grayscale(anilizeRGB) # Analysing images in grayscale is more effecient than in RGB
        grey_array = np.array(analizeGray.getcolors()) # Check if the sum of pixel is grey or not
        return grey_array.sum()

def main(argv):
    param = argv[0] if len(argv) > 0 else 'n'
    dino = botDinosaur()
    dino.restartGame()
    no_obstacle = dino.obstacleDetection()
    mouse = gui.displayMousePosition
    while(1):
        if dino.obstacleDetection() > no_obstacle:
            dino.dinoJump()
        if gui.displayMousePosition != mouse:
            return 1
        if param == '-r':
            dino.restartGame()
        
if __name__ == "__main__":
    main(sys.argv[1:])