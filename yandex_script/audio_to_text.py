from argparse import ArgumentParser
from config import yandex_config, recognize_config
from services import save_file_audio_to_text

# Аутентификация через API-ключ в Яндекс
yandex_config()


def recognize(audio: str) -> None:
    """Аудио в текст"""

    # Конфигурация аудио в текст
    model = recognize_config()

    # Распознавание речи в указанном аудиофайле и сохранение результатов в файл.
    result = model.transcribe_file(f'/YandexSpeechKit/data_asterisk/{audio}')

    # Сохранение результата расшифровки в файл
    save_file_audio_to_text(result)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--audio', type=str, help='Путь к аудиофайлу', required=True)

    args = parser.parse_args()

    recognize(args.audio)
