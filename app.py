import sys
import time
import random
from PySide6.QtCore import QTimer,QUrl
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel,QSizePolicy, QVBoxLayout
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor
import sys
from cell import Cell
from dashboard import Dashboard, MESSURE
from video import VideoWindow
from mainWindow import MainWindow
import streamlink
import threading
import requests
import json

def get_last_link():
    api_url = "https://io.adafruit.com/api/v2/GutD/feeds/live-stream"
    response = requests.get(api_url)
    if response.status_code == 200:
        content= json.loads(response.content)
        # print(json.dumps(content,indent=4))
        last_value = json.loads(content.get("last_value"))
        # print(type(last_value))
        # last_value = json.loads(last_value)
        link = last_value.get("link")
        return link


if __name__ == '__main__':
    app = QApplication(sys.argv)
    url = "https://www.twitch.tv/mrpokke"
    # url = "https://www.youtube.com/watch?v=rKn4EQ3-Ns0"
    # url = "https://www.youtube.com/watch?v=RqFZRIiduY4"
    link = get_last_link()
    print(link)
    main_window = MainWindow(1920,1080,link)
    main_window.dashboard.update_data()
    main_window.run()
    # print(main_window.video_window)
    # main_window.showFullScreen()
    # main_window.video_window.video_player.play()
    sys.exit(app.exec())

    
