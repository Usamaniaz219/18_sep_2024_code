# import os
# import cv2
# import numpy as np

# folder_path = "/media/usama/SSD/Usama_dev_ssd/data_12_Sep_5/"
# output_dir = "/media/usama/SSD/Usama_dev_ssd/Edge_detection_of_map_images/canny_edge_detection/Adaptive_thresholding_results_along_with_medianblur_morph_closing_op/"
# folder_name = os.path.basename(os.path.dirname(folder_path))
# print("folder name",folder_name)

# all_ori = os.listdir(folder_path)
# ori_renamed = [ori.replace(".jpg","").replace(".png","") for ori in all_ori]
# for renamed_ori in ori_renamed:
#     img_path = f"{folder_path}/{renamed_ori}.jpg"
#     image = cv2.imread(img_path)
     
#     img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     # LUV_img = cv2.cvtColor(image,cv2.COLOR_BGR2LUV)
#     # img_gray = cv2.GaussianBlur(img_gray,(3,3),0)
#     img_gray = cv2.medianBlur(img_gray,3)
#     thresh1 = cv2.adaptiveThreshold(img_gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 3, 2) 
#     kernel = np.ones((3, 3), np.uint8)
#     # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#     # kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
#     # cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
#     thresh_image_with_morph_closing = cv2.morphologyEx(thresh1,cv2.MORPH_CLOSE,kernel)


#     output_subdir = os.path.join(output_dir, os.path.basename(os.path.dirname(folder_path)))
#     os.makedirs(output_subdir, exist_ok=True)
#     output_file_path = os.path.join(output_subdir, f"{renamed_ori}_output_mask.jpg")
#     cv2.imwrite(output_file_path,thresh_image_with_morph_closing)




import cv2
import numpy as np
import os 

def bgr_threshold(src_bgr, thresh_bgr, maxval_bgr, type_bgr):
    b, g, r = cv2.split(src_bgr)
    thresh_b, thresh_g, thresh_r = thresh_bgr
    maxval_b, maxval_g, maxval_r = maxval_bgr
    type_b, type_g, type_r = type_bgr
    b = cv2.GaussianBlur(b,(3,3),0)
    g = cv2.GaussianBlur(g,(3,3),0)
    r = cv2.GaussianBlur(r,(3,3),0)

    thresh_img_b =  cv2.adaptiveThreshold(b, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 3, 2) 
    thresh_img_g = cv2.adaptiveThreshold(g, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 3, 2) 
    thresh_img_r = cv2.adaptiveThreshold(r, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 3, 2) 
    # ret_g, thresh_img_g = cv2.threshold(g, thresh_g, maxval_g, type_g)
    # ret_r, thresh_img_r = cv2.threshold(r, thresh_r, maxval_r, type_r)

    thresh_img_bgr = cv2.merge((thresh_img_b, thresh_img_g, thresh_img_r))

    return thresh_img_bgr
image  = cv2.imread('/media/usama/SSD/Usama_dev_ssd/original_map_images/ca_emeryville.tif_SwinIR.png')
th = bgr_threshold(image, (127, )*3, (255, )*3, (cv2.THRESH_BINARY, )*3)
# cv2.imwrite("thresh.jpg",th)