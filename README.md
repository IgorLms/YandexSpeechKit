```bash
# Сборка образа
docker build -t yandex_speech_kit:1 .
# Запуск образа в windows
docker run -d -t --rm --name yandex_speech_kit --env-file .env -v "/$(pwd)/data":/YandexSpeechKit/data yandex_speech_kit:1
# Запуск скрипта в докере
docker exec yandex_speech_kit python3 yandex_script/text_to_audio.py --export='название_файла' --text='текст_для_аудио'
```