import sys
import os
from PyQt6.QtCore import QUrl, QTimer
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineCore import QWebEngineProfile
from PyQt6.QtWebEngineWidgets import QWebEngineView

def run_global_king():
    # Force off-screen rendering
    os.environ["QT_QPA_PLATFORM"] = "offscreen"
    app = QApplication(sys.argv)
    browser = QWebEngineView()
    
    video_url = "https://www.facebook.com/share/v/16zN1Fo3qf/"
    
    profile = QWebEngineProfile.defaultProfile()
    profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    print(f"🚀 Signal Active: Sending to Rahim Yar Khan via USA Server...")
    browser.load(QUrl(video_url))
    
    def take_screenshot():
        browser.grab().save("result_signal.png")
        print("📸 Screenshot Saved! Check main page now.")
        app.quit()

    # 40 second wait for load
    QTimer.singleShot(40000, take_screenshot)
    app.exec()

if __name__ == "__main__":
    run_global_king()
