from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QRadioButton, QCheckBox,QStyle
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("QAbstractButton 测试程序")
        self.resize(500, 800)
        self.setup_ui()
        
    def setup_ui(self):
        self.QAbstractButtonTestSuit()
        
    def QAbstractButtonTestSuit(self):
        self.btn = QPushButton(self)
        self.movebase = 0
        self.QAbstractButtonTestText()
        self.QAbstractButtonTestIcon()
        self.QAbstractButtonTestShortcutKey()
        self.QAbstractButtonTestAutoRepeat()
        self.QAbstractButtonTestStatus()
        self.QAbstractButtonTestExclusive()
        self.QAbstractButtonTestClick()
    
    def btnTextPlusOne(self):
        num = int(self.btn.text()) + 1
        self.btn.setText(str(num))
    
    def QAbstractButtonTestText(self):
        """每按下一次按钮， 按钮上的数字加一
        """
        self.btn.setText("1")
        self.btn.pressed.connect(self.btnTextPlusOne)

    def QAbstractButtonTestIcon(self):
        """设置按钮的图标
        """
        icon = QApplication.style().standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon)
        
        self.btn.setIcon(icon)
        self.btn.setIconSize(QSize(50, 50))
        
    def QAbstractButtonTestShortcutKey(self):
        """设置按钮的快捷键
        """
        self.btn.setShortcut("Alt+Q")
        
        # 因为按键调用 setText 会清除 shortcut， 所以在每次按键松开重新去设置快捷键
        self.btn.released.connect(lambda: self.btn.setShortcut("Alt+Q"))
        
    def QAbstractButtonTestAutoRepeat(self):
        # 只对鼠标点击生效， 快捷键不生效
        self.btn.setAutoRepeat(True)
        self.btn.setAutoRepeatDelay(2000)
        self.btn.setAutoRepeatInterval(500)

    def QAbstractButtonTestStatus(self):
        btn_list = [QPushButton(self), QRadioButton(self), QCheckBox(self)]
        btn_name_list = ["push_button", "radio_button", "check_box"]
        self.movebase = 100
        
        for btn in btn_list:
            index = btn_list.index(btn)
            btn.setText(btn_name_list[index])
            btn.move(20, self.movebase + 50 * index)
            
        for btn in btn_list:
            print(btn, "isCheckable?", btn.isCheckable())
            
        btn_list[0].setCheckable(True)
        
        for btn in btn_list:
            print(btn, "isCheckable?", btn.isCheckable())
            
        def btnToggle():
            for btn in btn_list:
                btn.toggle()
        # 用按键翻转按钮的选中状态
        self.btn.pressed.connect(btnToggle)

    def QAbstractButtonTestExclusive(self):
        buttons = [QPushButton(self) for _ in range(3)]
        checkboxs = [QCheckBox(self) for _ in range(3)]
        self.movebase = 250
        
        for button in buttons:
            index = buttons.index(button)
            button.move(20, self.movebase + index * 50)
            button.setText("PushButton " + str(index))
            # 设置按钮可以选中， 并且具有排他性
            button.setCheckable(True)
            button.setAutoExclusive(True)
            
        for checkbox in checkboxs:
            index = checkboxs.index(checkbox)
            checkbox.move(220, self.movebase + index * 50)
            checkbox.setText("CheckBox " + str(index))
            # 设置复选框有排他性
            checkbox.setAutoExclusive(True)

    def QAbstractButtonTestClick(self):
        button = QPushButton(self)
        self.movebase = 400
        
        button.move(20, self.movebase)
        button.setText("动画模拟点击")
        
        def animateClick():
            button.animateClick(500)
            
        self.btn.clicked.connect(animateClick)

if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()
    
    sys.exit(app.exec_())