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

# Сборка образа
docker build -t yandex_speech_kit:1 .

# Запуск образа
docker run \
  -d \
  -t \
  --name yandex_speech_kit \
  --env-file .env \
  -v /$(pwd)/data:/YandexSpeechKit/data \
  -v /var/spool/asterisk/monitor:/YandexSpeechKit/data_asterisk \
  yandex_speech_kit:1

# Запуск скрипта 'текст в аудио' в докере
docker exec yandex_speech_kit python3 yandex/text_to_audio.py --export='название_файла' --text='текст_для_аудио'

# Запуск скрипта 'аудио в текст' в докере
docker exec yandex_speech_kit python3 yandex/audio_to_text.py --audio='путь_к_файлу_в_папке_/var/spool/asterisk/monitor'
# или
docker exec yandex_speech_kit python3 yandex/agi_audio_to_text.py 'путь_к_файлу_в_папке_/var/spool/asterisk/monitor'
```