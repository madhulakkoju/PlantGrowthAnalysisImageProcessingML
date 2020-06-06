import cv2
# Cv2 module imported - helps in Image Manipulationsand Morphology operations 
import math
import numpy as np
from matplotlib import pyplot as plt
# Matplotlib helps in plotting Histogram

# Method giveCoordinates is used to generate the Coordinates from the contours
def giveCoordinates(contours):
    arr=[]
    # arr is a list which handles the coordinates extracted from given contours
    for aa in contours:
        approx = cv2.approxPolyDP(aa, 0.009 * cv2.arcLength(aa, True), True)
        # an approximation is carried out from the coordinates of contours.
        # This approximation used to find nearest points to the contour and create a list
        n = approx.ravel()
        ca=[]
        i=0
        for j in n:
            if(i%2 == 0):
                x = n[i]
                y = n[i+1]
                ca.append((x,y))
            i = i+ 1
        arr.append(ca)
        # Each contour's approximated coordinate list is added to main list.
    return arr
# Method PolyArea2D Takes coordinates as Argument and returns the Area covered by that set of contours.
def PolyArea2D(pts):
    lines = np.hstack([pts,np.roll(pts,-1,axis=0)])
    areas = 0.5*abs(sum(x1*y2-x2*y1 for x1,y1,x2,y2 in lines))
    return areas
# Method perimeter is used to find the perimeter of the area covered by the points in argument
def perimeter(pt):
    pt.append(pt[0])
    per = 0
    for i in range(0,len(pts)-1):
        per = per + math.hypot(pt[i][0]-pt[i+1][0],pt[i][1]-pt[i+1][1])
    return per

