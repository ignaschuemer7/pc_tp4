from synthesizer import Synthesizer
from datetime import datetime


instanteInicial = datetime.now()
s=Synthesizer(44100, "Estrellita_donde_estas.txt", "flauta.txt").create_wav()
instanteFinal = datetime.now()
print(instanteFinal - instanteInicial)


