import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt

class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.khoi_tao_giao_dien()

    def khoi_tao_giao_dien(self):
        self.setWindowTitle("May tinh bo tui - PyQt5")
        self.resize(320, 420)

        # Màn hình hiển thị kết quả
        self.man_hinh = QLineEdit()
        self.man_hinh.setReadOnly(True)
        self.man_hinh.setAlignment(Qt.AlignRight)
        self.man_hinh.setStyleSheet("font-size: 26px; padding: 10px; background-color: #f0f0f0;")

        # Bố cục chính
        layout_chinh = QVBoxLayout()
        layout_chinh.addWidget(self.man_hinh)

        # Bố cục lưới cho các phím bấm
        layout_luoi = QGridLayout()

        # Danh sách các nút và vị trí (hàng, cột, độ rộng hàng, độ rộng cột)
        buttons = [
            ('7', 0, 0, 1, 1), ('8', 0, 1, 1, 1), ('9', 0, 2, 1, 1), ('/', 0, 3, 1, 1),
            ('4', 1, 0, 1, 1), ('5', 1, 1, 1, 1), ('6', 1, 2, 1, 1), ('*', 1, 3, 1, 1),
            ('1', 2, 0, 1, 1), ('2', 2, 1, 1, 1), ('3', 2, 2, 1, 1), ('-', 2, 3, 1, 1),
            ('0', 3, 0, 1, 1), ('.', 3, 1, 1, 1), ('=', 3, 2, 1, 1), ('+', 3, 3, 1, 1),
            ('C', 4, 0, 1, 4)  # Nút C trải dài hết hàng 4
        ]

        for text, row, col, rowspan, colspan in buttons:
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px; padding: 15px;")
            
            if text == '=':
                button.clicked.connect(self.tinh_ket_qua)
            elif text == 'C':
                button.clicked.connect(self.xoa_man_hinh)
                button.setStyleSheet("font-size: 18px; padding: 15px; background-color: #ffcccc;")
            else:
                button.clicked.connect(lambda checked, t=text: self.them_ky_tu(t))
            
            layout_luoi.addWidget(button, row, col, rowspan, colspan)

        layout_chinh.addLayout(layout_luoi)
        self.setLayout(layout_chinh)

    def them_ky_tu(self, ky_tu):
        hien_tai = self.man_hinh.text()
        self.man_hinh.setText(hien_tai + ky_tu)

    def xoa_man_hinh(self):
        self.man_hinh.clear()

    def tinh_ket_qua(self):
        try:
            bieu_thuc = self.man_hinh.text()
            ket_qua = str(eval(bieu_thuc))
            self.man_hinh.setText(ket_qua)
        except Exception:
            self.man_hinh.setText("Lỗi")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec_())