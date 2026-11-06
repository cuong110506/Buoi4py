import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import csdl_chi_tieu as db


DANH_MUC = {
    "Thu": ["Luong", "Thuong", "Kinh doanh", "Khac"],
    "Chi": ["An uong", "Mua sam", "Di lai",
            "Hoc tap", "Giai tri", "Khac"]
}


class UngDungChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("QUAN LY CHI TIEU CA NHAN")
        self.geometry("1050x680")
        self.minsize(950, 600)
        self.configure(bg="#f3f6fa")

        self.ma_dang_chon = None

        db.tao_bang_neu_chua_co()

        self.tao_giao_dien()
        self.tai_danh_sach()

    def tao_giao_dien(self):
        # Tieu de
        tk.Label(
            self,
            text="QUAN LY CHI TIEU CA NHAN",
            font=("Arial", 21, "bold"),
            bg="#1e40af",
            fg="white",
            pady=18
        ).pack(fill="x")

        # Khung thong ke
        khung_tk = tk.Frame(self, bg="#f3f6fa")
        khung_tk.pack(fill="x", padx=20, pady=15)

        self.nhan_thu = self.tao_the(
            khung_tk, "TONG THU", "#16a34a", 0
        )
        self.nhan_chi = self.tao_the(
            khung_tk, "TONG CHI", "#dc2626", 1
        )
        self.nhan_so_du = self.tao_the(
            khung_tk, "SO DU", "#2563eb", 2
        )

        # Khung nhap du lieu
        khung_nhap = ttk.LabelFrame(
            self, text="Thong tin giao dich", padding=12
        )
        khung_nhap.pack(fill="x", padx=20, pady=5)

        for cot in (1, 3):
            khung_nhap.columnconfigure(cot, weight=1)

        ttk.Label(khung_nhap, text="Ngay (YYYY-MM-DD):").grid(
            row=0, column=0, padx=5, pady=7, sticky="w"
        )
        self.o_ngay = ttk.Entry(khung_nhap)
        self.o_ngay.grid(
            row=0, column=1, padx=5, pady=7, sticky="ew"
        )
        self.o_ngay.insert(0, date.today().isoformat())

        ttk.Label(khung_nhap, text="Loai giao dich:").grid(
            row=0, column=2, padx=5, pady=7, sticky="w"
        )
        self.chon_loai = ttk.Combobox(
            khung_nhap, values=["Thu", "Chi"],
            state="readonly"
        )
        self.chon_loai.grid(
            row=0, column=3, padx=5, pady=7, sticky="ew"
        )
        self.chon_loai.set("Chi")
        self.chon_loai.bind(
            "<<ComboboxSelected>>", self.doi_danh_muc
        )

        ttk.Label(khung_nhap, text="Danh muc:").grid(
            row=1, column=0, padx=5, pady=7, sticky="w"
        )
        self.chon_danh_muc = ttk.Combobox(
            khung_nhap, values=DANH_MUC["Chi"],
            state="readonly"
        )
        self.chon_danh_muc.grid(
            row=1, column=1, padx=5, pady=7, sticky="ew"
        )
        self.chon_danh_muc.current(0)

        ttk.Label(khung_nhap, text="So tien (VND):").grid(
            row=1, column=2, padx=5, pady=7, sticky="w"
        )
        self.o_so_tien = ttk.Entry(khung_nhap)
        self.o_so_tien.grid(
            row=1, column=3, padx=5, pady=7, sticky="ew"
        )

        ttk.Label(khung_nhap, text="Ghi chu:").grid(
            row=2, column=0, padx=5, pady=7, sticky="w"
        )
        self.o_ghi_chu = ttk.Entry(khung_nhap)
        self.o_ghi_chu.grid(
            row=2, column=1, columnspan=3,
            padx=5, pady=7, sticky="ew"
        )

        # Cac nut chuc nang
        khung_nut = ttk.Frame(self)
        khung_nut.pack(pady=12)

        cac_nut = [
            ("Them giao dich", self.them_giao_dich),
            ("Sua giao dich", self.sua_giao_dich),
            ("Xoa giao dich", self.xoa_giao_dich),
            ("Lam moi", self.lam_moi),
            ("Bieu do thong ke", self.ve_bieu_do)
        ]

        for i, (ten, ham) in enumerate(cac_nut):
            ttk.Button(
                khung_nut, text=ten, command=ham
            ).grid(row=0, column=i, padx=6)

        # Bang danh sach
        khung_bang = ttk.LabelFrame(
            self, text="Danh sach giao dich", padding=10
        )
        khung_bang.pack(
            fill="both", expand=True, padx=20, pady=(0, 20)
        )

        cot = (
            "id", "ngay", "loai",
            "danh_muc", "so_tien", "ghi_chu"
        )

        self.bang = ttk.Treeview(
            khung_bang, columns=cot,
            show="headings", selectmode="browse"
        )

        tieu_de = [
            "ID", "Ngay", "Loai",
            "Danh muc", "So tien (VND)", "Ghi chu"
        ]

        do_rong = [50, 120, 90, 150, 150, 250]

        for c, ten, rong in zip(cot, tieu_de, do_rong):
            self.bang.heading(c, text=ten)
            self.bang.column(
                c, width=rong, anchor="center"
            )

        self.bang.pack(
            side="left", fill="both", expand=True
        )

        cuon = ttk.Scrollbar(
            khung_bang, orient="vertical",
            command=self.bang.yview
        )
        cuon.pack(side="right", fill="y")
        self.bang.configure(yscrollcommand=cuon.set)

        self.bang.bind(
            "<<TreeviewSelect>>", self.chon_giao_dich
        )

    def tao_the(self, cha, tieu_de, mau, cot):
        khung = tk.Frame(cha, bg=mau, padx=15, pady=12)
        khung.grid(
            row=0, column=cot, padx=7, sticky="ew"
        )
        cha.columnconfigure(cot, weight=1)

        tk.Label(
            khung, text=tieu_de, bg=mau,
            fg="white", font=("Arial", 11, "bold")
        ).pack()

        nhan = tk.Label(
            khung, text="0 VND", bg=mau,
            fg="white", font=("Arial", 17, "bold")
        )
        nhan.pack(pady=5)
        return nhan

    def dinh_dang_tien(self, so_tien):
        return f"{so_tien:,.0f}".replace(",", ".")

    def doi_danh_muc(self, event=None):
        loai = self.chon_loai.get()
        self.chon_danh_muc["values"] = DANH_MUC[loai]
        self.chon_danh_muc.current(0)

    def lay_du_lieu_nhap(self):
        ngay = self.o_ngay.get().strip()
        loai = self.chon_loai.get()
        danh_muc = self.chon_danh_muc.get()
        ghi_chu = self.o_ghi_chu.get().strip()

        try:
            date.fromisoformat(ngay)
        except ValueError:
            messagebox.showerror(
                "Loi", "Ngay phai co dang YYYY-MM-DD."
            )
            return None

        try:
            so_tien = float(self.o_so_tien.get().strip())
            if not (0 < so_tien < float("inf")):
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Loi", "So tien phai la so duong hop le."
            )
            return None

        if loai not in DANH_MUC:
            messagebox.showerror("Loi", "Loai khong hop le.")
            return None

        if danh_muc not in DANH_MUC[loai]:
            messagebox.showerror("Loi", "Danh muc khong hop le.")
            return None

        return ngay, loai, danh_muc, so_tien, ghi_chu

    def tai_danh_sach(self):
        for item in self.bang.get_children():
            self.bang.delete(item)

        danh_sach = db.lay_toan_bo_giao_dich()

        for gd in danh_sach:
            ma, ngay, loai, danh_muc, tien, ghi_chu = gd
            self.bang.insert(
                "", "end",
                values=(
                    ma, ngay, loai, danh_muc,
                    self.dinh_dang_tien(tien), ghi_chu
                )
            )

        tong_thu, tong_chi, so_du = db.thong_ke_tong_quan()

        self.nhan_thu.config(
            text=self.dinh_dang_tien(tong_thu) + " VND"
        )
        self.nhan_chi.config(
            text=self.dinh_dang_tien(tong_chi) + " VND"
        )
        self.nhan_so_du.config(
            text=self.dinh_dang_tien(so_du) + " VND"
        )

    def them_giao_dich(self):
        du_lieu = self.lay_du_lieu_nhap()
        if du_lieu is None:
            return

        db.them_giao_dich(*du_lieu)
        self.tai_danh_sach()
        self.lam_moi()

        messagebox.showinfo(
            "Thanh cong", "Da them giao dich thanh cong!"
        )

    def chon_giao_dich(self, event=None):
        lua_chon = self.bang.selection()
        if not lua_chon:
            return

        gia_tri = self.bang.item(
            lua_chon[0], "values"
        )
        self.ma_dang_chon = int(gia_tri[0])

        self.o_ngay.delete(0, tk.END)
        self.o_ngay.insert(0, gia_tri[1])

        self.chon_loai.set(gia_tri[2])
        self.doi_danh_muc()
        self.chon_danh_muc.set(gia_tri[3])

        self.o_so_tien.delete(0, tk.END)
        self.o_so_tien.insert(
            0, str(gia_tri[4]).replace(".", "")
        )

        self.o_ghi_chu.delete(0, tk.END)
        self.o_ghi_chu.insert(0, gia_tri[5])

    def sua_giao_dich(self):
        if self.ma_dang_chon is None:
            messagebox.showwarning(
                "Thong bao", "Hay chon giao dich can sua."
            )
            return

        du_lieu = self.lay_du_lieu_nhap()
        if du_lieu is None:
            return

        db.sua_giao_dich(
            self.ma_dang_chon, *du_lieu
        )

        self.tai_danh_sach()
        self.lam_moi()
        messagebox.showinfo(
            "Thanh cong", "Da sua giao dich!"
        )

    def xoa_giao_dich(self):
        if self.ma_dang_chon is None:
            messagebox.showwarning(
                "Thong bao", "Hay chon giao dich can xoa."
            )
            return

        xac_nhan = messagebox.askyesno(
            "Xac nhan", "Ban co chac muon xoa giao dich?"
        )

        if xac_nhan:
            db.xoa_giao_dich(self.ma_dang_chon)
            self.tai_danh_sach()
            self.lam_moi()
            messagebox.showinfo(
                "Thanh cong", "Da xoa giao dich!"
            )

    def lam_moi(self):
        self.ma_dang_chon = None

        for o in (
            self.o_ngay, self.o_so_tien, self.o_ghi_chu
        ):
            o.delete(0, tk.END)

        self.o_ngay.insert(
            0, date.today().isoformat()
        )

        self.chon_loai.set("Chi")
        self.doi_danh_muc()

        for item in self.bang.selection():
            self.bang.selection_remove(item)

    def ve_bieu_do(self):
        # Lay so tien da chi theo tung danh muc tu SQLite
        du_lieu = db.thong_ke_theo_danh_muc()
        if not du_lieu:
            messagebox.showinfo(
                "Thông báo", "Chưa có dữ liệu chi tiêu để thống kê."
            )
            return

        try:
            import matplotlib.pyplot as plt
            from matplotlib.ticker import FuncFormatter
        except ImportError:
            messagebox.showerror(
                "Thiếu thư viện",
                "Hãy cài Matplotlib bằng lệnh:\n"
                "python -m pip install matplotlib"
            )
            return

        # Chuyen danh muc trong CSDL thanh ten tieng Viet co dau
        ten_danh_muc = {
            "An uong": "Ăn uống",
            "Mua sam": "Mua sắm",
            "Di lai": "Đi lại",
            "Giai tri": "Giải trí",
            "Hoc tap": "Học tập",
            "Khac": "Khác"
        }
        danh_muc = [
            ten_danh_muc.get(dong[0], dong[0])
            for dong in du_lieu
        ]
        so_tien = [float(dong[1]) for dong in du_lieu]

        # Dinh dang so tien, VD: 2000000 -> 2.000.000
        def dinh_dang_vnd(gia_tri):
            return f"{gia_tri:,.0f}".replace(",", ".")

        # Arial phu hop cho chu tieng Viet tren Windows
        with plt.rc_context({"font.family": ["Arial", "DejaVu Sans"]}):
            fig, ax = plt.subplots(figsize=(9, 5.5))
            fig.canvas.manager.set_window_title("Biểu đồ chi tiêu")

            cot = ax.bar(
                danh_muc, so_tien,
                color="#3b82f6", width=0.55
            )

            # Ghi gia tri tien ngay tren moi cot
            for thanh, tien in zip(cot, so_tien):
                ax.annotate(
                    dinh_dang_vnd(tien) + " đ",
                    xy=(thanh.get_x() + thanh.get_width() / 2,
                        thanh.get_height()),
                    xytext=(0, 6),
                    textcoords="offset points",
                    ha="center", va="bottom",
                    fontsize=10, fontweight="bold"
                )

            ax.set_title(
                "THỐNG KÊ CHI TIÊU THEO DANH MỤC",
                fontsize=15, fontweight="bold", pad=20
            )
            ax.set_xlabel("Danh mục", fontsize=11)
            ax.set_ylabel("Số tiền (VNĐ)", fontsize=11)

            # Truc tung hien thi so VND day du, khong con ky hieu 1e6
            ax.yaxis.set_major_formatter(
                FuncFormatter(lambda x, pos: dinh_dang_vnd(x))
            )
            ax.set_ylim(0, max(so_tien) * 1.20)
            ax.grid(axis="y", linestyle="--", alpha=0.30)
            ax.set_axisbelow(True)
            ax.tick_params(axis="x", labelrotation=15)
            fig.tight_layout()
            plt.show()


if __name__ == "__main__":
    ung_dung = UngDungChiTieu()
    ung_dung.mainloop()
