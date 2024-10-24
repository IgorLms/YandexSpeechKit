import os
from datetime import datetime
from typing import Union

from pydub import AudioSegment
from speechkit.stt import Transcription


def save_file_audio_to_text(result: list[Transcription], path: str = None) -> str:
    """
    Сохранение результата расшифровки в файл.

    :param result: Результат расшифровки
    :param path: Путь для сохранения результата расшифровки
    """

    # Получаем дату и время
    date_time = datetime.now()

    # Создаем директорию для текущего дня, если её нет
    if path is not None:
        dir_name = f'{path}/data/text/{date_time.strftime("%Y/%m/%d/")}'
    else:
        dir_name = f'/YandexSpeechKit/data/text/{date_time.strftime("%Y/%m/%d/")}'
    filename = f'{dir_name}/{date_time.strftime("%H-%M-%S")}.txt'
    os.makedirs(dir_name, exist_ok=True)

    # Сохраняем текст в файле с именем в соответствии с датой и временем распознавания
    with open(filename, 'a', encoding='utf-8') as f:
        for _, res in enumerate(result):
            f.write(res.normalized_text)

    return filename


def save_file_text_to_audio(result: Union[bytes, AudioSegment], filename: str, path: str = None) -> None:
    """
    Сохранение результата расшифровки в файл.

    :param result: Результат расшифровки
    :param filename: Имя файла для сохранения
    :param path: Путь для сохранения результата расшифровки
    """

    # Создаем директорию
    if path is not None:
        dir_name = path
    else:
        dir_name = '/YandexSpeechKit/data/audio/'
    os.makedirs(dir_name, exist_ok=True)

    result.export(f'{dir_name}/{filename}.wav', 'wav')


def result_is_null(result: list[Transcription]) -> None:
    """
    Вывод в консоль 'yes' или 'no' в зависимости от результата расшифровки.
    'yes' - если результат расшифровки существует, 'no' - если нет.

    :param result: Результат расшифровки
    """

    if len(result) < 1:
        res = str(result[0])
        if res in ["", " ", ", "]:
            print("no")
        else:
            print("yes")
    else:
        print("no")


def read_file_to_text(filename: str) -> None:
    """
    Вывод в консоль текстового файла.

    :param filename: Имя файла для чтения
    """

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
