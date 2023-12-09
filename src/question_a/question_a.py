#write functions here, don't add input('') statements here!
def test_config():
    return True

def num_loop(outer_max, inner_max):
    o = 1
    outer_matrix = []
    while o <= outer_max:
        outer_matrix.append(num_loop_inner(o, inner_max))
        o += 1
    return outer_matrix

def num_loop_inner(o, limit):
    i = 1
    inner_list = []
    while i <= limit:
        inner_list.append(o*i)
        i += 1
    return inner_list

def display_multiplication_table(matrix):
    i = 0
    o = 0
    for i in matrix:
        for o in i:
            print(o, end=' ')
        print('')
    print('\n')
