TASAS_DE_CAMBIO = {
    "USD": 1.0,
    "MXN": 17.00,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 149.50,
    "CAD": 1.36,
    "BRL": 5.05,
}


def convertir(monto, moneda_origen, moneda_destino):

    if monto < 0:
        return 0

    moneda_origen = moneda_origen.upper()
    moneda_destino = moneda_destino.upper()

    if moneda_origen not in TASAS_DE_CAMBIO:
        return 0
    if moneda_destino not in TASAS_DE_CAMBIO:
        return 0

    monto_en_usd = monto / TASAS_DE_CAMBIO[moneda_origen]
    monto_convertido = monto_en_usd * TASAS_DE_CAMBIO[moneda_destino]

    return round(monto_convertido, 2)


def obtener_monedas_disponibles():
    return list(TASAS_DE_CAMBIO.keys())
    