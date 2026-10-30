def process_temperature(temperature):
    """
    Memproses data suhu dari sensor.
    Batas suhu di bawah ini hanya contoh untuk demonstrasi,
    bukan penentu keamanan makanan.
    """

    if temperature is None:
        return {
            "temperature": None,
            "status": "DATA_TIDAK_VALID"
        }

    try:
        temperature = float(temperature)
    except (ValueError, TypeError):
        return {
            "temperature": None,
            "status": "DATA_TIDAK_VALID"
        }

    if not -40 <= temperature <= 80:
        return {
            "temperature": temperature,
            "status": "DATA_TIDAK_VALID"
        }

    if temperature > 5:
        status = "PERLU_PEMERIKSAAN"
    else:
        status = "SUHU_DALAM_CONTOH_RENTANG"

    return {
        "temperature": temperature,
        "status": status
    }
