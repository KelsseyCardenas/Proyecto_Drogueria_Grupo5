from utilidades import validar_precio, validar_unidades, validar_mes


def registrar_medicamento(inventario, codigo, nombre, precio, unidades, mes):
    """
    Registra un medicamento en el inventario.

    Valida el código, nombre, precio, unidades y mes de vencimiento.

    Retorna:
        tuple: (True, mensaje) si se registra correctamente.
               (False, mensaje) si ocurre algún error.
    """
    codigo = str(codigo).strip()
    nombre = str(nombre).strip()

    precio_validado = validar_precio(precio)
    unidades_validadas = validar_unidades(unidades, permitir_cero=True)
    mes_validado = validar_mes(mes)

    if not codigo:
        return False, "El código no puede estar vacío."

    if codigo in inventario:
        return False, "Ya existe un medicamento con ese código."

    if not nombre:
        return False, "El nombre no puede estar vacío."

    if precio_validado is None:
        return False, "El precio debe ser un número mayor que cero."

    if unidades_validadas is None:
        return False, "Las unidades deben ser un entero igual o mayor que cero."

    if mes_validado is None:
        return False, "El mes de vencimiento debe estar entre 1 y 12."

    inventario[codigo] = [
        nombre,
        precio_validado,
        unidades_validadas,
        mes_validado
    ]

    return True, "Medicamento registrado correctamente."


def retirar_medicamento(inventario, codigo):
    """
    Retira un medicamento existente del inventario.

    Retorna:
        tuple: (True, mensaje) si se retira correctamente.
               (False, mensaje) si el código no existe.
    """
    codigo = str(codigo).strip()

    if codigo not in inventario:
        return False, "No se encontró un medicamento con ese código."

    del inventario[codigo]

    return True, "Medicamento retirado del inventario."


def actualizar_precio(inventario, codigo, nuevo_precio):
    """
    Actualiza el precio de un medicamento existente.

    Retorna:
        tuple: (True, mensaje) si se actualiza correctamente.
               (False, mensaje) si ocurre algún error.
    """
    codigo = str(codigo).strip()

    if codigo not in inventario:
        return False, "No se encontró un medicamento con ese código."

    precio_validado = validar_precio(nuevo_precio)

    if precio_validado is None:
        return False, "El precio debe ser un número mayor que cero."

    inventario[codigo][1] = precio_validado

    return True, "Precio actualizado correctamente."
from utilidades import validar_precio, validar_unidades, validar_mes


def registrar_medicamento(inventario, codigo, nombre, precio, unidades, mes):
    """Registra un medicamento si el código no existe y los datos son válidos."""
    codigo = str(codigo).strip()
    nombre = str(nombre).strip()
    precio_validado = validar_precio(precio)
    unidades_validadas = validar_unidades(unidades, permitir_cero=True)
    mes_validado = validar_mes(mes)

    if not codigo:
        return False, "El código no puede estar vacío."
    if codigo in inventario:
        return False, "Ya existe un medicamento con ese código."
    if not nombre:
        return False, "El nombre no puede estar vacío."
    if precio_validado is None:
        return False, "El precio debe ser un número mayor que cero."
    if unidades_validadas is None:
        return False, "Las unidades deben ser un entero igual o mayor que cero."
    if mes_validado is None:
        return False, "El mes de vencimiento debe estar entre 1 y 12."

    inventario[codigo] = [nombre, precio_validado, unidades_validadas, mes_validado]
    return True, "Medicamento registrado correctamente."


def retirar_medicamento(inventario, codigo):
    """Retira del inventario un medicamento existente."""
    codigo = str(codigo).strip()
    if codigo not in inventario:
        return False, "No se encontró un medicamento con ese código."
    del inventario[codigo]
    return True, "Medicamento retirado del inventario."


def actualizar_precio(inventario, codigo, nuevo_precio):
    """Actualiza el precio de un medicamento existente."""
    codigo = str(codigo).strip()
    if codigo not in inventario:
        return False, "No se encontró un medicamento con ese código."

    precio_validado = validar_precio(nuevo_precio)
    if precio_validado is None:
        return False, "El precio debe ser un número mayor que cero."

    inventario[codigo][1] = precio_validado
    return True, "Precio actualizado correctamente."