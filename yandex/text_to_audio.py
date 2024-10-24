from argparse import ArgumentParser

from services.config import synthesize_config, yandex_config
from services.services import save_file_text_to_audio

# Аутентификация через API-ключ в Яндекс
yandex_config()


def synthesize(text: str, filename: str):
    """Текст в аудио"""

    # Конфигурация текст в аудио
    model = synthesize_config()

    # Синтез речи и создание аудио с результатом.
    result = model.synthesize(text, raw_format=False)

    # Сохранение аудиофайла
    save_file_text_to_audio(result, filename)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--text', type=str, help='Текст для синтеза', required=True)
    parser.add_argument('--export', type=str, help='Название синтезированного звука', required=False)

    args = parser.parse_args()

    synthesize(args.text, args.export)
