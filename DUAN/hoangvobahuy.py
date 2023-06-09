""" CÂU 1:
def insertNum(n,A,k): # dòng này định nghĩa một hàm có tên là insertNum với 3 biến được thêm vào là n , A và k
    newlist = []    #khai báo một python string với tên là newlist và để rỗng
    # Ở những dòng sau là những câu điều kiện lồng ghép if else
    if (k==0):      # câu điều kiện nếu phần tử k bằng 0 sẽ thực hiện các câu lệnh trong if
        newlist = [n] + A       # dòng này có nghĩa là nếu k = 0 thì biến newlist = ký tự tại trí thứ n cộng cho chuỗi A
    elif (k == len(A) + 1):     # dòng này có nghĩa là k không bằng 0 mà k bằng chiều dài của chuỗi A cộng thêm 1
        newlist = A + [n]       #dòng này có nghĩa là biến newlist sẽ bằng chuỗi A cộng cho ký tự tại vị trí n
    else:
        newlist = A[:k] +[n] +A[k:]     # dòng này có nghĩa là chuỗi newlist bằng các ký tu của chuỗi A từ vị trí 0 đến k(ko lấy ký tự ở vị trí k) cộng cho ký tự tại vị trí n và cộng thêm các ký tự của chuỗi A từ vị trí K đến hết  chuỗi
    return  newlist #trả về giá trị của biến newlist """






"""CÂU 2:
def Circle(R,X,Y):
    C = 2 * 3.14 * R
    S = pow(R,2) * 3.14
    print("Chu vi hinh tron la: ", C)
    print("Dien tich hinh tron la:", S)



R= float(input("Gia tri ban kinh R la: "))
X= float(input("Gia tri X la: "))
Y = float(input("Gia tri Y la: "))
Circle(R,X,Y)
"""

"""CÂU 3
def number(n):
    A = []
    B = []
    k = 0
    t = 0
    for i in range (1,n):
        if (i % 2 != 0):
            A.insert(k,i)
            k = k + 1
        else:
            B.insert(t,i)
            t = t + 1
    print("Danh sach A la: ",A)
    print("Danh sach B la: ",B)

n=int(input("Nhap so tu nhien n: "))
number(n)"""


CAU 4
import numpy as np

def Diff(A,B):
    print("A - B = \n", A - B)

x = int(input("Nhap so hang: "))
y = int(input("Nhap so cot: "))
A=[]
B=[]
k,t,z = 0,0,0
input("Nhap cac phan tu cua mang A: ")
while(k<x*y - 1):
    n = float(input())
    A.insert(k,n)
    k = k + 1
    z = z + 1
input("Nhap cac phan tu cua mang B:")
while(t<x*y - 1):
    p = float(input())
    A.insert(t,p)
    t = t + 1
    z = z + 1
A = np.reshape(x,y)
B = np.reshape(x,y)
Diff(A,B)

