import os
from datetime import datetime
from argparse import ArgumentParser
from config import yandex_config, recognize_config


# Аутентификация через API-ключ в Яндекс
yandex_config()


def recognize(audio: str) -> str:
    """Аудио в текст"""

    # Конфигурация аудио в текст
    model = recognize_config()

    # Распознавание речи в указанном аудиофайле и сохранение результатов в файл.
    result = model.transcribe_file(f'/YandexSpeechKit/data_asterisk/{audio}')
    date_time = datetime.now()
    dirname = f'/YandexSpeechKit/data/text/{date_time.strftime("%Y/%m/%d/")}'
    filename = f'/YandexSpeechKit/data/text/{date_time.strftime("%Y/%m/%d/%H-%M-%S")}.txt'

    os.makedirs(dirname, exist_ok=True)
    with open(filename, 'a', encoding='utf-8') as f:
        for _, res in enumerate(result):
            f.write(res.normalized_text)

    return filename


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--audio', type=str, help='Путь к аудиофайлу', required=True)

    args = parser.parse_args()

    recognize(args.audio)
