# ATEMs

## Automated Traffic Event Management System

![Markdown](https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Bash](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white)
![Anaconda](https://img.shields.io/badge/Anaconda-44A833.svg?style=for-the-badge&logo=Anaconda&logoColor=white)

*Built for SSC Campus Traffic During Large-Scale Events*

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Project Roadmap](#project-roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview
This project aims to solve traffic management issues during large-scale events by automating license plate detection and reading. It reduces the need for manual traffic direction, making the process more efficient and less labor-intensive.

## Features
- **Camera Source Detection:** Automatically detects available camera sources on the system.
- **Camera Selection:** Allows the user to select a camera source for license plate detection.
- **License Plate Detection:** Utilizes the Haar Cascade classifier for Russian license plate detection.
- **OCR:** Extracts text from detected license plates using the EasyOCR engine.
- **Video Stream Display:** Displays the video stream with detected license plates highlighted and the extracted text.

## Repository Structure
```
automated_traffic_event_managment_system/
├── Main.py
├── README.md
├── LICENSE
└── requirements.txt
```

## Getting Started

### Prerequisites
- **Python:** Version 3.8.20 or later

### Installation
To build the project from source:

1. Clone the repository:
   ```sh
   git clone https://github.com/keyframesfound/ATEMS
   ```

2. Navigate to the project directory:
   ```sh
   cd ATEMS
   ```

3. For Linux installations only:
   ```sh
   source myenv/bin/activate
   ```

4. Install required packages:
   ```sh
   pip install opencv-python torch easyocr yolov5 numpy flask python-Levenshtein
   ```

### Usage
To run the project, execute the following command:
```sh
python3 Main.py
```

## Project Roadmap
- [x] **Task 1:** Add OCR engine to code
- [ ] **Task 2:** Achieve 80% accuracy in the system
- [ ] **Task 3:** Achieve 99% accuracy and connect light/traffic direction signs
- [ ] **Task 4:** Full automatic test for large-scale events

## License
This project is licensed under the MIT License.

## Acknowledgments
- [automatic-number-plate-recognition-python-yolov8](https://github.com/computervisioneng/automatic-number-plate-recognition-python-yolov8)
- [Car-Number-Plate-Recognition-System](https://github.com/hasaan21/Car-Number-Plate-Recognition-Sysytem/tree/master)
- [DetectCarDistanceAndRoadLane](https://github.com/ablanco1950/DetectCarDistanceAndRoadLane)
- [Huggingface Model](https://huggingface.co/keremberke/yolov5m-license-plate)

---
