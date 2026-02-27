import sys
from PyQt6.QtCore import QUrl, QTimer
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineCore import QWebEngineProfile
from PyQt6.QtWebEngineWidgets import QWebEngineView

def run_global_king():
    app = QApplication(sys.argv)
    browser = QWebEngineView()
    
    # Aapka Facebook Video Link
    video_url = "https://www.facebook.com/share/v/16zN1Fo3qf/"
    
    profile = QWebEngineProfile.defaultProfile()
    profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    print(f"🚀 Signal Active: Target Rahim Yar Khan via USA Server...")
    browser.load(QUrl(video_url))
    
    def take_screenshot():
        browser.grab().save("result_signal.png")
        print("📸 Screenshot Saved! Check your main page after the run finishes.")

    # 40 second baad video load hone par screenshot lega
    QTimer.singleShot(40000, take_screenshot)
    
    browser.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_global_king()
