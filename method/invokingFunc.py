import math

def area_of_circle(r):
	pi = 3.14
	area = pi * r * r
	return area

r = int(input("请输入圆的半径"))
print("圆的面积：",area_of_circle(r))