import json

modules = []

# Module 4 - SIMPLIFIED ALGORITHMS, PSEUDOCODE & VISUAL FLOWCHARTS
modules.append({
    "id": "m4",
    "num": 4,
    "title": "Problem Solving: Flowcharts & Pseudocode Made Simple",
    "subtitle": "The Recipe Analogy, Rosetta Stone Comparison, Rendered Flowcharts & Trace Tables",
    "slides": "Slides 31–45",
    "time": "40 mins",
    "content": """
      <div class="teaching-block">
        <h3><i class="fa-solid fa-cake-candles"></i> What is an Algorithm? Think of a Recipe!</h3>
        <p>Before you bake a cake, you need a recipe. If a recipe says <em>"mix stuff and bake until it looks ready,"</em> that's a terrible recipe because it's vague. But if it says:
        <br>&emsp;<code>1. Take 2 eggs and 1 cup of flour</code>
        <br>&emsp;<code>2. Whisk for 3 minutes until smooth</code>
        <br>&emsp;<code>3. Bake at 350°F for exactly 25 minutes</code>
        <br>Anyone following that recipe will get the exact same delicious cake!</p>

        <div class="teacher-callout insight">
          <div class="callout-icon"><i class="fa-solid fa-lightbulb"></i></div>
          <div class="callout-body">
            <div class="callout-title">The 4 Rules of Every Good Algorithm (Slide 31)</div>
            <p>&bull; <strong>Clear & Unambiguous:</strong> Every instruction has only one possible interpretation.
            <br>&bull; <strong>Has Inputs & Outputs:</strong> Takes raw ingredients (input) and gives a specific result (output).
            <br>&bull; <strong>Finiteness (Must Stop!):</strong> Must finish in a reasonable number of steps. It can never run forever.
            <br>&bull; <strong>Language-Independent:</strong> Written in plain logic so it can be programmed in C, Python, or Java alike.</p>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-bridge"></i> What is Pseudocode? The "Bridge" Between Thought and C</h3>
        <p>When you start coding, trying to figure out the logic while simultaneously worrying about semicolons, braces, and C syntax gives you a headache. <strong>Pseudocode</strong> solves this!</p>
        <p>Pseudocode is structured English. It looks like code, but has no strict syntax rules. Look at how cleanly logic translates across the <strong>Rosetta Stone Bridge</strong>:</p>

        <div class="rosetta-bridge">
          <div class="rosetta-col">
            <div class="rosetta-header english"><i class="fa-solid fa-user"></i> 1. Human English Thought</div>
            <div class="rosetta-body">
              "Ask the user for four exam marks. Find their average. If the average is below 40, they failed; otherwise they passed."
            </div>
          </div>

          <div class="rosetta-col">
            <div class="rosetta-header pseudocode"><i class="fa-solid fa-file-lines"></i> 2. Clean Pseudocode</div>
            <div class="rosetta-body">
              <pre>READ m1, m2, m3, m4
avg = (m1 + m2 + m3 + m4) / 4

IF avg < 40 THEN
    PRINT "Fail"
ELSE
    PRINT "Pass"
ENDIF</pre>
            </div>
          </div>

          <div class="rosetta-col">
            <div class="rosetta-header c-code"><i class="fa-solid fa-code"></i> 3. Actual C Language</div>
            <div class="rosetta-body">
              <pre>float m1, m2, m3, m4, avg;
scanf("%f %f %f %f", &m1, &m2, &m3, &m4);
avg = (m1 + m2 + m3 + m4) / 4.0;

if (avg < 40) {
    printf("Fail\\n");
} else {
    printf("Pass\\n");
}</pre>
            </div>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-shapes"></i> Standard Flowchart Shapes: What Each Shape Means</h3>
        <p>A <strong>Flowchart</strong> is simply drawing your algorithm with shapes and arrows so anyone can visually trace the flow of logic like water through a pipe:</p>

        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Shape</th><th>Name</th><th>Color Meaning</th><th>Real-Life Role in Flowchart</th></tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Oval / Pill</strong></td>
                <td>Terminal Symbol</td>
                <td><span style="color: #10b981; font-weight: 700;">GREEN</span></td>
                <td>Marks where the program <strong>STARTS</strong> and where it <strong>STOPS</strong>.</td>
              </tr>
              <tr>
                <td><strong>Parallelogram (Slanted)</strong></td>
                <td>Input / Output</td>
                <td><span style="color: #3b82f6; font-weight: 700;">BLUE</span></td>
                <td>Whenever the computer asks the user for data (<code>READ N</code>) or prints an answer on screen (<code>PRINT "Pass"</code>).</td>
              </tr>
              <tr>
                <td><strong>Rectangle (Box)</strong></td>
                <td>Process / Calculation</td>
                <td><span style="color: #f59e0b; font-weight: 700;">YELLOW</span></td>
                <td>Any internal calculation or variable assignment (<code>Sum = 0</code>, <code>avg = total / 4</code>).</td>
              </tr>
              <tr>
                <td><strong>Diamond</strong></td>
                <td>Decision / Question</td>
                <td><span style="color: #a855f7; font-weight: 700;">PURPLE</span></td>
                <td>Asks a Yes/No question with two exit arrows (e.g. <code>Is avg &lt; 40?</code> &rarr; Yes / No).</td>
              </tr>
              <tr>
                <td><strong>Arrows</strong></td>
                <td>Flowlines</td>
                <td><span style="color: var(--text-muted); font-weight: 700;">ARROWS</span></td>
                <td>Show the exact direction instructions travel.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-diagram-project"></i> Rendered Visual Flowchart: Student Grade Average (Slide 40–41)</h3>
        <p>Here is the visual diagram for calculating student grades and deciding pass/fail:</p>

        <div class="visual-flowchart">
          <div class="fc-node terminal"><i class="fa-solid fa-circle-play"></i> START</div>
          <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
          <div class="fc-node io"><i class="fa-solid fa-keyboard"></i> READ m1, m2, m3, m4</div>
          <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
          <div class="fc-node process"><i class="fa-solid fa-calculator"></i> avg = (m1 + m2 + m3 + m4) / 4</div>
          <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
          <div class="fc-node decision"><i class="fa-solid fa-question"></i> Is avg &lt; 40?</div>

          <div class="fc-decision-branches">
            <div class="fc-branch">
              <span class="fc-branch-tag true-tag">TRUE (Yes)</span>
              <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
              <div class="fc-node io"><i class="fa-solid fa-print"></i> PRINT "Fail"</div>
            </div>
            <div class="fc-branch">
              <span class="fc-branch-tag false-tag">FALSE (No)</span>
              <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
              <div class="fc-node io"><i class="fa-solid fa-print"></i> PRINT "Pass"</div>
            </div>
          </div>

          <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
          <div class="fc-node terminal"><i class="fa-solid fa-circle-stop"></i> STOP (END)</div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-arrow-rotate-right"></i> Rendered Visual Flowchart: Sum of Digits with Loop (Slide 42–44)</h3>
        <p>How does a program sum up digits of a number like <code>1234</code>? It repeatedly chops off the rightmost digit using <code>N % 10</code> and accumulates it:</p>

        <div class="visual-flowchart">
          <div class="fc-node terminal"><i class="fa-solid fa-circle-play"></i> START</div>
          <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
          <div class="fc-node io"><i class="fa-solid fa-keyboard"></i> READ N (e.g. 1234)</div>
          <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
          <div class="fc-node process"><i class="fa-solid fa-gear"></i> Set Sum = 0</div>
          <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
          <div class="fc-node decision"><i class="fa-solid fa-arrows-spin"></i> Loop: Is N != 0?</div>

          <div class="fc-decision-branches">
            <div class="fc-branch" style="border-color: var(--accent-blue);">
              <span class="fc-branch-tag true-tag">YES (Keep Looping)</span>
              <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
              <div class="fc-node process">Rem = N % 10 (get last digit)</div>
              <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
              <div class="fc-node process">Sum = Sum + Rem (add to total)</div>
              <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
              <div class="fc-node process">N = N / 10 (chop off last digit)</div>
              <p style="font-size: 0.75rem; color: var(--accent-cyan); margin-top: 0.5rem;">&uarr; Loop arrow flows back up to check N != 0</p>
            </div>
            <div class="fc-branch" style="border-color: var(--accent-emerald);">
              <span class="fc-branch-tag false-tag">NO (N reached 0)</span>
              <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
              <div class="fc-node io"><i class="fa-solid fa-print"></i> PRINT Sum</div>
              <div class="fc-arrow"><i class="fa-solid fa-arrow-down"></i></div>
              <div class="fc-node terminal"><i class="fa-solid fa-circle-stop"></i> END</div>
            </div>
          </div>
        </div>

        <h4>Step-by-Step Execution Trace Table for N = 1234</h4>
        <p>Watch exactly how variables change in each cycle of the loop:</p>
        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Iteration</th><th>Current N</th><th>Rem = N % 10 (Extracted Digit)</th><th>Sum = Sum + Rem</th><th>New N = N / 10 (Remaining)</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Before Loop</strong></td><td>1234</td><td>-</td><td>0</td><td>1234</td></tr>
              <tr><td><strong>Turn 1</strong></td><td>1234</td><td>4</td><td>0 + 4 = <strong>4</strong></td><td>123</td></tr>
              <tr><td><strong>Turn 2</strong></td><td>123</td><td>3</td><td>4 + 3 = <strong>7</strong></td><td>12</td></tr>
              <tr><td><strong>Turn 3</strong></td><td>12</td><td>2</td><td>7 + 2 = <strong>9</strong></td><td>1</td></tr>
              <tr><td><strong>Turn 4</strong></td><td>1</td><td>1</td><td>9 + 1 = <strong>10</strong></td><td><strong>0</strong> (Loop Exits!)</td></tr>
            </tbody>
          </table>
        </div>
        <p style="font-size: 0.95rem; font-weight: 700; color: var(--accent-emerald);">Final Output: Sum = 10 (since 1 + 2 + 3 + 4 = 10)!</p>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-list-ol"></i> Solutions to the 6 Practice Challenges (Slide 45)</h3>
        <ol>
          <li><strong>Sum of Multiples of 3 or 5 below 1000:</strong> Loop from 1 to 999. If $(i \\% 3 == 0 \\lor i \\% 5 == 0)$, add $i$ to sum. <strong>Answer = 233,168</strong>.</li>
          <li><strong>Roots of Quadratic Equation $ax^2 + bx + c = 0$:</strong> Calculate discriminant $D = b^2 - 4ac$. If $D &gt; 0$, roots are $\\frac{-b \\pm \\sqrt{D}}{2a}$. If $D == 0$, root is $\\frac{-b}{2a}$. If $D &lt; 0$, roots are imaginary.</li>
          <li><strong>Largest of 3 Numbers ($a, b, c$):</strong> Compare $a &gt; b$. If true, compare $a &gt; c$. If false, compare $b &gt; c$.</li>
          <li><strong>Even or Odd:</strong> Check remainder: <code>if (N % 2 == 0)</code> &rarr; Even, else Odd.</li>
          <li><strong>Quotient and Remainder:</strong> In C, <code>A / B</code> gives integer quotient, and <code>A % B</code> gives remainder.</li>
          <li><strong>Even Numbers between 100 and 200:</strong> Loop $i$ starting at 102 up to 198 with step $+2$.</li>
        </ol>
      </div>
    """,
    "code": {
        "title": "Sum of Digits in C (Slide 43)",
        "desc": "C implementation of the digit extraction and accumulation algorithm.",
        "lang": "c",
        "snippet": """#include <stdio.h>

int main(void) {
    int n = 12345;
    int sum = 0;
    int temp = n;

    while (n != 0) {
        int rem = n % 10;  // Extract rightmost digit
        sum += rem;        // Add to sum
        n = n / 10;        // Chop off rightmost digit
    }

    printf("Sum of digits of %d is: %d\\n", temp, sum);
    return 0;
}""",
        "output": "Sum of digits of 12345 is: 15"
    },
    "resources": [
        {"type": "gfg", "title": "Differences Between Algorithm and Flowchart", "url": "https://www.geeksforgeeks.org/difference-between-algorithm-and-flowchart/", "desc": "Tabular comparison of text vs pictorial problem solving."},
        {"type": "docs", "title": "ISO 5807 Information Processing Documentation Symbols", "url": "https://www.iso.org/standard/11955.html", "desc": "Official international standard for flowchart diagrams and data charts."},
        {"type": "tool", "title": "Draw.io / Diagrams.net Flowchart Builder", "url": "https://app.diagrams.net", "desc": "Interactive diagramming suite for creating ISO standard flowcharts."}
    ],
    "quiz": [
        {
            "id": "q4_1",
            "question": "Which flowchart symbol is used to indicate an Input or Output operation (e.g. reading a value or printing a grade)?",
            "options": [
                "Rectangle",
                "Diamond",
                "Parallelogram",
                "Oval"
            ],
            "answer": 2,
            "explanation": "As specified on Slide 33, a Parallelogram is the standard symbol where there is input to or output from the program."
        },
        {
            "id": "q4_2",
            "question": "Which of the following is a mandatory characteristic of any valid algorithm?",
            "options": [
                "It must be written in the C programming language",
                "It must contain at least 100 lines of code",
                "It must cease execution and terminate after a finite number of steps",
                "It must use a graphical user interface"
            ],
            "answer": 2,
            "explanation": "As stated on Slide 31, an algorithm must have finiteness: 'After a specific period, it must cease to run.' An infinite loop cannot be considered a valid algorithm."
        },
        {
            "id": "q4_3",
            "question": "In the Sum of Digits algorithm (Slide 42), what operations are used to extract the rightmost digit and then discard it?",
            "options": [
                "N / 10 to extract, N * 10 to discard",
                "N % 10 to extract, N / 10 to discard",
                "N + 10 to extract, N - 10 to discard",
                "sqrt(N) to extract, log(N) to discard"
            ],
            "answer": 1,
            "explanation": "Modulo by 10 (N % 10) yields the remainder, which is the rightmost digit. Integer division by 10 (N / 10) truncates the integer, discarding that rightmost digit."
        },
        {
            "id": "q4_4",
            "question": "What is the primary advantage of writing pseudocode before converting an algorithm into C code?",
            "options": [
                "Pseudocode runs directly on the CPU without compilation",
                "Pseudocode is written using control structures closely related to high-level language structures, making translation seamless",
                "Pseudocode automatically detects hardware memory leaks",
                "Pseudocode compiles 10x faster than C"
            ],
            "answer": 1,
            "explanation": "Slide 32 explains: 'Transforming an algorithm presented in pseudocode to programming code could be much easier than converting an algorithm written in natural language.'"
        },
        {
            "id": "q4_5",
            "question": "What does a Diamond (rhombus) shape represent in a flowchart?",
            "options": [
                "A calculation or assignment statement",
                "The beginning or termination of a program",
                "A decision point where a conditional test evaluates to True or False",
                "A comment statement"
            ],
            "answer": 2,
            "explanation": "Slide 33: 'A diamond indicates a point where a decision is made.' It has multiple exit branches (e.g. Yes/No, True/False)."
        }
    ]
})

