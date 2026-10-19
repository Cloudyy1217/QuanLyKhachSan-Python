from models import PhongThuong, PhongVIP, KhachHang, PhieuThue
from file_handler import save_data


class QuanLyKhachSan:
    def __init__(
        self,
        danh_sach_phong=None,
        danh_sach_phieu=None,
        lich_su_doanh_thu=None
    ):
        self.danh_sach_phong = (
            danh_sach_phong if danh_sach_phong is not None else []
        )
        self.danh_sach_phieu = (
            danh_sach_phieu if danh_sach_phieu is not None else []
        )
        self.lich_su_doanh_thu = (
            lich_su_doanh_thu if lich_su_doanh_thu is not None else []
        )

    def tim_phong(self, ma_phong):
        for phong in self.danh_sach_phong:
            if phong.ma_phong == ma_phong:
                return phong

        return None

    def them_phong(self, phong):
        if self.tim_phong(phong.ma_phong) is not None:
            raise ValueError("Mã phòng đã tồn tại!")

        self.danh_sach_phong.append(phong)

    def hien_thi_phong(self):
        if not self.danh_sach_phong:
            print("Khách sạn chưa có phòng nào.")
            return

        print("\n===== DANH SÁCH PHÒNG =====")

        for phong in self.danh_sach_phong:
            if isinstance(phong, PhongVIP):
                loai = "VIP"
            else:
                loai = "Thường"

            print(
                f"Mã: {phong.ma_phong} | "
                f"Tên: {phong.ten_phong} | "
                f"Loại: {loai} | "
                f"Giá: {phong.gia_co_ban:,.0f} | "
                f"Trạng thái: {phong.trang_thai}"
            )

    def dat_phong(self, ma_phong, ma_khach, ten_khach,
                  cccd, so_ngay):
        phong = self.tim_phong(ma_phong)

        if phong is None:
            raise ValueError("Không tìm thấy phòng!")

        if phong.trang_thai != "Trống":
            raise ValueError("Phòng đã được thuê!")

        if so_ngay <= 0:
            raise ValueError("Số ngày thuê phải lớn hơn 0!")

        khach = KhachHang(ma_khach, ten_khach, cccd)
        phieu = PhieuThue(khach, phong, so_ngay)

        phong.dat_phong()
        self.danh_sach_phieu.append(phieu)

        return phieu

    def tra_phong(self, ma_phong):
        phieu_can_tra = None

        for phieu in self.danh_sach_phieu:
            if phieu.phong.ma_phong == ma_phong:
                phieu_can_tra = phieu
                break

        if phieu_can_tra is None:
            raise ValueError(
                "Không tìm thấy phiếu thuê của phòng này!"
            )

        phong = phieu_can_tra.phong

        tong_tien = phong.tinh_tien(
            phieu_can_tra.so_ngay_thue
        )

        lich_su = {
            "ma_phong": phong.ma_phong,
            "ma_khach": phieu_can_tra.khach_hang.ma_khach,
            "ten_khach": phieu_can_tra.khach_hang.ten,
            "so_ngay_thue": phieu_can_tra.so_ngay_thue,
            "tong_tien": tong_tien
        }

        self.lich_su_doanh_thu.append(lich_su)

        phong.tra_phong()
        self.danh_sach_phieu.remove(phieu_can_tra)

        return tong_tien

    def bao_cao_doanh_thu(self):
        tong_doanh_thu = sum(
            item["tong_tien"]
            for item in self.lich_su_doanh_thu
        )

        so_phong_trong = sum(
            1 for phong in self.danh_sach_phong
            if phong.trang_thai == "Trống"
        )

        print("\n===== BÁO CÁO KHÁCH SẠN =====")
        print(f"Tổng doanh thu: {tong_doanh_thu:,.0f} VNĐ")
        print(f"Số phòng đang trống: {so_phong_trong}")
        print(f"Tổng số phòng: {len(self.danh_sach_phong)}")

    def luu_du_lieu(self):
        save_data(
            self.danh_sach_phong,
            self.danh_sach_phieu,
            self.lich_su_doanh_thu
        )
