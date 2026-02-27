import sys
from PyQt6.QtCore import QUrl, QTimer
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineCore import QWebEngineProfile
from PyQt6.QtWebEngineWidgets import QWebEngineView

def run_global_king():
    # 1. System start
    app = QApplication(sys.argv)
    browser = QWebEngineView()
    
    # 2. Target Video Link
    video_url = "https://www.facebook.com/share/v/16zN1Fo3qf/"
    
    # 3. USA Server Identity (User Agent)
    profile = QWebEngineProfile.defaultProfile()
    profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    print(f"🚀 Signal Active: Target Rahim Yar Khan via USA Server...")
    browser.load(QUrl(video_url))
    
    # 4. Success Proof (Screenshot)
    def take_screenshot():
        browser.grab().save("result_signal.png")
        print("📸 Screenshot Saved! Check main page after 1 minute.")

    # 40 second intezar taake video load ho jaye
    QTimer.singleShot(40000, take_screenshot)
    
    browser.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_global_king()
