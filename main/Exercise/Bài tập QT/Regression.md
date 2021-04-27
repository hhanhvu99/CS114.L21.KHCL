<h1 align="center"><b>CS114.L21 - MÁY HỌC - MACHINE LEARNING</b></h1>
<h1 align="center"><b>BÀI TẬP QUÁ TRÌNH</b></h1>

## **Yêu cầu:**
* Mỗi nhóm tìm vài ví dụ về bài toán regression ***TRONG THỰC TẾ***
* Ghi rõ input, output và cách thu thập + xử lý data, commit vào github repository và dẫn link lên Topic trên Classroom.

## **Thành viên:**
 * 18521665 - Huỳnh Đỗ Anh Vũ
 * 18520548 - Phan Khắc Cường
 * 19520504 - Đặng Trần Hồng Hà

## **Bài toán:**
### **1. Dự đoán độ ẩm không khí tại Hà Nội.**
* ***Input***: Nhiệt độ và sức gió (toàn bộ data có kiểu float).
* ***Output***: Độ ẩm không khí (kiểu float).
* ***Thu thập data***:
    * Data lấy từ trang www.meteoblue.com.
* ***Xử lý data***:
    * Dùng thư viện có sẵn để lấy ra nhiệt độ, độ ẩm và sức gió, bỏ đi những dòng nào không có đủ 3 thành phần vừa nêu.
    * Lưu data đã xử lý dưới dạng file CSV.

### **2. Dự đoán giá thành khi in một cuốn sách (đơn vị VND).**
* ***Input***: Số lượng trang (kiểu integer), diện tích (kiểu integer), có màu không (kiểu boolean).
* ***Output***: Thành tiền VND của sách (kiểu integer).
* ***Thu thập data***:
    * Lấy data từ các sách trong thư viện.
    * Với số tiền thì tìm ở bìa cuốn sách.
    * Với diện tích thì ta lấy thước đo chiều dài, chiều rộng của cuốn sách rồi nhân lại với nhau.
    * Cuốn sách được coi là có màu khi có nhiều hơn 5% tổng số trang có màu (không tính bìa sách).
* ***Xử lý data***:
    * Xóa những dữ liệu bị thiếu, không đủ 3 thành phần của input hoặc sai kiểu.
    * Tổng hợp data thành file CSV.

### 3. **Dự đoán tổng chi phí khi mua thuốc trừ sâu của một thửa ruộng (đơn vị VND).**
* ***Input***: Diện tích, lượng mưa, khoảng cách từ nơi hiện tại tới chỗ mua thuốc, giá xăng trong ngày, giá thuốc trừ sâu (toàn bộ data có kiểu float).
* ***Output***: Tổng chi phí VND (kiểu float).
* ***Thu nhập data***:
    * Tổng chi phí và diện tích lấy từ việc khảo sát các hộ nông dân trên địa bàn.
    * Lấy giá xăng trong năm từ trang www.petrolimex.com.vn
    * Dùng Google Map để lấy khoảng cách.
    * Xin data từ đài thủy văn để lấy lượng mưa theo từng tháng trong năm.
* ***Xử lý data***:
    * Nếu data thu thập được có bị lỗi, bị thiếu thì bỏ.
    * Gôm nhóm các data lại với nhau theo từng tháng.
    * Giá xăng trong tháng sẽ là trung bình cộng giá xăng trong toàn bộ ngày của tháng đó.
    * Lưu tất cả trong một file CSV.


