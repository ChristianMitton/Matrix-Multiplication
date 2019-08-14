m1NumRow, m1NumCol = input().split()

m1NumRow = int(m1NumRow)
m1NumCol = int(m1NumCol)

matrix1 = []

count = 0
while count < m1NumRow:
	rowOfNumbers = input()
	rowOfNumbers = rowOfNumbers.split()
	rowOfNumbers = [float(i) for i in rowOfNumbers]
	matrix1.append(rowOfNumbers)
	count += 1

#####################################

m2NumRow, m2NumCol = input().split()

m2NumRow = int(m2NumRow)
m2NumCol = int(m2NumCol)

matrix2 = []

count = 0
while count < m2NumRow:
	rowOfNumbers = input()
	rowOfNumbers = rowOfNumbers.split()
	rowOfNumbers = [float(i) for i in rowOfNumbers]
	matrix2.append(rowOfNumbers)
	count += 1

#####################################

#As columns must equal Bs rows 2x3 3x4
#As rows and Bs columns become size of new matrix

if m1NumCol != m2NumRow:
	print("invalid input")
	quit()

resultMatrix = []

count = 0
while count < m1NumRow:
	resultMatrix.append([0]*m2NumCol)
	count+=1


for i in range(m1NumRow):
	for j in range(m2NumCol):
		for k in range(m1NumCol):
			resultMatrix[i][j] += matrix1[i][k] * matrix2[k][j]

for row in resultMatrix:
        print(' '.join(str(i) for i in row))
