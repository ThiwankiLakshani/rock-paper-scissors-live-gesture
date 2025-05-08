import cv2
import mediapipe as mp
import time
from gesture import detect_gesture, CHOICES
from game import ScoreBoard, determine_winner, get_ai_choice

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize MediaPipe Hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

scoreboard = ScoreBoard()
game_active = False
countdown = 0
countdown_start = 0
player_choice = None
ai_choice = None
result = None
last_round_time = 0
next_round_time = 0

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    frame = cv2.flip(frame, 1)

    # --- Visualization: Grayscale ---
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", gray)

    # --- Visualization: Binarization (Thresholding) ---
    _, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
    cv2.imshow("Thresholded", thresh)

    # --- Visualization: Contours ---
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0,255,0), 2)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    # Handle countdown and gesture detection
    if game_active and countdown > 0:
        elapsed = time.time() - countdown_start
        countdown_display = 3 - int(elapsed)
        if countdown_display <= 0:
            countdown = 0
            # Capture gesture at end of countdown
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    gesture = detect_gesture(hand_landmarks.landmark)
                    if gesture:
                        player_choice = gesture
                        ai_choice = get_ai_choice()
                        result = determine_winner(player_choice, ai_choice)
                        scoreboard.update(result)
                        last_round_time = time.time()
                        next_round_time = time.time() + 5
            else:
                player_choice = None
                ai_choice = None
                result = "No hand detected"
                last_round_time = time.time()
                next_round_time = time.time() + 5

    # Start new round every 5 seconds if game is active
    if game_active and countdown == 0 and time.time() >= next_round_time:
        countdown = 3
        countdown_start = time.time()
        player_choice = None
        ai_choice = None
        result = None

    # Draw landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display countdown
    if countdown > 0:
        cv2.putText(frame, f"Countdown: {3 - int(time.time() - countdown_start)}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display player choice, AI choice, and result
    if player_choice:
        cv2.putText(frame, f"Player: {player_choice}", (10, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    if ai_choice:
        cv2.putText(frame, f"AI: {ai_choice}", (10, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    if result:
        cv2.putText(frame, f"Result: {result}", (10, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display scores
    cv2.putText(frame, f"Score - You: {scoreboard.player}  AI: {scoreboard.ai}", (10, 250),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    # Display instructions
    cv2.putText(frame, f"Press 's' to {'stop' if game_active else 'start'} game, 'r' to reset, 'q' to quit",
                (10, frame.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Show the frame
    cv2.imshow("Rock Paper Scissors", frame)

    # Handle key presses
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        game_active = not game_active
        if game_active:
            countdown = 3
            countdown_start = time.time()
            next_round_time = time.time() + 5
            player_choice = None
            ai_choice = None
            result = None
        else:
            countdown = 0
    elif key == ord('r'):
        scoreboard.reset()
        player_choice = None
        ai_choice = None
        result = None

cap.release()
cv2.destroyAllWindows() 