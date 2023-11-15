from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

isrunning = True

while isrunning:
    ret, frame = cap.read()

    plt.imshow(frame[:, :, ::-1])
    plt.show()

    result = DeepFace.analyze(frame, actions=['emotion'])

    print(result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        isrunning=False

cap.release()
cv2.destroyAllWindows()