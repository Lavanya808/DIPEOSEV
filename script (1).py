# Create the main HTML structure for the programming education platform
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodeLearn Pro - Intelligent Programming Education Platform</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.13/codemirror.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.13/theme/monokai.min.css">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <h2>CodeLearn Pro</h2>
                <span class="ai-badge">AI-Powered</span>
            </div>
            <ul class="nav-menu">
                <li><a href="#home" class="nav-link active">Home</a></li>
                <li><a href="#courses" class="nav-link">Courses</a></li>
                <li><a href="#coding-lab" class="nav-link">Coding Lab</a></li>
                <li><a href="#debug-assistant" class="nav-link">Debug Assistant</a></li>
                <li><a href="#progress" class="nav-link">Progress</a></li>
            </ul>
            <div class="hamburger">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="hero-content">
            <h1>Master Programming with AI-Powered Learning</h1>
            <p>Experience personalized coding education with intelligent debugging, real-time feedback, and adaptive learning paths.</p>
            <div class="hero-buttons">
                <button class="btn-primary" onclick="startLearning()">Start Learning</button>
                <button class="btn-secondary" onclick="showDemo()">Watch Demo</button>
            </div>
        </div>
        <div class="hero-visual">
            <div class="code-animation">
                <pre class="animated-code">
<span class="keyword">function</span> <span class="function">smartLearning</span>() {
  <span class="keyword">const</span> <span class="variable">student</span> = <span class="string">"you"</span>;
  <span class="keyword">const</span> <span class="variable">ai</span> = <span class="keyword">new</span> <span class="class">IntelligentTutor</span>();
  
  <span class="keyword">return</span> ai.<span class="method">teach</span>(student);
}
                </pre>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="features">
        <div class="container">
            <h2>Why Choose CodeLearn Pro?</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🤖</div>
                    <h3>AI-Powered Debugging</h3>
                    <p>Get instant, intelligent help with code errors and suggestions for improvement.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📊</div>
                    <h3>Adaptive Learning</h3>
                    <p>Personalized learning paths that adjust to your skill level and progress.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>Real-time Feedback</h3>
                    <p>Immediate code evaluation and suggestions as you type.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎯</div>
                    <h3>Interactive Challenges</h3>
                    <p>Hands-on coding exercises with automated testing and grading.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Courses Section -->
    <section id="courses" class="courses">
        <div class="container">
            <h2>Programming Courses</h2>
            <div class="course-filters">
                <button class="filter-btn active" data-filter="all">All</button>
                <button class="filter-btn" data-filter="beginner">Beginner</button>
                <button class="filter-btn" data-filter="intermediate">Intermediate</button>
                <button class="filter-btn" data-filter="advanced">Advanced</button>
            </div>
            <div class="courses-grid" id="coursesGrid">
                <!-- Courses will be dynamically loaded here -->
            </div>
        </div>
    </section>

    <!-- Coding Lab Section -->
    <section id="coding-lab" class="coding-lab">
        <div class="container">
            <h2>Interactive Coding Lab</h2>
            <div class="lab-container">
                <div class="lab-sidebar">
                    <div class="language-selector">
                        <label for="language">Language:</label>
                        <select id="language" onchange="changeLanguage()">
                            <option value="javascript">JavaScript</option>
                            <option value="python">Python</option>
                            <option value="java">Java</option>
                            <option value="cpp">C++</option>
                        </select>
                    </div>
                    <div class="lab-controls">
                        <button class="btn-run" onclick="runCode()">▶ Run Code</button>
                        <button class="btn-debug" onclick="debugCode()">🔍 Debug</button>
                        <button class="btn-ai-help" onclick="getAIHelp()">🤖 AI Help</button>
                    </div>
                    <div class="problem-statement">
                        <h3>Current Problem</h3>
                        <div id="problemDescription">
                            <p><strong>FizzBuzz Challenge</strong></p>
                            <p>Write a program that prints numbers 1-100, but:</p>
                            <ul>
                                <li>Print "Fizz" for multiples of 3</li>
                                <li>Print "Buzz" for multiples of 5</li>
                                <li>Print "FizzBuzz" for multiples of both</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="lab-editor">
                    <div class="editor-header">
                        <span class="file-name">main.js</span>
                        <div class="editor-controls">
                            <button onclick="resetCode()">Reset</button>
                            <button onclick="saveCode()">Save</button>
                        </div>
                    </div>
                    <div class="editor-container">
                        <textarea id="codeEditor" placeholder="// Start coding here...
