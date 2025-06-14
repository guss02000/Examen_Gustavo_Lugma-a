from transformers import pipeline

classificador = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def clasificar_mensaje(texto):
    etiquetas = ["Urgente", "Moderado", "Normal"]
    resultado = classificador(texto, etiquetas)
    
    return {
        "mensaje": texto,
        "clasificacion": resultado["labels"][0],
        "confianza": resultado["scores"][0]
    }

