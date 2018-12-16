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
	dict_list={}	
	list_output=[]
	list_temp=[]
	for i in range(len(list_input)):
		if(list_input[i] > sum_num/2):
			break
		else:
			dict_list[sum_num-list_input[i]] = list_input[i]    #将列表中的数字放到字典中，key值是sum_num减去列表的值，value是列表的值
	for i in range(len(list_input)-1,-1,-1):
		if(dict_list.get(list_input[i])):
			if(list_input[i] == sum_num/2): 
				if(i == len(list_input)-1):
					continue
				elif(list_input[i+1] == sum_num/2):
					list_temp = [dict_list.get(list_input[i]),list_input[i]]
					list_output.append(list_temp)
				else:
					continue
			else:
				list_temp = [dict_list.get(list_input[i]),list_input[i]]
				list_output.append(list_temp)
	print(str(list_output)[1:-1])
