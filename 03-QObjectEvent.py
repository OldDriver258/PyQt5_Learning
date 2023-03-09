import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5 import QtCore

class myApp(QApplication):
    def notify(self, a0: QtCore.QObject, a1: QtCore.QEvent) -> bool:
        """操作系统将发送的时间首先投递到 QAppliaction

        Args:
            a0 (QtCore.QObject): 事件发生的对象
            a1 (QtCore.QEvent): 发生的事件类型

        Returns:
            bool: 返回值
        """
        if a0.inherits("QPushButton") and a1.type() == QtCore.QEvent.Type.MouseButtonPress:
            print("button pressed notify.")
        return super().notify(a0, a1)

class myBtn(QPushButton):
    def event(self, e: QtCore.QEvent) -> bool:
        """QApplication 会将发生的时间投递到对应的对象中

        Args:
            e (QtCore.QEvent): 触发的事件类型

        Returns:
            bool: 返回值
        """
        if e.type() == QtCore.QEvent.Type.MouseButtonPress:
            print("button pressed event.")
        return super().event(e)

if __name__ == "__main__":
    app = myApp(sys.argv)

    window = QMainWindow()
    btn    = myBtn(window)

    btn.setText("按键")
    
    def btnPressedSlot():
        """当对象处理对应的时间的时候， 如果注册了槽函数， 最终会调用到注册的槽函数中
        """
        print("button pressed slot.")
    
    btn.pressed.connect(btnPressedSlot)

    window.show()

    sys.exit(app.exec_())