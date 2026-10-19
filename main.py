from models import PhongThuong, PhongVIP
from services import QuanLyKhachSan
from file_handler import load_data


def nhap_so_nguyen(thong_bao):
    while True:
        try:
            return int(input(thong_bao))
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")


def nhap_so_thuc(thong_bao):
    while True:
        try:
            gia_tri = float(input(thong_bao))

            if gia_tri < 0:
                print("Giá trị không được âm!")
                continue

            return gia_tri

        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")


def hien_thi_menu():
    print("\n========== QUẢN LÝ KHÁCH SẠN ==========")
    print("1. Hiển thị danh sách phòng")
    print("2. Thêm phòng mới")
    print("3. Đặt phòng")
    print("4. Trả phòng và thanh toán")
    print("5. Xem báo cáo doanh thu")
    print("6. Thoát và lưu dữ liệu")
    print("========================================")


def main():
    danh_sach_phong, danh_sach_phieu, lich_su = load_data()

    quan_ly = QuanLyKhachSan(
        danh_sach_phong,
        danh_sach_phieu,
        lich_su
    )

    print("Đã khởi động hệ thống quản lý khách sạn!")

    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn: ").strip()

        try:
            if lua_chon == "1":
                quan_ly.hien_thi_phong()

            elif lua_chon == "2":
                ma_phong = input("Nhập mã phòng: ").strip()
                ten_phong = input("Nhập tên phòng: ").strip()

                gia = nhap_so_thuc("Nhập giá cơ bản: ")

                if gia <= 0:
                    print("Giá cơ bản phải lớn hơn 0!")
                    continue

                print("1. Phòng thường")
                print("2. Phòng VIP")

                loai = input("Chọn loại phòng: ").strip()

                if loai == "1":
                    phong = PhongThuong(
                        ma_phong, ten_phong, gia
                    )

                elif loai == "2":
                    phi_don_dep = nhap_so_thuc(
                        "Nhập phí dọn dẹp: "
                    )
                    phi_minibar = nhap_so_thuc(
                        "Nhập phí minibar: "
                    )

                    phong = PhongVIP(
                        ma_phong,
                        ten_phong,
                        gia,
                        phi_don_dep,
                        phi_minibar
                    )

                else:
                    print("Loại phòng không hợp lệ!")
                    continue

                quan_ly.them_phong(phong)
                print("Thêm phòng thành công!")

            elif lua_chon == "3":
                ma_phong = input("Nhập mã phòng cần đặt: ").strip()
                ma_khach = input("Nhập mã khách hàng: ").strip()
                ten_khach = input("Nhập tên khách hàng: ").strip()
                cccd = input("Nhập số CCCD/CMND: ").strip()

                so_ngay = nhap_so_nguyen(
                    "Nhập số ngày thuê: "
                )

                quan_ly.dat_phong(
                    ma_phong,
                    ma_khach,
                    ten_khach,
                    cccd,
                    so_ngay
                )

                print("Đặt phòng thành công!")

            elif lua_chon == "4":
                ma_phong = input(
                    "Nhập mã phòng cần trả: "
                ).strip()

                tong_tien = quan_ly.tra_phong(ma_phong)

                print("\n========== HÓA ĐƠN ==========")
                print(f"Mã phòng: {ma_phong}")
                print(f"Tổng tiền: {tong_tien:,.0f} VNĐ")
                print("Trả phòng thành công!")

            elif lua_chon == "5":
                quan_ly.bao_cao_doanh_thu()

            elif lua_chon == "6":
                quan_ly.luu_du_lieu()
                print("Đã lưu dữ liệu. Tạm biệt!")
                break

            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn 1-6.")

        except ValueError as loi:
            print(f"Lỗi: {loi}")

        except KeyError:
            print("Dữ liệu không hợp lệ hoặc không tìm thấy mã.")

        except OSError as loi:
            print(f"Lỗi đọc/ghi file: {loi}")


if __name__ == "__main__":
    main()
