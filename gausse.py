import numpy as np 
from fractions import Fraction
from copy import copy




def max_elem_column(array_data,index):
    array_size = array_data.shape
    list_number = [array_data[x][y]  for x in range(0,array_size[0]) for y in range(array_size[1]) if y==index]
    max_val=list_number[0]
    for i in range(0,len(list_number)):
        if(i>=index):
            if(max_val<list_number[i]):
                max_val=list_number[i]
                index=i
    index+=1
    return index, max_val


def change_row(array_data,index_one,index_two):
    row_one = copy(array_data[index_one-1])
    row_two = copy(array_data[index_two-1])
    array_data[index_one-1] = row_two
    array_data[index_two-1] = row_one

     
def deliver_row(array_data,row_index,value):
    row=array_data[row_index-1]
    return np.divide(row,value)
    
    

def reset_column_to_zero(array_data,row_index):
    array_size = array_data.shape
    value = array_data[row_index-1][row_index-1]
    row = array_data[row_index-1]
    column=[array_data[x][y]  for x in range(0,array_size[0]) for y in range(array_size[1]) if y == row_index-1]
    coefi_multi=[]
    for i in column:
        if(i!=0):
            coefi_multi.append(i/value)
        else:
            coefi_multi.append(0)
    rest_array = [(row * -coefi_multi[x]) + array_data[x] for x in range(0, array_size[0]) for y in range(array_size[1]) if y == row_index-1]
    for i in range(0,array_size[0]):
        if(i != row_index-1):
            if(coefi_multi[i] != 0):
                array_data[i] = rest_array[i]

def replace_b(array_data,new_b_vector,array_data_size):
    for i in range(0,array_data_size[0]):
        for j in range(0,array_data_size[1]):
            if j==array_data_size[1]-1:
                array_data[i][j]=new_b_vector[i]
   



def main():

    # array = np.array([[4,2,-2,4,-12],[2,10,-7,4,9],[-2,-7,6,-5,-9],[-4,4,-5,18,39]])
    # array = np.array([[1,-2,3,1,-1],[-2,5,-8,1,-1],[3,-8,17,-7,3],[1,1,-7,18,-4]])
    array = np.array([[1,2,3,1],[2,8,10,3],[3,10,22,7]])
   


    array_size = array.shape
    array_A= np.delete(array,array_size[1]-1,1)

    new_b=np.dot(array_A,np.ones(array_size[1]-1))
    replace_b(array,new_b,array_size)
    array = array + Fraction()
    print(array)
    for i in range(0, array_size[1]-1):
        row_index = max_elem_column(array,i)
        change_row(array,i+1,row_index[0])
        reset_column_to_zero(array, i+1)  
    value=[array[i][j] for i in range(0, array_size[0]) for j in range(0,array_size[1]) if  j==array_size[0]] 
    variables= [array[i][j] for i in range(0, array_size[0]) for j in range(0,array_size[1]) if  j==i]
    score = np.divide(value,variables)
    for i in range(0,len(score)):
        print("x{0}:{1}".format(i+1,score[i]))

main()
