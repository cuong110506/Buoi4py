while True:
    try:
        tuoi = int(input("Nhap tuoi: "))
        print("Tuoi cua ban la:", tuoi)
        break
    except ValueError:
        print("Ban da nhap sai dinh dang, vui long nhap lai!")