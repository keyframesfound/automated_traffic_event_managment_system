<p align="center">
 <h1 align="center">ATEMs</h1>
    <h3><code>Automated Traffic Event Management System</code></h3>
    <p>
        <img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
        <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
        <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="Bash" />
        <img src="https://img.shields.io/badge/Anaconda-44A833.svg?style=for-the-badge&logo=Anaconda&logoColor=white" alt="Anaconda" />
    </p>
    <em>Built for SSC Campus Traffic During Large Scale Events:</em>
</p>

<h5>🔗 Table of Contents</h5>
<ul>
    <li><a href="#-overview">📍 Overview</a></li>
    <li><a href="#-features">👾 Features</a></li>
    <li><a href="#-getting-started">🚀 Getting Started</a>
        <ul>
            <li><a href="#-prerequisites">🔖 Prerequisites</a></li>
            <li><a href="#-installation">📦 Installation</a></li>
            <li><a href="#-usage">🤖 Usage</a></li>
        </ul>
    </li>
    <li><a href="#-project-roadmap">📌 Project Roadmap</a></li>
    <li><a href="#-license">🎗 License</a></li>
    <li><a href="#-acknowledgments">🙌 Acknowledgments</a></li>
</ul>

<hr>

<h2 id="-overview">📍 Overview</h2>
<p>License Plate Detection and Reading. This project aims to solve traffic management issues during events, reducing the need for staff to direct traffic manually. We focus on three main objectives: identifying cars between staff and guests, managing campus traffic effectively, and minimizing on-site personnel to two operators. Our team is confident in our skills and aims to contribute to solving this problem.</p>

<hr>

<h2 id="-features">👾 Features</h2>
<ul>
    <li>Automatically detects available camera sources on the system.</li>
    <li>Allows the user to select a camera source for license plate detection.</li>
    <li>Utilizes the Haar Cascade classifier for Russian license plate detection.</li>
    <li>Extracts text from detected license plates using the EasyOCR engine.</li>
    <li>Displays the video stream with highlighted detected license plates and extracted text.</li>
</ul>

<hr>

<h2 id="-repository-structure">📂 Repository Structure</h2>
<pre><code>└── automated_traffic_event_management_system/
    ├── Main.py
    ├── README.md
    ├── LICENSE
    └── requirements.txt
</code></pre>

<hr>

<h2 id="-getting-started">🚀 Getting Started</h2>

<h3 id="-prerequisites">🔖 Prerequisites</h3>
<p><strong>Python</strong>: <code>version 3.8.20</code></p>

<h3 id="-installation">📦 Installation</h3>
<p>Build the project from source:</p>
<ol>
    <li>
        Clone the repository:
        <pre><code>git clone https://github.com/keyframesfound/automated_traffic_event_management_system</code></pre>
    </li>
    <li>
        Navigate to the project directory:
        <pre><code>cd automated_traffic_event_management_system</code></pre>
    </li>
</ol>
<p>For Linux Installations Only:</p>
<pre><code>source myenv/bin/activate</code></pre>
<ol>
    <li>Install the required dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
</ol>

<h3 id="-run-the-script">🤖 Run the script</h3>
<p>Execute the following command to run the project:</p>
<pre><code>python3 Main.py</code></pre>

<hr>

<h2 id="-project-roadmap">📌 Project Roadmap</h2>
<ul>
    <li>[X] <strong><code>Task 1</code></strong>: <strike>Add OCR engine to code</strike></li>
    <li>[ ] <strong><code>Task 2</code></strong>: Achieve 80% accuracy in the system</li>
    <li>[ ] <strong><code>Task 3</code></strong>: Achieve 99% accuracy & connect light/traffic direction sign</li>
    <li>[ ] <strong><code>Task 4</code></strong>: Full automatic test for large scale event</li>
</ul>

<hr>

<h2 id="-license">🎗 License</h2>
<p>This project is licensed under the MIT License.</p>

<hr>

<h2 id="-acknowledgments">🙌 Acknowledgments</h2>
<ul>
    <li><a href="https://github.com/computervisioneng/automatic-number-plate-recognition-python-yolov8">automatic-number-plate-recognition-python-yolov8</a></li>
    <li><a href="https://github.com/hasaan21/Car-Number-Plate-Recognition-Sysytem/tree/master">Car-Number-Plate-Recognition-Sysytem</a></li>
    <li><a href="https://github.com/ablanco1950/DetectCarDistanceAndRoadLane">DetectCarDistanceAndRoadLane</a></li>
    <li><a href="https://huggingface.co/keremberke/yolov5m-license-plate">Huggingface Model</a></li>
</ul>

<hr>
