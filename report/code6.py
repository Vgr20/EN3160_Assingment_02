bf = cv2.BFMatcher()
matches = bf.knnMatch(descriptors1, descriptors5, k=2)
good_matches = []
for m, n in matches:
    if m.distance < 0.85 * n.distance:
        good_matches.append(m)
src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([keypoints5[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
homography_matrix, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 0.75)