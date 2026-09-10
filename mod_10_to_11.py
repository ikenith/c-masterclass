import json

modules = []

# Module 10
modules.append({
    "id": "m10",
    "num": 10,
    "title": "Decision Control: If-Else & Switch-Case Mastery",
    "subtitle": "The Crossroads: Branching, Jump Tables, Unreachable Switch Trap & Strict Case Rules",
    "slides": "Slides 134–146",
    "time": "40 mins",
    "content": r"""
      <div class="teaching-block">
        <h3><i class="fa-solid fa-code-fork"></i> Decision Making: The Fork in the Road (Slides 134–141)</h3>
        <p class="lead-text">
          By default, computers execute code sequentially, one line after another.
          <strong>Decision control statements</strong> act as forks in the road, inspecting conditions and routing execution down different paths.
        </p>

        <div class="teacher-callout analogy">
          <div class="callout-icon"><i class="fa-solid fa-traffic-light"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Truthy vs Falsy Rule in C (Slide 138)</div>
            <p>Unlike languages that require a strict <code>true</code> or <code>false</code> boolean keyword, C evaluates every integer expression natively:
            <br>&bull; <strong>Zero (<code>0</code>)</strong> is <strong>FALSE</strong>.
            <br>&bull; <strong>ANY non-zero value</strong> (positive, negative like <code>-1</code>, or fractional like <code>3.14</code>) is <strong>TRUE</strong>!
            <br>Exam favorite from Slide 138: <code>if (-1) printf("Hello");</code> &rarr; Prints <code>"Hello"</code> because <code>-1</code> is non-zero, hence TRUE!</p>
          </div>
        </div>

        <div class="comparison-card">
          <div class="comparison-header">
            <span><i class="fa-solid fa-diagram-project"></i> The If Family Tree</span>
            <span class="badge">Control Patterns</span>
          </div>
          <div class="comparison-grid">
            <div class="comparison-col">
              <h4>Simple if</h4>
              <p>One-way branch: executes the block only if true; otherwise skips past it.</p>
              <code>if (score &gt;= 50) { pass(); }</code>
            </div>
            <div class="comparison-col">
              <h4>if ... else</h4>
              <p>Two-way fork: executes block A if true, or block B if false. Exactly one executes.</p>
              <code>if (x % 2 == 0) even(); else odd();</code>
            </div>
            <div class="comparison-col">
              <h4>if-else-if Ladder</h4>
              <p>Multi-way sequential tests: tests conditions top-to-bottom until the first match.</p>
              <code>if (m &gt; 90) 'A'; else if (m &gt; 80) 'B'; else 'C';</code>
            </div>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-toggle-on"></i> The Switch-Case Statement & The Jump Table (Slides 142–146)</h3>
        <p>The <code>switch</code> statement tests an expression against a series of constant case labels. Why do systems programmers use it instead of a long <code>if-else-if</code> ladder?</p>

        <div class="teacher-callout analogy">
          <div class="callout-icon"><i class="fa-solid fa-elevator"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Hallway vs. Express Elevator Analogy (Slide 143)</div>
            <p>
              &bull; <strong><code>if-else-if</code> Ladder:</strong> Walking down a long hotel hallway and knocking on Room 1, then Room 2, then Room 3, until you find your room ($O(N)$ sequential search).<br>
              &bull; <strong><code>switch</code> Statement:</strong> An <strong>Express Elevator with a Jump Table</strong>! The C compiler synthesizes an array of code memory addresses indexed by the switch value. The CPU jumps directly to the target case in <strong>$O(1)$ constant time</strong>, regardless of whether there are 3 cases or 300 cases!
            </p>
          </div>
        </div>

        <h4>The 5 Golden Rules of C Switch Statements (Slides 144–146)</h4>
        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>#</th><th>Rule (Slides 144–146)</th><th>Valid Example</th><th>Invalid Example (Compiler Rejection!)</th></tr>
            </thead>
            <tbody>
              <tr>
                <td>1</td>
                <td><strong>Integral Expressions Only:</strong> Switch expression must evaluate to an integer type (<code>int</code>, <code>char</code>, <code>enum</code>). Floats and doubles are strictly forbidden! (You cannot press button 3.14 in an elevator!).</td>
                <td><code>switch(choice)</code> where <code>choice</code> is <code>int</code> or <code>char</code></td>
                <td><code>float x = 2.5; switch(x)</code> &rarr; <em>Error: switch quantity not an integer</em></td>
              </tr>
              <tr>
                <td>2</td>
                <td><strong>Constant Case Labels:</strong> Each case label must be a compile-time constant integer expression. Variables are strictly illegal!</td>
                <td><code>case 1:</code> or <code>case 'A':</code> or <code>case 2 + 3:</code></td>
                <td><code>int k = 5; switch(x) { case k: ... }</code> &rarr; <em>Error: case label does not reduce to an integer constant</em></td>
              </tr>
              <tr>
                <td>3</td>
                <td><strong>Unique Case Labels:</strong> Two case labels cannot have identical values.</td>
                <td><code>case 1: ... case 2:</code></td>
                <td><code>case 2: ... case 1 + 1:</code> &rarr; <em>Error: duplicate case value '2'</em></td>
              </tr>
              <tr>
                <td>4</td>
                <td><strong>The Unreachable Code Trap:</strong> Any code written inside the switch block <em>before</em> the very first <code>case</code> label will <strong>never execute</strong>! The jump table bypasses it entirely!</td>
                <td>Place statements inside the case labels.</td>
                <td><code>switch(x) { printf("Hi"); case 1: ... }</code> &rarr; <code>printf("Hi")</code> is permanently skipped! (Slide 146)</td>
              </tr>
              <tr>
                <td>5</td>
                <td><strong>Fallthrough & break:</strong> If you omit <code>break;</code>, execution does not stop; it falls through and runs every subsequent case regardless of label!</td>
                <td>Always end each case with <code>break;</code> unless intentional fallthrough is desired.</td>
                <td>Missing break cascades execution into subsequent cases.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    "code": {
        "title": "Switch Unreachable Code & Fallthrough Mechanics (Slides 145–146)",
        "desc": "Demonstrating how statements placed before the first case are skipped, and intentional break termination.",
        "lang": "c",
        "snippet": """#include <stdio.h>

int main(void) {
    int choice = 1;

    switch (choice) {
        printf("I am unreachable and never execute!\\n"); // SLIDE 146 TRAP!

        case 1:
            printf("Choice is 1\\n");
            break;
        case 2:
            printf("Choice is 2\\n");
            break;
        default:
            printf("Default choice\\n");
            break;
    }

    // Truthy test with negative number (Slide 138)
    if (-1) {
        printf("In C, -1 is non-zero, hence TRUE!\\n");
    }

    return 0;
}""",
        "output": "Choice is 1\nIn C, -1 is non-zero, hence TRUE!"
    },
    "resources": [
        {"type": "gfg", "title": "Switch Statement in C", "url": "https://www.geeksforgeeks.org/switch-statement-in-c/", "desc": "GeeksforGeeks detailed guide on switch-case rules and jump table mechanics."},
        {"type": "docs", "title": "Compiler Explorer: Jump Table Disassembly", "url": "https://godbolt.org", "desc": "Write a dense switch case and view the emitted assembly jump table (jmp *%rax)."}
    ],
    "quiz": [
        {
            "id": "q10_1",
            "question": "Which of the following data types CANNOT be used as the controlling expression in a C switch statement (Slide 144)?",
            "options": [
                "int",
                "char",
                "float",
                "enum"
            ],
            "answer": 2,
            "explanation": "Slide 144: 'The expression used in switch must be integral type (int, char and enum). Any other type of expression (such as float or double) is not allowed.'"
        },
        {
            "id": "q10_2",
            "question": "What happens to statements placed inside a switch block BEFORE the very first case label (Slide 146)?",
            "options": [
                "They execute before every case",
                "They are never executed and are completely bypassed during jump table dispatch",
                "They cause a fatal compiler syntax error",
                "They execute only if the default case triggers"
            ],
            "answer": 1,
            "explanation": "Slide 146: 'The statements written above cases are never executed.' The switch jumps directly to the matching case label or default, skipping any preamble code."
        },
        {
            "id": "q10_3",
            "question": "What occurs if you omit the 'break;' statement at the end of a matching case block (Slide 145)?",
            "options": [
                "The program crashes with a segmentation fault",
                "The compiler flags a syntax error",
                "Execution falls through and sequentially executes statements in subsequent cases until a break or switch end is reached",
                "The loop restarts from the beginning"
            ],
            "answer": 2,
            "explanation": "Slide 145: 'All the statements following a matching case execute until a break statement is reached.' This cascading behavior is known as fallthrough."
        },
        {
            "id": "q10_4",
            "question": "Why is a switch statement often significantly faster in execution than an equivalent if-else-if ladder with many conditions (Slide 143)?",
            "options": [
                "Because switch statements run in kernel mode",
                "Because compilers optimize dense switches into a Jump Table yielding O(1) constant-time dispatch, avoiding sequential condition checks",
                "Because switch statements bypass CPU registers",
                "Because switch statements use multithreading"
            ],
            "answer": 1,
            "explanation": "Slide 143 notes that switch allows best-optimized implementation for faster code execution through jump tables with a fixed depth, unlike linear evaluation in if-else-if."
        },
        {
            "id": "q10_5",
            "question": "Given: 'int i = 10; switch(x) { case i: printf(\"Hi\"); }'. Why will GCC reject this code?",
            "options": [
                "Because printf cannot be called in a case",
                "Because case labels must be compile-time integer constants, and variable 'i' is not a constant expression",
                "Because switch cannot contain only one case",
                "Because curly braces are not allowed inside switch"
            ],
            "answer": 1,
            "explanation": "Slide 144: 'In C switch statement, the expression of each case label must be an integer constant expression.' A variable like `i` is not a constant expression."
        }
    ]
})

# Module 11
modules.append({
    "id": "m11",
    "num": 11,
    "title": "Iteration: Loops & Advanced I/O Quirks",
    "subtitle": "The Loops: While, For, Do-While, Continue Traps, and Return Values of printf & scanf",
    "slides": "Slides 147–162",
    "time": "45 mins",
    "content": r"""
      <div class="teaching-block">
        <h3><i class="fa-solid fa-repeat"></i> The Three Loops: Repetition Without Redundancy (Slides 147–154)</h3>
        <p class="lead-text">
          Loops allow running a block of statements repeatedly until a specified termination condition becomes False.
          C provides three primary loop constructs:
        </p>

        <div class="comparison-card">
          <div class="comparison-header">
            <span><i class="fa-solid fa-arrows-spin"></i> The Three C Loop Constructs</span>
            <span class="badge">Execution Comparison</span>
          </div>
          <div class="comparison-grid">
            <div class="comparison-col">
              <h4>while Loop</h4>
              <p><strong>"The Nightclub Bouncer"</strong></p>
              <p><strong>Entry-Controlled:</strong> Tests the condition <em>before</em> entering the loop.</p>
              <p>If the condition is initially False, the body executes <strong>0 times</strong>!</p>
              <code>while (count &lt; 5) { count++; }</code>
            </div>
            <div class="comparison-col">
              <h4>for Loop</h4>
              <p><strong>"The Lap Counter"</strong></p>
              <p><strong>Entry-Controlled:</strong> Compact syntax packing initialization, condition, and update in one line with 2 semicolons.</p>
              <p>Ideal when the number of iterations is known in advance.</p>
              <code>for (int i=0; i&lt;5; i++) { ... }</code>
            </div>
            <div class="comparison-col">
              <h4>do-while Loop</h4>
              <p><strong>"The Rollercoaster Ride"</strong></p>
              <p><strong>Exit-Controlled:</strong> You get to ride once first; ticket is checked at the exit!</p>
              <p>Guaranteed to execute <strong>at least once</strong>! Must end with a semicolon <code>;</code>!</p>
              <code>do { work(); } while (more);</code>
            </div>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-infinity"></i> Infinite Loops & The continue Trap (Slides 155–159)</h3>
        <p>An <strong>Infinite Loop</strong> runs forever because its condition never evaluates to False:</p>
        <ul>
          <li><code>for ( ; ; ) { /* infinite loop */ }</code></li>
          <li><code>while (1) { /* infinite loop */ }</code></li>
        </ul>

        <h4>Loop Control Statements (Slide 158)</h4>
        <ul>
          <li><strong><code>break</code>:</strong> Instantly breaks out of the loop and jumps to the code following the loop.</li>
          <li><strong><code>continue</code>:</strong> Skips the rest of the current iteration and jumps directly to the next iteration.</li>
        </ul>

        <div class="teacher-callout pitfall">
          <div class="callout-icon"><i class="fa-solid fa-bomb"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Sneaky continue Trap in while vs. for</div>
            <p>
              &bull; In a <strong><code>for</code> loop</strong>: <code>continue</code> jumps to the <strong>update step</strong> (<code>i++</code>) before checking the condition. The counter increments safely.<br>
              &bull; In a <strong><code>while</code> loop</strong>: <code>continue</code> jumps directly to the <strong>condition check</strong>! If your counter update (<code>i++</code>) was located at the bottom of the loop body, it is completely skipped, trapping your program in an <strong>accidental infinite loop</strong>!
            </p>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-receipt"></i> High-Yield Exam Topic: Return Values of printf() & scanf() (Slides 160–162)</h3>
        <p>Both <code>printf()</code> and <code>scanf()</code> are functions that return valuable status information. Think of their return values as <strong>store receipts</strong>!</p>

        <div class="comparison-card">
          <div class="comparison-header">
            <span><i class="fa-solid fa-file-invoice"></i> The Store Receipt Analogy for I/O Functions</span>
            <span class="badge">Return Value Rules</span>
          </div>
          <div class="comparison-grid">
            <div class="comparison-col">
              <h4>Function</h4>
              <p><strong>printf(...)</strong></p>
              <br>
              <p><strong>scanf(...)</strong></p>
            </div>
            <div class="comparison-col">
              <h4>What It Returns (Slide 160)</h4>
              <p>Returns the total number of <strong>characters successfully printed</strong> to the screen.</p>
              <p>Returns the total number of <strong>input items successfully matched and assigned</strong> into memory variables.</p>
            </div>
            <div class="comparison-col">
              <h4>Classic Exam Code Trace</h4>
              <p>
                <code>printf(" %d", printf("geeksforgeeks"));</code><br>
                1. Inner <code>printf("geeksforgeeks")</code> prints 13 characters and returns <strong>13</strong>.<br>
                2. Outer <code>printf</code> prints <code>" 13"</code>.<br>
                <strong>Screen Output: <code>geeksforgeeks 13</code></strong>!
              </p>
              <p>
                <code>char a[50]; printf(" %d", scanf("%s", a));</code><br>
                Regardless of the word entered (e.g. "Computer"), exactly 1 item was assigned, so <code>scanf</code> returns <strong>1</strong> (Slide 161).
              </p>
            </div>
          </div>
        </div>

        <div class="teacher-callout insight">
          <div class="callout-icon"><i class="fa-solid fa-keyboard"></i></div>
          <div class="callout-body">
            <div class="callout-title">Reading Strings with Spaces using Scansets (Slide 162)</div>
            <p>Normal <code>scanf("%s", str);</code> terminates at the first whitespace character (space, tab, or newline).
            <br>To read an entire line including spaces, use a <strong>Scanset</strong>:
            <br><code>scanf("%[^\\n]s", str);</code>
            <br>The <code>^\\n</code> tells <code>scanf</code>: <em>"Accept and read every character until you encounter a newline!"</em></p>
          </div>
        </div>
      </div>
    """,
    "code": {
        "title": "Return Values of printf() and scanf() in C (Slides 160–161)",
        "desc": "Demonstrating nested printf character counts, empty printf return, and do-while guaranteed execution.",
        "lang": "c",
        "snippet": """#include <stdio.h>

int main(void) {
    // 1. Nested printf return value (Slide 160)
    // Inner prints "geeksforgeeks" (13 chars) and returns 13
    // Outer prints " 13"
    printf(" %d\\n", printf("geeksforgeeks"));

    // 2. Empty printf returns 0 characters
    printf("Empty printf returned: %d\\n", printf(""));

    // 3. do-while loop executing at least once (Slide 153-154)
    int i = 2;
    do {
        printf("do-while body executed with i = %d\\n", i);
        i++;
    } while (i < 1); // condition false initially, but executed once!

    return 0;
}""",
        "output": "geeksforgeeks 13\nEmpty printf returned: 0\ndo-while body executed with i = 2"
    },
    "resources": [
        {"type": "gfg", "title": "Scansets in C", "url": "https://www.geeksforgeeks.org/scansets-in-c/", "desc": "Curriculum link from Slide 162 on using %[^\\n]s to read spaces."},
        {"type": "gfg", "title": "Taking String Input with Spaces in C", "url": "https://www.geeksforgeeks.org/taking-string-input-space-c-3-different-methods/", "desc": "Curriculum link comparing scanf scansets, fgets, and gets."},
        {"type": "docs", "title": "TutorialsPoint: C continue Statement", "url": "https://www.tutorialspoint.com/cprogramming/c_continue_statement.htm", "desc": "Curriculum link referenced in Slide 159 on loop control."}
    ],
    "quiz": [
        {
            "id": "q11_1",
            "question": "What is printed on the screen by executing: 'printf(\" %d\", printf(\"geeksforgeeks\"));' (Slide 160)?",
            "options": [
                "13 geeksforgeeks",
                "geeksforgeeks 13",
                "geeksforgeeks",
                "13 13"
            ],
            "answer": 1,
            "explanation": "The inner printf(\"geeksforgeeks\") prints 'geeksforgeeks' (13 characters long) and returns 13. The outer printf prints ' 13'. Combined output: 'geeksforgeeks 13' (Slide 160)."
        },
        {
            "id": "q11_2",
            "question": "Which loop construct is guaranteed to execute its body at least once, even if its condition is False from the start (Slide 153)?",
            "options": [
                "for loop",
                "while loop",
                "do-while loop",
                "nested loop"
            ],
            "answer": 2,
            "explanation": "Slide 153: 'In a do-while loop, the loop body will execute at least once irrespective of the test condition' because the condition is evaluated at the end of the loop."
        },
        {
            "id": "q11_3",
            "question": "What does scanf() return when successfully reading user input into variables (Slide 160–161)?",
            "options": [
                "The total number of characters entered",
                "The number of input items successfully matched and assigned",
                "Always 0",
                "The memory address of the first variable"
            ],
            "answer": 1,
            "explanation": "Slide 160 explicitly specifies: 'scanf() returns number of items successfully read.' For example, `scanf(\"%s\", a)` returns 1."
        },
        {
            "id": "q11_4",
            "question": "How can scanf() be formatted to read an entire line of text including spaces until the Enter key is pressed (Slide 162)?",
            "options": [
                "scanf(\"%s\", str);",
                "scanf(\"%[^\\n]s\", str);",
                "scanf(\"%line\", str);",
                "scanf(\"%c*\", str);"
            ],
            "answer": 1,
            "explanation": "Slide 162: Using the scanset `scanf(\"%[^\\n]s\", str);` tells scanf to read all characters until the newline character is encountered, thus preserving spaces."
        },
        {
            "id": "q11_5",
            "question": "What is the critical syntax requirement at the end of a do-while loop statement?",
            "options": [
                "A colon (:)",
                "A semicolon (;)",
                "A double bracket (]])",
                "No punctuation is permitted"
            ],
            "answer": 1,
            "explanation": "Slide 153 highlights: 'Note: Notice the semi-colon (\";\") in the end of loop.' Example: `do { ... } while (condition);`."
        },
        {
            "id": "q11_6",
            "question": "What is the key difference in behavior when 'continue' is executed inside a 'for' loop versus a 'while' loop?",
            "options": [
                "In 'for', continue terminates the program; in 'while', it restarts the system",
                "In 'for', continue jumps to the update expression (e.g. i++); in 'while', it jumps directly to the condition check",
                "There is no difference in behavior",
                "continue cannot be used inside a while loop"
            ],
            "answer": 1,
            "explanation": "In a `for` loop, `continue` jumps to the loop's update step (e.g. `i++`). In a `while` loop, it jumps straight to evaluating the condition, which can cause an infinite loop if the counter update was at the end of the loop body."
        }
    ]
})

with open("/home/hinazu/.gemini/antigravity/scratch/c-unit1-course/modules_10_11.json", "w", encoding="utf-8") as f:
    json.dump(modules, f, indent=2)
print("Modules 10 and 11 written to modules_10_11.json successfully!")
