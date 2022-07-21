import cv2, numpy as np, matplotlib.pyplot as plt
#####################################
H = 0.16
# f_y = 358.355916
# f_x = 357.719727
f_y = 356
f_x = 356
tile = 0.45

left_x, left_y = 3 * tile, tile
mid_x, mid_y = 4 * tile, 0
right_x, rigth_y = 3*tile+0.3, -tile

# left_u, left_v = 180, 284
# mid_u, mid_v = 325, 271
# right_u, right_v = 443, 274

left_u, left_v = 168, 284
mid_u, mid_v = 324, 271
right_u, right_v = 447, 275

mtx = np.array([[357.719727, 0.0, 332.547112],
                [0.0, 358.355916, 249.312209],
                [0.0, 0.0, 1.0]])

dist = np.array([-0.326641, 0.092732, -0.000171, 0.000783, 0.0])
####################################
src = cv2.imread("image.png", cv2.IMREAD_COLOR)
un_src = cv2.undistort(src, mtx, dist, None)

# left_y_norm = (left_v - mtx[1][2]) / mtx[1][1]
# mid_y_norm = (mid_v - mtx[1][2]) / mtx[1][1]
# right_y_norm = (right_v - mtx[1][2]) / mtx[1][1]

left_y_norm = (left_v - 240)
mid_y_norm = (mid_v - 240)
right_y_norm = (right_v - 240)

left_x_norm = (left_u - 320)
mid_x_norm = (mid_u - 320)
right_x_norm = (right_u - 320)

#fy*H/y
pred_left_y = f_y*H/left_y_norm
pred_mid_y = f_y*H/mid_y_norm
pred_right_y = f_y*H/right_y_norm

pred_left_x = f_x*H/left_x_norm
pred_mid_x = f_x*H/mid_x_norm
pred_right_x = f_x*H/right_x_norm

print("Left :{} / {}".format(left_x, pred_left_y))
print("Mid :{} / {}".format(mid_x, pred_mid_y))
print("Right :{} / {}".format(right_x, pred_right_y))

# plt.imshow(un_src); plt.show()
# while cv2.waitKey(0) != 27:
#     cv2.imshow("src", un_src);
print(np.arctan(15/13.3)*2*180/np.pi)
