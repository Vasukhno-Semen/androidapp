[app]
# Имя вашего приложения
title = PaperLab

# Пакетное имя (должно быть уникальным)
package.name = PaperLab
package.domain = org.example

# Версия вашего приложения
version = 0.1

# Основной файл вашего приложения
source.main = main.py

# Папка, содержащая ваш код
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

# Значок приложения
#icon.filename = %(source.dir)s/data/icon.png

# Картинка загрузочного экрана (опционально)
# presplash.filename = %(source.dir)s/экран загрузки.png

# Минимальная версия Android
android.minapi = 21

# Целевая версия Android
android.sdk = 30

# Архитектуры, которые вы хотите поддерживать
android.archs = arm64-v8a, armeabi-v7a

# Разрешения, необходимые вашему приложению
# android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (Опционально) Используемые библиотеки и модули
requirements = python3,kivy,Pillow,babel,kivy-garden.mapview,kivycalendar3,sqlite3
fullscreen = 1

[buildozer]
# Лог уровня отладки (0 - минимальный, 2 - максимальный)
log_level = 2

# Платформа, для которой вы собираете приложение
target = android