# Feature Extract method constitutes Image Processing and Feature extraction wxecution 
def FeatureExtract(imgpath):
    #The Image path is taken as argument
    img = cv2.imread(imgpath,0)
    # img is the copy of Image read in gray scale
    colorimg = cv2.imread(imgpath)
    original = cv2.imread(imgpath)
    # Copies of the same image are generated in rgb scale.
    # Opening Operations to IMAGE
    kernel = np.ones((5,5),np.uint8)
    #Black Empty Image for morphological operations
    opened = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
    #--------Opened Image
    eroded = cv2.erode(opened,kernel,iterations = 1)
    #--------Opened is eroded
    dilated = cv2.dilate(eroded,kernel,iterations = 1)
    #cv2.imwrite('dilated.jpg',dilated)
    #--------eroded is dilated
    closed = cv2.morphologyEx(dilated,cv2.MORPH_CLOSE,kernel)
    #blur = cv2.cvtColor(dilated,cv2.COLOR_BGR2GRAY)
    # Applying Gaussian Filter on the eroded image
    blur = cv2.GaussianBlur(eroded,(5,5),0)
    blur = ~blur
    # The Image Inversion is done to nullify hidden holes
    # Finding the Threshold value from the obtained Blur picture
    ret,thresholdval = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # Obtaining contours of the inverted Image
    contours, hierarchy = cv2.findContours(thresholdval, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # Drawing Contours
    #cv2.drawContours(colorimg, contours, -1, (0, 0, 255), 2)
    # Finding EXTREME POINTS IN CONTOUR parts
    c = max(contours, key=cv2.contourArea)
    # Computing MAX extremities
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    '''
    # MARKING the Extremeties for Contours
    cv2.circle(colorimg, extLeft, 8, (0, 0, 255), -1)
    cv2.circle(colorimg, extRight, 8, (0, 255, 0), -1)
    cv2.circle(colorimg, extTop, 8, (255, 0, 0), -1)
    cv2.circle(colorimg, extBot, 8, (255, 255, 0), -1)
    '''
    # CROPPING THE image based on the extremities
    cropped = original[extTop[1]:extBot[1],extLeft[0]:extRight[0]].copy()
    # Obtaining the Color Histogram of the cropped picture.
    (hist,bins,patches) = plt.hist(cropped.ravel(),bins = 64,range=(0,256),density=0)
    #  hist is the array of the top points in the Histogram
    area = 0
    area_fullc= 0
    #Select longest contour as this should be the casing
    lengthC=0
    ID=-1
    idCounter=-1
    for x in contours:
        idCounter=idCounter+1 
        if len(x) > lengthC:
            lengthC=len(x)
        ID=idCounter
    if ID != -1:
        cnt = contours[ID]
        cntFull=cnt.copy()
    #approximate the contour, where epsilon is the distance to the original contour
        cnt = cv2.approxPolyDP(cnt, epsilon=1, closed=True)
    #add the first point as the last point, to ensure it is closed
        lenCnt=len(cnt)
        cnt= np.append(cnt, [[cnt[0][0][0], cnt[0][0][1]]]) 
        cnt=np.reshape(cnt, (lenCnt+1,1, 2))

        lenCntFull=len(cntFull)
        cntFull= np.append(cntFull, [[cntFull[0][0][0], cntFull[0][0][1]]]) 
        cntFull=np.reshape(cntFull, (lenCntFull+1,1, 2))
    #find the moments
        M = cv2.moments(cnt)
        MFull = cv2.moments(cntFull)
        area = M['m00']
        area_fullc = MFull['m00']
    # Moments generated are used to generate area enclosed by Contours    
    perimeter = 0
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        cv2.drawContours(colorimg, [approx], -1, (0, 255, 0), 2)
        perimeter = perimeter+cv2.arcLength(c,True)
    #print(perimeter)   
    #perimeter is the perimeter of the contour

        
    #Constructing Hull casing to the contours generated
    hull = []
    # calculate points for each contour
    for i in range(len(contours)):
    # creating convex hull object for each contour
        hull.append(cv2.convexHull(contours[i], False))
    # create an empty black image
    drawing = np.zeros((thresholdval.shape[0], thresholdval.shape[1], 3), np.uint8)
    # draw contours and hull points
    for i in range(len(contours)):
        color_contours = (0, 255, 0) # green - color for contours
        color = (255, 0, 0) # blue - color for convex hull
    # draw ith contour
        #cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
    # draw ith convex hull object
    #cv2.drawContours(colorimg, hull, i, color, 1, 8)
    # Contours are marked and proceeded for Feature Extraction
    ''' Required shape feature generating things are extracted  '''
    
    #Feature Extraction
    # 1 ... Aspect Ratio = width / length 
    length = math.hypot(extRight[0]-extLeft[0] , extRight[1]-extLeft[1])
    # Length of the Image is found from the extremes generated
    width = math.hypot(extTop[0]-extBot[0] , extTop[1]-extBot[1])
    # width is found from the extremes generated
    if (length < width):
        xxxx = length
        length = width
        width = xxxx
    aspectratio = width / length
    # Aspect Ratio is Extracted with Leaf 
    # 2 ... White area Ratio = Area of Leaf / ( Width * Lenght)  -> ( EXTENT ) 
    whitearearatio = area / (width * length)
    # 3 ... perimetertoarea ratio = leaf perimeter / leaf area  
    leafarea = PolyArea2D(giveCoordinates(contours)[0])
    # Leaf area is generated
    perimetertoarea = 0
    if(leafarea > 0.0):
        perimetertoarea = float(perimeter) / leafarea
        # perimeter to area ratio is generated
    # 4 ... perimeter to hull ratio = perimeter of hull / perimeter of leaf  
    hullcoordinates = giveCoordinates(hull)
    hullarea = PolyArea2D(hullcoordinates[0])
    hullperimeter = 0
    for c in hull:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        #cv2.drawContours(colorimg, [approx], -1, (0, 255, 0), 2)
        hullperimeter = hullperimeter+cv2.arcLength(c,True)
    # Hull perimeter generated
    perimetertohull = hullperimeter/perimeter
    # Perimeter to Hull Ratio generated
    # 5 ... HULL Area ratio = leaf area / Hull area    ( SOLIDITY )
    hullarearatio = 0
    if hullarea == 0.0:
        hullarearatio = 0
    else:
        hullarearatio = leafarea / hullarea
    #Solidity of the leaf is generated
    # 6 ... Circularity = 4*pi*area / hill perimeter**2
    circularity = (4*22/7)*leafarea/(hullperimeter**2)
    # Circularity of the Leaf is computed
    # 7 ... COLOR HIHSTOGRAM
    # 8 Equivalent Diameter = sqrt((4* contour area)/pi)
    equivalentdiameter = np.sqrt(4*leafarea/np.pi)
    #The Leaf's Equivalent diameter is computed for size of leaf
    # Feature Record hold all the Feature extracted from the Leaf Image
    featurerecord = [perimetertohull,aspectratio,circularity,equivalentdiameter,whitearearatio,perimetertoarea,hullarea,hullarearatio]
    featurerecord.extend(list(hist))
    return featurerecord
    #print(list(featurerecord))



#FeatureExtract("execute1.jpg")
