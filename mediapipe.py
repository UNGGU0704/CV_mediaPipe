import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import cv2
import mediapipe as mp
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import random
import time

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        start_button = QPushButton('Start Game', self)
        start_button.clicked.connect(self.run_code)
        vbox.addWidget(start_button)

        self.setLayout(vbox)

        self.setWindowTitle('Rock Scissors face game with Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()
      
    def countdown_timer(self, countdown_time, elapsed_time):
        if elapsed_time < countdown_time:
            return countdown_time - elapsed_time
        else:
            return None

    def run_code(self):
        text = ""
        # 컴퓨터의 선택 생성
        choices = ["rock", "scissors", "face"]
        computer_choice = random.choice(choices)
        countdown = 15
        start_time = time.time()
        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands
        mp_drawing_styles = mp.solutions.drawing_styles
        
        # For webcam input:
        cap = cv2.VideoCapture(0)
        
        start_time = time.time()
        with mp_hands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
        
          
          while cap.isOpened():
            success, image = cap.read()
        
            if not success:
              print("Ignoring empty camera frame.")
        
              # If loading a video, use 'break' instead of 'continue'.
              continue
        
            # Flip the image horizontally for a later selfie-view display, and convert
            # the BGR image to RGB.
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            results = hands.process(image)
        
        
            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            image_height, image_width, _ = image.shape
        


            if results.multi_hand_landmarks:
              for hand_landmarks in results.multi_hand_landmarks:
                elapsed_time = int(time.time() - start_time)
                time_remaining = self.countdown_timer(countdown, elapsed_time)
                print(time_remaining)
                if time_remaining is not None:
                   font_face = cv2.FONT_HERSHEY_SIMPLEX
                   font_scale = 1.5
                   font_thickness = 2
                   text_color = (255, 255, 255)

                   timer_text = f"{time_remaining}"
                   text_size, _ = cv2.getTextSize(timer_text, font_face, font_scale, font_thickness)

                   text_x = (image.shape[1] - text_size[0]) // 2
                   text_y = (image.shape[0] + text_size[1]) // 4
                   cv2.putText(image, timer_text, (text_x, text_y), font_face, font_scale, text_color, font_thickness)

        
                # 엄지를 제외한 나머지 4개 손가락의 마디 위치 관계를 확인하여 플래그 변수를 설정합니다. 손가락을 일자로 편 상태인지 확인합니다.
                thumb_finger_state = 0
                if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y * image_height:
                  if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y * image_height:
                    if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height:
                      thumb_finger_state = 1
        
                index_finger_state = 0
                if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height:
                  if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height:
                    if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height:
                      index_finger_state = 1
        
                middle_finger_state = 0
                if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height:
                  if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height:
                    if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height:
                      middle_finger_state = 1
        
                ring_finger_state = 0
                if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height:
                  if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height:
                    if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height:
                      ring_finger_state = 1
        
                pinky_finger_state = 0
                if hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y * image_height:
                  if hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y * image_height:
                    if hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_height:
                      pinky_finger_state = 1
        
        
                # 손가락 위치 확인한 값을 사용하여 가위,바위,보 중 하나를 출력 해줍니다.
                font = ImageFont.truetype("Helvetica", 80)
                image = Image.fromarray(image)
                draw = ImageDraw.Draw(image)
        
                
               
                if thumb_finger_state == 1 and index_finger_state == 1 and middle_finger_state == 1 and ring_finger_state == 1 and pinky_finger_state == 1:
                  text = "face"
                elif thumb_finger_state == 0 and index_finger_state == 1 and middle_finger_state == 1 and ring_finger_state == 0 and pinky_finger_state == 0:
                  text = "scissors"
                elif   thumb_finger_state == 0 and index_finger_state == 0 and middle_finger_state == 0 and ring_finger_state == 0 and pinky_finger_state == 0:
                  text = "rock"
        
                w, h = font.getsize(text)
        
                x = 50
                y = 50
        
                draw.rectangle((x, y, x + w, y + h), fill='black')
                draw.text((x, y),  text, font=font, fill=(255, 255, 255))
                image = np.array(image)
        
                if time_remaining is None:
                    
                    # 카운트다운이 완료된 경우
                    result = ""
                    if text == computer_choice:  # 비긴 경우
                        result = "Tie"
                    elif (text == "rock" and computer_choice == "scissors") or (
                        text == "scissors" and computer_choice == "face"
                    ) or (text == "face" and computer_choice == "rock"):  # 이긴 경우
                        result = "You Win"
                    else:  # 진 경우
                        result = "You Lose"
                        
               
                    text_result = f"Player: {text} vs Computer: {computer_choice} Result: {result}"
                    font_face = cv2.FONT_HERSHEY_SIMPLEX
                    font_scale = 1.5
                    font_thickness = 2
                    text_color = (255, 255, 255)
                    
                    text_size, _ = cv2.getTextSize(text_result, font_face, font_scale, font_thickness)
                    
                    x_result = (image.shape[1] - text_size[0]) // 2
                    y_result = (image.shape[0] + text_size[1]) // 4
                    
                    cv2.putText(image, text_result, (x_result, y_result), font_face, font_scale, text_color, font_thickness)
                    
                   
                    break
                # 손가락 뼈대를 그려줍니다.
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
          
            cv2.imshow('MediaPipe Hands', image)
        
            if cv2.waitKey(5) & 0xFF == 27:
              break



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
