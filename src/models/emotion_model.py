from transformers import pipeline

# Creamos una instancia global para evitar recargar el modelo cada vez
_emotion_pipeline = pipeline("sentiment-analysis")

def analizar_sentimiento_texto(texto):
    """
    Analiza el sentimiento de un texto y retorna la emoción y el score de confianza.
    """
    resultado = _emotion_pipeline(texto)
    emocion = resultado[0]["label"]
    score = resultado[0]["score"]
    return emocion, score

class EmotionModel:
    def __init__(self):
        self.pipeline = _emotion_pipeline

    def analizar(self, texto):
        resultado = self.pipeline(texto)
        return resultado[0]["label"]
