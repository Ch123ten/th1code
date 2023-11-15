import cv2             # pip install opencv-python
import mediapipe as mp  # pip install mediapipe

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)  

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks and len(results.multi_hand_landmarks) == 1:
        hand_landmarks = results.multi_hand_landmarks[0] 
        landmarks = [(int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])) for landmark in hand_landmarks.landmark]
        extended_fingers = [landmarks[i][1] < landmarks[i - 2][1] for i in [4, 8, 12, 16, 20]]
        finger_count = sum(1 for extended in extended_fingers if extended) -1

        cv2.putText(frame, f"Detected: {finger_count}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
