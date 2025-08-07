def detect_ai_text(text):
    # Função simulada - aqui entra o modelo real no futuro
    return {
        "percentage": 42,
        "highlights": [
            {"start": 12, "end": 56, "confidence": "alta"},
            {"start": 123, "end": 180, "confidence": "moderada"},
        ],
        "suggestions": [
            {
                "original": "Este artigo visa elucidar...",
                "rewrite": "Neste estudo, buscamos esclarecer..."
            }
        ]
    }

def extract_text_from_pdf(filepath):
    return "Texto extraído do PDF (simulado)"

def generate_pdf_report():
    path = "/tmp/relatorio_detect_ai.pdf"
    with open(path, "w") as f:
        f.write("Relatório PDF simulado")
    return path
