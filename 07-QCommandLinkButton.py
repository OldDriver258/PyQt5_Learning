from PyQt5.QtWidgets import QApplication, QWidget, QStyle
from PyQt5.QtWidgets import QCommandLinkButton

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("07-QCommandLinkButton 测试程序")
        self.resize(500, 500)
        self.setup_ui()
        
    def setup_ui(self):
        btn = QCommandLinkButton("标题", "描述", self)
        btn.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_ArrowRight))

if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()
    
    sys.exit(app.exec_())