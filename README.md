<p align="center">
    <h1 align="center">ATEMs</h1>
</p>
<p align="center">
    <h3 align="center"><code>Automated Traffic Event Management System</code></h3>
  <p align="center">
   <img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
   <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
   <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="Bash" />
   <img src="https://img.shields.io/badge/Anaconda-44A833.svg?style=for-the-badge&logo=Anaconda&logoColor=white" alt="Anaconda" />
 </p>
<p align="center">
        <em>Built for SSC Campus Traffic During Large Scale Events:</em>
</p>

<p><br></p>
<h5 id="-table-of-contents">🔗 Table of Contents</h5>
<ul>
<li><a href="#-overview">📍 Overview</a></li>
<li><a href="#-features">👾 Features</a></li>
<li><a href="#-getting-started">🚀 Getting Started</a><ul>
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
<p>License Plate Detection and Reading
Originally, this project was aimed at helping solve the ongoing traffic management issue we face during events, requiring lots of people to stand in the heat for hours at a time to direct traffic. Through this project, we hope to solve 3 major issues: 1 identifying cars between staff members and outside guests, two effectively managing campus traffic, and three making the whole system remote and requiring only two on-site operators. While this sounds like a very difficult and complicated endeavour, our team is confident in our skills and hopes to, through this project, contribute &amp; finally solve this problem.</p>
<hr>
<h2 id="-features">👾 Features</h2>
<p>Automatically detects available camera sources on the system.
Allows the user to select a camera source for license plate detection.
Utilizes the Haar Cascade classifier for Russian license plate detection.
Extracts the text from the detected license plates using the EasyOCR engine.
Displays the video stream with the detected license plates highlighted and the extracted text displayed.</p>
<hr>
<h2 id="-repository-structure">📂 Repository Structure</h2>
<pre><code class="lang-sh">└── automated_traffic_event_managment_system/
    ├── Main<span class="hljs-selector-class">.py</span>
    ├── README<span class="hljs-selector-class">.md</span>
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
<li><p>Clone the automated_traffic_event_managment_system repository:</p>
<pre><code class="lang-sh">git <span class="hljs-keyword">clone</span> <span class="hljs-title">https</span>://github.com/keyframesfound/automated_traffic_event_managment_system
</code></pre>
</li>
<li><p>Navigate to the project directory:</p>
<pre><code class="lang-sh"><span class="hljs-built_in">cd</span> automated_traffic_event_managment_system
</code></pre>
</li>
</ol>
<p>2.1 For Linux Installations Only:</p>
<pre><code class="lang-sh"><span class="hljs-keyword">source</span> myenv<span class="hljs-regexp">/bin/</span>activate
</code></pre>
<ol>
<li>Install the required dependencies:<pre><code class="lang-sh">pip <span class="hljs-keyword">install</span> -r requirements.txt
</code></pre>
</li>
</ol>
<h3 id="-run-the-script">🤖 Run the script</h3>
<p>To run the project, execute the following command:</p>
<pre><code class="lang-sh"><span class="hljs-keyword">python3</span> Main.<span class="hljs-keyword">py</span>
</code></pre>
<hr>
<h2 id="-project-roadmap">📌 Project Roadmap</h2>
<ul>
<li>[X] <strong><code>Task 1</code></strong>: <strike>Add OCR engine to code</strike></li>
<li>[ ] <strong><code>Task 2</code></strong>: Achive a 80% Accuracy to the system</li>
<li>[ ] <strong><code>Task 3</code></strong>: Achive a 99% Accuracy to the system &amp; connect light / traffic direction sign</li>
<li>[ ] <strong><code>Task 3</code></strong>: Full automatic test for large scale event</li>
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
