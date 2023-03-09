from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
import sys

app = QApplication(sys.argv)

# 创建一个窗口
window = QWidget()
window.setWindowTitle("")

# 创建其他控件


# 展示窗口
window.show()

#程序运行
app.exit(app.exec_())