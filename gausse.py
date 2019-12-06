import numpy as np 
from fractions import Fraction


def max_elem_column(array_data):
    array_size = array_data.shape
    list_number = [array_data[x][y]  for x in range(0,array_size[0]) for y in range(array_size[1]) if y==0]
    max_number=max(list_number)
    index = np.where(array_data == max_number)[0][0]
    index+=1
    return index, max_number


def change_row(array_data,index_one,index_two):
    row_one = (array_data[index_one-1]).copy()
    row_two = array_data[index_two-1].copy()
    array_data[index_one-1] = row_two
    array_data[index_two-1] = row_one
     



def reset_column_to_zero(array_data,row_index):
    array_size = array_data.shape
    value = array_data[row_index-1][row_index-1].copy()
    print(value,'value')
    row = array_data[row_index-1].copy()
   
    number_list=[array_data[x][y]  for x in range(0,array_size[0]) for y in range(array_size[1]) if y == row_index-1 ]
    print(number_list,'number_list')
    coefi_multi=[]
    for i in number_list:
        if(i!=0):
            coefi_multi.append(value/i)
        else:
            coefi_multi.append(0)

    rest_array = [(array_data[x] * coefi_multi[x]) - row for x in range(0, array_size[0]) for y in range(array_size[1]) if y == row_index-1]
    for i in range(0,array_size[0]):
        if(i != row_index-1):
            array_data[i] = rest_array[i]


def main():
    
    array = np.array([[1,1,2,-1],[2,-1,2,-4],[4,1,4,2]])
    array_size = array.shape
    
    row_index = max_elem_column(array)
    change_row(array, 1, row_index[0])
    for i in range(0, array_size[1]-1):
       
        reset_column_to_zero(array, i+1)
        print(array)
        print('next')


main()
