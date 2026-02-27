import sys
from PyQt6.QtCore import QUrl, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEngineSettings

class GlobalKingBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GLOBAL KING BROWSER | SYSTEM ACTIVE")
        self.setGeometry(100, 100, 1200, 800)

        # High-Speed Settings
        profile = QWebEngineProfile.defaultProfile()
        profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
        settings = profile.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        toolbar = QHBoxLayout()

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL to Inject Signals...")
        self.url_input.setFixedHeight(35)
        self.url_input.returnPressed.connect(self.load_url)

        self.go_btn = QPushButton("ACTIVATE GLOBAL")
        self.go_btn.setFixedSize(150, 35)
        self.go_btn.setStyleSheet("background-color: gold; color: black; font-weight: bold;")
        self.go_btn.clicked.connect(self.load_url)

        toolbar.addWidget(self.url_input)
        toolbar.addWidget(self.go_btn)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        layout.addLayout(toolbar)
        layout.addWidget(self.browser)

    def load_url(self):
        url = self.url_input.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GlobalKingBrowser()
    window.show()
    sys.exit(app.exec())
