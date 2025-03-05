import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator, QSettings, QLocale
from PySide6.QtGui import QScreen
from mainwindow import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # Set up translators
    translator = QTranslator()
    gui_translator = QTranslator()
    
    # Get language settings
    settings = QSettings("Blikoon Technologies", "Painter App")
    user_language = settings.value("language", "english")
    
    system_lang = QLocale.system().name()
    print(f"System language is: {system_lang}")
    
    # Load appropriate translation based on settings
    if user_language == "default":
        if system_lang == "zh_CN":
            translator.load(":/translations/chinese.qm")
            gui_translator.load(":/translations/qt_zh_CN_official.qm")
            app.installTranslator(translator)
            app.installTranslator(gui_translator)
        
        if system_lang == "fr_FR":
            translator.load(":/translations/french.qm")
            gui_translator.load(":/translations/qt_fr_FR_official.qm")
            app.installTranslator(translator)
            app.installTranslator(gui_translator)
    
    elif user_language == "english":
        # English loaded by default
        pass
    
    elif user_language == "french":
        translator.load(":/translations/french.qm")
        gui_translator.load(":/translations/qt_fr_FR_official.qm")
        app.installTranslator(translator)
        app.installTranslator(gui_translator)
    
    elif user_language == "chinese":
        translator.load(":/translations/chinese.qm")
        gui_translator.load(":/translations/qt_zh_CN_official.qm")
        app.installTranslator(translator)
        app.installTranslator(gui_translator)
    
    window = MainWindow()
    window.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())