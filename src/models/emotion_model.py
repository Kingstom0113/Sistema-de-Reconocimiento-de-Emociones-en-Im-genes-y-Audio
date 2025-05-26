from transformers import pipeline

def analizar_sentimiento_texto(texto):
    try:
        clasificador = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
        resultado = clasificador(texto)[0]
        return resultado['label'], resultado['score']
    except Exception as e:
        print(f"❌ Error al analizar el sentimiento: {e}")
        return None, None
