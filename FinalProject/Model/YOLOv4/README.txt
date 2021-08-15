Thư mục này chứa những thứ cần thiết để chạy YOLOv4:
darknet: chứa model YOLOv4
Data: chứa file config của YOLOv4
mask_yolo_test: chứa ảnh test và file nhãn theo format YOLO
mask_yolo_train: chứa tất cả các ảnh trong DataMask và file nhãn theo format YOLO
get_file_path.py: code này tạo 2 file txt chứa absolute path tới từng ảnh trong 2 folder mask_yolo_train và mask_yolo_test
xml_to_yolo.py: code này chia tập train và tập test theo một tỉ lệ cho trước và tạo file nhãn theo định dạng YOLO từ file XML
train.txt: chứa absolute path tới từng ảnh train trong folder mask_yolo_train 
test.txt: chứa absolute path tới từng ảnh test trong folder mask_yolo_test