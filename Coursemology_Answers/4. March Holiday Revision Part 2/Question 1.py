#the vehicle number without the suffix has been declared as vehicle_reg_num
#a value, with three-letter prefix, has been assigned to vehicle_reg_num
#and the code is hidden
#Enter your code below to calculate the suffix for the vehicle registration number

VRN=[]
counter=0
for char in vehicle_reg_number[:3]:
    VRN.append(ord(char) - 64)
for char in vehicle_reg_number[3:]:
    VRN.append(int(char))
VRN.pop(0)
total=0
Arr=[9,4,5,4,3,2]
for char in range(6):
    total+=VRN[char]*Arr[char]
Array=["A","Z","Y","X","U","T","S","R","P","M","L","K","J","H","G","E","D","C","B"]
suffix=Array[total%19]
