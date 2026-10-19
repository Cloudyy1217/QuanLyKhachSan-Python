class Phong:
    def __init__(self, ma_phong, ten_phong, gia_co_ban):
        self.ma_phong = ma_phong
        self.ten_phong = ten_phong
        self.gia_co_ban = gia_co_ban
        self.__trang_thai = "Trống"

    @property
    def trang_thai(self):
        return self.__trang_thai

    def dat_phong(self):
        if self.__trang_thai != "Trống":
            raise ValueError("Phòng đã được thuê!")

        self.__trang_thai = "Đã thuê"

    def tra_phong(self):
        self.__trang_thai = "Trống"

    def tinh_tien(self, so_ngay):
        raise NotImplementedError(
            "Lớp con phải tự định nghĩa tinh_tien()"
        )


class PhongThuong(Phong):
    def tinh_tien(self, so_ngay):
        return self.gia_co_ban * so_ngay


class PhongVIP(Phong):
    def __init__(
        self,
        ma_phong,
        ten_phong,
        gia_co_ban,
        phi_don_dep,
        phi_minibar
    ):
        super().__init__(ma_phong, ten_phong, gia_co_ban)
        self.phi_don_dep = phi_don_dep
        self.phi_minibar = phi_minibar

    def tinh_tien(self, so_ngay):
        tien_phong = self.gia_co_ban * so_ngay

        return tien_phong + self.phi_don_dep + self.phi_minibar


class KhachHang:
    def __init__(self, ma_khach, ten, cccd):
        self.ma_khach = ma_khach
        self.ten = ten
        self.cccd = cccd


class PhieuThue:
    def __init__(self, khach_hang, phong, so_ngay_thue):
        self.khach_hang = khach_hang
        self.phong = phong
        self.so_ngay_thue = so_ngay_thue
