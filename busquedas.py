from utilidades import texto_medicamento


def consultar_por_codigo(inventario, codigo):
    """Consulta un medicamento usando su código."""
    codigo = str(codigo).strip()
    if codigo in inventario:
        return texto_medicamento(codigo, inventario[codigo])
    return "No se encontró un medicamento con ese código."


def buscar_por_nombre(inventario, parte_nombre):
    """Busca coincidencias en el nombre sin distinguir mayúsculas."""
    parte_nombre = str(parte_nombre).strip().lower()
    resultados = []

    if not parte_nombre:
        return resultados

    for codigo, medicamento in inventario.items():
        if parte_nombre in medicamento[0].lower():
            resultados.append(texto_medicamento(codigo, medicamento))

    return resultados


def medicamentos_con_pocas_unidades(inventario):
    """Lista medicamentos con menos de diez unidades disponibles."""
    return [
        texto_medicamento(codigo, medicamento)
        for codigo, medicamento in inventario.items()
        if medicamento[2] < 10
    ]
