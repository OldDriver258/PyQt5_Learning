from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
import sys

class MyWidget(QWidget):
    def timerEvent(self, evt) -> None:
        width = self.width()
        height = self.height()
        
        width += 10
        height += 10
        # 修改窗口的尺寸
        self.resize(width, height)

class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("0")
        self.move(100, 100)
        self.setStyleSheet("font-size: 52px")
        
    def setSecond(self, sec: int):
        self.sec = sec
        self.setText(str(self.sec))
        
    def startTimer(self, interval: int, timerType: Qt.TimerType = Qt.TimerType.CoarseTimer) -> int:
        self.timer_id = super().startTimer(interval, timerType)
        return self.timer_id
        
    def timerEvent(self, evt) -> None:
        """倒计时结束后自动结束定时器

        Args:
            evt (_type_): 定时器事件类型
        """
        self.sec  = int(self.text())
        self.sec -= 1
        
        if (self.sec > 0):
            self.setText(str(self.sec))
        else:
            self.sec = 0
            self.setText(str(self.sec))
            self.killTimer(self.timer_id)

app = QApplication(sys.argv)

window = MyWidget()
window.setWindowTitle("QObject 定时器的使用")
window.resize(500, 500)
# 窗口随着时间逐渐变大
window.startTimer(100)

label = MyLabel(window)
# 设置倒计时的计时数
label.setSecond(10)
# 设置定时器的间隔
label.startTimer(500)

window.show()

sys.exit(app.exec_())

