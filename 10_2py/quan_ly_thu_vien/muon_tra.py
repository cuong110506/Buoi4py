from du_lieu import danh_sach_sach, lich_su_muon_tra
from hien_thi import tim_sach_theo_ma


def muon_sach(ma_sach, nguoi_muon):

    sach = tim_sach_theo_ma(ma_sach)

    if sach is None:
        print(
            f"-> Khong tim thay sach {ma_sach}."
        )
        return

    if sach["trang_thai"] == "Dang muon":
        print(
            f"-> Sach {ma_sach} da duoc muon, "
            f"khong the muon."
        )
        return

    sach["trang_thai"] = "Dang muon"
    sach["nguoi_muon"] = nguoi_muon

    print(
        f"-> Cho {nguoi_muon} muon sach "
        f"{ma_sach} thanh cong."
    )


def tra_sach(ma_sach):

    sach = tim_sach_theo_ma(ma_sach)

    if sach is None:
        print(
            f"-> Khong tim thay sach {ma_sach}."
        )
        return

    if sach["trang_thai"] == "Co san":
        print(
            f"-> Sach {ma_sach} dang co san, "
            f"khong co nguoi muon de tra."
        )
        return

    lich_su_muon_tra.append({
        "ma_sach": ma_sach,
        "ten_sach": sach["ten_sach"],
        "nguoi_muon": sach["nguoi_muon"]
    })

    print(
        f"-> {sach['nguoi_muon']} da tra sach "
        f"{ma_sach} thanh cong."
    )

    sach["trang_thai"] = "Co san"
    sach["nguoi_muon"] = ""


def thong_ke_muon_sach():

    if len(lich_su_muon_tra) == 0:
        print(
            "-> Chua co giao dich muon tra sach nao."
        )
        return

    tong_luot_muon = 0

    print("\nLICH SU MUON TRA:")

    for giao_dich in lich_su_muon_tra:

        print(
            f"- {giao_dich['ma_sach']} - "
            f"{giao_dich['ten_sach']} - "
            f"{giao_dich['nguoi_muon']}"
        )

        tong_luot_muon += 1

    print(
        f"\n>>> TONG SO LUOT MUON: "
        f"{tong_luot_muon} luot"
    )