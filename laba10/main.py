import numpy as np

def outer_product(vector_a, vector_b):
    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)

    product = np.outer(vector_a, vector_b)

    return product

vector_a = [1, 2, 3]
vector_b = [4, 5, 6]

print(outer_product(vector_a,vector_b))
