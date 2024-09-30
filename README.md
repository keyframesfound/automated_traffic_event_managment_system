
<p align="center">
    <h1 align="center">ATEMs</h1>
</p>
<p align="center">
    <em><code>❯Automated Traffic Event Management System</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/keyframesfound/ssc-plateschecker?style=flat&logo=opensourceinitiative&logoColor=white&color=f9f9ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/keyframesfound/ssc-plateschecker?style=flat&logo=git&logoColor=white&color=f9f9ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/keyframesfound/ssc-plateschecker?style=flat&color=f9f9ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/keyframesfound/ssc-plateschecker?style=flat&color=f9f9ff" alt="repo-language-count">
</p>
<p align="center">
		<em>Built for SSC Campus Traffic During Large Scale Events:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>

<br>

##### 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [🚀 Getting Started](#-getting-started)
    - [🔖 Prerequisites](#-prerequisites)
    - [📦 Installation](#-installation)
    - [🤖 Usage](#-usage)
- [📌 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

<code>❯ License Plate Detection and Reading
Originally, this project was aimed at helping solve the ongoing traffic management issue we face during events, requiring lots of people to stand in the heat for hours at a time to direct traffic. Through this project, we hope to solve 3 major issues: 1 identifying cars between staff members and outside guests, two effectively managing campus traffic, and three making the whole system remote and requiring only two on-site operators. While this sounds like a very difficult and complicated endeavour, our team is confident in our skills and hopes to, through this project, contribute & finally solve this problem.  </code>

---

## 👾 Features

<code>❯ 
Automatically detects available camera sources on the system.
Allows the user to select a camera source for license plate detection.
Utilizes the Haar Cascade classifier for Russian license plate detection.
Extracts the text from the detected license plates using the Tesseract OCR engine.
Displays the video stream with the detected license plates highlighted and the extracted text displayed</code>

---

## 📂 Repository Structure

```sh
└── ssc-plateschecker/
    ├── Main.py
    ├── README.md
    ├── LICENSE
    └── requirements.txt

```


---

## 🚀 Getting Started

### 🔖 Prerequisites

**Python**: `version 3.12.3`

### 📦 Installation

Build the project from source:

1. Clone the ssc-plateschecker repository:
```sh
❯ git clone https://github.com/keyframesfound/ssc-plateschecker
```

2. Navigate to the project directory:
```sh
❯ cd ssc-plateschecker
```

3. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

### 🤖 Usage

To run the project, execute the following command:

```sh
❯ python main.py
```
---

## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Add OCR engine to code</strike>
- [ ] **`Task 2`**: Achive a 80% Accuracy to the system
- [ ] **`Task 3`**: Achive a 99% Accuracy to the system & connect light / traffic direction sign
- [ ] **`Task 3`**: Full automatic test for large scale event

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/keyframesfound/ssc-plateschecker/issues)**: Submit bugs found or log feature requests for the `ssc-plateschecker` project.
- **[Join the Discussions](https://github.com/keyframesfound/ssc-plateschecker/discussions)**: Share your insights, provide feedback, or ask questions.

<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/keyframesfound/ssc-plateschecker/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=keyframesfound/ssc-plateschecker">
   </a>
</p>
</details>

---

## 🎗 License
This project is licensed under the MIT License.

---

## 🙌 Acknowledgments

- [automatic-number-plate-recognition-python-yolov8](https://github.com/computervisioneng/automatic-number-plate-recognition-python-yolov8)
- [Car-Number-Plate-Recognition-Sysytem](https://github.com/hasaan21/Car-Number-Plate-Recognition-Sysytem/tree/master)
- [DetectCarDistanceAndRoadLane](https://github.com/ablanco1950/DetectCarDistanceAndRoadLane)

---
