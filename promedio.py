
PESOS = {"T1": 0.10, "EP": 0.20, "T2": 0.20, "EF": 0.50}

def validar_nota(nota):
    """Verifica que la nota esté en la escala vigesimal (0 a 20)."""
    if not 0 <= nota <= 20:
        raise ValueError(f"Nota fuera de rango: {nota}")
    return nota


def calcular_promedio(notas):
    """Recibe un diccionario con las cuatro notas y devuelve el promedio ponderado."""
    total = 0
    for evaluacion,  peso in PESOS.items():
      total += validar_nota(notas[evaluacion]) * peso
    return round(total, 2)

if __name__ == "__main__":
    # Notas de ejemplo de un estudiante (escala vigesimal)
    notas_ejemplo = {"T1": 14, "EP": 15, "T2": 13, "EF": 16}
    print("Promedio final:", calcular_promedio(notas_ejemplo))