# Module 5 - SIMPLIFIED GCC COMPILATION WITH CONVEYOR BELT DIAGRAM
modules.append({
    "id": "m5",
    "num": 5,
    "title": "C Program Structure & GCC Compilation Pipeline",
    "subtitle": "The 4-Stage Conveyor Belt: Preprocessor, Compiler, Assembler, Linker",
    "slides": "Slides 46–61",
    "time": "40 mins",
    "content": """
      <div class="teaching-block">
        <h3><i class="fa-solid fa-industry"></i> The Software Factory: The 4 Stages of GCC</h3>
        <p>When you type <code>gcc main.c -o main</code>, your code goes through a <strong>4-station conveyor belt</strong>. Here is the visual pipeline:</p>

        <div class="conveyor-pipeline">
          <div class="conveyor-step">
            <span class="conveyor-tool">Source Code</span>
            <span class="conveyor-name">Your C Code</span>
            <span class="conveyor-ext">.c</span>
          </div>
          <div class="conveyor-arrow"><i class="fa-solid fa-arrow-right"></i></div>

          <div class="conveyor-step">
            <span class="conveyor-tool">1. Preprocessor (cpp)</span>
            <span class="conveyor-name">Text Expander</span>
            <span class="conveyor-ext">.i</span>
          </div>
          <div class="conveyor-arrow"><i class="fa-solid fa-arrow-right"></i></div>

          <div class="conveyor-step">
            <span class="conveyor-tool">2. Compiler (cc1)</span>
            <span class="conveyor-name">Assembly Gen</span>
            <span class="conveyor-ext">.s</span>
          </div>
          <div class="conveyor-arrow"><i class="fa-solid fa-arrow-right"></i></div>

          <div class="conveyor-step">
            <span class="conveyor-tool">3. Assembler (as)</span>
            <span class="conveyor-name">Object Machine Code</span>
            <span class="conveyor-ext">.o</span>
          </div>
          <div class="conveyor-arrow"><i class="fa-solid fa-arrow-right"></i></div>

          <div class="conveyor-step" style="border-color: var(--accent-emerald);">
            <span class="conveyor-tool">4. Linker (ld)</span>
            <span class="conveyor-name">Executable Binary</span>
            <span class="conveyor-ext" style="background: rgba(16, 185, 129, 0.2); color: var(--accent-emerald);">.exe / binary</span>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-wrench"></i> What Each Station Does in Simple Terms</h3>
        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Station</th><th>Tool & GCC Command</th><th>What It Does in Simple Words</th><th>Input &rarr; Output</th></tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1. Preprocessing</strong></td>
                <td><code>gcc -E file.c -o file.i</code></td>
                <td><strong>The Text Editor Assistant:</strong> Erases all comments (<code>/* */</code>), replaces all <code>#define</code> words with their actual values, and copies the entire content of header files (like <code>stdio.h</code>) directly into your file.</td>
                <td><code>.c</code> &rarr; <code>.i</code></td>
              </tr>
              <tr>
                <td><strong>2. Compilation</strong></td>
                <td><code>gcc -S file.i -o file.s</code></td>
                <td><strong>The Blueprint Translator:</strong> Checks grammar/syntax rules and translates the clean C code into human-readable <strong>Assembly Language</strong>.</td>
                <td><code>.i</code> &rarr; <code>.s</code></td>
              </tr>
              <tr>
                <td><strong>3. Assembly</strong></td>
                <td><code>gcc -c file.s -o file.o</code></td>
                <td><strong>The Machine Stamper:</strong> Translates assembly words into actual binary opcodes (0s and 1s) to produce a relocatable <strong>Object File</strong>.</td>
                <td><code>.s</code> &rarr; <code>.o</code></td>
              </tr>
              <tr>
                <td><strong>4. Linking</strong></td>
                <td><code>gcc file.o -o file</code></td>
                <td><strong>The Puzzle Solver:</strong> Merges your object file with precompiled library files (e.g. brings in <code>printf.o</code> from the C runtime library) and creates the final runnable program.</td>
                <td><code>.o</code> &rarr; Executable</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="teacher-callout exam-alert">
          <div class="callout-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
          <div class="callout-body">
            <div class="callout-title">Who Throws What Errors? (Slides 55, 104)</div>
            <p>&bull; <strong>Syntax Errors:</strong> Caught by the <strong>Compiler (cc1)</strong> during stage 2 (e.g. missing semicolons, misspelled keywords).
            <br>&bull; <strong>Linker Errors:</strong> Caught by the <strong>Linker (ld)</strong> during stage 4 (e.g. <code>undefined reference to 'main'</code> or <code>undefined reference to 'sqrt'</code> when a function is called but its body cannot be found!).</p>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-arrows-turn-to-dots"></i> Transpilers: Source-to-Source Compilers (Slide 61)</h3>
        <p>A <strong>Transpiler</strong> takes code written in one high-level language and translates it into another high-level language:</p>
        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Source Language</th><th>Target Language</th><th>Historical Transpiler Name (Slide 61)</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>C++</strong></td><td><strong>C</strong></td><td><strong>CFRONT</strong> (Bjarne Stroustrup's original C++ compiler)</td></tr>
              <tr><td><strong>C#</strong></td><td><strong>JavaScript</strong></td><td><strong>SCRIPTSHARP</strong></td></tr>
              <tr><td><strong>PHP</strong></td><td><strong>C++</strong></td><td><strong>HIPHOP for PHP</strong> (developed by Facebook for speed)</td></tr>
              <tr><td><strong>COBOL</strong></td><td><strong>C</strong></td><td><strong>Open COBOL</strong></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    "code": {
        "title": "Preprocessing Macro & Area of Circle (Slides 49–50)",
        "desc": "Demonstrating preprocessor #define macro replacement and standard formatted I/O.",
        "lang": "c",
        "snippet": """#include <stdio.h>
#define PI 3.14159265
#define GREETING "Welcome to C Compilation Pipeline"

int main(void) {
    float radius = 5.0f;
    float area = PI * radius * radius;

    printf("%s\\n", GREETING);
    printf("Radius: %.2f | Area of Circle: %.4f\\n", radius, area);
    return 0;
}""",
        "output": "Welcome to C Compilation Pipeline\nRadius: 5.00 | Area of Circle: 78.5398"
    },
    "resources": [
        {"type": "tool", "title": "Compiler Explorer (Godbolt)", "url": "https://godbolt.org", "desc": "Inspect interactive GCC assembly generation side-by-side with C code."},
        {"type": "video", "title": "How to Install TDM-GCC on Windows (YouTube)", "url": "https://www.youtube.com/watch?v=BgcygHaX7sA", "desc": "Official video referenced in Slide 47 showing Windows MinGW setup."},
        {"type": "gfg", "title": "Compiling a C Program: Behind the Scenes", "url": "https://www.geeksforgeeks.org/compiling-a-c-program-behind-the-scenes/", "desc": "Detailed breakdown of Preprocessor, Compiler, Assembler, and Linker."},
        {"type": "docs", "title": "Concept of Assembler, Compiler, Interpreter & Linker", "url": "https://www.efaculty.in/c-language/concept-of-assembler-compiler-interpreter-loader-and-linker/", "desc": "Curriculum reference on translation phases."}
    ],
    "quiz": [
        {
            "id": "q5_1",
            "question": "Which GCC command line flag stops execution immediately after the Preprocessing phase and outputs preprocessed C code (.i)?",
            "options": [
                "gcc -S",
                "gcc -c",
                "gcc -E",
                "gcc -O2"
            ],
            "answer": 2,
            "explanation": "As detailed on Slide 52, `gcc -E -o Program1.i Program1.c` runs only the preprocessor, stripping comments and expanding macros/headers into Program1.i."
        },
        {
            "id": "q5_2",
            "question": "What is the output artifact generated by the Assembler stage (as / gcc -c)?",
            "options": [
                "Assembly language text file (.s)",
                "Preprocessed C file (.i)",
                "Relocatable machine language object file (.o)",
                "Finished executable binary (.exe)"
            ],
            "answer": 2,
            "explanation": "Slide 53: The assembler (as) translates assembly language instructions into machine language instructions (binary 0 and 1) and generates an object file Program1.o."
        },
        {
            "id": "q5_3",
            "question": "If your C program calls printf() from <stdio.h>, which software component is responsible for merging the precompiled printf.o object file with your program's object file?",
            "options": [
                "The Preprocessor",
                "The Compiler (cc1)",
                "The Linker (ld)",
                "The Text Editor"
            ],
            "answer": 2,
            "explanation": "Slide 54: The linker (ld) performs the task of linking object files with external resources (system functions, C runtime libraries like printf.o) to produce the final executable."
        },
        {
            "id": "q5_4",
            "question": "According to Slide 61, which historic transpiler was used to convert C++ code into standard C code?",
            "options": [
                "SCRIPTSHARP",
                "HIPHOP",
                "CFRONT",
                "Open COBOL"
            ],
            "answer": 2,
            "explanation": "Slide 61 lists CFRONT as the transpiler with source language C++ and target language C (originally created by Bjarne Stroustrup)."
        },
        {
            "id": "q5_5",
            "question": "What is the role of the OS Loader in the program development cycle?",
            "options": [
                "It translates assembly language into machine code",
                "It copies the executable program from secondary disk storage into primary memory (RAM) and starts execution",
                "It checks syntax errors in source files",
                "It expands #include preprocessor directives"
            ],
            "answer": 1,
            "explanation": "Slide 58 specifies phase 5: 'Loader puts program in memory (RAM). CPU takes each instruction and executes it.'"
        }
    ]
})

# Module 6 - SIMPLIFIED PROCESS MEMORY LAYOUT
modules.append({
    "id": "m6",
    "num": 6,
    "title": "Process Memory Layout in C",
    "subtitle": "The 5-Story Building Analogy: Text, Data, BSS, Heap, Stack & size Command",
    "slides": "Slides 62–69",
    "time": "35 mins",
    "content": """
      <div class="teaching-block">
        <h3><i class="fa-solid fa-building"></i> The 5-Story Building Analogy (Slide 63)</h3>
        <p>When you double-click your compiled C program, the Operating System rents an entire building of RAM addresses for your program to live in:</p>

        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Building Floor</th><th>Memory Segment</th><th>What Lives Here in Plain Words</th><th>Direction</th></tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Top Floor (Penthouse)</strong></td>
                <td><strong>Arguments & Environment</strong></td>
                <td>Stores command line arguments (e.g. <code>argc, argv</code>) and OS environment settings.</td>
                <td>Fixed at Highest Address (~0x7FFF...)</td>
              </tr>
              <tr>
                <td><strong>4th Floor</strong></td>
                <td><strong>Stack Segment</strong></td>
                <td><strong>The Quick Notepad:</strong> Local variables declared inside functions. Fast and automatic! Every time a function is called, a stack frame is created; when the function finishes, everything is automatically tossed in the trash.</td>
                <td><strong>Grows Downward &darr;</strong></td>
              </tr>
              <tr>
                <td><em>Middle Space</em></td>
                <td><em>Unallocated Free RAM</em></td>
                <td>Empty space allowing Stack to grow down and Heap to grow up without crashing into each other.</td>
                <td>-</td>
              </tr>
              <tr>
                <td><strong>3rd Floor</strong></td>
                <td><strong>Heap Segment</strong></td>
                <td><strong>The Rental Storage Unit:</strong> Memory requested manually by you at runtime using <code>malloc()</code>. You are responsible for releasing it with <code>free()</code>!</td>
                <td><strong>Grows Upward &uarr;</strong></td>
              </tr>
              <tr>
                <td><strong>2nd Floor</strong></td>
                <td><strong>Uninitialized Data (.bss)</strong></td>
                <td>Global variables with no starting value (e.g. <code>int a;</code>). Automatically initialized to <strong>0</strong> by the OS kernel. Takes ZERO space in your disk file!</td>
                <td>Fixed</td>
              </tr>
              <tr>
                <td><strong>1st Floor</strong></td>
                <td><strong>Initialized Data (.data)</strong></td>
                <td>Global variables with starting values (e.g. <code>int count = 10;</code>) and text string literals.</td>
                <td>Fixed</td>
              </tr>
              <tr>
                <td><strong>Ground Floor / Bedrock</strong></td>
                <td><strong>Text Segment (Code)</strong></td>
                <td>The pure machine code instructions executed by the CPU. Marked <strong>Read-Only</strong> so a buggy program cannot accidentally overwrite its own code!</td>
                <td>Fixed at Lowest Address (~0x0040...)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-terminal"></i> The 'size' Command Experiment (Slides 68–69)</h3>
        <div class="teacher-callout under-hood">
          <div class="callout-icon"><i class="fa-solid fa-microscope"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Classroom Demonstration</div>
            <p>Slide 68 shows a program with no globals: <code>size Memory.exe</code> &rarr; <strong>bss = 96</strong>.
            <br>Slide 69 adds one global: <code>int a;</code> outside <code>main()</code>.
            <br>Run again: <code>size Memory.exe</code> &rarr; <strong>bss = 100</strong>!
            <br>Notice: <code>bss</code> increased by exactly <strong>4 bytes</strong> (the size of 1 integer)! Neither <code>text</code> nor <code>data</code> changed!</p>
          </div>
        </div>
      </div>
    """,
    "code": {
        "title": "Verifying Memory Segment Addresses in C",
        "desc": "Printing runtime memory addresses to prove how Text, BSS, Data, Heap, and Stack are positioned.",
        "lang": "c",
        "snippet": """#include <stdio.h>
#include <stdlib.h>

int global_initialized = 42;      // .data segment
int global_uninitialized;          // .bss segment

void demo_code(void) {}            // .text segment

int main(void) {
    static int static_initialized = 100; // .data segment
    static int static_uninitialized;     // .bss segment
    int stack_variable = 10;             // Stack segment
    int *heap_pointer = (int*)malloc(sizeof(int)); // Heap segment

    printf("=== Memory Layout Addresses ===\\n");
    printf("1. Text (Code)      : %p\\n", (void*)&demo_code);
    printf("2. Initialized Data : %p\\n", (void*)&global_initialized);
    printf("3. BSS (Uninit Data): %p\\n", (void*)&global_uninitialized);
    printf("4. Heap (Dynamic)   : %p\\n", (void*)heap_pointer);
    printf("5. Stack (Local)    : %p\\n", (void*)&stack_variable);

    free(heap_pointer);
    return 0;
}""",
        "output": "1. Text (Code)      : 0x55b1c2... (Lowest)\n2. Initialized Data : 0x55b1c4...\n3. BSS (Uninit Data): 0x55b1c4...\n4. Heap (Dynamic)   : 0x55b1d8...\n5. Stack (Local)    : 0x7fffef... (Highest)"
    },
    "resources": [
        {"type": "gfg", "title": "Memory Layout of C Programs", "url": "https://www.geeksforgeeks.org/memory-layout-of-c-program/", "desc": "Curriculum link referenced in Slide 67 detailing BSS, Data, Heap, and Stack."},
        {"type": "gfg", "title": "Static Variables in C", "url": "https://www.geeksforgeeks.org/static-variables-in-c/", "desc": "Curriculum link referenced in Slide 67 explaining scope and lifetime of statics."},
        {"type": "tool", "title": "Python Tutor (C Memory Visualizer)", "url": "https://pythontutor.com/c.html", "desc": "Interactive diagramming of C stack frames, pointers, and heap blocks."}
    ],
    "quiz": [
        {
            "id": "q6_1",
            "question": "In which memory segment is an uninitialized global variable (e.g. 'int a;') stored?",
            "options": [
                "Stack segment",
                "Text segment",
                "Uninitialized Data segment (.bss)",
                "Heap segment"
            ],
            "answer": 2,
            "explanation": "Slide 65: Uninitialized global and static variables are stored in the uninitialized data segment, historically called the 'bss' (Block Started by Symbol) segment, initialized to 0 by the OS kernel."
        },
        {
            "id": "q6_2",
            "question": "What happens in memory when an uninitialized global variable 'int a;' is added to a 32-bit C program, as demonstrated on Slides 68–69?",
            "options": [
                "The text segment size increases by 4 bytes",
                "The data segment size increases by 4 bytes",
                "The bss segment size increases by 4 bytes (from 96 to 100)",
                "The heap segment size doubles"
            ],
            "answer": 2,
            "explanation": "Slides 68–69 demonstrate with the `size` command that adding `int a;` increases only the `bss` column by exactly 4 bytes (96 bytes to 100 bytes)."
        },
        {
            "id": "q6_3",
            "question": "Why is the Text segment marked as Read-Only in modern operating systems?",
            "options": [
                "To save electrical power",
                "To prevent running programs from accidentally or maliciously modifying their own instructions",
                "Because hard drives cannot write back to ROM",
                "Because machine code consists only of 0s"
            ],
            "answer": 1,
            "explanation": "Slide 64: 'The text segment is often read-only, to prevent a program from accidentally modifying its instructions.'"
        },
        {
            "id": "q6_4",
            "question": "Which of the following statements about the Stack segment is FALSE?",
            "options": [
                "Variables created on the stack are automatically deallocated when they go out of scope",
                "Stack allocation is much faster than heap allocation",
                "The stack grows upward towards higher memory addresses",
                "Infinite recursion can cause a stack overflow"
            ],
            "answer": 2,
            "explanation": "Slide 63 & 65 show that the Stack grows DOWNWARD towards lower memory addresses (towards the Heap), while the Heap grows upward."
        },
        {
            "id": "q6_5",
            "question": "When should dynamically allocated memory on the Heap be used instead of the Stack?",
            "options": [
                "When we need ultra-fast allocation for small integers",
                "When the exact amount of data needed is unknown at compile time and must be allocated on demand at runtime",
                "When declaring local function parameters",
                "When writing the main() function definition"
            ],
            "answer": 1,
            "explanation": "Slide 67 states: 'We use the heap if we don't know exactly how much data we will need at run time.'"
        }
    ]
})

with open("modules_4_6.json", "w", encoding="utf-8") as f:
    json.dump(modules, f, indent=2)
print("Updated modules_4_6.json with simplified pseudocode, rendered flowcharts, and trace tables!")
