# Интеграция Yandex SpeechKit с FreePBX + Asterisk

Проект по внедрению Yandex SpeechKit в FreePBX + Asterisk, который позволит решать следующие задачи:
- [x] Переводить текст в аудио;
- [x] Переводить аудио в текст.

## Быстрый старт
```bash
# Клонирование проекта
git clone https://github.com/IgorLms/YandexSpeechKit.git

# Переход в папку
cd YandexSpeechKit/

# Добавление API ключа YandexSpeechKit
echo API_KEY=API_KEY > .env

# Запуск скрипта 'аудио в текст'
python3 yandex/audio_to_text.py --audio='путь_к_аудио_файлу'
# Запуск скрипта 'аудио в текст' с распечаткой существования текста распознавания
python3 yandex/audio_to_text.py --audio='путь_к_аудио_файлу' --return_='exist_text'
# Запуск скрипта 'аудио в текст' с распечаткой текста распознавания
python3 yandex/audio_to_text.py --audio='путь_к_аудио_файлу' --return_='text'
```