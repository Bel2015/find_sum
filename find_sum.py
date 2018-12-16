def find_sum(listx,n):
	dictx={}
	for i in range(len(listx)-1):
		if(listx[i]>(n/2) or (listx[i]==(n/2) and listx[i+1]!=(n/2))):
			break;
		else:
			dictx[n-listx[i]] = listx[i];
	print(dictx)
	for i in range(len(listx)-1):
		if(dictx.get(listx[i])!=None):
			if(listx[i] == n/2 and (listx[i+1] != n/2)):
				continue
			else:
				print(n-listx[i],listx[i])		
	if(dictx.get(listx[len(listx)-1])!=None and listx[i] != n/2):
				print(n-listx[len(listx)-1],listx[len(listx)-1])			
strx = input("Please input a sorted array of intergers(splited by ','):")
try:
	listx = list(map(int,(strx.split(','))))
except:
	print("Not an array of intergers!")
else:
	for i in range(len(listx)-1):
		if listx[i] > listx[i+1]:
			print("Not a sorted array!")
			break
	else:
		n = input("Please input the sum number:")
		try:
			n = int(n)
		except:
			print("Not an available number")
		else:
			find_sum(listx,int(n))
