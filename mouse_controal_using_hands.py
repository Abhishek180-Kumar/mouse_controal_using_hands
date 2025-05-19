import cv2
import mediapipe as mp
import pyautogui
import time

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
drawing_utils = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
click_down = False

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    hand_landmarks = result.multi_hand_landmarks

    if hand_landmarks:
        for handLMs in hand_landmarks:
            drawing_utils.draw_landmarks(frame, handLMs, mp_hands.HAND_CONNECTIONS)
            landmarks = handLMs.landmark

            index_tip = landmarks[8]
            thumb_tip = landmarks[4]

            index_x = int(index_tip.x * frame_width)
            index_y = int(index_tip.y * frame_height)
            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)

            cv2.circle(frame, (index_x, index_y), 8, (255, 0, 255), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 8, (0, 255, 0), -1)

            screen_x = int(index_tip.x * screen_width)
            screen_y = int(index_tip.y * screen_height)
            pyautogui.moveTo(screen_x, screen_y)

            distance = abs(index_x - thumb_x) + abs(index_y - thumb_y)
            if distance < 40:
                if not click_down:
                    click_down = True
                    pyautogui.click()
                    time.sleep(0.3)
            else:
                click_down = False

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
