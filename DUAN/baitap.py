f = open("D:\cau3.txt","a")

n = int(input("Nhap so ho dan cua mot chung cu:"))

ls = []
def dntthu(n):
  if dntt <= 100:
    price = dntt * 1450
  if dntt > 100 and dntt <=150:
    price = 100 * 1450 + (dntt-100) * 1750
  if dntt > 150 and dntt <= 250:
    price = 100 * 1450 + 50 * 1750 + (dntt -150) * 1800
    
for i in range(0,n):
    print("Nhap thong tin ho dan thu:",i+1)
    soph = str(input("Nhap so phong:"))
    sotoanha = str(input("Nhap so toa nha:"))
    while(True):
      dntt = int(input("Nhap dien nang tieu thu:"))
      if dntt>=0:
        break
      s = dntthu(dntt)
    
    dict = {"Toa nha":sotoanha,"Phong":soph,"So dien tieu thu":dntt}
    ls.append(dict)
print("Toa nha \t Phong \t So dien tieu thu")
for i in range(0,n):
  print(ls[i]["Toa nha"],"\t",ls[i]["Phong"],"\t",ls[i]["So dien tieu thu"])











f.close()

f = open("D:\cau3.txt","r")