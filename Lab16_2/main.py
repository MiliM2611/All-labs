import sys
from PyQt5 import QtWidgets
from photoCalculator import Ui_PhotoCalcWindow


class PhotoCalculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_PhotoCalcWindow()
        self.ui.setupUi(self)

        self.ui.calculate_button.clicked.connect(self.calculatePrice)

    def calculatePrice(self):
        prices = {
            "Репортаж": 2500,
            "Свадьба": 4000,
            "Портретная съёмка": 3000,
            "Контент для бизнеса": 3500,
            "Предметная съёмка": 2500
        }

        processingPrices = {
            "Без обработки": 0,
            "Базовая обработка": 50,
            "Ретушь выбранных кадров": 150
        }

        photoFormat = self.ui.format_combo.currentText()
        hours = self.ui.hours_spin.value()
        photos = self.ui.photos_spin.value()
        processing = self.ui.processing_combo.currentText()
        expenses = self.ui.expenses_spin.value()

        shootingPrice = prices[photoFormat] * hours
        processingPrice = processingPrices[processing] * photos
        totalPrice = shootingPrice + processingPrice + expenses

        self.ui.result_label.setText(f"Стоимость: {totalPrice:.0f} ₽")


app = QtWidgets.QApplication(sys.argv)
window = PhotoCalculator()
window.show()

sys.exit(app.exec_())
