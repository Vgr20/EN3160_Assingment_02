def draw_circle(event,x,y,flags,param):
    global n
    architectural_points = param[0]
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(param[1],(x,y),5,(255,0,0),-1)
        architectural_points[n] = (x,y)
        n += 1
cv.namedWindow('Image', cv.WINDOW_AUTOSIZE)
param = [architectural_points, architectural_image]
cv.setMouseCallback('Image',draw_circle, param)
while(1):
    cv.imshow('Image', architectural_image)
    if n == number_of_points:
        break
    if cv.waitKey(20) & 0xFF == 27:
        break
flag_points = np.array([[0, 0], [flag_image.shape[1], 0], [flag_image.shape[1], flag_image.shape[0]], [0, flag_image.shape[0]]], dtype=np.float32)
homography_matrix, _ = cv.findHomography(flag_points, architectural_points)
flag_warped = cv.warpPerspective(flag_image, homography_matrix, (architectural_image.shape[1], architectural_image.shape[0]))
blended_image = cv.addWeighted(architectural_image, 1, flag_warped, 0.7, 0)