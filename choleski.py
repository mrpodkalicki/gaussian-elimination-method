import numpy as np 
from fractions import Fraction
from copy import copy
import math



def calc_l(array,array_size):
    L = array.copy()
    for i in range(0,array_size[0]):
        for j in range(0,array_size[1]):
            L[i][j]=0
    for i in range(0,array_size[0]):
        sum=0
        for k in range(0,i):
            print()
            if(k != i):
                sum_two=0
                for j in range(0,k):
                    sum_two+=L[i][j]*L[k][j]
                num_one= int(array[i][k]-sum_two)
                num_two=int(L[k][k])
               
                L[i][k] = Fraction(num_one/num_two)
                
            else:
                sum+=array[k][i]
                L[k][k]=array[k][k]-sum
        for j in range(0,i):
            sum+=(L[i][j])**2
        numb=array[i][i]-sum
        sqrt_numb=numb**Fraction(1,2)
        L[i][i]=int(math.sqrt(array[i][i]-sum))
    return L

def calc_y(l_array,b_array,array_size):
    y_array=[]
    for i in range(0,array_size[0]):
        sum_y_l=0
        for j in range(0,i):
            sum_y_l=sum_y_l+l_array[i][j]*y_array[j]
        num_one=int(b_array[i]-sum_y_l)
        y=Fraction((num_one)/l_array[i][i])
        y_array.append(y)
  
    return y_array



def cacl_x(i,arr_size,l_arr,y_arr,x_array):
    l_array=l_arr
    y_array=y_arr
    array_size=arr_size
    
    if ( i==0):
        a=2
    else:
        sum_L_x=0
        for j in range(array_size[1]-1,i,-1):
            sum_L_x= sum_L_x+l_array[i-1][j-1] * x_array[j-1]
        num_one = y_array[i-1] - sum_L_x
        num_two = int(l_array[i-1][i-1])
        x=Fraction(num_one,num_two)  
        
        x_array[i-1]=x

        cacl_x(i-1,array_size,l_arr,y_array,x_array)
    
     




def main():
    
    array = np.array([[1,2,3,1],[2,8,10,3],[3,10,22,7]]) 
    # array = np.array([[4,2,-2,4,-12],[2,10,-7,4,9],[-2,-7,6,-5,-9],[-4,4,-5,18,39]])
    # array = np.array([[1,-2,3,1,-1],[-2,5,-8,1,-1],[3,-8,17,-7,3],[1,1,-7,18,-4]])
    
    b_array=np.array([1,3,7])
    # b_array=np.array([-12,9,-9,39])
    # b_array=np.array([-1,-1,3,-4])
   
    
    array = array + Fraction()
    print(array)
    array_size = array.shape
    x_array=[1 for i in range(0,array_size[1]-1)]
    l_array = calc_l(array,array_size)
    # print(l_array)
    # l_array = l_array + Fraction()
    
    l_trasnpose= np.transpose(l_array)
  
    y_array=calc_y(l_array,b_array,array_size)
    
    cacl_x(array_size[0],array_size,l_trasnpose, y_array,x_array)
    print(x_array)
main()



