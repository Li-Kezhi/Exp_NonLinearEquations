import numpy as np
import scipy.optimize

def func(x):
    res1 = x[0] - 1
    res2 = x[0] - 2
    res3 = x[1] - 3
    return np.array([res1, res2, res3])

x0 = np.array([0, 0])

ans = scipy.optimize.leastsq(func, x0, ftol=1.49012e-08, xtol=1.49012e-08, full_output = True)

print("The leastsq solution:")
for i in xrange(len(x0)):
    print("x" + str(i) + " = " + str(ans[0][i]))
res = func(ans[0])
print("The residual is:")
for i in xrange(len(res)):
    print("x" + str(i) + " = " + str(res[i]))