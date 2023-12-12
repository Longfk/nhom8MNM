import cv2
import matplotlib.pyplot as plt

# Đọc ảnh từ file
img = cv2.imread('tenhinh.jpg')  # Thay 'path_to_your_image.jpg' bằng đường dẫn tới ảnh của bạn

# Chuyển đổi ảnh từ BGR sang RGB (OpenCV sử dụng BGR, Matplotlib sử dụng RGB)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Cân bằng histogram
img_equalized = cv2.equalizeHist(img_rgb)

# Làm tăng độ tương phản
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
img_clahe = clahe.apply(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

# Hiển thị ảnh gốc và ảnh sau khi tăng cường
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.title('Ảnh Gốc')
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Cân Bằng Histogram')
plt.imshow(img_equalized, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('CLAHE')
plt.imshow(img_clahe, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
