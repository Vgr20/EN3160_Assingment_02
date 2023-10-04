# create dataset
N = X.shape[0]
data = X
def calculate_distance(x1, y1, x2, y2):
    distance_mag =  math.sqrt((x2-x1)**2 + (y2-y1)**2)
    a = (x2-x1)/distance_mag
    b = (y2-y1)/distance_mag
    d = a*x1 + b*y1
    return a , b, d 
def calc_tls (x,indices):
    a,b,d = x[0],x[1],x[2]
    return np.sum(np.square(a*data[indices,0] + b*data[indices,1] - d))
def g(x):
    return x[0]**2 + x[1]**2 - 1
constraints = ({'type': 'eq', 'fun': g})
def best_fit_line(X,x,t):
    a,b,d = x[0],x[1],x[2]
    e = np.absolute(a*X[:,0] + b*X[:,1] - d)
    return e < t
while iters < max_iters:
    indices = np.random.randint(0, N, 2)
    x0 = np.array([1,1,0])
    res = minimize(fun = calc_tls, args = indices, x0 = x0, tol= 1e-6, constraints=constraints, options={'disp': True})
    line_inliers = best_fit_line(data,res.x,threshold_value)

    if line_inliers.sum() > d :
        x0 = res.x
        res = minimize(fun = calc_tls, args = line_inliers, x0 = x0, tol= 1e-6, constraints=constraints, options={'disp': True})
        if res.fun < best_error:
            best_error = res.fun
            best_line_model = res.x
            best_sample_line = data[indices,:]
            best_inlier_line = line_inliers
            res_only_with_sample = x0
    iters += 1