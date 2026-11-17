from registro import registrar_medicamento, retirar_medicamento, actualizar_precio
from calculos import vender_medicamento
from busquedas import (
    consultar_por_codigo,
    buscar_por_nombre,
    medicamentos_con_pocas_unidades,
)
from reportes import generar_informe, listar_todos
from utilidades import validar_precio, validar_unidades, validar_mes


def pedir_precio(mensaje):
    while True:
        valor = input(mensaje)
        precio = validar_precio(valor)
        if precio is not None:
            return precio
        print("Dato inválido. Escriba un precio mayor que cero.")


def pedir_unidades(mensaje, permitir_cero=False):
    while True:
        valor = input(mensaje)
        unidades = validar_unidades(valor, permitir_cero)
        if unidades is not None:
            return unidades
        if permitir_cero:
            print("Dato inválido. Escriba un número entero igual o mayor que cero.")
        else:
            print("Dato inválido. Escriba un número entero mayor que cero.")


def pedir_mes():
    while True:
        mes = validar_mes(input("Mes de vencimiento (1-12): "))
        if mes is not None:
            return mes
        print("Mes inválido. Debe estar entre 1 y 12.")


def mostrar_menu():
    print("\\n" + "=" * 45)
    print("       SISTEMA DE INVENTARIO - DROGUERÍA")
    print("=" * 45)
    print("1. Registrar medicamento")
    print("2. Retirar medicamento")
    print("3. Actualizar precio")
    print("4. Vender medicamento")
    print("5. Consultar por código")
    print("6. Buscar por nombre")
    print("7. Listar medicamentos con menos de 10 unidades")
    print("8. Mostrar informe de la droguería")
    print("9. Mostrar todo el inventario")
    print("0. Salir")
    print("=" * 45)


def main():
    # Cada clave es el código y su valor es:
    # [nombre, precio, unidades disponibles, mes de vencimiento].
    inventario = {}
    ventas_realizadas = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\\nREGISTRAR MEDICAMENTO")
            codigo = input("Código: ").strip()
            nombre = input("Nombre del medicamento: ").strip()
            precio = pedir_precio("Precio: $")
            unidades = pedir_unidades("Unidades disponibles: ", permitir_cero=True)
            mes = pedir_mes()
            correcto, mensaje = registrar_medicamento(
                inventario, codigo, nombre, precio, unidades, mes
            )
            print(mensaje)

        elif opcion == "2":
            codigo = input("Código del medicamento que desea retirar: ").strip()
            correcto, mensaje = retirar_medicamento(inventario, codigo)
            print(mensaje)

        elif opcion == "3":
            codigo = input("Código del medicamento: ").strip()
            nuevo_precio = pedir_precio("Nuevo precio: $")
            correcto, mensaje = actualizar_precio(inventario, codigo, nuevo_precio)
            print(mensaje)

        elif opcion == "4":
            codigo = input("Código del medicamento que va a vender: ").strip()
            unidades = pedir_unidades("Cantidad de unidades que va a vender: ")
            correcto, mensaje, total = vender_medicamento(
                inventario, codigo, unidades, ventas_realizadas
            )
            print(mensaje)

        elif opcion == "5":
            codigo = input("Código del medicamento que desea consultar: ").strip()
            print(consultar_por_codigo(inventario, codigo))

        elif opcion == "6":
            parte_nombre = input("Escriba el nombre o una parte del nombre: ")
            resultados = buscar_por_nombre(inventario, parte_nombre)
            if resultados:
                for resultado in resultados:
                    print(resultado)
            else:
                print("No se encontraron medicamentos con ese nombre.")

        elif opcion == "7":
            resultados = medicamentos_con_pocas_unidades(inventario)
            if resultados:
                print("\\nMedicamentos con menos de diez unidades:")
                for resultado in resultados:
                    print(resultado)
            else:
                print("No hay medicamentos con menos de diez unidades.")

        elif opcion == "8":
            generar_informe(inventario, ventas_realizadas)

        elif opcion == "9":
            listar_todos(inventario)

        elif opcion == "0":
            print("Gracias por utilizar el sistema de inventario de la droguería.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
