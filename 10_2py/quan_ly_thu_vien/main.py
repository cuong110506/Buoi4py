from hien_thi import (
    hien_thi_danh_sach_sach,
    xem_sach_co_san
)

from sach import them_sach

from muon_tra import (
    muon_sach,
    tra_sach,
    thong_ke_muon_sach
)

from tien_ich import nhap_so_nguyen


def hien_thi_menu():

    print("\n==============================================")
    print("             QUAN LY THU VIEN")
    print("==============================================")

    print("1. Hien thi danh sach tat ca sach")
    print("2. Xem cac sach dang co san")
    print("3. Them sach moi")
    print("4. Cho muon sach")
    print("5. Tra sach")
    print("6. Thong ke luot muon")
    print("0. Thoat chuong trinh")

    print("==============================================")


def chay_chuong_trinh():

    while True:

        hien_thi_menu()

        lua_chon = input(
            "Nhap lua chon cua ban: "
        ).strip()


        # ==============================
        # 1. HIỂN THỊ DANH SÁCH
        # ==============================

        if lua_chon == "1":

            hien_thi_danh_sach_sach()


        # ==============================
        # 2. XEM SÁCH CÓ SẴN
        # ==============================

        elif lua_chon == "2":

            xem_sach_co_san()


        # ==============================
        # 3. THÊM SÁCH
        # ==============================

        elif lua_chon == "3":

            ma_sach = input(
                "Nhap ma sach moi: "
            ).strip().upper()

            ten_sach = input(
                "Nhap ten sach: "
            ).strip().title()

            the_loai = input(
                "Nhap the loai: "
            ).strip().title()

            gia = nhap_so_nguyen(
                "Nhap gia sach: "
            )

            them_sach(
                ma_sach,
                ten_sach,
                the_loai,
                gia
            )


        # ==============================
        # 4. MƯỢN SÁCH
        # ==============================

        elif lua_chon == "4":

            ma_sach = input(
                "Nhap ma sach can muon: "
            ).strip().upper()

            nguoi_muon = input(
                "Nhap ten nguoi muon: "
            ).strip().title()

            muon_sach(
                ma_sach,
                nguoi_muon
            )


        # ==============================
        # 5. TRẢ SÁCH
        # ==============================

        elif lua_chon == "5":

            ma_sach = input(
                "Nhap ma sach can tra: "
            ).strip().upper()

            tra_sach(ma_sach)


        # ==============================
        # 6. THỐNG KÊ
        # ==============================

        elif lua_chon == "6":

            thong_ke_muon_sach()


        # ==============================
        # 0. THOÁT
        # ==============================

        elif lua_chon == "0":

            print(
                "Cam on da su dung chuong trinh. "
                "Tam biet!"
                )

            break


        # ==============================
        # NHẬP SAI
        # ==============================

        else:

            print(
                "-> Lua chon khong hop le, "
                "vui long chon lai."
            )


if __name__ == "__main__":
    chay_chuong_trinh()