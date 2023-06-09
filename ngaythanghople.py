day = int(input("Nhap vao ngay:"))
month = int(input("Nhap vao thang:"))
year = int(input("Nhap vao nam:"))

if (year%400==0) or ((year%4==0 and year%100!=0)):
    def week(month):
        switcher={
                4,6,9,11: if day>30 or day<1: print(input("Ngay nhap vao bi loi!"));
                2: if day<1 or day>29: print(input("Ngay nhap vao bi loi!"));
                
                 }
        return switcher.get(month,"nothing")
                 
