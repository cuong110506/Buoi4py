import sqlite3
import sys
from pathlib import Path

# Ten file co so du lieu
# Khi chay file .exe: luu CSDL cung thu muc voi file .exe.
# Khi chay file .py: luu CSDL cung thu muc voi file .py.
if getattr(sys, "frozen", False):
    TEN_FILE_CSDL = Path(sys.executable).resolve().parent / "chi_tieu.db"
else:
    TEN_FILE_CSDL = Path(__file__).resolve().parent / "chi_tieu.db"


# 1. Ket noi co so du lieu
def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)


# 2. Tao bang giao dich
def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS giao_dich (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ngay TEXT NOT NULL,
            loai TEXT NOT NULL,
            danh_muc TEXT NOT NULL,
            so_tien REAL NOT NULL,
            ghi_chu TEXT
        )
    """)

    ket_noi.commit()
    ket_noi.close()


# 3. Them giao dich
def them_giao_dich(ngay, loai, danh_muc, so_tien, ghi_chu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        INSERT INTO giao_dich
        (ngay, loai, danh_muc, so_tien, ghi_chu)
        VALUES (?, ?, ?, ?, ?)
    """, (ngay, loai, danh_muc, so_tien, ghi_chu))

    ket_noi.commit()
    ket_noi.close()


# 4. Lay danh sach giao dich
def lay_toan_bo_giao_dich():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        SELECT * FROM giao_dich
        ORDER BY ngay DESC, id DESC
    """)

    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua


# 5. Sua giao dich
def sua_giao_dich(id_giao_dich, ngay, loai, danh_muc, so_tien, ghi_chu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        UPDATE giao_dich
        SET ngay = ?, loai = ?, danh_muc = ?,
            so_tien = ?, ghi_chu = ?
        WHERE id = ?
    """, (ngay, loai, danh_muc, so_tien, ghi_chu, id_giao_dich))

    ket_noi.commit()
    ket_noi.close()


# 6. Xoa giao dich
def xoa_giao_dich(id_giao_dich):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute(
        "DELETE FROM giao_dich WHERE id = ?",
        (id_giao_dich,)
    )

    ket_noi.commit()
    ket_noi.close()


# 7. Thong ke tong thu, tong chi
def thong_ke_tong_quan():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        SELECT
            COALESCE(SUM(CASE WHEN loai = 'Thu' THEN so_tien ELSE 0 END), 0),
            COALESCE(SUM(CASE WHEN loai = 'Chi' THEN so_tien ELSE 0 END), 0)
        FROM giao_dich
    """)

    tong_thu, tong_chi = con_tro.fetchone()
    ket_noi.close()

    return tong_thu, tong_chi, tong_thu - tong_chi


# 8. Thong ke chi tieu theo danh muc
def thong_ke_theo_danh_muc():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        SELECT danh_muc, SUM(so_tien)
        FROM giao_dich
        WHERE loai = 'Chi'
        GROUP BY danh_muc
    """)

    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua


# 9. Khoi tao co so du lieu
if __name__ == "__main__":
    tao_bang_neu_chua_co()
    print("Da tao co so du lieu thanh cong!")
