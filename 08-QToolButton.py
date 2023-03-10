from PyQt5.QtWidgets import QApplication, QWidget, QStyle
from PyQt5.QtWidgets import QToolButton, QMenu
from PyQt5.QtCore import Qt, QSize

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("08-QToolButton 测试程序")
        self.menu = self.customMenu()
        self.resize(500, 500)
        self.setup_ui()
        
    def setup_ui(self):
        # self.QToolButtonTestBasic()
        # self.QToolButtonTestArrow()
        # self.QToolButtonTestAutoRise()
        # self.QToolButtonTestMenu()
        self.QToolButtonTestSignal()
        
    def customMenu(self) -> QMenu:
        mainMenu = QMenu("File", self)
        subMenu  = QMenu("Open Recent File", self)
        
        subMenu.addAction("xxx.py", lambda: print("Open Recent File xxx.py"))

        mainMenu.addAction(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_FileIcon), "New File", lambda: print("New File"))
        mainMenu.addAction(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon), "Open File", lambda: print("Open File"))
        mainMenu.addMenu(subMenu)
        mainMenu.addSeparator()
        mainMenu.addAction(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_DialogCloseButton), "Exit", lambda: print("Exit"))
        
        return mainMenu
        
    def getCustomMenu(self) -> QMenu:
        return self.menu
    
    def QToolButtonTestBasic(self):
        """测试 QToolButton 的基本功能
        """
        btn  = QToolButton(self)
        icon = QApplication.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarContextHelpButton)
        
        btn.setText("工具按键")
        btn.setIcon(icon)
        btn.setIconSize(QSize(100, 100))
        btn.setToolTip("工具按键")
        
        btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

    def QToolButtonTestArrow(self):
        """测试 QToolButton 用 Arrow 箭头图标替换原有图标
        """
        btn  = QToolButton(self)
        
        btn.setText("工具按键")
        btn.setIconSize(QSize(100, 100))
        btn.setToolTip("工具按键")
        
        btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        # 设置 Arrow 图标， 效果和图标一样
        btn.setArrowType(Qt.ArrowType.RightArrow)
        
    def QToolButtonTestAutoRise(self):
        """测试 QToolButton 设置 auto rise, 按键会被设置为扁平化, 并且鼠标放到按键上会有选中效果
        """
        btn  = QToolButton(self)
        icon = QApplication.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarContextHelpButton)
        
        btn.setText("工具按键")
        btn.setIcon(icon)
        btn.setIconSize(QSize(100, 100))
        btn.setToolTip("工具按键")
        
        btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        
        btn.setAutoRaise(True)
        
    def QToolButtonTestMenu(self):
        """测试 QToolButton 的菜单的三种不同的弹出方式
        
            QToolButton.ToolButtonPopupMode.DelayedPopup    延迟弹出
            QToolButton.ToolButtonPopupMode.MenuButtonPopup 侧边菜单按键弹出
            QToolButton.ToolButtonPopupMode.InstantPopup    立刻弹出
        """
        btn  = QToolButton(self)
        icon = QApplication.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarContextHelpButton)
        
        btn.setText("工具按键")
        btn.setIcon(icon)
        btn.setIconSize(QSize(100, 100))
        btn.setToolTip("工具按键")
        
        btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        
        btn.setAutoRaise(True)
        
        btn.setMenu(self.getCustomMenu())
        # 设置为 侧边菜单按键弹出
        btn.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)
        
    def QToolButtonTestSignal(self):
        btn  = QToolButton(self)
        icon = QApplication.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarContextHelpButton)
        
        btn.setText("工具按键")
        btn.setIcon(icon)
        btn.setIconSize(QSize(100, 100))
        btn.setToolTip("工具按键")
        
        btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        
        btn.setAutoRaise(True)
        
        btn.setMenu(self.getCustomMenu())
        
        btn.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        
        def btnTriggered(action):
            print("button triggered.", action, action.text())
        
        btn.triggered.connect(btnTriggered)

if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()
    
    sys.exit(app.exec_())