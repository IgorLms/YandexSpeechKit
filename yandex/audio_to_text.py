from argparse import ArgumentParser
from services.config import yandex_config, recognize_config
from services.services import save_file_audio_to_text, read_file_to_text, result_is_null

# Аутентификация через API-ключ в Яндекс
yandex_config()


def recognize(audio: str, return_: str = None) -> None:
    """
    Аудио в текст.

    :param audio: Путь к аудиофайлу.
    :param return_: text: Вернуть текст расшифровки; exist_text: Вернуть наличие текста расшифровки.
    """

    # Конфигурация аудио в текст
    model = recognize_config()

    # Распознавание речи в указанном аудиофайле и сохранение результатов в файл.
    result = model.transcribe_file(audio)

    # Сохранение результата расшифровки в файл
    filename = save_file_audio_to_text(result)

    # Вывод результата расшифровки или наличие расшифровки в зависимости параметра return_
    if return_ == 'text':
        read_file_to_text(filename)
    elif return_ == 'exist_text':
        result_is_null(result)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--audio', type=str, help='Путь к аудиофайлу', required=True)
    parser.add_argument('--return_', type=str, help='Что нужно вывести text или exist_text', required=False)

    args = parser.parse_args()

    recognize(args.audio, args.return_)
