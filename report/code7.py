def calculate_error(homography, src_points, dst_points):
    transformed_points = cv2.perspectiveTransform(src_points, homography)
    errors = np.sqrt(np.sum((transformed_points - dst_points)**2, axis=2))
    return np.mean(errors)
def ransac_homography(src_points, dst_points, num_iterations=100, error_threshold=1.0):
    best_homography = None
    best_error = float('inf')
    for _ in range(num_iterations):
        indices = np.random.choice(len(src_points), 4, replace=False)
        sampled_src = src_points[indices]
        sampled_dst = dst_points[indices]
        homography, _ = cv2.findHomography(sampled_src, sampled_dst)
        current_error = calculate_error(homography, src_points, dst_points)
        if current_error < best_error:
            best_error = current_error
            best_homography = homography
        if current_error < error_threshold:
            break

    return best_homography