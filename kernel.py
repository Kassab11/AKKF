import numpy as np




def quadratic_kernel(x, x_prime, alpha, C):
    """
    Compute the quadratic kernel function k(x, x') = (alpha * <x, x'> + C)^2

    Parameters:
    x, x_prime: Input vectors
    alpha: Scaling factor
    C: Constant term

    Returns:
    The result of the quadratic kernel function
    """
    #print(x.shape,x_prime.shape)
    kk = (alpha * (x * x_prime) + C) ** 2
	
    return kk[::-1]
    #return kk


def quadratic_feature_mapping(X):
    """
    Compute the feature mapping for a polynomial kernel of degree 2 (quadratic kernel) for each column in a matrix X.
    For a vector x with elements (x1, x2, ..., xn), the feature mapping is:
    (x1^2, x2^2, ..., xn^2, sqrt(2)*x1*x2, ..., sqrt(2)*xi*xj, ..., 1)

    Args:
    X: A numpy array of shape (n, m) where each column represents a vector

    Returns:
    A numpy array representing the feature mappings for each vector, stacked horizontally.
    """
    X = X[::-1]
    n, m = X.shape
    
    # Compute the squares of each element in each vector
    squares = np.square(X)

    # Compute cross terms only for consecutive elements sqrt(2)*xi*xi+1
    # This uses advanced slicing and avoids explicit looping
    cross_terms = np.sqrt(2) * X[:-1] * X[1:]

    # Calculate sqrt(2)*X for each element
    sqrts = np.sqrt(2) * X

    # Combine squares, consecutive cross terms and sqrt(2)*X
    if cross_terms.any():
      features = np.vstack([squares, cross_terms, sqrts])
    else:
      features = np.vstack([squares, sqrts])

    # Add the constant term '1' to the end of each feature vector
    ones = np.ones((1, m))
    features = np.vstack([features, ones])

    return features