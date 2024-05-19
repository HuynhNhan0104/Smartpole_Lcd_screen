from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel,QSizePolicy, QVBoxLayout
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor
import sys
import random
from cell import Cell
from dashboard import Dashboard, MESSURE
from video import VideoWindow

class MainWindow(QWidget):
    def __init__(self,width,height,url) -> None:
        super().__init__()
        self.setFixedSize(width,height)
        
        layout = QVBoxLayout()
        self.dashboard = Dashboard(width,height*0.3)
        layout.addWidget(self.dashboard,stretch=1)
        
        
        self.video_window = VideoWindow(width,height*0.7,url)
        layout.addWidget(self.video_window)
        layout.addStretch(1)
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(10000)
    
    def run(self):
        self.showFullScreen()
        self.video_window.video_player.play()
        
    def update_data(self):
        co2 = random.randrange(1,100)
        nox = random.randrange(1,100)
        pm1 = random.randrange(1,100)
        pm25 = random.randrange(1,100)
        pm10 = random.randrange(1,100)
        voc = random.randrange(1,100)
        self.dashboard.update_text_cell(MESSURE.CO2,f"{co2} ppm")
        self.dashboard.update_text_cell(MESSURE.NOx,f"{nox} ppm")
        self.dashboard.update_text_cell(MESSURE.PM1_0,f"{pm1} μg/m³")
        self.dashboard.update_text_cell(MESSURE.PM2_5,f"{pm25} μg/m³")
        self.dashboard.update_text_cell(MESSURE.PM10,f"{pm10} μg/m³")
        self.dashboard.update_text_cell(MESSURE.VOC,f"{voc} μg/m³")   
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = AirQualityMonitor()
    # ex = Cell("CO2_icon.png","CO2",300, 200,color="#00FF00")
    ex = MainWindow(1920,1080,"https://www.youtube.com/watch?v=rKn4EQ3-Ns0")
    ex.showFullScreen()
    ex.video_window.video_player.play()
    ex.dashboard.update_text_cell(MESSURE.CO2,"100")
    ex.dashboard.update_text_cell(MESSURE.NO2,"100")
    ex.dashboard.update_text_cell(MESSURE.SO2,"100")
    ex.dashboard.update_text_cell(MESSURE.CO,"100")
    ex.dashboard.update_text_cell(MESSURE.O3,"100")
    ex.dashboard.update_text_cell(MESSURE.VOC,"100")
    
        
    
    
    
    
    
    # ex.show()

    sys.exit(app.exec())

        