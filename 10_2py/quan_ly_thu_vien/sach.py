from du_lieu import danh_sach_sach
from hien_thi import tim_sach_theo_ma


def them_sach(ma_sach, ten_sach, the_loai, gia):

    if tim_sach_theo_ma(ma_sach) is not None:
        print(
            f"-> Ma sach {ma_sach} da ton tai, "
            f"khong the them."
        )
        return

    danh_sach_sach.append({
        "ma_sach": ma_sach,
        "ten_sach": ten_sach,
        "the_loai": the_loai,
        "gia": gia,
        "trang_thai": "Co san",
        "nguoi_muon": ""
    })

    print(
        f"-> Da them sach {ma_sach} thanh cong."
    )