def determine_listing_status(stock, expiry_passed=False):
    """
    Menentukan status listing makanan berdasarkan stok
    dan informasi kedaluwarsa yang diberikan.
    """

    if expiry_passed:
        return "LISTING_DITUTUP"

    if stock <= 0:
        return "STOK_HABIS"

    return "TERSEDIA"


def determine_waste_action(food_type, is_edible_surplus):
    """
    Memberikan rekomendasi awal untuk surplus makanan.
    Keputusan akhir harus mengikuti pemeriksaan dan
    prosedur keamanan pangan yang sesuai.
    """

    if is_edible_surplus:
        return "EVALUASI_UNTUK_DONASI_ATAU_PENJUALAN"

    if food_type.lower() == "organik":
        return "PILAH_UNTUK_EVALUASI_PENGOMPOSAN"

    return "PILAH_SESUAI_JENIS_LIMBAH"
