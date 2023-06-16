import numpy as np
from PIL import Image
import torch
import cv2
import switch

def identify_sport(image_encoded):

    image = np.array(Image.open(image_encoded.file))

    img_width = image.shape[1]
    img_height = image.shape[0]

    sports_list = []

    if img_width > img_height:
        img_height = (img_height / img_width) * 640
        img_height = round(img_height)

        img_width = 640
    else:
        img_width = (img_width / img_height) * 640
        img_width = round(img_width)

        img_height = 640

    image_resized = cv2.resize(image,(img_width,img_height))

    model = torch.hub.load('ultralytics/yolov5','custom', 'yolov5model.pt')

    result = model(image_resized)

    print(result)

    df = result.pandas().xyxy[0]

    for ind in df.index:
        x1, y1 = int(df['xmin'][ind]), int(df['ymin'][ind])
        x2, y2 = int(df['xmax'][ind]), int(df['ymax'][ind])
        label = df['name'][ind]
        conf = df['confidence'][ind]
        sportClass = df['class'][ind]

        cv2.rectangle(image_resized, (x1,y1), (x2,y2), (0, 0, 225), 2)
        cv2.putText(image_resized, label, (x1,y1-5), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 225), 2)

        #Add sprots list to the array
        sports_list.append(switch.detect_sport(sportClass))

        #get the sport name
        res = max(set(sports_list), key=sports_list.count)

    if len(sports_list) == 0:
        return ''
    else:
        return str(res)