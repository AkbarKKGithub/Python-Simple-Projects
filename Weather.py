import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap
import requests

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.city_label = QLabel('Enter city name:')
        self.city_edit = QLineEdit()
        self.get_weather_button = QPushButton('Get Weather')
        self.get_weather_button.clicked.connect(self.get_weather)
        self.result_label = QLabel()

        layout.addWidget(self.city_label)
        layout.addWidget(self.city_edit)
        layout.addWidget(self.get_weather_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def get_weather(self):
        city = self.city_edit.text()
        weather_data = self.fetch_weather(city)
        if weather_data['cod'] == 200:
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            self.result_label.setText(f"Weather in {city}: {description}, Temperature: {temperature}°C")
        else:
            QMessageBox.critical(self, 'Error', 'City not found or error in fetching weather data.')

    def fetch_weather(self, city):
        api_key = 'f7da5b6b47d5213a006bec438d62fa91'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        return data

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
