list = [8930,15006,8930,10302,11772,13806,13340,11556,12432,13340,10712,10100,11556,12432,9312,10712,10100,10100,8930,10920,8930,5256,9312,9702,8930,10712,15500,9312]
order = [19,4,14,3,10,17,24,22,8,2,5,11,7,26,0,25,18,6,21,23,9,13,16,1,12,15,27,20]
New_dict = dict(zip(order,list))
Reorder = New_dict.values()

#finding consecutive numbers and append big one
flag=[]
for i in Reorder:
	n = int(i ** 0.5)
	decimal_char = n+1 
	flag.append(decimal_char)

#Decimal to ascii part
flag_list=[]
for x in flag:
	flag_list.append(chr(x))
FinalFlag = ''.join(flag_list)


print FinalFlag
