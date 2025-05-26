import sys
sys.path.append("..")  # Para permitir imports entre módulos

from images.image_processor import detectar_emocion_imagen
from audio.audio_processor import transcribir_audio
from models.emotion_model import analizar_sentimiento_texto
from utils.helpers import validar_ruta

# Colores ANSI para consola (Windows 10+ soporta)
class Colores:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[90m'

def print_banner():
    print(f"{Colores.HEADER}{Colores.BOLD}=== Sistema de Reconocimiento de Emociones ==={Colores.ENDC}")

def menu():
    print_banner()
    print(f"{Colores.OKCYAN}1. Analizar emoción en una imagen facial{Colores.ENDC}")
    print(f"{Colores.OKCYAN}2. Analizar emoción desde un archivo de voz{Colores.ENDC}")
    opcion = input(f"{Colores.BOLD}Selecciona una opción (1 o 2): {Colores.ENDC}")

    if opcion == "1":
        ruta = input(f"{Colores.BOLD}Ruta de la imagen: {Colores.ENDC}")
        if validar_ruta(ruta):
            emocion = detectar_emocion_imagen(ruta)
            if emocion:
                print(f"{Colores.OKGREEN}🧠 Emoción detectada: {emocion}{Colores.ENDC}")
            else:
                print(f"{Colores.WARNING}⚠️ No se pudo detectar la emoción en la imagen.{Colores.ENDC}")
        else:
            print(f"{Colores.FAIL}❌ Imagen no encontrada.{Colores.ENDC}")
    elif opcion == "2":
        ruta = input(f"{Colores.BOLD}Ruta del archivo de audio (.wav): {Colores.ENDC}")
        if validar_ruta(ruta):
            texto = transcribir_audio(ruta)
            if texto:
                print(f"{Colores.OKBLUE}🗣 Transcripción: {texto}{Colores.ENDC}")
                emocion, score = analizar_sentimiento_texto(texto)
                if emocion:
                    print(f"{Colores.OKGREEN}🧠 Sentimiento detectado: {emocion} {Colores.GRAY}(Confianza: {score:.2f}){Colores.ENDC}")
                else:
                    print(f"{Colores.WARNING}⚠️ No se pudo detectar el sentimiento en el texto.{Colores.ENDC}")
            else:
                print(f"{Colores.WARNING}⚠️ No se pudo transcribir el audio.{Colores.ENDC}")
        else:
            print(f"{Colores.FAIL}❌ Archivo de audio no encontrado.{Colores.ENDC}")
    else:
        print(f"{Colores.FAIL}❌ Opción no válida.{Colores.ENDC}")

if __name__ == "__main__":
    menu()
