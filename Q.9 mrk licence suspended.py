def driver_speed(speed):
    point=0
    if speed<=70:
        print("okay")
    elif speed>70:
        point=(speed-70)//5
        print("points=",point)
    if point>12:
        print('"points is out of 12"=',point)
        print("your licence is suspended")
n=int(input("Enter your number of speed:"))
driver_speed(n)