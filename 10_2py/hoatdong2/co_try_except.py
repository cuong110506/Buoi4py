try:
    tuoi = int(input("Nhap tuoi: "))
    print("Tuoi cua ban la:", tuoi)
except ValueError:
    print("Ban da nhap sai dinh dang, vui long nhap mot so nguyen.")