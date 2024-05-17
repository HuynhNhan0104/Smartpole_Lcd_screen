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
        layout.setSpacing(0)
        # Tạo và thêm biểu tượng vào layout
        self.icon_label = QLabel()
        icon_pixmap = QPixmap(icon_path)
        icon_pixmap = icon_pixmap.scaled(width*0.2,height)
        self.icon_label.setPixmap(icon_pixmap)
        layout.addWidget(self.icon_label,stretch=1)  # chiếm 20% bên trái
        
        
        
        # Tạo và thêm văn bản vào layout
        self.text_label = QLabel(text)
        font = QFont('Arial', 40)
        self.text_label.setFont(font)
        self.text_label.resize(width*0.8,height)
        # print(f"{text_label.width}x{text_label.height}")
        layout.addWidget(self.text_label, stretch=1)  # chiếm 80% còn lại
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])

    # Tạo và hiển thị thành phần
    
    component = Cell("CO2_icon.png", "Text content")
    component.show()

    sys.exit(app.exec())
