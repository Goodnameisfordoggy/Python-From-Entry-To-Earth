PyQt5 入门记录

一般按照以下格式记录

- #包(模块)
- ##类
- ###子类
- ####子子类
- #####方法/一块儿用法
- `实例方法` 

- 官方文档: https://doc.qt.io/qt-5/qmainwindow.html

# PyQt5.QtWidgets
- 常见总览
  
类名|功能
:--|:--:  
QWidget| 提供用户界面对象的基类，包括窗口小部件和控件。
QMainWindow| 主窗口类，提供了应用程序主窗口的功能。
QDialog| 对话框类，用于显示模态或非模态的对话框。
QMessageBox| 弹出消息框类，用于显示通知、警告或错误信息。
QVBoxLayout, QHBoxLayout, QGridLayout| 布局管理器，用于管理小部件的位置和大小。
QPushButton, QCheckBox, QRadioButton, QLineEdit| 常见的用户界面控件。
QLabel| 用于显示文本或图像的标签。
QComboBox, QSpinBox, QSlider| 用于选择或调整数值的控件。
QListView, QTreeView, QTableView| 显示列表、树形视图和表格的控件。
QTabWidget| 选项卡控件，用于创建多个选项卡页面。
QToolBar| 工具栏控件，包含一组工具按钮。
QMenuBar, QMenu, QAction| 菜单和菜单项的相关类。
QStatusBar| 状态栏控件，用于显示应用程序的状态信息。
QScrollBar, QSlider, QDial| 滚动条和滑块控件。
QFileDialog, QColorDialog, QFontDialog| 文件对话框、颜色对话框、字体对话框等。
QGraphicsView, QGraphicsScene, QGraphicsItem| 用于创建图形和图形场景的类。
QDockWidget| 可停靠的窗口小部件，可以附加到主窗口的边缘。
QUndoStack, QUndoCommand| 用于实现撤销和重做的框架类。
QWizard, QWizardPage| 向导对话框的相关类，用于逐步引导用户完成任务。  
## QApplication (应用程序对象)
- 继承自QCoreApplication 提供了一些额外的功能，特别是与图形用户界面（GUI）应用程序相关的功能。
```py
app = QApplication([])

# 启动应用程序的主事件循环。在这个方法被调用后，应用程序将开始处理用户交互、定时器事件等。
app.exec_()
# 请求应用程序退出。这将导致主事件循环退出，应用程序的 exec_() 方法返回。
app.quit()
# 设置应用程序的名称，这通常用于标识应用程序
app.setApplicationName("MyApp")
# 设置应用程序的组织名称。这通常用于标识应用程序的组织或公司
app.setOrganizationName("MyOrganization")
# 设置应用程序的全局样式表。样式表用于定义应用程序的外观。
app.setStyleSheet("QLabel { color: red; }")
# 处理当前所有待处理的事件。在一些情况下，你可能需要主动调用这个方法以确保及时处理事件。
app.processEvents()
# 返回一个 QClipboard 对象，用于访问系统剪贴板。
clipboard = app.clipboard()
# 显示关于 Qt 的信息对话框。
app.aboutQt()
```

## QWidget (用户界面元素基类)

- 可用于构建简单的窗口
- 常用的子类有: 

|类名|功能
:--|:--:  
QMainWindow| 主窗口类。
QDialog| 对话框类。
QMessageBox| 弹出消息框类。
QFrame| 框架类，提供基本的框架功能。
QLabel| 标签类，用于显示文本或图像。
QPushButton| 按钮类。
QCheckBox| 复选框类。
QRadioButton| 单选按钮类。
QLineEdit| 单行文本输入框类。
QTextEdit| 多行文本输入框类。
QComboBox| 组合框类。
QSlider| 滑动条类。
QProgressBar| 进度条类。
QListWidget| 列表框类。
QTreeWidget| 树形列表框类。
QTableWidget| 表格类。
QSpinBox| 数字调节框类。
QCalendarWidget| 日历控件类。
QTimeEdit| 时间编辑器类。
QDateEdit| 日期编辑器类。
QGraphicsView| 图形视图类，用于显示图形元素。
QWebView| Web 视图类，用于显示 Web 内容。
QDockWidget| 可停靠窗口类。


- 常用方法

