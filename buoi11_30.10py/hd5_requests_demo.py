import requests

# =========================
# BAI TAP 5.1: GOI API GITHUB
# =========================

print("===== BAI TAP 5.1: API GITHUB =====")

try:
    response = requests.get(
        "https://api.github.com/repos/python/cpython",
        timeout=15
    )

    if response.status_code == 200:
        du_lieu = response.json()

        print("Ten repository:", du_lieu["full_name"])
        print("So luot gan sao:", du_lieu["stargazers_count"])
        print("Ngon ngu chinh:", du_lieu["language"])

    else:
        print("Goi API that bai:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Loi ket noi GitHub:", e)


# =========================
# BAI TAP 5.2: TY GIA NGOAI TE
# =========================

print("\n===== BAI TAP 5.2: TY GIA NGOAI TE =====")

try:
    response = requests.get(
        "https://open.er-api.com/v6/latest/USD",
        timeout=15
    )

    if response.status_code == 200:
        du_lieu = response.json()

        if du_lieu["result"] == "success":
            ty_gia_vnd = du_lieu["rates"]["VND"]

            print(f"1 USD = {ty_gia_vnd:,.0f} VND")

        else:
            print("Khong lay duoc ty gia")

    else:
        print("Loi lay ty gia:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Loi ket noi API:", e)


print("\n===== KET THUC HOAT DONG 5 =====")