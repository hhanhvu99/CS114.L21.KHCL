Thư mục này chứa 3 model EfficientDet, CenterNet MobileNetV2 và CenterNet ResNet50 và các thành phần cần thiết khác để chạy các model:
models: chứa thư viện TensorFlow
CenterNet-MobileNetV2: chứa model CenterNet MobileNetV2
CenterNet-Resnet50: chứa model CenterNet ResNet50
SSD-Efficentnet: chứa model EfficientDet
xml_to_tf.py: code này chia nhãn train và test theo các ảnh train, ảnh test đã chia trước của YOLOv4 và chuyển nó về file csv
label_map.pbtxt: file này chứa label của model
test_labels.csv: file chứa nhãn test dưới dạng csv
train_labels.csv: file chứa nhãn train dưới dạng csv
test_labels.record: file chứa nhãn và ảnh test theo định dạng TensorFlow, file này nằm trong Drive của nhóm
train_labels.record: file chứa nhãn và ảnh train theo định dạng TensorFlow, file này nằm trong Drive của nhóm