##### QWidget(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()): 
构造函数，用于创建 QWidget 对象。
##### show(): 
显示窗口或小部件。
##### hide(): 
隐藏窗口或小部件。
##### close(): 
关闭窗口。
##### setLayout(layout: QLayout): 
设置小部件的布局管理器。
##### setGeometry(x: int, y: int, width: int, height: int): 
设置小部件的几何属性。
##### setWindowTitle(title: str): 
设置窗口标题。
##### setWindowIcon(icon: QIcon): 
设置窗口图标。
##### setEnabled(enable: bool): 
启用或禁用小部件。
##### isVisible() -> bool: 
检查小部件是否可见。
##### update(): 
请求小部件重绘。
##### repaint(): 
强制小部件重绘。
##### setStyleSheet(styleSheet: str): 
设置小部件的样式表。
##### resize(width: int, height: int): 
调整小部件的大小。
##### move(x: int, y: int): 
移动小部件的位置。
##### size() -> QSize: 
获取小部件的大小。
##### pos() -> QPoint: 
获取小部件的位置。
##### closeEvent(event: QCloseEvent): 
关闭事件处理函数
##### keyPressEvent(event: QKeyEvent): 
```py
def keyPressEvent(self, event):
    # 判断按下的按键是否是数字键 1
    if event.key() == Qt.Key_1:
        self.mousePressEvent(event)
    else:
        # 其他情况下，调用基类的方法以确保正常的按键处理
        super().keyPressEvent(event)
```
键盘按下事件处理函数
##### mousePressEvent(event: QMouseEvent): 
鼠标按下事件处理函数
```py
def mousePressEvent(self, event):
    # 记录鼠标按下时的位置
    self.drag_start_position = self.event.globalPos()
```
##### mouseMoveEvent(event: QMouseEvent):
用于处理鼠标移动事件
```py
def mouseMoveEvent(self, event):
    # 计算鼠标移动的距离
    delta = event.globalPos() - self.drag_start_position

    # 更新窗口位置
    new_position = self.pos() + delta
    self.move(new_position)

    # 更新起始位置，以便下一次移动计算
    self.drag_start_position = event.globalPos()
```
##### mouseReleaseEvent(event: QMouseEvent):
用于处理鼠标释放事件
```py
def mouseReleaseEvent(self, event):
    # 鼠标释放时清空起始位置
    self.drag_start_position = QPoint()
```

## QMainWindow (主窗口)

- 一般用于继承,来构建更复杂的窗口类

```py
# 创建一个QMainWindow实例
main_window = QMainWindow()
# 显示主窗口。
main_window.show()
# 关闭主窗口。
main_window.close()
# 设置主窗口的标题。
main_window.setWindowTitle("My Application")
# 设置主窗口的中心部件，通常是应用程序的主要内容区域。
main_window.setCentralWidget(widget)
# 返回与主窗口关联的菜单栏对象。
menu_bar = main_window.menuBar()
# 返回与主窗口关联的状态栏对象。
status_bar = main_window.statusBar()
# 将工具栏添加到主窗口。
tool_bar = QToolBar("MyToolBar")
main_window.addToolBar(tool_bar)
# 隐藏窗口标题栏
main_window.setWindowFlag(Qt.FramelessWindowHint)
# 设置窗口透明度
main_window.setWindowOpacity(0.9)
```
##### 窗口的大小
```py
# 可调整主窗口的大小
main_window.resize(800, 600)
# 禁止调整窗口大小
main_window.setFixedSize(width, height)
# 设置窗口最小值
main_window.setMinimumSize(800, 600)
# 最小/大化窗口
main_window.showMinimized()
main_window.showMaximized()
# 还原窗口
main_window.showNormal()
```

## QPushButton (按钮)
```py
# 创建一个 QPushButton 实例
button = QPushButton(parent=parent, text="Click me")
# 将按钮添加到窗口
button.setParent(widget)
# 显示按钮
button.show()
# 创建一个 QPushButton 实例，并设置图标
button = QPushButton(QIcon("path/to/icon.png"), "Click me")
# 设置按钮的位置和大小
button.setGeometry(50, 50, 100, 30)
# 阻止按钮获得键盘焦点(按钮无法被键盘访问/点击)
button.setFocusPolicy(Qt.NoFocus)
```
##### 设置按钮样式
```py
#可以分着写
button.setStyleSheet("background-color: #3498db;")
button.setStyleSheet("color: #ffffff;")
#也可以合在一起
button.setStyleSheet("background-color: #3498db; "
                     "color: #ffffff; "
                     "border-style: outset;"#outset/inset
                    )
```

##### 连接按钮事件到自定义函数
```py
# 连接按钮点击事件到函数
def on_button_click():
    print("Button clicked!")
button.clicked.connect(on_button_click)
##其他信号
#pressed：当按钮被按下时触发的信号。
#released：当按钮被释放时触发的信号。
#toggled：当按钮的状态切换（按下或释放）时触发的信号。
#hovered：当鼠标悬停在按钮上时触发的信号。
```


## QLabel (文本/图片)
```py
# 创建文本标签实例(parent为父参数,一般为窗口,或布局)
label = QLabel(text="文本标签", parent=parent)
# 用于设置标签的文本内容。
label.setText("Hello, PyQt!")
# 设置标签的字体。
font = QFont('Arial', 12)
label.setFont(font)
# 设置标签的样式表，允许使用 CSS 样式。
label.setStyleSheet('color: red; font-weight: bold;')
# 设置标签的位置,大小
label.setGeometry(250, 680, 800, 100)
# 返回标签的当前文本内容。
current_text = label.text()
# 用于设置标签显示的图片。
label.setPixmap(QPixmap('image.png'))
# 设置是否启用文本自动换行。
label.setWordWrap(True)
# 清除标签的文本内容或图片。
label.clear()
```

##### setAlignment (文本对齐方式)
```py
##单个对齐方式(当前为默认,等于不设置)
label.setAlignment(Qt.Alignment())
##可以通过按位或运算符 | 结合使用，以设置多个对齐方式
label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
####对齐方式:
#Qt.AlignLeft
#Qt.AlignRight
#Qt.AlignTop
#Qt.AlignBottom
#Qt.AlignHCenter 居中水平对齐
#Qt.AlignVCenter 居中垂直对齐
####
```

##### setTextInteractionFlags (文本交互)
```py
label.setTextInteractionFlags(Qt.NoTextInteraction) # 默认
####
# Qt.NoTextInteraction: 无文本交互。
# Qt.TextSelectableByMouse: 文本可以通过鼠标选择。
# Qt.TextSelectableByKeyboard: 文本可以通过键盘选择。
# Qt.LinksAccessibleByMouse: 可以通过鼠标点击访问链接。
# Qt.LinksAccessibleByKeyboard: 可以通过键盘访问链接。
# Qt.TextEditorInteraction: 文本可以编辑。
# Qt.TextBrowserInteraction: 文本可以被浏览，包括超链接可点击。
####

# 用于设置标签是否应该打开外部链接,默认为False,设置True则使用系统默认的web浏览器打开
label.setOpenExternalLinks(True) 
# 禁用了鼠标右键点击时的上下文菜单呼出功能
label.setContextMenuPolicy(Qt.NoContextMenu)
####
# Qt.NoContextMenu: 不显示上下文菜单。
# Qt.DefaultContextMenu: 显示默认上下文菜单。
# Qt.ActionsContextMenu: 显示与操作相关的上下文菜单。
# Qt.CustomContextMenu: 显示自定义上下文菜单。
####
```

## QLineEdit (输入框)
```py
# 创建 QLineEdit 实例
qlineEdit = QLineEdit()
# 设置占位符文本(提示文本)
qlineEdit.setPlaceholderText('你的占位符文本')
# 设置 QLineEdit 中显示的文本
qlineEdit.setText("Hello, PyQt!")
# 返回 QLineEdit 中当前显示的文本。
current_text = qlineEdit.text()
# 清空 QLineEdit 中的文本。
qlineEdit.clear()
# 设置 QLineEdit 中允许输入的最大字符数。
qlineEdit.setMaxLength(length: int)
# 设置 QLineEdit 是否可编辑。
qlineEdit.setEnabled(False)
# 设置 QLineEdit 是否只读。
qlineEdit.setReadOnly(True)
# 选中 QLineEdit 中的所有文本。
qlineEdit.selectAll()
```
## QMessageBox (消息框)
```py
# 显示信息框
QMessageBox.information(parent, 'Title', 'Message', QMessageBox.Ok)
# 显示警告框
QMessageBox.warning(parent, 'Title', 'Warning message', QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
# 显示错误框
QMessageBox.critical(parent, 'Title', 'Critical error message', QMessageBox.Retry | QMessageBox.Abort, QMessageBox.Retry)
# 显示显示询问框，并获取用户的选择
reply = QMessageBox.question(parent, 'Title', 'Do you want to proceed?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
if reply == QMessageBox.Yes:
    # 用户点击了 "是" 按钮的操作
else:
    # 用户点击了 "否" 按钮的操作
# 显示关于框
QMessageBox.about(parent, 'About', 'This is an example of QMessageBox about dialog.')
```
## QTreeWidget (树形图)
```py
main_window = QMainWindow()

# 创建 QTreeWidget 实例
myTree = QTreeWidget()
# 设置表头(列标签)
myTree.setHeaderLabels(["Column 1", "Column 2", "Column 3"])
# 禁止拖拽表头
myTree.header().setSectionsMovable(False)
# 设置表头的长度，这里将第一列设置为固定长度
myTree.header().setSectionResizeMode(0, QHeaderView.Fixed)
# 设置第一列的宽度为100
myTree.setColumnWidth(0, 100)
# 设置项目
main_window.add_tree_item("Root", "Root Value")
# 嵌套设置
parent_item = main_window.add_tree_item("Parent 2", "Parent 2 Value")
main_window.add_tree_item_to_parent(parent_item, "Child 3", "Child 3 Value")
# 在树形图的指定项和列位置设置自定义的小部件。
item = QTreeWidgetItem(["Item"])
widget = QPushButton("Button")
myTree.setItemWidget(item, 0, widget)
# 获取当前选择的项。
current_item = myTree.currentItem()
# 使用 setFixedSize 方法设置固定大小
myTree.setFixedSize(400, 300)
# 或者使用 resize 方法设置大小
myTree.resize(400, 300)
```

##### 设置顶层项
```py
# 向树形图添加一个顶层项（根节点）
item = QTreeWidgetItem(["Root Item"])
myTree.addItem(item)
# 同样是向树形图添加一个顶层项（根节点）
item = QTreeWidgetItem(["Root Item"])
myTree.addTopLevelItem(item)
# 向树形图添加多个顶层项。
items = [QTreeWidgetItem(["Item 1"]), QTreeWidgetItem(["Item 2"])]
myTree.addTopLevelItems(items)
# 向指定父项添加一个顶层项。
parent = QTreeWidgetItem(["Parent"])
item = QTreeWidgetItem(["Child"])
myTree.addTopLevelItem(parent, item)
# 向指定父项添加多个顶层项。
parent = QTreeWidgetItem(["Parent"])
items = [QTreeWidgetItem(["Child 1"]), QTreeWidgetItem(["Child 2"])]
myTree.addTopLevelItems(parent, items)
```
```py
# 
def add_tree_item(self, text1, text2, text3) -> None:
    item = QTreeWidgetItem(self.treeview_search_result)
    item.setText(0, text1)
    item.setText(1, text2)
    item.setText(2, text3)
```
##### 设置子项
```py
# 向指定父项添加一个子项。
parent = QTreeWidgetItem(["Parent"])
item = QTreeWidgetItem(["Child"])
parent.addChild(item)
# 向指定父项添加多个子项。
parent = QTreeWidgetItem(["Parent"])
items = [QTreeWidgetItem(["Child 1"]), QTreeWidgetItem(["Child 2"])]
parent.addChildren(items)
```

##### 连接事件
```py
# 连接项单击事件的槽函数。
treeWidget.itemClicked.connect(self.on_item_clicked)
def on_item_clicked(self, item, column):
    print(f"Item clicked: {item.text(column)}")
```

## QMenuBar (菜单栏)
```py
main_window = QMainWindow()

# 创建空的菜单栏对象
menu_bar = QMenuBar(main_window)
# 将菜单栏添加到主窗口
main_window.setMenuBar(menu_bar)
# 设置菜单栏高度为30
menu_bar.setFixedHeight(30)

```
## QLayoutItem (布局)

## QVBoxLayout (垂直布局)
```py
# 创建布局实例
layout = QVBoxLayout()
# 添加控件 (stretch 参数指定控件的拉伸因子，alignment 参数指定对齐方式。)
layout.addWidget(widget, stretch=0, alignment=0)
# 删除控件
layout.removeWidget(widget)
```

### QHBoxLayout (水平布局)

### QGridLayout (网格布局 )
- 将小部件排列成网格形式，可以在行和列中放置小部件。

### QStackedLayout (堆叠布局)

### QFormLayout (表单布局)


# PyQt5.QtGui
- 常见总览
  
类名|功能
:--|:--:  
QPainter|提供在小部件上进行绘图的功能。
QPixmap|用于处理图像的类，可以加载、保存、显示图像。
QIcon|图标类，用于表示应用程序、窗口或控件的图标。
QFont|字体类，用于设置文本的字体、大小、样式等属性。
QPalette|调色板类，用于设置小部件的颜色。
QBrush|画刷类，用于填充小部件的背景。
QColor|颜色类，用于表示和操作颜色。
QImage|图像类，用于在内存中表示和处理图像。
QKeySequence|键盘序列类，用于表示组合键。
QMouseEvent|鼠标事件类，用于表示鼠标事件的信息。
QKeyEvent|键盘事件类，用于表示键盘事件的信息。
QCursor|光标类，用于设置和获取光标的属性。
## QIcon (图标)
```py
# 从文件加载图标
icon_path = "path/to/icon.png"
icon = QIcon(icon_path)

# 从资源文件加载图标
#这里使用了 "edit-cut" 作为资源文件中的图标名称
icon_from_theme = QIcon.fromTheme("edit-cut")

# 从 QPixmap 创建图标
# 首先创建一个 QPixmap 对象
pixmap = QPixmap("path/to/image.png")
icon_from_pixmap = QIcon(pixmap)

# 设置图标尺寸
# 这里将图标的实际尺寸设置为 64x64
icon_actual_size = icon.actualSize(QSize(64, 64))
```
## QFont (字体)
```py
# 创建字体设置的实例
font = QFont() 
# 设置字体族（Family），例如 "Arial"、"Times New Roman" 等。
font.setFamily("Arial")
# 设置字体的大小。
font.setPointSize(12)
# 设置字体是否加粗。
font.setBold(True)
# 设置字体是否为斜体。
font.setItalic(True)
# 设置字体是否有下划线。
font.setUnderline(True)
# 设置字体是否有删除线。
font.setStrikeOut(True)
# 设置字体的大写形式，可选值包括 QFont.AllUppercase、QFont.AllLowercase 等
font.setCapitalization(QFont.AllUppercase)
# 设置字母间距。
font.setLetterSpacing(QFont.PercentageSpacing, 120)
# 设置单词间距。
font.setWordSpacing(5.0)
```

# PyQt5.QtCore

# PyQt5.QtNetwork

# PyQt5.QtSql

# PyQt5.QtXml


# PyQt5 && CSS

#### 直接使用组件名
```py
# 读取CSS配置
with open('your/CSS/file/path', 'r', encoding='utf-8') as style:
    css_data = style.read()
# 创建一个组件(以普通按钮为例)
my_button = QpushButton()
# 为组件设置样式表
my_button.setStyleSheet(css_data)
```

```css
@charset "UTF-8";

QPushButton {
    color: #fff;
    background-color: #3498db;
    border: 2px solid #2980b9;
    border-radius: 5px;
    padding: 5px 10px;
}

QPushButton:hover {
    background-color: #2980bb;
}
```

#### 使用样式类
```py
# 读取CSS配置
with open('your/CSS/file/path', 'r', encoding='utf-8') as style:
    css_data = style.read()
# 为组件设置样式类名
my_button.setObjectName("button-1")
# 为组件设置样式表
my_button.setStyleSheet(css_data)
```

```css
@charset "UTF-8";

QPushButton#button-1 {
    color: #fff;
    background-color: #3498db;
    border: 2px solid #2980b9;
    border-radius: 5px;
    padding: 5px 10px;
}

QPushButton#button-1:hover {
    background-color: #2980bb;
}

QPushButton#button-2 {
    color: #fff;
    background-color: #3498db;
    border: 2px solid rgb(115, 41, 185);
    border-radius: 5px;
    padding: 5px 10px;
}

QPushButton#button-2:hover {
    background-color: #1b9c14;
}

```