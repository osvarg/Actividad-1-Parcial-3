# test_conversor.py
# Ingeniero de Pruebas (QA / JUnit)
# Pruebas unitarias estilo JUnit usando 'assert' de Python

from conversor import convertir, obtener_monedas_disponibles

# ─────────────────────────────────────────────
# PRUEBA 1: Conversión estándar MXN → USD
# ─────────────────────────────────────────────
def test_conversion_dolares():
    # Si convierto 100 pesos a dólares (tipo de cambio 17.00)
    # Resultado esperado: 100 / 17.00 = 5.88
    resultado = convertir(100, "MXN", "USD")
    assert resultado == 5.88, f"Error: se esperaba 5.88 pero se obtuvo {resultado}"
    print("✅ test_conversion_dolares PASÓ")


# ─────────────────────────────────────────────
# PRUEBA 2: Monto negativo debe devolver 0
# ─────────────────────────────────────────────
def test_valores_negativos():
    # Si meten un monto negativo, el sistema debe devolver un error o 0
    resultado = convertir(-50, "MXN", "USD")
    assert resultado == 0, f"Error: se esperaba 0 pero se obtuvo {resultado}"
    print("✅ test_valores_negativos PASÓ")


# ─────────────────────────────────────────────
# PRUEBA 3: Misma moneda origen y destino
# ─────────────────────────────────────────────
def test_misma_moneda():
    # Convertir 200 USD a USD debe devolver 200.0
    resultado = convertir(200, "USD", "USD")
    assert resultado == 200.0, f"Error: se esperaba 200.0 pero se obtuvo {resultado}"
    print("✅ test_misma_moneda PASÓ")


# ─────────────────────────────────────────────
# PRUEBA 4: Moneda inexistente debe devolver 0
# ─────────────────────────────────────────────
def test_moneda_inexistente():
    resultado = convertir(100, "XYZ", "USD")
    assert resultado == 0, f"Error: se esperaba 0 pero se obtuvo {resultado}"
    print("✅ test_moneda_inexistente PASÓ")


# ─────────────────────────────────────────────
# PRUEBA 5: Conversión MXN → EUR
# ─────────────────────────────────────────────
def test_conversion_euros():
    # 170 MXN → USD → EUR: (170/17.00) * 0.92 = 9.2
    resultado = convertir(170, "MXN", "EUR")
    assert resultado == 9.2, f"Error: se esperaba 9.2 pero se obtuvo {resultado}"
    print("✅ test_conversion_euros PASÓ")


# ─────────────────────────────────────────────
# Ejecutar todas las pruebas
# ─────────────────────────────────────────────
if _name_ == "_main_":
    print("\n══════════════════════════════════════════")
    print("   EJECUTANDO PRUEBAS ESTILO JUNIT")
    print("══════════════════════════════════════════\n")

    pruebas = [
        test_conversion_dolares,
        test_valores_negativos,
        test_misma_moneda,
        test_moneda_inexistente,
        test_conversion_euros,
    ]

    aprobadas = 0
    fallidas = 0

    for prueba in pruebas:
        try:
            prueba()
            aprobadas += 1
        except AssertionError as e:
            print(f"❌ {prueba._name_} FALLÓ: {e}")
            fallidas += 1

    print(f"\n══════════════════════════════════════════")
    print(f"   RESULTADO: {aprobadas} aprobadas | {fallidas} fallidas")
    if fallidas == 0:
        print("   🟢 TODOS LOS TESTS EN VERDE - Listo para fusionar")
    else:
        print("   🔴 HAY FALLOS - No se puede fusionar")
    print("══════════════════════════════════════════\n")