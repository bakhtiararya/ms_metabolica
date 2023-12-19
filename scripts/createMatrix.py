import pprint
from functools import reduce 
from operator import mul

def create_matrix(data_lst, num_row, num_col):
    new_lst = []
    for i in range(num_row):
        row_list = []
        for j in range(num_col):
            row_list.append(data_lst[num_row * i + j])
        new_lst.append(row_list)
    return new_lst

def reshape(lst, shape):
    """
    #(depth, row, col)
    """
    if len(shape) == 1:
        return lst
    n = reduce(mul, shape[1:])
    return [reshape(lst[i*n:(i+1)*n], shape[1:]) for i in range(len(lst)//n)]

def main():
    shape = [1, 3, 2]
    lst = [0]*12
    x = reshape(lst, shape)
    pprint.pprint(x[0])


main()