# Yeh code run karo — kya error aata hai? Fix karo.

# vehicle_count = 15
# green_time = 10 + vehicle_count * 2
# print('Green time:', green_time)

# Yahan fix likho: vehicle_count

# Bug 2 — if condition
# Condition check karo — kya sahi hai?

# signal_state = 'GREEN'
# if signal_state == 'GREEN':
#  print('Gaadiyaan chal sakti hain!')
# else:
#  print('Ruko!')

# Yahan fix likho:
#  ==

# Bug 3 — List aur Loop
# Yeh code 4 lanes print karna chahta hai — kya hoga actually?

# lanes = ['North', 'South', 'East', 'West']
# for lane in lanes:
#  print('Lane:', lane)

#  Yahan fix likho: :

# Bug 4 — OpenCV
# Image load hogi ya nahi? Kya missing hai?

# import cv2
# img = cv2.imread('traffic.jpg')
# cv2.imshow('Traffic', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# Window open hoti hai aur turant band ho jaati hai!

# yahan fix karo : cv2.waitKey(0)

# Bug 5 — YOLO Detection
# Yeh code YOLO detection chalata hai — kya galat hai?
# from ultralytics import YOLO
# import cv2
# model = YOLO('yolov8n.pt')
# img = cv2.imread('traffic.jpg')
# results = model(img)

# for result in results:
#  for box in results.boxes: # <-- yahan dhyan do
#   class_id = int(box.cls[0])
#   print(model.names[class_id])

# yahan fix kare :  for result in results: