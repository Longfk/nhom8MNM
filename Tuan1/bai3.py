from tkinter import *
import matplotlib.pyplot as plt

def calculate_rectangle():
    length = float(length_entry.get())
    width = float(width_entry.get())
    area = length * width
    perimeter = 2 * (length + width)
    result_label.config(text="Diện tích: %.2f   Chu vi: %.2f" % (area, perimeter))

def calculate_square():
    side = float(side_entry.get())
    area = side * side
    perimeter = 4 * side
    result_label.config(text="Diện tích: %.2f   Chu vi: %.2f" % (area, perimeter))
def calculate_square1():
    side = float(side_entry.get())
    # Tạo figure và axes
    fig, ax = plt.subplots()

    # Vẽ hình vuông
    square = plt.Rectangle((0.2, 0.2), side, side, edgecolor='red', fill=False)

    # Thêm hình vuông vào axes
    ax.add_patch(square)

    # Đặt giới hạn trục x và y để hình vuông không bị méo
    plt.axis('equal')

    # Đặt tiêu đề và nhãn trục
    plt.title('Hình vuông')
    plt.xlabel('Trục x')
    plt.ylabel('Trục y')

    # Hiển thị plot
    plt.show()
def calculate_triangle():
    side1 = float(side1_entry.get())
    side2 = float(side2_entry.get())
    side3 = float(side3_entry.get())
    area = calculate_triangle_area(side1, side2, side3)
    perimeter = side1 + side2 + side3
    result_label.config(text="Diện tích: %.2f   Chu vi: %.2f" % (area, perimeter))

def calculate_triangle1():
    side1 = float(side1_entry.get())
    side2 = float(side2_entry.get())
    side3 = float(side3_entry.get())
    area = calculate_triangle_area(side1, side2, side3)
    perimeter = side1 + side2 + side3
    result_label.config(text="Diện tích: %.2f   Chu vi: %.2f" % (area, perimeter))
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        # Tính toán tọa độ của các đỉnh tam giác
        x = [0, side2, side1, 0]  # Tọa độ x của các đỉnh tam giác
        y = [0, 0, (side1 ** 2 - side2 ** 2 + side3 ** 2) / (2 * side1), 0]  # Tọa độ y của các đỉnh tam giác

        # Vẽ tam giác
        plt.figure(figsize=(5, 5))  # Kích thước của plot
        plt.plot(x, y, 'r')  # Vẽ đường viền tam giác, 'r' đại diện cho màu đỏ (có thể thay đổi)

        # Đặt tiêu đề và nhãn trục
        plt.title('Hình tam giác')
        plt.xlabel('Trục x')
        plt.ylabel('Trục y')

        plt.grid()  # Hiển thị lưới

        # Hiển thị plot
        plt.show()
def calculate_triangle_area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    return area

def calculate_circle():
    radius = float(radius_entry.get())
    area = 3.14159 * radius * radius
    perimeter = 2 * 3.14159 * radius
    result_label.config(text="Diện tích: %.2f   Chu vi: %.2f" % (area, perimeter))
def calculate_circle1():
    radius = float(radius_entry.get())
    circle = plt.Circle((0.5, 0.5), radius, color='blue', fill=False)

    # Tạo figure và axes
    fig, ax = plt.subplots()

    # Thêm hình tròn vào axes
    ax.add_patch(circle)

    # Đặt giới hạn trục x và y để hình tròn không bị méo
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Đặt tiêu đề và nhãn trục
    ax.set_title('Hình tròn')
    ax.set_xlabel('Trục x')
    ax.set_ylabel('Trục y')

    # Hiển thị plot
    plt.show()
root = Tk()
root.title("Hỗ trợ học tập - Hình học")

# Giao diện cho hình chữ nhật
rectangle_label = Label(root, text="Hình chữ nhật")
length_label = Label(root, text="Chiều dài:")
length_entry = Entry(root)
width_label = Label(root, text="Chiều rộng:")
width_entry = Entry(root)
rectangle_button = Button(root, text="Tính diện tích và chu vi", command=calculate_rectangle)

# Giao diện cho hình vuông
square_label = Label(root, text="Hình vuông")
side_label = Label(root, text="Cạnh:")
side_entry = Entry(root)
square_button = Button(root, text="Tính diện tích và chu vi", command=calculate_square)
square_button1 = Button(root, text="vẽ hình vuông", command=calculate_square1)
# Giao diện cho tam giác
triangle_label = Label(root, text="Tam giác")
side1_label = Label(root, text="Cạnh 1:")
side1_entry = Entry(root)
side2_label = Label(root, text="Cạnh 2:")
side2_entry = Entry(root)
side3_label = Label(root, text="Cạnh 3:")
side3_entry = Entry(root)
triangle_button = Button(root, text="Tính diện tích và chu vi", command=calculate_triangle)
triangle_button1 = Button(root, text="Vẽ tam giác", command=calculate_triangle1)
# Giao diện cho hình tròn
circle_label = Label(root, text="Hình tròn")
radius_label = Label(root, text="Bán kính:")
radius_entry = Entry(root)
circle_button = Button(root, text="Tính diện tích và chu vi", command=calculate_circle)
circle_button1 = Button(root, text="vẽ hình tròn", command=calculate_circle1)
result_label = Label(root, text="Kết quả sẽ được hiển thị ở đây")

# Định vị trí các widget trong giao diện
rectangle_label.pack()
length_label.pack()
length_entry.pack()
width_label.pack()
width_entry.pack()
rectangle_button.pack()

square_label.pack()
side_label.pack()
side_entry.pack()
square_button.pack()
square_button1.pack()
triangle_label.pack()
side1_label.pack()
side1_entry.pack()
side2_label.pack()
side2_entry.pack()
side3_label.pack()
side3_entry.pack()
triangle_button.pack()
triangle_button1.pack()
circle_label.pack()
radius_label.pack()
radius_entry.pack()
circle_button.pack()
circle_button1.pack()

result_label.pack()

root.mainloop()