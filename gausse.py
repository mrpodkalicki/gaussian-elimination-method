import numpy as np 
from fractions import Fraction


def max_elem_column(array_data,index):
    print(index,"index")
    array_size = array_data.shape
    list_number = [array_data[x][y]  for x in range(0,array_size[0]) for y in range(array_size[1]) if y==index and x>=index]
    # print(list_number,'list_numb')
    max_number=max(list_number)
    index = np.where(list_number == max_number)[0][0]
    index+=1
    return index, max_number


def change_row(array_data,index_one,index_two):
    # print(index_one,'ind_on')
    # print(index_two,'inde_two')
    row_one = (array_data[index_one-1]).copy()
    row_two = array_data[index_two-1].copy()
    array_data[index_one-1] = row_two
    array_data[index_two-1] = row_one

    # print(array_data,'change_row')
     
def deliver_row(array_data,row_index,value):
    row=array_data[row_index-1]
    return np.divide(row,value)
    
    

def reset_column_to_zero(array_data,row_index):
    array_size = array_data.shape
    value = array_data[row_index-1][row_index-1].copy()
    row = array_data[row_index-1].copy()
    column=[array_data[x][y]  for x in range(0,array_size[0]) for y in range(array_size[1]) if y == row_index-1 ]
    coefi_multi=[]
    
    for i in column:
        if(i!=0):
            coefi_multi.append(value/i)
        else:
            coefi_multi.append(0)

    # print(coefi_multi)
    rest_array = [(array_data[x] * coefi_multi[x]) - row for x in range(0, array_size[0]) for y in range(array_size[1]) if y == row_index-1]

    for i in range(0,array_size[0]):
        if(i != row_index-1):
            if(coefi_multi[i] != 0):
                array_data[i] = rest_array[i]


def main():
    
    array = np.array([[1,5,0,1],[1,2,-3,-5],[2,4,1,]])  
    array_size = array.shape
    
    for i in range(0, array_size[1]-1):
        # print(i,'i')
        row_index = max_elem_column(array,i)
        # print(row_index,'row')
        change_row(array, i+1, row_index[0])
        
        reset_column_to_zero(array, i+1)
        print(array,'array')
        print('next')
    
    value=[array[i][j] for i in range(0, array_size[0]) for j in range(0,array_size[1]) if  j==array_size[0]] 
    variables= [array[i][j] for i in range(0, array_size[0]) for j in range(0,array_size[1]) if  j==i]


    score = np.divide(value,variables)
    print(score)

main()
