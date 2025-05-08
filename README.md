#  🪨📄✂️ rock-paper-scissors-live-gesture


A computer vision-powered twist on the classic game **Rock, Paper, Scissors**, where your **hand gestures** control the game and your opponent is a quick-thinking AI!

Built with **Python**, **OpenCV**, and **MediaPipe**, this project lets you play RPS using just your webcam, detecting your gestures in real-time and pitting them against an AI opponent. No clicks. No buttons. Just hand signs.

---

## 🎮 How It Works

1. **Webcam feed** is launched.
2. **Hand gestures** are detected using **MediaPipe Hands**.
3. When the game starts:

   * A **3-second countdown** begins.
   * Your hand gesture is captured.
   * The AI randomly picks Rock, Paper, or Scissors.
   * A winner is decided based on traditional rules.
4. **Results are displayed**, and the next round begins every 10 seconds.

---

## 🧠 Features

* 🤖 AI randomly selects its move.
* ✋ Real-time hand gesture recognition (Rock, Paper, or Scissors).
* ⏱ Countdown timer for gesture capture.
* 🪞 Mirror-style webcam feed.
* 🖥 Visual game feedback (Player move, AI move, result).
* 🎯 Works entirely from your webcam—no keyboard or mouse needed after starting!

---

## 🛠 Tech Stack

* **Python 3**
* [OpenCV](https://opencv.org/) – Video capture & UI rendering
* [MediaPipe](https://mediapipe.dev/) – Hand landmark detection
* **NumPy** – Coordinate handling
* **Random**, **Time** – Game logic & timers

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ThiwankiLakshani/rock-paper-scissors-vs-ai.git
cd rock-paper-scissors-vs-ai
```

### 2. Install Requirements

Make sure Python 3 is installed. Then install dependencies:

```bash
pip install opencv-python mediapipe numpy
```

### 3. Run the Game

```bash
python rps_vs_ai.py
```

---

## 🎥 Controls

| Key | Action               |
| --- | -------------------- |
| `s` | Start/Stop the game  |
| `q` | Quit the application |

---

## 🖐 Gesture Guide

| Gesture                      | Meaning  |
| ---------------------------- | -------- |
| ✊ (Fist)                     | Rock     |
| 🖐 (All fingers extended)    | Paper    |
| ✌️ (Index + Middle extended) | Scissors |

---


## 💡 Ideas for Future Enhancements

* ✨ Add gesture smoothing or confidence thresholds
* 📈 Show game statistics (Wins, Losses, Ties)
* 🧑‍🤝‍🧑 Multiplayer over LAN
* 🎨 Better UI with overlay graphics or animations
* 📲 Mobile version using device camera

---

## 🤝 Contributing

Pull requests are welcome! If you’ve got an idea to make this game even better, feel free to fork, improve, and open a PR.

