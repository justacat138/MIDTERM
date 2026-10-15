import numpy as np

def cholupdate(R, x, sign='+'):
    """Cập nhật tại chỗ R (upper-triangular) sao cho R'R = R'R ± x x'."""
    x = np.array(x, dtype=float).ravel()
    n = len(x)
    for k in range(n):
        if sign == '+':
            r = np.sqrt(R[k, k]**2 + x[k]**2)
        else:
            r = np.sqrt(R[k, k]**2 - x[k]**2)
        c = r / R[k, k]
        s = x[k] / R[k, k]
        R[k, k] = r
        if k < n - 1:
            if sign == '+':
                R[k, k+1:] = (R[k, k+1:] + s * x[k+1:]) / c
            else:
                R[k, k+1:] = (R[k, k+1:] - s * x[k+1:]) / c
            x[k+1:] = c * x[k+1:] - s * R[k, k+1:]
    return R