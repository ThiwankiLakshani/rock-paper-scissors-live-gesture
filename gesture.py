import mediapipe as mp

CHOICES = ["Rock", "Paper", "Scissors"]

# Helper function to check if a finger is extended
def is_finger_extended(tip, mcp, threshold=0.05):
    return tip.y < mcp.y - threshold

def detect_gesture(landmarks):
    thumb_tip = landmarks[4]
    thumb_mcp = landmarks[2]
    index_tip = landmarks[8]
    index_mcp = landmarks[5]
    middle_tip = landmarks[12]
    middle_mcp = landmarks[9]
    ring_tip = landmarks[16]
    ring_mcp = landmarks[13]
    pinky_tip = landmarks[20]
    pinky_mcp = landmarks[17]

    thumb_extended = is_finger_extended(thumb_tip, thumb_mcp)
    index_extended = is_finger_extended(index_tip, index_mcp)
    middle_extended = is_finger_extended(middle_tip, middle_mcp)
    ring_extended = is_finger_extended(ring_tip, ring_mcp)
    pinky_extended = is_finger_extended(pinky_tip, pinky_mcp)

    if not index_extended and not middle_extended and not ring_extended and not pinky_extended:
        return "Rock"
    elif index_extended and middle_extended and ring_extended and pinky_extended:
        return "Paper"
    elif index_extended and middle_extended and not ring_extended and not pinky_extended:
        return "Scissors"
    return None 