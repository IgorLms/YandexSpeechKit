import argparse
import subprocess

import requests

from services.config import synthesize_config


def synthesize(text: str):
    """Текст в аудио"""

    # Конфигурация текст в аудио
    url, headers, data = synthesize_config(text)

    # Синтез речи и создание аудио с результатом.
    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError(f"Получен неверный ответ: код: {resp.status_code}, сообщение: {resp.text}")

        for chunk in resp.iter_content(chunk_size=None):
            yield chunk


def save_audio(output: str, text: str) -> None:
    """
    Сохранение аудиофайла в формате wav.

    :param output: Путь для сохранения синтезированного звука.
    :param text: Текст для синтеза.
    """

    # Сохранение аудиофайла в формате raw
    with open(output, "wb") as f:
        for audio_content in synthesize(text):
            f.write(audio_content)

    # Преобразование в формат wav с использованием sox
    output_raw = output
    output_wav = f"{output_raw[:-4]}.wav"
    subprocess.run(['sox', '-r', '-8000', '-b', '16', '-e', 'signed-integer', '-c', '1', output_raw, output_wav])

    # Удаление ненужного raw-файла
    subprocess.run(['rm', output_raw])

    # Вывод информации о созданном аудиофайле
    print(output_wav)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True, help="Текст для синтеза")
    parser.add_argument("--output", required=True, help="Путь для сохранения синтезированного звука")
    args = parser.parse_args()

    save_audio(args.output, args.text)
