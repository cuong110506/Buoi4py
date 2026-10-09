from du_lieu import danh_sach_sach


def hien_thi_danh_sach_sach():
    print("\n" + "=" * 95)

    print(
        f"{'Ma sach':<10}"
        f"{'Ten sach':<25}"
        f"{'The loai':<15}"
        f"{'Gia':<15}"
        f"{'Trang thai':<15}"
        f"{'Nguoi muon':<15}"
    )

    print("-" * 95)

    for sach in danh_sach_sach:
        print(
            f"{sach['ma_sach']:<10}"
            f"{sach['ten_sach']:<25}"
            f"{sach['the_loai']:<15}"
            f"{sach['gia']:>10,} VND   "
            f"{sach['trang_thai']:<15}"
            f"{sach['nguoi_muon']:<15}"
        )

    print("=" * 95)


def tim_sach_theo_ma(ma_sach):
    for sach in danh_sach_sach:
        if sach["ma_sach"] == ma_sach:
            return sach

    return None


def xem_sach_co_san():
    sach_co_san = [
        sach
        for sach in danh_sach_sach
        if sach["trang_thai"] == "Co san"
    ]

    if len(sach_co_san) == 0:
        print("-> Hien khong con sach co san.")
        return

    print("\nCAC SACH DANG CO SAN:")

    for sach in sach_co_san:
        print(
            f"- {sach['ma_sach']} - "
            f"{sach['ten_sach']} - "
            f"{sach['the_loai']} - "
            f"{sach['gia']:,} VND"
        )