def create_gaussian_kernel(size, sigma, verbose=False):
    kernel_1D = np.linspace(-(size // 2), size // 2, size)
    kernel_1D = np.exp(-(kernel_1D**2) / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))
    kernel_2D = np.outer(kernel_1D.T, kernel_1D.T)
    kernel_2D *= 1.0 / kernel_2D.max()
    return kernel_2D
sigma = 0.6375
gaussian_kernel = create_gaussian_kernel(5, sigma, verbose=False) 
laplace_of_gaussian_kernel = cv.Laplacian(gaussian_kernel, cv.CV_64F) * sigma**2
laplace_of_gaussian_img = cv.filter2D(img, -1, laplace_of_gaussian_kernel)
threshold_value = 81 # Adjust as needed
_, binary_img = cv.threshold(np.abs(laplace_of_gaussian_img), threshold_value, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(binary_img.astype(np.uint8), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
original_img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
for contour in contours:
    ((x, y), radius) = cv.minEnclosingCircle(contour)
    center = (int(x), int(y))
    radius = int(radius)
    cv.circle(original_img, center, radius, (0, 255, 0), 2)  # (0, 255, 0) is color (green), 2 is thickness