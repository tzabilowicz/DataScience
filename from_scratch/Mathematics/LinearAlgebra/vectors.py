# Vectors
# A vector represents a point or direction in an n-dimensional space.

Vector = list[float]

def add(v1: Vector, v2: Vector) -> Vector:
    """Add v2 to v1"""
    # Validate dimensions
    assert len(v1) == len(v2)
    
    return [c1 + c2 for c1, c2 in zip(v1, v2)]

def sub(v1: Vector, v2: Vector) -> Vector:
    """Subtract v2 from v1"""
    # Validate dimensions
    assert len(v1) == len(v2)
    
    return [c1 - c2 for c1, c2 in zip(v1, v2)]

def mult(v1: Vector, v2: Vector) -> Vector:
    """Multiply v1 and v2"""
    # Validate dimensions
    assert len(v1) == len(v2)
    
    return [c1 * c2 for c1, c2 in zip(v1, v2)]

def div(v1: Vector, v2: Vector) -> Vector:
    """Divide v1 by v2"""
    # Validate dimenstions
    assert len(v1) == len(v2)
    
    return [c1 / c2 for c1, c2 in zip(v1, v2)]

def dot(v1: Vector, v2: Vector) -> float:
    """Sum of element-size product"""
    return sum(mult(v1, v2))

def square(v: Vector) -> Vector:
    """Element-wise square"""
    return [v_i ** 2 for v_i in v]

def scalar_mult(c: float, v: Vector) -> Vector:
    """Multiply each element by c"""
    return [c * v_i for v_i in v]

def scalar_div(c: float, v: Vector) -> Vector:
    """Divide each element by c"""
    return [c / v_i for v_i in v]

def vector_sum(vectors: list[Vector]) -> Vector:
    """Add all vectors in list"""
    assert vectors
    
    # Expected dimension of vectors
    n = len(vectors[0])
    assert all(len(v) == n for v in vectors)
    
    return [sum(vector[i] for vector in vectors) for i in range(n)]

def vector_mean(vectors: list[Vector]) -> float:
    """Compute element-wise mean of vectors"""
    n = len(vectors)
    return scalar_mult(1/n, vector_sum(vectors))

def sum_of_squares(v: Vector) -> float:
    """Compute sum of squares"""
    return dot(v, v)

if __name__ == "__main__":
    # Examples (Vector Operations)
    test_v1: Vector = [1, 2, 3]
    test_v2: Vector = [4, 5, 6]
    test_v3: Vector = [9, 8, 7]

    v_add = add(test_v1, test_v3)
    v_sub = sub(test_v1, test_v3)
    print(v_add)
    print(v_sub)

    c = 10
    v_scl = scalar_mult(c, test_v1)
    print(v_scl)

    v_s = [[1, 2], [3, 4], [5, 6], [7, 8]]
    v_sum = vector_sum(v_s)
    print(v_sum)

    v_mean = vector_mean(v_s)
    print(v_mean)

    dot_prod = dot(test_v1, test_v2)
    print(dot_prod)