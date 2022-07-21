import cv2, numpy as np, matplotlib.pyplot as plt

H = 0.16
f_y = 356
f_x = 356
tile = 0.45

mtx = np.array([[357.567039, 0.0, 331.016276],
                [0.0, 358.750825, 243.534121],
                [0.0, 0.0, 1.0]])

dist = np.array([-0.303023, 0.068071, 0.002586, 0.000215, 0.0])
src = cv2.imread("..\extrinsic.png", cv2.IMREAD_COLOR)
src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
un_src = cv2.undistort(src, mtx, dist, None)

# plt.imshow(un_src); plt.show()
# cv2.imshow("src", src); cv2.waitKey(0)


img_mid_1 = [332, 332]
img_mid_2 = [333, 288]
img_mid_3 = [334, 272]

img_left_1 = [60, 328]
img_left_2 = [178, 286]
img_left_3 = [226, 271]

img_right_1 = [613, 332]
img_right_2 = [488, 289]
img_right_3 = [443, 273]

obj_mid_1 = [2*tile, 0, 0]
obj_mid_2 = [3*tile, 0, 0]
obj_mid_3 = [4*tile, 0, 0]

obj_left_1 = [2*tile, tile, 0]
obj_left_2 = [3*tile, tile, 0]
obj_left_3 = [4*tile, tile, 0]

obj_right_1 = [2*tile, -tile, 0]
obj_right_2 = [3*tile, -tile, 0]
obj_right_3 = [4*tile, -tile, 0]

img_points = np.array([img_left_1, img_mid_1, img_right_1,
                       img_left_2, img_mid_2, img_right_2,
                       img_left_3, img_mid_3, img_right_3])
obj_points = np.array([obj_left_1, obj_mid_1, obj_right_1,
                       obj_left_2, obj_mid_2, obj_right_2,
                       obj_left_3, obj_mid_3, obj_right_3])

homography, _ = cv2.findHomography(img_points, obj_points)
homo_inv = np.linalg.inv(homography)
print("homography")
print(homography)


warped_img = cv2.warpPerspective(un_src, homography, (int(tile*6), int(tile*6)))
cv2.imshow("dst",warped_img); cv2.waitKey(0)
# cv2.imshow("dst",un_src); cv2.waitKey(0)
# appned_image_points = np.append(img_points.reshape(9, 2), np.ones([1, 9]).T, axis=1)

# print(appned_image_points)
# print(homography.shape)
# for i, image_point in enumerate(appned_image_points):
#     # estimation point(object_point) -> homography * src(image_point)
#     x, y, z = np.dot(homography, image_point)
#     print("x: {}, y: {}".format(round(x/z, 3), round(y/z, 3)))
#     print("X: {}, Y: {}".format(obj_points[i,0], obj_points[i,1]))
#     print("---"*5)
    
