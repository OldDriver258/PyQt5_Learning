from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
import sys

app = QApplication(sys.argv)

# 创建一个窗口
window = QWidget()
window.setWindowTitle("Hello World")
window.resize(800, 800)
window.move(800, 400)

# 创建一个标签
label = QLabel(window)
label.setText("Hello Sz")
label.move(400, 400)

window.show()

app.exit(app.exec_())
