import sys
import time
import random
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel,QSizePolicy, QVBoxLayout
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor
import sys
from cell import Cell
from dashboard import Dashboard, MESSURE
from video import VideoWindow
from mainWindow import MainWindow




if __name__ == '__main__':
    app = QApplication(sys.argv)
    url = "https://www.youtube.com/watch?v=rKn4EQ3-Ns0"
    # url = "https://www.youtube.com/watch?v=RqFZRIiduY4"
    
    main_window = MainWindow(1920,1080,url)
    main_window.run()
    # main_window.showFullScreen()
    # main_window.video_window.video_player.play()
    sys.exit(app.exec())

    
