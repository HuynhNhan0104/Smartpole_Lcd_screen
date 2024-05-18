from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer , QAudioOutput, QAudioDevice,QMediaDevices
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel,QSizePolicy, QVBoxLayout, QFrame,QMainWindow
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor

import sys
import vlc
import streamlink

class VideoWindow(QWidget):
    def __init__(self,width=1000, height=1000, url=None) -> None:
        super().__init__()
        self.setFixedSize(width,height)
        layout = QVBoxLayout()
        
        # url = "https://www.youtube.com/watch?v=rKn4EQ3-Ns0"
        # url=
        stream = streamlink.streams(url)
        url = stream['best'].to_url()
        self.video_player = QMediaPlayer()
        self.video_player.setSource(QUrl(url))
        
        
        # Video frame
        self.videoWidget   = QVideoWidget()
        self.video_player.setVideoOutput(self.videoWidget)
        
        #audio output
        self.audio_output  = QAudioOutput()
        self.video_player.setAudioOutput(self.audio_output)
        device = QAudioDevice(QMediaDevices.defaultAudioOutput())
        self.audio_output.setDevice(device)
        self.audio_output.setVolume(1)
        
        
        # addlayout
        layout.addWidget(self.videoWidget)
        self.setLayout(layout)
        
   
    



if __name__ == "__main__":

    app = QApplication(sys.argv)

    player = VideoWindow(url="https://www.youtube.com/watch?v=rKn4EQ3-Ns0")
    player.show()
    player.video_player.play()
    
    
    
    

    


    sys.exit(app.exec_())