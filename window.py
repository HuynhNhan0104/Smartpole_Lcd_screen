from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel,QSizePolicy, QVBoxLayout
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor
import sys
from cell import Cell
from dashboard import Dashboard
from video import VideoWindow

class Window(QWidget):
    def __init__(self,width,height,url) -> None:
        super().__init__()
        self.setFixedSize(1920,1080)
        
        layout = QVBoxLayout()
        self.dashboard = Dashboard(width,height*0.3)
        layout.addWidget(self.dashboard,stretch=1)
        
        
        self.video_window = VideoWindow(width,height*0.7,url)
        layout.addWidget(self.video_window)
        layout.addStretch(1)
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = AirQualityMonitor()
    # ex = Cell("CO2_icon.png","CO2",300, 200,color="#00FF00")
    ex = Window(1920,1080,"https://www.youtube.com/watch?v=rKn4EQ3-Ns0")
    ex.showFullScreen()
    ex.video_window.video_player.play()
    # ex.show()

    sys.exit(app.exec())

        