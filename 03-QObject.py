from PyQt5.QtWidgets import QWidget, QApplication, QLabel, qApp, QPushButton, QLabel
from PyQt5.QtCore import QObject, Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject 的学习")
        self.resize(500, 500)
        self.setup_ui()
        
    def setup_ui(self):
        # self.QObjectTest()
        # self.QObjectTestName()
        # self.QObjectTestNameProperty()
        # self.QObjectTestParentChildren()
        # self.QObjectTestMemory()
        # self.QObjectTestSignalSlot()
        # self.QObjectTestButtonSignal()
        # self.QObjectTestWindowSignal()
        # self.QObjectTestType()
        self.QObjectTestDeleteLater()

    def QObjectTest(self):
        """展示 QObject 的父类以及子类都有哪些
        """
        QObject.__subclasses__()
        mros = QObject.mro()
        for mro in mros:
            print(mro)

    def QObjectTestName(self):
        """设置 QObject 的 Name 以及 Property
        """
        obj = QObject()
        obj.setObjectName("New Name")
        print(obj.objectName())

        obj.setProperty("notice_level", "error")
        obj.setProperty("notice_level2", "warning")

        print(obj.property("notice_level"))
        print(obj.property("notice_level2"))
        print(obj.dynamicPropertyNames())

    def QObjectTestNameProperty(self):
        """通过 QObject 的 Name 以及 Property 匹配 qss 文件中对应的样式
        """
        with open("QObject.qss", "r") as f:
            qApp.setStyleSheet(f.read())

        label = QLabel(self)
        label.move(0, 0)
        label.setText("正常信息")
        label.setObjectName("notice")
        label.setProperty("notice_level", "normal")

        label = QLabel(self)
        label.move(0, 100)
        label.setText("警告信息")
        label.setObjectName("notice")
        label.setProperty("notice_level", "warning")

        label = QLabel(self)
        label.move(0, 200)
        label.setText("错误信息")
        label.setObjectName("notice")
        label.setProperty("notice_level", "error")

    def QObjectTestParentChildren(self):
        """配置 QObject 的父子对象关系， 以及在父对象中查找子对象
        """
        obj0 = QObject()
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()
        obj4 = QObject()
        obj5 = QObject()

        obj1.setParent(obj0)
        obj2.setParent(obj0)

        obj3.setParent(obj1)

        obj4.setParent(obj2)
        obj5.setParent(obj2)

        print("obj0: ", obj0)
        print("obj1: ", obj1)
        print("obj2: ", obj2)
        print("obj3: ", obj3)
        print("obj4: ", obj4)
        print("obj5: ", obj5)

        # 展示 QObject 的父子关系
        print(obj3.parent())
        print(obj2.children())

        obj2.setObjectName("2")
        obj3.setObjectName("3")

        # 查询 QObject 的子对象， 可以指定 ObjectName, 以及是否递归查找
        print(obj0.findChild(QObject))
        print(obj0.findChild(QObject, "2"))
        print(obj0.findChild(QObject, "3"))
        print(obj0.findChild(QObject, "3", Qt.FindChildOption.FindDirectChildrenOnly))

        # 用法与 findChild 相似， 可以查找所有的符合条件的对象
        print(obj0.findChildren(QObject))

    def QObjectTestMemory(self):
        """QObject 的内存管理机制， 释放父对象的时候会自动释放子对象的内存资源
        """
        obj1 = QObject()
        obj2 = QObject()

        self.obj = obj1

        obj2.setParent(obj1)

        obj2.destroyed.connect(lambda : print("obj2 对象被释放"))

        del self.obj

    def QObjectTestSignalSlot(self):
        """测试 QObject 的两个信号

            QObject 默认携带两个信号： objectNameChanged 和 destroyed
        """
        self.obj = QObject()
        
        def objDestoryed(obj):
            print("对象被释放", obj)
        # 测试 destroyed 信号
        self.obj.destroyed.connect(objDestoryed)
        
        del self.obj
        
        obj = QObject()
        
        def objNameChanged(objectName):
            print("对象被修改名称: ", objectName)
            
        def objNameChanged2(objectName):
            print("对象被修改名称2: ", objectName)
        # 测试 objectNameChanged 信号
        obj.objectNameChanged.connect(objNameChanged)
        
        obj.setObjectName("hello1")
        
        obj.objectNameChanged.disconnect()
        
        obj.setObjectName("hello2")
        
        obj.objectNameChanged.connect(objNameChanged)
        
        obj.setObjectName("hello3")
        
        print("1", obj.signalsBlocked())
        obj.blockSignals(True)
        print("2", obj.signalsBlocked())
        
        obj.setObjectName("hello4")
        
        obj.blockSignals(False)
        print("3", obj.signalsBlocked())
        
        obj.setObjectName("hello5")
        
        # 一个信号可以触发多个槽函数
        obj.objectNameChanged.connect(objNameChanged2)
        print(obj.receivers(obj.objectNameChanged), "signals connected.") # type: ignore
        
        obj.setObjectName("hello6")

    def QObjectTestButtonSignal(self):
        """测试按钮的信号与槽函数
        """
        btn = QPushButton(self)
        btn.setText("请点击我")
        
        def btnClicked():
            print("点我干啥?")
        
        btn.clicked.connect(btnClicked)
        
    def QObjectTestWindowSignal(self):
        """测试窗口的信号与槽函数
        
            为了防止 windowTitleChanged 的信号发生递归触发， 需要再槽函数中对信号进行阻塞
        """
        def windowTitleChanged(title):
            self.blockSignals(True)
            self.setWindowTitle("666-" + title)
            self.blockSignals(False)
        
        self.windowTitleChanged.connect(windowTitleChanged)
        
        self.setWindowTitle("hello")
        self.setWindowTitle("hello2")
        
    def QObjectTestType(self):
        """测试判定类的类型的 API
        
            有两个类型判断 API: isWidgetType 判断类是否是一个控件， inherits(Type) 判断类是否继承于 Type 类型
        """
        objs = [QObject(), QWidget(), QPushButton(), QLabel()]
        
        for obj in objs:
            print(obj, "is widget type? ", obj.isWidgetType())
            
        for obj in objs:
            print(obj, "is inherits from QWidget? ", obj.inherits("QWidget"))
            
        for obj in objs:
            print(obj, "is inherits from QPushButton? ", obj.inherits("QPushButton"))
    
    def QObjectTestDeleteLater(self):
        """稍后删除一个对象
        
            删除一个对象时， 也会解除他与父对象之间的父子关系， 并且会释放所有的子对象
            删除后并没有立即对对象进行销毁， 而是向消息循环中发送了一个事件， 下一次消息循环中才会销毁这个对象
        """
        import threading
        
        obj1 = QObject()
        obj2 = QObject(obj1)
        obj3 = QObject(obj2)
        
        obj1.setObjectName("QObject <1>")
        obj2.setObjectName("QObject <2>")
        obj3.setObjectName("QObject <3>")
        
        def showObj1():
            print("\nshow children of obj1:")
            for obj in obj1.findChildren(QObject):
                print(obj.objectName(), obj)
                
        showObj1()
        
        obj2.deleteLater()
        
        self.timer = threading.Timer(5, showObj1)
        self.timer.start()
        
        showObj1()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec())