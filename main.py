from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QVBoxLayout, QWidget, \
    QPushButton, QLabel, QDoubleSpinBox

from GeometryFileLoader import GeometryFileLoader
from GeometryManager import GeometryManager

PATH = "Data/DataFile.txt"


class GeometryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Геометрические построения")
        self.setGeometry(100, 100, 850, 850)

        # Создаем сцену и виджет для отображения
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.view.setSceneRect(-200, -200, 400, 400)

        # Основной виджет и layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Добавляем виджет сцены
        self.layout.addWidget(self.view)

        # Создаем элементы управления
        self.create_controls()

        # Хранение объектов
        self.objects = []

        # Загрузка примеров из файла
        self.file_loader = GeometryFileLoader(PATH)
        self.geometry_manager = GeometryManager(self.scene)
        self.load_data()

    def load_data(self):
        """Загружает данные из файла."""
        objects = self.file_loader.load_data()
        for obj in objects:
            self.geometry_manager.add_object(*obj)

    def create_controls(self):
        """Создает элементы управления."""
        # Кнопка для добавления точки
        self.add_point_button = QPushButton("Добавить точку")
        self.add_point_button.clicked.connect(self.add_point)

        # Поля для ввода координат точки
        self.layout.addWidget(QLabel("Координаты точки:"))  # Общая подсказка

        self.layout.addWidget(QLabel("x:"))  # Подсказка для x
        self.point_x_input = QDoubleSpinBox()
        self.point_x_input.setRange(-200, 400)
        self.point_x_input.setSingleStep(1)
        self.point_x_input.setValue(0)
        self.layout.addWidget(self.point_x_input)

        self.layout.addWidget(QLabel("y:"))  # Подсказка для y
        self.point_y_input = QDoubleSpinBox()
        self.point_y_input.setRange(-200, 400)
        self.point_y_input.setSingleStep(1)
        self.point_y_input.setValue(0)
        self.layout.addWidget(self.point_y_input)
        self.layout.addWidget(self.add_point_button)

        # Кнопка для добавления линии
        self.add_line_button = QPushButton("Добавить линию")
        self.add_line_button.clicked.connect(self.add_line)

        # Поля для ввода координат двух точек линии
        self.layout.addWidget(QLabel("Координаты двух точек линии:"))  # Общая подсказка

        self.layout.addWidget(QLabel("x1:"))
        self.line_x1_input = QDoubleSpinBox()
        self.line_x1_input.setRange(-200, 400)
        self.line_x1_input.setSingleStep(1)
        self.line_x1_input.setValue(0)
        self.layout.addWidget(self.line_x1_input)

        self.layout.addWidget(QLabel("y1:"))
        self.line_y1_input = QDoubleSpinBox()
        self.line_y1_input.setRange(-200, 400)
        self.line_y1_input.setSingleStep(1)
        self.line_y1_input.setValue(0)
        self.layout.addWidget(self.line_y1_input)

        self.layout.addWidget(QLabel("x2:"))
        self.line_x2_input = QDoubleSpinBox()
        self.line_x2_input.setRange(-200, 400)
        self.line_x2_input.setSingleStep(1)
        self.line_x2_input.setValue(0)
        self.layout.addWidget(self.line_x2_input)

        self.layout.addWidget(QLabel("y2:"))
        self.line_y2_input = QDoubleSpinBox()
        self.line_y2_input.setRange(-200, 400)
        self.line_y2_input.setSingleStep(1)
        self.line_y2_input.setValue(0)
        self.layout.addWidget(self.line_y2_input)

        self.layout.addWidget(self.add_line_button)

        # Кнопка для добавления окружности
        self.add_circle_button = QPushButton("Добавить окружность")
        self.add_circle_button.clicked.connect(self.add_circle)

        # Поля для ввода центра и радиуса окружности
        self.layout.addWidget(QLabel("Центр окружности и радиус:"))

        self.layout.addWidget(QLabel("x:"))  # Подсказка для x
        self.circle_x_input = QDoubleSpinBox()
        self.circle_x_input.setRange(-200, 400)
        self.circle_x_input.setSingleStep(1)
        self.circle_x_input.setValue(0)
        self.layout.addWidget(self.circle_x_input)

        self.layout.addWidget(QLabel("y:"))  # Подсказка для y
        self.circle_y_input = QDoubleSpinBox()
        self.circle_y_input.setRange(-200, 400)
        self.circle_y_input.setSingleStep(1)
        self.circle_y_input.setValue(0)
        self.layout.addWidget(self.circle_y_input)

        self.layout.addWidget(QLabel("Радиус:"))
        self.circle_radius_input = QDoubleSpinBox()
        self.circle_radius_input.setRange(1, 400)
        self.circle_radius_input.setSingleStep(1)
        self.circle_radius_input.setValue(1)
        self.layout.addWidget(self.circle_radius_input)

        self.layout.addWidget(self.add_circle_button)

    def add_point(self):
        """Добавляет точку на сцену."""
        x = self.point_x_input.value()
        y = self.point_y_input.value()
        self.geometry_manager.add_object("point", x, y)

    def add_line(self):
        """Добавляет линию на сцену."""
        x1 = self.line_x1_input.value()
        y1 = self.line_y1_input.value()
        x2 = self.line_x2_input.value()
        y2 = self.line_y2_input.value()
        self.geometry_manager.add_object("line", x1, y1, x2, y2)

    def add_circle(self):
        """Добавляет окружность на сцену."""
        x = self.circle_x_input.value()
        y = self.circle_y_input.value()
        radius = self.circle_radius_input.value()
        self.geometry_manager.add_object("circle", x, y, radius)


def main():
    app = QApplication([])
    window = GeometryApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
