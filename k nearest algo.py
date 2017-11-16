import math
x1 = [5, 6, 7, 8, 9, 10, 4, 12, 13, 14, 15, 16, 16, 18, 19, 20, 21, 22, 23, 24]
x2=[7,4,4,4,3,5,8,8,5,6,6,5,15,13,11,5,1,2,10,14]
x3=[3]
x4=[7]
output = []
class_label=['Bad','Bad','Bad','Good','Good','Good','Good','Bad','Good','Bad','Good','Bad','Bad','Bad','Bad','Bad','Good','Good','Bad','Bad']
for i in range(0,len(x1),1):
    distance = ((x1[i]-x3[0])**2+(x2[i]-x4[0])**2)
    a=math.sqrt(distance)
    x= output.append(int(a))
print("The Euclidien Distance:",output)
print('Sorted Output List:    ',sorted(output))
seq = sorted(output)
index = [seq.index(v) for v in seq]
print('The Ranking List:      ',index)
for i in range(len(index)-1):
    if index[i] == index[i + 1]:
        index[i + 1] += 1
print('The final Ranking:     ',index)
print('The Class Label:',class_label)
k=int(input("Please Enter the K: "))
for i in range(len(class_label)):
    if i==k:
         print(class_label[0:k])
         if class_label[0:k].count('Good')>class_label[0:k].count('Bad'):
             print('The Prediction is : Good')
         elif class_label[0:k].count('Bad')>class_label[0:k].count('Good'):
             print('The Prediction is :Bad')
         elif class_label[0:k].count('Good')==class_label[0:k].count('Bad'):
             print('The Prediction is : Neutral')

