CREATE SCHEMA `quanlycuahangtrangsuc` ;

-- Bảng SanPham: Lưu thông tin sản phẩm
CREATE TABLE SanPham (
    MaSanPham INT AUTO_INCREMENT PRIMARY KEY,
    TenSanPham VARCHAR(255) NOT NULL,
    MaVach VARCHAR(50) UNIQUE, -- Mã vạch
    GiaVang DECIMAL(10, 2), -- Giá vàng
    TienCong DECIMAL(10, 2), -- Tiền công
    TienGiaCong DECIMAL(10, 2), -- Tiền gia công
    TonKho INT NOT NULL, -- Số lượng tồn kho
    NgayTao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bảng HoaDon: Lưu thông tin hóa đơn
CREATE TABLE HoaDon (
    MaHoaDon INT AUTO_INCREMENT PRIMARY KEY,
    MaKhachHang INT,
    NgayHoaDon DATETIME DEFAULT CURRENT_TIMESTAMP,
    TongTien DECIMAL(10, 2), -- Tổng tiền hóa đơn
    FOREIGN KEY (MaKhachHang) REFERENCES KhachHang(MaKhachHang)
);

-- Bảng ChiTietHoaDon: Chi tiết hóa đơn
CREATE TABLE ChiTietHoaDon (
    MaChiTiet INT AUTO_INCREMENT PRIMARY KEY,
    MaHoaDon INT,
    MaSanPham INT,
    SoLuong INT NOT NULL,
    Gia DECIMAL(10, 2), -- Giá bán
    FOREIGN KEY (MaHoaDon) REFERENCES HoaDon(MaHoaDon),
    FOREIGN KEY (MaSanPham) REFERENCES SanPham(MaSanPham)
);

-- Bảng KhachHang: Lưu trữ thông tin khách hàng
CREATE TABLE KhachHang (
    MaKhachHang INT AUTO_INCREMENT PRIMARY KEY,
    HoTen VARCHAR(255),
    SoDienThoai VARCHAR(15),
    Email VARCHAR(255),
    DiemTichLuy INT DEFAULT 0 -- Điểm tích lũy
);

-- Bảng KhuyenMai: Chương trình khuyến mãi
CREATE TABLE KhuyenMai (
    MaKhuyenMai INT AUTO_INCREMENT PRIMARY KEY,
    TenKhuyenMai VARCHAR(255),
    MucGiam DECIMAL(5, 2), -- Mức giảm giá (%)
    NgayBatDau DATE,
    NgayKetThuc DATE
);

-- Bảng MuaLaiHang: Chính sách mua lại
CREATE TABLE MuaLaiHang (
    MaMuaLai INT AUTO_INCREMENT PRIMARY KEY,
    MaSanPham INT,
    TiLeMuaLai DECIMAL(5, 2), -- Tỷ lệ mua lại (%)
    GiaCoDinh DECIMAL(10, 2), -- Giá cố định (cho đá quý)
    FOREIGN KEY (MaSanPham) REFERENCES SanPham(MaSanPham)
);

-- Bảng ThongKe: Báo cáo thống kê
CREATE TABLE ThongKe (
    MaBaoCao INT AUTO_INCREMENT PRIMARY KEY,
    NgayBaoCao DATE,
    DoanhThuTong DECIMAL(10, 2), -- Tổng doanh thu
    SanPhamBanChay VARCHAR(255), -- Sản phẩm bán chạy nhất
    BaoCaoTonKho TEXT -- Báo cáo tồn kho
);

-- Tạo hóa đơn
INSERT INTO HoaDon (MaKhachHang, TongTien)
VALUES (1, 0); -- Tạo hóa đơn cho khách hàng có mã 1

-- Thêm sản phẩm vào hóa đơn
INSERT INTO ChiTietHoaDon (MaHoaDon, MaSanPham, SoLuong, Gia)
VALUES (1, 101, 2, (SELECT GiaVang + TienCong + TienGiaCong FROM SanPham WHERE MaSanPham = 101));

-- Cập nhật tổng tiền hóa đơn
UPDATE HoaDon
SET TongTien = (SELECT SUM(SoLuong * Gia) FROM ChiTietHoaDon WHERE MaHoaDon = 1)
WHERE MaHoaDon = 1;

-- Thêm khách hàng mới
INSERT INTO KhachHang (HoTen, SoDienThoai, Email)
VALUES ('Nguyen Van A', '0123456789', 'example@gmail.com');

-- Cập nhật điểm tích lũy cho khách hàng
UPDATE KhachHang
SET DiemTichLuy = DiemTichLuy + 100 -- Thêm 100 điểm tích lũy
WHERE MaKhachHang = 1;

-- Tính giá mua lại trang sức
SELECT MaSanPham, (GiaVang * 0.7) AS GiaMuaLai -- Tỷ lệ mua lại 70%
FROM SanPham
WHERE MaSanPham = 101;

-- Cập nhật giá mua lại cố định cho đá quý
UPDATE MuaLaiHang
SET GiaCoDinh = (SELECT GiaVang * 0.7 FROM SanPham WHERE MaSanPham = 201)
WHERE MaSanPham = 201;

-- Doanh thu theo ngày
SELECT DATE(NgayHoaDon) AS NgayBaoCao, SUM(TongTien) AS DoanhThuTong
FROM HoaDon
GROUP BY DATE(NgayHoaDon);

-- Sản phẩm bán chạy nhất
SELECT MaSanPham, TenSanPham, SUM(SoLuong) AS TongSoLuong
FROM ChiTietHoaDon
JOIN SanPham ON ChiTietHoaDon.MaSanPham = SanPham.MaSanPham
GROUP BY MaSanPham
ORDER BY TongSoLuong DESC
LIMIT 1;

-- Báo cáo tồn kho
SELECT MaSanPham, TenSanPham, TonKho
FROM SanPham
WHERE TonKho < 10; -- Cảnh báo nếu tồn kho dưới 10
