# test_selenium_consola.py
# Ingeniero de Pruebas (QA)
# Simulación de Selenium para pruebas de interfaz de consola
# Inyecta entradas simuladas al menú y valida las respuestas

import io
import sys
from interfaz import iniciar_menu


def capturar_salida(input_simulado):
    """
    Ejecuta iniciar_menu con entradas simuladas y captura la salida en consola.
    Retorna el texto impreso como string.
    """
    salida_capturada = io.StringIO()
    sys.stdout = salida_capturada
    try:
        iniciar_menu(input_simulado=input_simulado)
    finally:
        sys.stdout = sys.__stdout__
    return salida_capturada.getvalue()


# PRUEBA 1: Opción inválida muestra mensaje de error
def test_opcion_invalida():
    """
    Simula que el usuario ingresa la opción "9" (inexistente).
    Se espera el mensaje: 'Opción inválida, intente de nuevo'
    """
    entradas = ["9", "S"]  # Primero opción inválida, luego salir
    salida = capturar_salida(entradas)
    assert "Opción inválida, intente de nuevo" in salida, \
        "No se mostró el mensaje de opción inválida"
    print("test_opcion_invalida PASÓ (Se mostró mensaje de opción inválida)")


# PRUEBA 2: Conversión correcta desde el menú
def test_conversion_desde_menu():
    """
    Simula una conversión completa: 100 MXN → USD.
    Se espera ver el resultado en la salida.
    """
    entradas = ["C", "MXN", "USD", "100", "S"]
    salida = capturar_salida(entradas)
    assert "5.88" in salida, \
        f"No se encontró el resultado esperado (5.88) en la salida:\n{salida}"
    print("test_conversion_desde_menu PASÓ")


# PRUEBA 3: El menú muestra las opciones C y S
def test_menu_muestra_opciones():
    """
    Verifica que el menú muestre las opciones disponibles.
    """
    entradas = ["S"]
    salida = capturar_salida(entradas)
    assert "Convertir divisas" in salida, "No se mostró la opción Convertir"
    assert "Salir" in salida, " No se mostró la opción Salir"
    print("test_menu_muestra_opciones PASÓ")


# Ejecutar todas las pruebas de interfaz
if __name__ == "__main__":
    print("\n══════════════════════════════════════════════════")
    print("   SIMULACIÓN SELENIUM - PRUEBAS DE INTERFAZ")
    print("══════════════════════════════════════════════════\n")

    pruebas = [
        test_opcion_invalida,
        test_conversion_desde_menu,
        test_menu_muestra_opciones,
    ]

    aprobadas = 0
    fallidas = 0

    for prueba in pruebas:
        try:
            prueba()
            aprobadas += 1
        except AssertionError as e:
            print(f" {prueba.__name__} FALLÓ: {e}")
            fallidas += 1
        except Exception as e:
            print(f" {prueba.__name__} ERROR INESPERADO: {e}")
            fallidas += 1

    print(f"\n══════════════════════════════════════════════════")
    print(f"   RESULTADO: {aprobadas} aprobadas | {fallidas} fallidas")
    if fallidas == 0:
        print("SELENIUM: TODOS LOS TESTS EN VERDE")
    else:
        print("SELENIUM: HAY FALLOS - Revisar interfaz")
    print("══════════════════════════════════════════════════\n")
