# Módulo de reportes para la droguería - Integrante 4: Keyller Fabian Blandón Lozano

# Recibe: inventario (dict)
# Devuelve: float con el valor total monetario de todos los medicamentos en stock.
def calcular_valor_inventario(inventario):
    """Calcula el valor total del inventario multiplicando precio por unidades."""
    total = 0.0
    for datos in inventario.values():
        precio = datos[1]
        unidades = datos[2]
        total += precio * unidades
    return total


# Recibe: inventario (dict), mes_actual (int)
# Devuelve: list con los datos de los medicamentos que vencen en los próximos 3 meses.
def medicamentos_proximos_vencer(inventario, mes_actual):
    """Identifica los medicamentos que se vencen en los próximos tres meses."""
    por_vencer = []
    for codigo, datos in inventario.items():
        nombre = datos[0]
        mes_vencimiento = datos[3]
        # Calcula los próximos 3 meses manejando el ciclo de 12 meses
        meses_limite = [(mes_actual + i - 1) % 12 + 1 for i in range(1, 4)]
        if mes_vencimiento in meses_limite:
            por_vencer.append((codigo, nombre, mes_vencimiento))
    return por_vencer


# Recibe: inventario (dict)
# Devuelve: str con el nombre del medicamento más costoso o un mensaje si está vacío.
def medicamento_mas_costoso(inventario):
    """Encuentra el medicamento con el precio unitario más alto en el inventario."""
    if not inventario:
        return "No hay medicamentos registrados."
    
    mas_costoso = None
    max_precio = -1
    for datos in inventario.values():
        nombre = datos[0]
        precio = datos[1]
        if precio > max_precio:
            max_precio = precio
            mas_costoso = nombre
    return mas_costoso


# Recibe: inventario (dict), mes_actual (int)
# Devuelve: str con el informe formateado de la droguería para mostrar en pantalla de forma limpia.
def generar_informe_general(inventario, mes_actual):
    """Genera un informe completo y visualmente claro del estado actual de la droguería."""
    valor_total = calcular_valor_inventario(inventario)
    costoso = medicamento_mas_costoso(inventario)
    vencimientos = medicamentos_proximos_vencer(inventario, mes_actual)
    
    informe = "\n" + "="*45 + "\n"
    informe += "         INFORME GENERAL DE LA DROGUERÍA\n"
    informe += "="*45 + "\n"
    informe += f"💰 Valor total del inventario: ${valor_total:,.2f}\n"
    informe += f"💎 Medicamento más costoso: {costoso}\n"
    informe += f"⚠️ Próximos a vencer (3 meses): {len(vencimientos)} medicamento(s)\n"
    informe += "="*45
    return informe