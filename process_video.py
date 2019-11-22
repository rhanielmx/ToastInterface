# import imutils
# import cv2
#
# cap = cv2.VideoCapture('video_pre_procesado.avi')
# count = 0
#
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#
# x = 300
# y = 8

#
# def show_video(contours):
#     while cap.isOpened():
#         ret, frame = cap.read()
#         img = imutils.resize(frame, width=400)
#
#         # print(count)
#         # if count > 300 and count < 500:
#         #     cv2.rectangle(img, (0 + x, 2 + y), (40 + x, 26 + y), (0, 0, 255), 2)
#
#         for contour in contours:
#             cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)
#
#         cv2.rectangle(img, (295, 0), (346, 300), (0, 255, 0), 2)
#
#         cv2.imshow('Image', img)
#         count = count + 1
#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()


import cv2

cap = cv2.VideoCapture('video_pre_procesado.avi')


def show_video(contours):
    while True:
        _, frame = cap.read()

        for contour in contours:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
