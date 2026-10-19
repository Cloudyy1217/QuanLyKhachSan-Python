import json
from models import PhongThuong, PhongVIP, KhachHang, PhieuThue


TEN_FILE = "khachsan_data.json"


def save_data(danh_sach_phong, danh_sach_phieu,
              lich_su_doanh_thu=None):

    if lich_su_doanh_thu is None:
        lich_su_doanh_thu = []

    du_lieu = {
        "phong": [],
        "phieu_thue": [],
        "lich_su_doanh_thu": lich_su_doanh_thu
    }

    for phong in danh_sach_phong:
        thong_tin = {
            "ma_phong": phong.ma_phong,
            "ten_phong": phong.ten_phong,
            "gia_co_ban": phong.gia_co_ban,
            "trang_thai": phong.trang_thai
        }

        if isinstance(phong, PhongVIP):
            thong_tin["loai"] = "VIP"
            thong_tin["phi_don_dep"] = phong.phi_don_dep
            thong_tin["phi_minibar"] = phong.phi_minibar
        else:
            thong_tin["loai"] = "Thuong"

        du_lieu["phong"].append(thong_tin)

    for phieu in danh_sach_phieu:
        du_lieu["phieu_thue"].append({
            "ma_khach": phieu.khach_hang.ma_khach,
            "ten_khach": phieu.khach_hang.ten,
            "cccd": phieu.khach_hang.cccd,
            "ma_phong": phieu.phong.ma_phong,
            "so_ngay_thue": phieu.so_ngay_thue
        })

    with open(TEN_FILE, "w", encoding="utf-8") as file:
        json.dump(
            du_lieu,
            file,
            ensure_ascii=False,
            indent=4
        )


def load_data():
    try:
        with open(TEN_FILE, "r", encoding="utf-8") as file:
            du_lieu = json.load(file)

    except FileNotFoundError:
        return [], [], []

    danh_sach_phong = []

    for item in du_lieu.get("phong", []):
        if item["loai"] == "VIP":
            phong = PhongVIP(
                item["ma_phong"],
                item["ten_phong"],
                item["gia_co_ban"],
                item["phi_don_dep"],
                item["phi_minibar"]
            )
        else:
            phong = PhongThuong(
                item["ma_phong"],
                item["ten_phong"],
                item["gia_co_ban"]
            )

        if item["trang_thai"] == "Đã thuê":
            phong.dat_phong()

        danh_sach_phong.append(phong)

    phong_theo_ma = {
        phong.ma_phong: phong
        for phong in danh_sach_phong
    }

    danh_sach_phieu = []

    for item in du_lieu.get("phieu_thue", []):
        khach = KhachHang(
            item["ma_khach"],
            item["ten_khach"],
            item["cccd"]
        )

        phong = phong_theo_ma[item["ma_phong"]]

        phieu = PhieuThue(
            khach,
            phong,
            item["so_ngay_thue"]
        )

        danh_sach_phieu.append(phieu)

    lich_su = du_lieu.get("lich_su_doanh_thu", [])

    return danh_sach_phong, danh_sach_phieu, lich_su
