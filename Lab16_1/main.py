# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import QIcon
# from ui import Ui_MainWindow
# from currency_converter import CurrencyConverter


# class CurrencyConv(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(CurrencyConv, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.init_UI()
    
#     def init_UI(self):
#         self.setWindowTitle('Конвертер валют') 
#         self.setWindowIcon(QIcon('exchanging.png'))
#         self.ui.input_currency.setPlaceholderText('Из валюты:')
#         self.ui.input_amount.setPlaceholderText('У меня есть:')
#         self.ui.output_currency.setPlaceholderText('В валюту:')
#         self.ui.output_amount.setPlaceholderText('Я получу:')        
#         self.ui.pushButton.clicked.connect(self.converter)

#     def converter(self):
#         c = CurrencyConverter()
#         input_currency = self.ui.input_currency.text()
#         output_currency = self.ui.output_currency.text()
#         input_amount = int(self.ui.input_amount.text())     
#         output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)
#         self.ui.output_amount.setText(str(output_amount))

# app = QtWidgets.QApplication([])
# application = CurrencyConv()
# application.show()
 
# sys.exit(app.exec())


import sys
import requests
import xml.etree.ElementTree as ET
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Конвертер валют')
        self.setWindowIcon(QIcon('exchanging.png'))
        self.ui.input_currency.setPlaceholderText('Из валюты:')
        self.ui.input_amount.setPlaceholderText('У меня есть:')
        self.ui.output_currency.setPlaceholderText('В валюту:')
        self.ui.output_amount.setPlaceholderText('Я получу:')
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        response = requests.get(
            'https://www.cbr.ru/scripts/XML_daily.asp',
            timeout=10
        )
        response.raise_for_status()
        root = ET.fromstring(response.content)

        rates = {'RUB': 1}

        for valute in root.findall('Valute'):
            code = valute.findtext('CharCode')
            nominal = int(valute.findtext('Nominal'))
            value = float(valute.findtext('Value').replace(',', '.'))
            rates[code] = value / nominal

        input_currency = self.ui.input_currency.text().strip().upper()
        output_currency = self.ui.output_currency.text().strip().upper()
        input_amount = float(self.ui.input_amount.text())

        output_amount = round(
            input_amount * rates[input_currency] / rates[output_currency], 2
        )

        self.ui.output_amount.setText(str(output_amount))


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
