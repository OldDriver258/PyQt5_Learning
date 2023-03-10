from PyQt5.QtWidgets import QApplication, QWidget, QStyle, QAction
from PyQt5.QtWidgets import QPushButton, QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("06-QPushButton 测试程序")
        self.resize(500, 500)
        self.menu = self.customMenu()
        self.setup_ui()
        
    def setup_ui(self):
        # self.QPushButtonTestCtrate()
        # self.QPushButtonTestMenu()
        # self.QPushButtonTestFlat()
        # self.QPushButtonTestDefault()
        self.QPushButtonTestContextMenu()
        
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
        
    def QPushButtonTestCtrate(self):
        QPushButton(self).move(20, 0)
        QPushButton("hello", self).move(20, 50)
        QPushButton(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon) ,"hello", self).move(20, 100)
        
    def QPushButtonTestMenu(self):
        """按钮控件可以添加菜单, 并且在菜单下还可以添加子菜单
        """
        button = QPushButton("File", self)

        button.setMenu(self.getCustomMenu())
        
    def QPushButtonTestFlat(self):
        """设置按钮控件的扁平化
        """
        fileIcon = QApplication.style().standardIcon(QStyle.StandardPixmap.SP_FileIcon)
        button   = QPushButton(fileIcon, "File", self)
        
        button.setFlat(True)
        
    def QPushButtonTestDefault(self):
        """设置按钮空间的默认选中
        
            setAutoDefault 可以记忆上次用户的选中， 设置为默认选中
            setDefault 可以固定默认选中的控件
        """
        fileIcon     = QApplication.style().standardIcon(QStyle.StandardPixmap.SP_FileIcon)
        fileButton   = QPushButton(fileIcon, "File", self)
        
        folderIcon   = QApplication.style().standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon)
        folderButton = QPushButton(folderIcon, "Folder", self)
        
        fileButton.move(20, 0)
        folderButton.move(120, 0)
        
        fileButton.setAutoDefault(True)
        folderButton.setAutoDefault(True)
        
    def QPushButtonTestContextMenu(self):
        """实现右键自定义菜单
        """
        def customContextMenu(pos):
            self.getCustomMenu().exec_(self.mapToGlobal(pos))
        
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(customContextMenu)

if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()
    
    sys.exit(app.exec_())