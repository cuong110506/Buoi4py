chuoi_so = "25"
so = int(chuoi_so)
print(so, type(so))
so_thuc = float("3.14")
print(so_thuc, type(so_thuc))
# Tuple -> List
danh_sach = list((1, 2, 3))
# List -> Tuple
bo_ba = tuple([4, 5, 6])
# List -> Set(sẽ tự loại bỏ phần tử trùng lặp)
tap_hop = set([1, 2, 2, 3, 3, 3])
# List các cặp -> Dictionary
tu_dien = dict([("a", 1), ("b", 2)])
print(danh_sach)
print(bo_ba)
print(tap_hop)
print(tu_dien)