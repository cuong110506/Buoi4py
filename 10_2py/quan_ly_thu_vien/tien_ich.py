def nhap_so_nguyen(loi_nhac):

    while True:

        try:
            return int(input(loi_nhac))

        except ValueError:
            print(
                "-> Du lieu khong hop le, "
                "vui long nhap lai mot so nguyen."
            )