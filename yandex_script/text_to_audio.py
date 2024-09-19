import os
from argparse import ArgumentParser

from config import synthesize_config, yandex_config

# Аутентификация через API-ключ в Яндекс
yandex_config()


def synthesize(text: str, export_path: str):
    """Текст в аудио"""

    # Конфигурация текст в аудио
    model = synthesize_config()

    # Синтез речи и создание аудио с результатом.
    result = model.synthesize(text, raw_format=False)

    dirname = '/YandexSpeechKit/data/audio/'
    os.makedirs(dirname, exist_ok=True)

    result.export(f'/YandexSpeechKit/data/audio/{export_path}.wav', 'wav')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--text', type=str, help='Текст для синтеза', required=True)
    parser.add_argument('--export', type=str, help='Название синтезированного звука', required=False)

    args = parser.parse_args()

    synthesize(args.text, args.export)
