from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
from time import sleep
import cv2

subscription_key = "7a2607ca622b4e449763a5417111f329"
endpoint = "https://bayern.cognitiveservices.azure.com/"
img_path = 'C:\\Users\\cjjun\\Desktop\\img2.jpg'

client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

img = open(img_path, 'rb')
recognize_results = client.read_in_stream(img, raw=True)
img.close()

location_remote = recognize_results.headers["Operation-Location"]
operation_id = location_remote.split("/")[-1]


while True:
    result = client.get_read_result(operation_id)
    if result.status not in ['notStarted', 'running']:
        break
    sleep(0.5)

img_text = cv2.imread(img_path)
if result.status == OperationStatusCodes.succeeded:
    for text_result in result.analyze_result.read_results:
        for line in text_result.lines:
            box = [int(i) for i in line.bounding_box]
            print(line.text)
            
            for i in range(0, 8, 2):
                pt1 = (*box[i : i + 2],)
                pt2 = (*box[(i + 2) % 8 : (i + 3) % 8 + 1],) 
                cv2.line(img_text, pt1, pt2, (255,0,0), 3)
            cv2.putText(img_text, line.text, (*box[0:2],), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)


cv2.imshow('result', img_text)
cv2.waitKey(0)
