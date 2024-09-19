import sys
from yandex_script.audio_to_text import recognize

sys.stdout = recognize(sys.argv[-1])