function fizzBuzz() {
    for (let i = 1; i <= 100; i++) {
        // Your code here
    }
}

fizzBuzz();"></textarea>
                    </div>
                </div>
                <div class="lab-output">
                    <div class="output-tabs">
                        <button class="tab-btn active" data-tab="console">Console</button>
                        <button class="tab-btn" data-tab="ai-feedback">AI Feedback</button>
                        <button class="tab-btn" data-tab="tests">Test Results</button>
                    </div>
                    <div class="output-content">
                        <div class="tab-content active" id="console">
                            <div class="console-output" id="consoleOutput">
                                <p class="console-info">Ready to run your code...</p>
                            </div>
                        </div>
                        <div class="tab-content" id="ai-feedback">
                            <div class="ai-feedback-content" id="aiFeedbackContent">
                                <p>Click "AI Help" to get personalized suggestions!</p>
                            </div>
                        </div>
                        <div class="tab-content" id="tests">
                            <div class="test-results" id="testResults">
                                <p>Run your code to see test results...</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Debug Assistant Section -->
    <section id="debug-assistant" class="debug-assistant">
        <div class="container">
            <h2>AI Debug Assistant</h2>
            <div class="debug-container">
                <div class="debug-input">
                    <h3>Paste Your Code Here</h3>
                    <textarea id="debugCode" placeholder="Paste your problematic code here, and our AI will help you debug it..."></textarea>
                    <div class="debug-controls">
                        <button class="btn-primary" onclick="analyzeCode()">🔍 Analyze Code</button>
                        <button class="btn-secondary" onclick="clearDebugInput()">Clear</button>
                    </div>
                </div>
                <div class="debug-results">
                    <h3>Analysis Results</h3>
                    <div id="debugResults" class="debug-output">
                        <p class="placeholder-text">Submit your code to get AI-powered debugging assistance...</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Progress Section -->
    <section id="progress" class="progress-section">
        <div class="container">
            <h2>Your Learning Progress</h2>
            <div class="progress-grid">
                <div class="progress-card">
                    <h3>Overall Progress</h3>
                    <div class="circular-progress" data-progress="65">
                        <div class="progress-circle">
                            <span class="progress-text">65%</span>
                        </div>
                    </div>
                </div>
                <div class="progress-card">
                    <h3>Skills Mastered</h3>
                    <div class="skills-list">
                        <div class="skill-item">
                            <span>JavaScript Basics</span>
                            <div class="skill-bar">
                                <div class="skill-fill" style="width: 90%;"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span>Problem Solving</span>
                            <div class="skill-bar">
                                <div class="skill-fill" style="width: 75%;"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span>Debugging</span>
                            <div class="skill-bar">
                                <div class="skill-fill" style="width: 60%;"></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="progress-card">
                    <h3>Recent Achievements</h3>
                    <div class="achievements">
                        <div class="achievement">🏆 Completed 50 exercises</div>
                        <div class="achievement">⭐ Perfect score on Arrays</div>
                        <div class="achievement">🔥 7-day coding streak</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>CodeLearn Pro</h3>
                    <p>Empowering the next generation of programmers with AI-enhanced education.</p>
                </div>
                <div class="footer-section">
                    <h4>Features</h4>
                    <ul>
                        <li>AI Debugging</li>
                        <li>Interactive Lessons</li>
                        <li>Real-time Feedback</li>
                        <li>Progress Tracking</li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Support</h4>
                    <ul>
                        <li>Help Center</li>
                        <li>Community Forum</li>
                        <li>Contact Us</li>
                        <li>Documentation</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 CodeLearn Pro. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Scripts -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.13/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.13/mode/javascript/javascript.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.13/mode/python/python.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.13/mode/clike/clike.min.js"></script>
    <script src="script.js"></script>
</body>
</html>'''

# Save the HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML file created successfully: index.html")