# Internationalization in PySide6 Painter Application

This document explains how internationalization (i18n) is implemented in the PySide6 Painter application, allowing the application to be displayed in multiple languages.

## Features

- Support for multiple languages (English, French, Chinese)
- Language selection through the Settings dialog
- Automatic language detection based on system locale
- Persistence of language preferences across application restarts

## Implementation Details

### Translation Files

The application uses Qt's translation system with `.qm` binary translation files:

- `chinese.qm`: Application translations for Simplified Chinese
- `french.qm`: Application translations for French
- `qt_zh_CN_official.qm`: Qt framework translations for Simplified Chinese
- `qt_fr_FR_official.qm`: Qt framework translations for French

### Settings Dialog

Users can select their preferred language through the Settings dialog:

1. Default: Uses the system language if available, otherwise falls back to English
2. English: Forces the application UI to display in English
3. French: Translates the application UI to French
4. Chinese: Translates the application UI to Simplified Chinese

### Translation Mechanism

1. **QTranslator**: The application uses Qt's `QTranslator` class to load and apply translations
2. **tr()**: UI text is wrapped in `tr()` calls to mark it for translation
3. **Resource System**: Translation files are embedded in the application binary using Qt's resource system

### Language Persistence

The application stores language preferences in the application settings using `QSettings`:

```python
settings = QSettings("Blikoon Technologies", "Painter App")
settings.setValue("language", selected_language)

```