from datetime import date

# Descuento aplicado a medicamentos próximos a vencerse: 8 %.
DESCUENTO_VENCIMIENTO = 0.08


def proximo_a_vencerse(mes_vencimiento, mes_actual=None):
    """Devuelve True si el vencimiento está en los próximos tres meses.
    Como el proyecto solo guarda el mes, se compara con los meses del calendario.
    """
    if mes_actual is None:
        mes_actual = date.today().month

    meses_proximos = [((mes_actual - 1 + i) % 12) + 1 for i in range(1, 4)]
    return mes_vencimiento in meses_proximos


def vender_medicamento(inventario, codigo, unidades, ventas_realizadas):
    """Vende unidades si existen suficientes y devuelve el total de la venta."""
    codigo = str(codigo).strip()

    if codigo not in inventario:
        return False, "No se encontró un medicamento con ese código.", None

    try:
        unidades = int(unidades)
    except (ValueError, TypeError):
        return False, "La cantidad debe ser un número entero.", None

    if unidades <= 0:
        return False, "La cantidad a vender debe ser mayor que cero.", None

    medicamento = inventario[codigo]
    if unidades > medicamento[2]:
        return False, f"No hay suficientes unidades. Disponibles: {medicamento[2]}.", None

    subtotal = medicamento[1] * unidades
    descuento = 0

    if proximo_a_vencerse(medicamento[3]):
        descuento = subtotal * DESCUENTO_VENCIMIENTO

    total = subtotal - descuento
    medicamento[2] -= unidades
    ventas_realizadas[codigo] = ventas_realizadas.get(codigo, 0) + unidades

    detalle = (
        f"Subtotal: ${subtotal:,.2f}\n"
        f"Descuento: ${descuento:,.2f}\n"
        f"Total a pagar: ${total:,.2f}"
    )
    return True, detalle, total
