import os
from dotenv import load_dotenv
from speechkit import configure_credentials, creds, model_repository
from speechkit.stt import AudioProcessingType, RecognitionModel
from speechkit.tts import SynthesisModel


def yandex_config() -> None:
    """Аутентификация через API-ключ в Яндекс версия 3"""

    # Парсинг файла .env
    load_dotenv()

    # Аутентификация через API-ключ.
    configure_credentials(
        yandex_credentials=creds.YandexCredentials(
            api_key=str(os.getenv("API_KEY")),
        )
    )


def recognize_config() -> RecognitionModel:
    """Конфигурация аудио в текст"""

    model = model_repository.recognition_model()

    # Настройки распознавания.
    model.model = 'general'
    model.language = 'ru-RU'
    model.audio_processing_type = AudioProcessingType.Stream

    return model


def synthesize_config(text: str) -> tuple:
    """Конфигурация текст в аудио"""

    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'

    headers = {
        'Authorization': 'Api-Key ' + str(os.getenv("API_KEY")),
    }

    data = {
        'text': text,
        'lang': 'ru-RU',
        'voice': 'jane',
        'emotion': 'neutral',
        'speed': 1.14,
        'folderId': str(os.getenv("FOLDER_ID")),
        'format': 'lpcm',
        'sampleRateHertz': 8000,
    }

    return url, headers, data
