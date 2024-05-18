from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel,QSizePolicy
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor
import sys

class Cell(QWidget):
    def __init__(self, icon_path, text, width , height,x = 0,y = 0, color="#FF0000"):
        super().__init__()
        self.setFixedSize(width,height)
        self.setAutoFillBackground(True)
        self.x = x
        self.y = y

        palette = QPalette()
        palette.setColor(self.backgroundRole() ,QColor(color))
        self.setPalette(palette)
        
        
        
        layout = QHBoxLayout()
        
        # Tạo và thêm biểu tượng vào layout
        self.icon_label = QLabel()
        icon_pixmap = QPixmap(icon_path)
        icon_pixmap = icon_pixmap.scaled(width*0.2,height)
        self.icon_label.setPixmap(icon_pixmap)
        layout.addWidget(self.icon_label,stretch=1)  # chiếm 20% bên trái
        
        
        
        # Tạo và thêm văn bản vào layout
        self.text_label = QLabel(text)
        font = QFont('Verdana', 90)
        self.text_label.setFont(font)
        self.text_label.resize(width*0.8,height)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.text_label.setStyleSheet("color: white;")
        layout.addWidget(self.text_label, stretch=4)  # chiếm 80% còn lại
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        
        
    def update_text(self, new_text):
        self.text_label.setText(new_text)

if __name__ == "__main__":
    app = QApplication([])

    # Tạo và hiển thị thành phần
    
    component = Cell("CO2_icon.png", "Text content")
    component.show()

    sys.exit(app.exec())
