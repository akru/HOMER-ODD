import cv

def detect(image):
    image_size = cv.GetSize(image)

    # create grayscale version
    grayscale = cv.CreateImage(image_size, 8, 1)
    cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)

    # create storage
    storage = cv.CreateMemStorage(0)
    #cv.ClearMemStorage(storage)

    # equalize histogram
    cv.EqualizeHist(grayscale, grayscale)

    # detect objects
    cascade = cv.Load('haarcascade_frontalface_alt.xml')
    faces = cv.HaarDetectObjects(grayscale, cascade, storage, 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (50, 50))

    for (x,y,w,h),n in faces:
        cv.Rectangle(image, (x,y), (x+w,y+h), 255)
        return True

def face_detect(image_file):
    frame = cv.LoadImage(image_file)

    # mirror
    cv.Flip(frame, None, 1)

    # face detection
    if detect(frame):
        cv.SaveImage(image_file, frame)
        return True
    return False
