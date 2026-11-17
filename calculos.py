# Módulo de cálculos y ventas para la droguería - Integrante 2: Fanny Zuleyka Martínez Lloreda

# Constante global para el descuento de medicamentos próximos a vencer
DESCUENTO_VENCIMIENTO = 0.08


# Recibe: inventario (dict), codigo (str), unidades_a_vender (int)
# Devuelve: tupla (bool, str) indicando si la venta fue exitosa y descontada, o un mensaje de error si no hay stock.
def vender_medicamento(inventario, codigo, unidades_a_vender):
    """Descuenta unidades del inventario validando que exista stock suficiente."""
    codigo = str(codigo).strip()
    
    if codigo not in inventario:
        return False, "El medicamento no existe en el inventario."
    
    try:
        unidades_a_vender = int(unidades_a_vender)
    except ValueError:
        return False, "La cantidad a vender debe ser un número entero."
    
    if unidades_a_vender <= 0:
        return False, "La cantidad a vender debe ser mayor a cero."
        
    nombre, precio, unidades_disponibles, mes_vencimiento = inventario[codigo]
    
    if unidades_a_vender > unidades_disponibles:
        return False, f"Stock insuficiente. Solo hay {unidades_disponibles} unidades disponibles."
        
    # Descuenta las unidades del inventario
    inventario[codigo][2] -= unidades_a_vender
    return True, f"Venta exitosa de {unidades_a_vender} unidad(es) de {nombre}."


# Recibe: precio (float), unidades (int), mes_vencimiento (int), mes_actual (int)
# Devuelve: float con el valor total a pagar aplicando el 8% de descuento si está próximo a vencer.
def calcular_valor_venta(precio, unidades, mes_vencimiento, mes_actual):
    """Calcula el costo total aplicando la constante de descuento si vence pronto."""
    subtotal = precio * unidades
    
    # Si vence en el mes actual o en el siguiente, aplica la constante de descuento del 8%
    if mes_vencimiento == mes_actual or mes_vencimiento == (mes_actual % 12) + 1:
        descuento = subtotal * DESCUENTO_VENCIMIENTO
        total_con_descuento = subtotal - descuento
        return total_con_descuento
        
    return subtota