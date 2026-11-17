PROYECTO 2 - DROGUERÍA
Grupo 5

Integrantes:
1. Kelssey Tifanny Cardenas Quejada
2. Fanny Zuleyka Martínez Lloreda
3. Handerson Correa Córdoba
4. Keyller Fabian Blandon Lozano
5. Lina Jhajaira Lemos Moren

ARCHIVOS:
- registro.py: registrar, retirar y actualizar precio.
- calculos.py: vender medicamentos y aplicar el descuento del 8 %.
- busquedas.py: consultar por código, buscar por nombre y listar pocas unidades.
- reportes.py: informe general e inventario completo.
- utilidades.py: validaciones y formato de los medicamentos.
- main.py: menú principal.

CÓMO EJECUTAR:
1. Tener Python 3 instalado.
2. Guardar todos los archivos en la misma carpeta.
3. Abrir una terminal dentro de esa carpeta.
4. Ejecutar: python main.py

DATOS DEL INVENTARIO:
Cada medicamento se guarda en un diccionario:
código: [nombre, precio, unidades disponibles, mes de vencimiento]

El mes de vencimiento se ingresa como número del 1 al 12.
El sistema aplica el descuento del 8 % cuando el mes de vencimiento está
dentro de los tres meses siguientes al mes actual.

NOTA:
El proyecto solo registra el mes de vencimiento, no el año, porque así lo
especifica el enunciado. Para un control real de medicamentos sería necesario
guardar la fecha completa de vencimiento.
