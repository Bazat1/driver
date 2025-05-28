import sys
from PyQt5.QtWidgets import *

class DriverDirectory(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Справочник водителей")
        self.current_id = 1

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "ФИО", "Номер телефона", "Стаж", "ID автомобиля", "Статус"])
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 120)
        self.table.setColumnWidth(3, 50)
        self.table.setColumnWidth(4, 100)
        self.table.setColumnWidth(5, 100)
        self.table.verticalHeader().setVisible(False)

        self.fio_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.experience_input = QLineEdit()
        self.car_id_input = QLineEdit()
        self.status_input = QLineEdit()

        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_driver)

        self.delete_button = QPushButton("Удалить")
        self.delete_button.clicked.connect(self.delete_driver)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.delete_button)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(QLabel("ФИО:"))
        layout.addWidget(self.fio_input)
        layout.addWidget(QLabel("Номер телефона:"))
        layout.addWidget(self.phone_input)
        layout.addWidget(QLabel("Стаж:"))
        layout.addWidget(self.experience_input)
        layout.addWidget(QLabel("ID автомобиля:"))
        layout.addWidget(self.car_id_input)
        layout.addWidget(QLabel("Статус:"))
        layout.addWidget(self.status_input)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def add_driver(self):
        try:
            fio = self.fio_input.text()
            phone = self.phone_input.text()
            experience = int(self.experience_input.text())
            car_id_val = self.car_id_input.text()
            status = self.status_input.text()

            if not fio or not phone or not car_id_val or not status:
                raise ValueError("Все поля должны быть заполнены")

        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", str(e))
            return

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        self.table.setItem(row_position, 0, QTableWidgetItem(str(self.current_id)))
        self.table.setItem(row_position, 1, QTableWidgetItem(fio))
        self.table.setItem(row_position, 2, QTableWidgetItem(phone))
        self.table.setItem(row_position, 3, QTableWidgetItem(str(experience)))
        self.table.setItem(row_position, 4, QTableWidgetItem(car_id_val))
        self.table.setItem(row_position, 5, QTableWidgetItem(status))

        self.current_id += 1

        self.fio_input.clear()
        self.phone_input.clear()
        self.experience_input.clear()
        self.car_id_input.clear()
        self.status_input.clear()

    def delete_driver(self):
        selected_rows = self.table.selectionModel().selectedRows()

        if not selected_rows:
            QMessageBox.warning(self, "Ошибка", "Выберите водителя для удаления")
            return


        for row in sorted(selected_rows, key=lambda x: x.row(), reverse=True):
            self.table.removeRow(row.row())

        QMessageBox.information(self, "Успех", "Водитель удален")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    directory = DriverDirectory()
    directory.show()
    sys.exit(app.exec_())