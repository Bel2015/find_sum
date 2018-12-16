#!/usr/bin/python3
def find_sum(list_input,sum_num):
	if not isinstance(sum_num, int):
		print("Error: Your input sum is not a valid num!")	#判断是否是整数
		return
	if not isinstance(list_input, list):
		print("Error: Your input list is not a valid list!")  #判断是否是列表
		return
	for i in range(len(list_input)):
		if (type(list_input[i]) is not int):
			print("Error: Your input list is not a number list!")	#判断是否是整数型列表
			return
	for i in range(len(list_input)-1):
		if (list_input[i] > list_input[i+1]):
			print("error: Your input is not a sorted list!")	#判断是否是有序的列表
			return
	list_output=[]
	list_temp=[]
	for i in range(len(list_input)):
		for j in range(i+1, len(list_input)):
			if list_input[i] + list_input[j] == sum_num:
				list_temp = [list_input[i],list_input[j]]
				list_output.append(list_temp)
	print(str(list_output)[1:-1].replace(' ',''))
