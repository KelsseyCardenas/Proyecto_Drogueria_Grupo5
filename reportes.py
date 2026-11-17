from datetime import date
from calculos import proximo_a_vencerse
from utilidades import texto_medicamento


def generar_informe(inventario, ventas_realizadas):
    """Genera el informe general de la droguería."""
    print("\\n" + "=" * 55)
    print("          INFORME GENERAL DE LA DROGUERÍA")
    print("=" * 55)

    valor_total = sum(medicamento[1] * medicamento[2]
                      for medicamento in inventario.values())
    print(f"Valor total del inventario: ${valor_total:,.2f}")

    print("\\nMedicamentos que vencen en los próximos tres meses:")
    proximos = [
        (codigo, medicamento)
        for codigo, medicamento in inventario.items()
        if proximo_a_vencerse(medicamento[3])
    ]
    if proximos:
        for codigo, medicamento in proximos:
            print("- " + texto_medicamento(codigo, medicamento))
    else:
        print("No hay medicamentos registrados con vencimiento en los próximos tres meses.")

    print("\\nMedicamento más vendido:")
    vendidos = [
        (codigo, cantidad)
        for codigo, cantidad in ventas_realizadas.items()
        if codigo in inventario and cantidad > 0
    ]
    if vendidos:
        codigo, cantidad = max(vendidos, key=lambda elemento: elemento[1])
        print(f"{inventario[codigo][0]} (código {codigo}), unidades vendidas: {cantidad}")
    elif ventas_realizadas:
        print("Hay ventas registradas, pero los medicamentos vendidos ya fueron retirados del inventario.")
    else:
        print("Todavía no se han realizado ventas.")

    print("\\nMedicamento más costoso:")
    if inventario:
        codigo, medicamento = max(inventario.items(), key=lambda elemento: elemento[1][1])
        print(texto_medicamento(codigo, medicamento))
    else:
        print("El inventario está vacío.")

    print("=" * 55)


def listar_todos(inventario):
    """Muestra todos los medicamentos registrados."""
    print("\\nINVENTARIO COMPLETO")
    if not inventario:
        print("No hay medicamentos registrados.")
        return
    for codigo, medicamento in inventario.items():
        print(texto_medicamento(codigo, medicamento))
