import cv2

def colored_image():
    img = cv2.imread("logo.png")

    dimensions = img.shape

    #(img.size = height * width * channels)
    total_number_of_elements = img.size

    image_dtype = img.dtype


    (b,g,r) = img[6,40]

    print(b,g,r)
    print(dimensions)
    print(total_number_of_elements)
    print(image_dtype)
    #b = img[6,40,0]

    #change color
    img2 = img
    img2[6,40] = (255,255,255)

    #get the top left corner of the image
    top_left_corner = img[0:50, 0:50]

    cv2.imshow("Original Image", img)
    cv2.imshow("Changed Color",img2)
    cv2.imshow("Corner",top_left_corner)

    cv2.waitKey(0)

def gray_scale_image():
    gray_img = cv2.imread("logo.png",cv2.IMREAD_GRAYSCALE)

    dimensions = gray_img.shape

    #(img.size = height * width * channels)
    total_number_of_elements = gray_img.size

    image_dtype = gray_img.dtype

    # X = 40, Y = 6
    intensity = gray_img[6,40]

    print(intensity)
    print(dimensions)
    print(total_number_of_elements)
    print(image_dtype)
    #b = img[6,40,0]

    #change intensity of the image
    img2 = gray_img
    img2[6,40] = 0

    #get the top left corner of the image

    cv2.imshow("Gray Image", gray_img)
    cv2.imshow("Changed Intensity",img2)

    cv2.waitKey(0)