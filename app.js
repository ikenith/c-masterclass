/**
 * C Programming Masterclass: Unit 1 — Application Engine
 * Curated from Unit 1: Overview of Computer Organization & Programming Fundamentals
 * Author: Prof. Uday Kumar M Courseware
 */

// Global Course Curriculum Dataset
const COURSE_MODULES = [
  {
    "id": "m1",
    "num": 1,
    "title": "Genesis of Computing, Architecture & C",
    "subtitle": "Computer Organization, 5 Generations of Languages, Dennis Ritchie & Standards",
    "slides": "Slides 1\u20137, 15, 25",
    "time": "25 mins",
    "content": "\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-chalkboard-user\"></i> Professor's Welcome: What is a Computer System?</h3>\n        <p>Hello and welcome! Think of a computer not as a magic black box, but as an <strong>orchestra of interconnected parts</strong> working together:</p>\n        \n        <div class=\"teacher-callout insight\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-lightbulb\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The Master Philosophy of C</div>\n            <p>Dennis Ritchie created C in 1972 at Bell Labs to write the <strong>UNIX operating system</strong>. Most languages hide how the computer works; C gives you direct control over CPU memory addresses, individual bits, and raw hardware speed. That's why Windows, Linux, macOS, iOS, Android, and car engine controllers are still powered by C today!</p>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-sitemap\"></i> The 4 Layers: How You Talk to the Silicon (Slide 25)</h3>\n        <p>Whenever you tap an app on your phone or computer, instructions pass through four distinct layers:</p>\n        \n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Layer</th><th>Simple Real-World Role</th><th>Examples</th></tr>\n            </thead>\n            <tbody>\n              <tr>\n                <td><strong>1. User</strong></td>\n                <td>The human being directing the action.</td>\n                <td>You, a gamer, a software developer.</td>\n              </tr>\n              <tr>\n                <td><strong>2. Application Software</strong></td>\n                <td>The tool designed to do a specific job for the user.</td>\n                <td>Chrome browser, WhatsApp, VS Code, VLC player.</td>\n              </tr>\n              <tr>\n                <td><strong>3. Operating System (OS)</strong></td>\n                <td>The <strong>Master Manager</strong>. It translates what the app wants into commands the physical hardware understands, while managing memory and security.</td>\n                <td>Linux, Windows 11, macOS, Android, UNIX.</td>\n              </tr>\n              <tr>\n                <td><strong>4. Hardware</strong></td>\n                <td>The physical electronics and chips that execute electric pulses.</td>\n                <td>CPU (Processor), RAM (Memory), Motherboard, SSD/HDD.</td>\n              </tr>\n            </tbody>\n          </table>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-clock-rotate-left\"></i> The Five Generations of Programming Languages</h3>\n        <p>How did programming evolve from tedious electric wiring to human-readable code?</p>\n        <ul>\n          <li><strong>1GL (Machine Language):</strong> Pure binary (<code>01010011</code>). Only the CPU understands it directly. Painful for humans to read or write!</li>\n          <li><strong>2GL (Assembly Language):</strong> Short human codes called <em>mnemonics</em> (e.g., <code>ADD</code>, <code>MOV</code>). Requires an <strong>Assembler</strong> to convert into machine code. Still tied to a specific processor model.</li>\n          <li><strong>3GL (High-Level Procedural Languages):</strong> Readable, English-like code using math expressions. <strong>C, FORTRAN, Pascal, BASIC</strong> belong here. Programs can run on any computer once compiled!</li>\n          <li><strong>4GL (Declarative Languages):</strong> Tell the computer <em>what</em> you want, not <em>how</em> to calculate it (e.g. <strong>SQL</strong> database queries: <code>SELECT * FROM Students</code>).</li>\n          <li><strong>5GL (AI & Constraint Languages):</strong> Problem-solving through rules and neural logic (e.g. Prolog, Mercury, modern AI systems).</li>\n        </ul>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-timeline\"></i> The Evolution of C Standards</h3>\n        <p>Over the decades, international committees created official standards so C programs run consistently everywhere:</p>\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Standard</th><th>Year</th><th>Why It Matters to You</th></tr>\n            </thead>\n            <tbody>\n              <tr><td><strong>K&R C</strong></td><td>1978</td><td>The original book by Brian Kernighan & Dennis Ritchie. Set the de-facto baseline.</td></tr>\n              <tr><td><strong>ANSI C (C89)</strong></td><td>1989</td><td>The first official ANSI standard. Introduced function prototypes and standard library headers (<code>stdio.h</code>).</td></tr>\n              <tr><td><strong>ISO C (C90)</strong></td><td>1990</td><td>The international ISO edition of C89. <strong>C89 and C90 are identical!</strong></td></tr>\n              <tr><td><strong>C99</strong></td><td>1999</td><td>Modernized C: added <code>//</code> single-line comments, <code>long long int</code>, <code>stdbool.h</code>, and <code>__func__</code>.</td></tr>\n              <tr><td><strong>C11</strong></td><td>2011</td><td>Added built-in multithreading (<code>threads.h</code>) and atomic memory operations.</td></tr>\n              <tr><td><strong>C17 / C18</strong></td><td>2018</td><td>Defect corrections and clarifications (the standard used in modern university courses).</td></tr>\n            </tbody>\n          </table>\n        </div>\n      </div>\n    ",
    "code": {
      "title": "The Historic First C Program",
      "desc": "The canonical 'Hello, World!' program written by Dennis Ritchie and Brian Kernighan.",
      "lang": "c",
      "snippet": "#include <stdio.h>\n\n/* Written by Dennis Ritchie at Bell Labs (1972)\n   The canonical entry point for all C software */\nint main(void) {\n    printf(\"Hello, World!\\n\");\n    return 0;\n}",
      "output": "Hello, World!"
    },
    "resources": [
      {
        "type": "gfg",
        "title": "Introduction to Programming Languages",
        "url": "https://www.geeksforgeeks.org/introduction-to-programming-languages/",
        "desc": "GeeksforGeeks overview of programming paradigms and abstraction levels."
      },
      {
        "type": "gfg",
        "title": "The Evolution of Programming Languages",
        "url": "https://www.geeksforgeeks.org/the-evolution-of-programming-languages/",
        "desc": "Chronological history from machine code to modern compiled systems."
      },
      {
        "type": "docs",
        "title": "ISO/IEC 9899 C Standard Working Group",
        "url": "https://www.open-std.org/jtc1/sc22/wg14/",
        "desc": "The official international committee governing the C programming language specification."
      }
    ],
    "quiz": [
      {
        "id": "q1_1",
        "question": "In what year and at which laboratory was the C programming language originally created by Dennis Ritchie?",
        "options": [
          "1985 at Microsoft Research",
          "1972 at AT&T Bell Laboratories",
          "1969 at Xerox PARC",
          "1991 at CERN"
        ],
        "answer": 1,
        "explanation": "Dennis Ritchie developed C in 1972 at AT&T's Bell Laboratories in the USA primarily to build the UNIX operating system."
      },
      {
        "id": "q1_2",
        "question": "Which statement correctly distinguishes ANSI C (C89) and ISO C (C90)?",
        "options": [
          "C90 introduced object-oriented programming while C89 was strictly procedural",
          "C89 is 16-bit only, while C90 is 32-bit only",
          "They refer to the exact same language; ISO adopted ANSI C in 1990 with formatting changes",
          "C89 was developed for Linux, whereas C90 was created for Microsoft Windows"
        ],
        "answer": 2,
        "explanation": "In 1989, ANSI established standard X3.159-1989 (C89). In 1990, ISO adopted it as ISO/IEC 9899:1990 (C90). Hence, C89 and C90 denote the exact same language standard."
      },
      {
        "id": "q1_3",
        "question": "Which generation of programming languages does C belong to?",
        "options": [
          "1GL (First Generation)",
          "2GL (Second Generation)",
          "3GL (Third Generation)",
          "4GL (Fourth Generation)"
        ],
        "answer": 2,
        "explanation": "C is a 3GL (Third Generation High-Level Procedural Language). 1GL is raw binary machine code, 2GL is assembly mnemonics, and 4GL includes declarative query languages like SQL."
      },
      {
        "id": "q1_4",
        "question": "Why is C predominantly chosen for writing device drivers and operating system kernels?",
        "options": [
          "Because C automatically manages memory through garbage collection",
          "Because C provides direct access to CPU memory addresses via pointers and allows bit-level manipulation with near-zero overhead",
          "Because C code does not require a compiler to run",
          "Because C is an interpreted scripting language"
        ],
        "answer": 1,
        "explanation": "As noted on Slide 5 of the curriculum, device drivers are written in C because it provides direct access to hardware memory via pointers, allows manipulation of individual bits and bytes, and delivers unmatched execution speed."
      },
      {
        "id": "q1_5",
        "question": "According to the system architecture hierarchy, which component acts as the direct intermediary bridge between user applications and the raw hardware?",
        "options": [
          "The Web Browser",
          "The Operating System",
          "The Compiler",
          "The Assembler"
        ],
        "answer": 1,
        "explanation": "As illustrated on Slide 25: User -> Application Software -> Operating System -> Hardware. The OS acts as the vital software interface abstracting physical hardware for end-user applications."
      }
    ]
  },
  {
    "id": "m2",
    "num": 2,
    "title": "Number Systems & Architecture Mathematics",
    "subtitle": "Binary, Octal, Hexadecimal, 3-bit/4-bit Grouping, 32-bit vs 64-bit & CPU Cycles",
    "slides": "Slides 8\u201314, 24, 26\u201330",
    "time": "35 mins",
    "content": "\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-lightbulb\"></i> The Light Switch Secret: Why Computers Use Binary</h3>\n        <p>Imagine a light switch on the wall. It can only be in one of two states: <strong>OFF (0)</strong> or <strong>ON (1)</strong>. That's a <strong>Bit</strong> (binary digit)!</p>\n        <p>A computer doesn't know letters, colors, or decimal numbers. Inside, it has billions of microscopic switches (transistors). By combining switches together, we can represent numbers, text, and music:</p>\n        \n        <div class=\"teacher-callout insight\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-calculator\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The Fundamental Rule: 2\u207f Patterns (Slide 8)</div>\n            <p>Every time you add 1 bit, you <strong>double</strong> the number of things you can represent:\n            <br>&bull; <strong>1 bit:</strong> 2 patterns ($2^1$) &rarr; <code>0, 1</code>\n            <br>&bull; <strong>2 bits:</strong> 4 patterns ($2^2$) &rarr; <code>00, 01, 10, 11</code>\n            <br>&bull; <strong>3 bits:</strong> 8 patterns ($2^3$) &rarr; <code>000, 001, 010, 011, 100, 101, 110, 111</code>\n            <br>&bull; <strong>8 bits (1 Byte):</strong> 256 patterns ($2^8$) &rarr; enough for every key on your keyboard!\n            <br>&bull; <strong>n bits:</strong> can represent up to <strong>2\u207f distinct entities</strong>!\n            </p>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-layer-group\"></i> Visual Diagram: The Power-of-2 Weight Buckets</h3>\n        <p>How does a computer convert binary into a number you understand? Think of 8 buckets, where each bucket holds a fixed power of 2:</p>\n\n        <div class=\"weight-buckets\">\n          <div class=\"bucket-col\">\n            <span class=\"bucket-power\">2\u2077</span>\n            <span class=\"bucket-weight\">128</span>\n            <div class=\"bucket-bit\">0</div>\n          </div>\n          <div class=\"bucket-col\">\n            <span class=\"bucket-power\">2\u2076</span>\n            <span class=\"bucket-weight\">64</span>\n            <div class=\"bucket-bit\">0</div>\n          </div>\n          <div class=\"bucket-col\">\n            <span class=\"bucket-power\">2\u2075</span>\n            <span class=\"bucket-weight\">32</span>\n            <div class=\"bucket-bit active-one\">1</div>\n          </div>\n          <div class=\"bucket-col\">\n            <span class=\"bucket-power\">2\u2074</span>\n            <span class=\"bucket-weight\">16</span>\n            <div class=\"bucket-bit\">0</div>\n          </div>\n          <div class=\"bucket-col\">\n            <span class=\"bucket-power\">2\u00b3</span>\n            <span class=\"bucket-weight\">8</span>\n            <div class=\"bucket-bit\">0</div>\n          </div>\n          <div class=\"bucket-col\">\n            <span class=\"bucket-power\">2\u00b2</span>\n            <span class=\"bucket-weight\">4</span>\n            <div class=\"bucket-bit\">0</div>\n          </div>\n          <div class=\"bucket-col\">\n            <span class=\"bucket-power\">2\u00b9</span>\n            <span class=\"bucket-weight\">2</span>\n            <div class=\"bucket-bit active-one\">1</div>\n          </div>\n          <div class=\"bucket-col\">\n            <span class=\"bucket-power\">2\u2070</span>\n            <span class=\"bucket-weight\">1</span>\n            <div class=\"bucket-bit active-one\">1</div>\n          </div>\n        </div>\n\n        <p><strong>To find the value of binary <code>00100011</code>:</strong> Just add the active buckets where bit is 1!\n        <br>&rarr; $32 + 2 + 1 = \\mathbf{35}$! It's that simple!</p>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-shapes\"></i> The Four Number Bases Compared</h3>\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>System</th><th>Base (Radix)</th><th>Digits Used</th><th>Why Humans & Computers Use It</th><th>C Notation</th></tr>\n            </thead>\n            <tbody>\n              <tr><td><strong>Binary</strong></td><td>2</td><td>0, 1</td><td>Directly matches physical on/off electric voltages.</td><td>Suffix <code>B</code> (or <code>0b</code>)</td></tr>\n              <tr><td><strong>Octal</strong></td><td>8</td><td>0 to 7</td><td>Shortens binary by grouping bits into sets of <strong>3 bits</strong> ($2^3 = 8$). Used in UNIX file permissions (e.g. <code>chmod 755</code>).</td><td>Prefix <code>0</code> (e.g. <code>0527</code>)</td></tr>\n              <tr><td><strong>Decimal</strong></td><td>10</td><td>0 to 9</td><td>Human standard counting system (based on our 10 fingers).</td><td>Default (e.g. <code>735</code>)</td></tr>\n              <tr><td><strong>Hexadecimal</strong></td><td>16</td><td>0\u20139 and A\u2013F (A=10, B=11, C=12, D=13, E=14, F=15)</td><td><strong>The Programmer's Best Friend!</strong> Groups binary into sets of <strong>4 bits (1 nibble)</strong> ($2^4 = 16$). Represents huge binary addresses compactly.</td><td>Prefix <code>0x</code> (e.g. <code>0xA3C5</code>)</td></tr>\n            </tbody>\n          </table>\n        </div>\n\n        <div class=\"teacher-callout insight\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-wand-magic-sparkles\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The 4-Bit Hex Secret (Slides 10\u201311)</div>\n            <p>Reading <code>1010001111000101</code> makes your eyes hurt. But notice how clean it becomes when split into 4-bit nibbles:\n            <br>&emsp;<code>1010</code> = <strong>A</strong> (10)\n            <br>&emsp;<code>0011</code> = <strong>3</strong>\n            <br>&emsp;<code>1100</code> = <strong>C</strong> (12)\n            <br>&emsp;<code>0101</code> = <strong>5</strong>\n            <br>&rarr; Together: <strong>0xA3C5</strong>! Hexadecimal is not a separate math; it is just friendly shorthand nicknames for 4-bit binary chunks!</p>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-pen-ruler\"></i> Visual Step-by-Step Radix Conversions (Slide 14)</h3>\n        <p>Let's look at the exact handwritten examples from Slide 14 broken down into clear visual steps:</p>\n\n        <div class=\"conversion-ladder\">\n          <div class=\"ladder-col\">\n            <h5><i class=\"fa-solid fa-arrow-down-9-1\"></i> Example 1: Convert (108.78)\u2081\u2080 to Octal</h5>\n            <p style=\"font-size: 0.8rem; color: var(--text-muted);\"><strong>Integer Part (108):</strong> Successive division by 8, reading remainders from bottom to top:</p>\n            <div class=\"ladder-step\"><span class=\"calc\">108 &divide; 8 = 13</span><span class=\"rem\">Remainder 4 &uarr; (LSD)</span></div>\n            <div class=\"ladder-step\"><span class=\"calc\">13 &divide; 8 = 1</span><span class=\"rem\">Remainder 5 &uarr;</span></div>\n            <div class=\"ladder-step\"><span class=\"calc\">1 &divide; 8 = 0</span><span class=\"rem\">Remainder 1 &uarr; (MSD)</span></div>\n            <p style=\"font-size: 0.82rem; margin-top: 0.4rem;\">&rarr; Integer part = <strong>154\u2088</strong></p>\n\n            <p style=\"font-size: 0.8rem; color: var(--text-muted); margin-top: 0.75rem;\"><strong>Fractional Part (0.78):</strong> Successive multiplication by 8, taking the integer part from top to bottom:</p>\n            <div class=\"ladder-step\"><span class=\"calc\">0.78 &times; 8 = 6.24</span><span class=\"rem\">Take 6 &darr;</span></div>\n            <div class=\"ladder-step\"><span class=\"calc\">0.24 &times; 8 = 1.92</span><span class=\"rem\">Take 1 &darr;</span></div>\n            <div class=\"ladder-step\"><span class=\"calc\">0.92 &times; 8 = 7.36</span><span class=\"rem\">Take 7 &darr;</span></div>\n            <div class=\"ladder-step\"><span class=\"calc\">0.36 &times; 8 = 2.88</span><span class=\"rem\">Take 2 &darr;</span></div>\n            <p style=\"font-size: 0.82rem; margin-top: 0.4rem;\">&rarr; Fractional part = <strong>.6172...\u2088</strong></p>\n            <p style=\"font-size: 0.88rem; font-weight: 700; color: var(--accent-emerald); margin-top: 0.5rem;\">Result: (108.78)\u2081\u2080 &approx; (154.6172)\u2088</p>\n          </div>\n\n          <div class=\"ladder-col\">\n            <h5><i class=\"fa-solid fa-arrow-right-arrow-left\"></i> Example 2 & 3: Hex & Binary to Octal</h5>\n            <p style=\"font-size: 0.8rem; color: var(--text-muted);\"><strong>Example 2: Convert (FE.4A)\u2081\u2086 to Decimal:</strong></p>\n            <div class=\"ladder-step\"><span class=\"calc\">F &times; 16\u00b9 = 15 &times; 16</span><span class=\"rem\">240</span></div>\n            <div class=\"ladder-step\"><span class=\"calc\">E &times; 16\u2070 = 14 &times; 1</span><span class=\"rem\">14</span></div>\n            <div class=\"ladder-step\"><span class=\"calc\">4 &times; 16\u207b\u00b9 = 4 / 16</span><span class=\"rem\">0.25</span></div>\n            <div class=\"ladder-step\"><span class=\"calc\">A &times; 16\u207b\u00b2 = 10 / 256</span><span class=\"rem\">0.0390625</span></div>\n            <p style=\"font-size: 0.88rem; font-weight: 700; color: var(--accent-emerald); margin-top: 0.5rem;\">Total = 240 + 14 + 0.25 + 0.039 = 254.289\u2081\u2080</p>\n\n            <p style=\"font-size: 0.8rem; color: var(--text-muted); margin-top: 1rem;\"><strong>Example 3: Convert (101010111)\u2082 to Octal:</strong></p>\n            <p style=\"font-size: 0.85rem;\">Group binary digits by 3 bits from right:</p>\n            <div class=\"ladder-step\"><span class=\"calc\">101 | 010 | 111</span><span class=\"rem\">5 | 2 | 7</span></div>\n            <p style=\"font-size: 0.88rem; font-weight: 700; color: var(--accent-emerald); margin-top: 0.5rem;\">Result: (527)\u2088</p>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-microchip\"></i> 32-bit vs. 64-bit Processors: Why the 4 GB Limit? (Slides 26\u201329)</h3>\n        <p>A CPU register is like a notepad where the processor scribbles memory addresses. The bit-width tells us how big of an address the processor can write:</p>\n        <ul>\n          <li><strong>32-bit Processor:</strong> Can write up to $2^{32}$ distinct addresses. Since each address points to 1 byte, $2^{32}\\text{ bytes} = \\mathbf{4\\text{ GB}}$! Even if you physically plug 16 GB of RAM into a 32-bit machine, the CPU physically cannot address beyond ~3.5 to 4 GB.</li>\n          <li><strong>64-bit Processor:</strong> Can write up to $2^{64}$ addresses = <strong>18 Quintillion bytes (16 Exabytes)</strong>! It can effortlessly handle 8 GB, 32 GB, 128 GB, or Terabytes of RAM.</li>\n        </ul>\n\n        <div class=\"teacher-callout exam-alert\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-triangle-exclamation\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The Teacher's Takeaway</div>\n            <p>If your computer has 8 GB of RAM or more, it <em>must</em> have a 64-bit processor and a 64-bit operating system to use that memory (Slide 28).</p>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-arrows-spin\"></i> The 4-Step CPU Heartbeat (Slide 30)</h3>\n        <p>Every single millisecond, your CPU loops through four fundamental steps to execute instructions:</p>\n        <ol>\n          <li><strong>1. Fetch:</strong> Grabs the next instruction from RAM into the CPU.</li>\n          <li><strong>2. Decode:</strong> Figures out what the instruction means (e.g. \"Add two numbers\" or \"Move data\").</li>\n          <li><strong>3. Execute:</strong> The ALU (Arithmetic Logic Unit) actually computes the math or logic.</li>\n          <li><strong>4. Write Back:</strong> Saves the result into a register or RAM so you can see it.</li>\n        </ol>\n      </div>\n    ",
    "code": {
      "title": "Inspecting Binary and Bit-Width in C",
      "desc": "Demonstrating how numbers are stored and how bitwise operations inspect architecture representation.",
      "lang": "c",
      "snippet": "#include <stdio.h>\n#include <stdint.h>\n\nvoid print_binary(uint32_t num) {\n    for (int i = 31; i >= 0; i--) {\n        printf(\"%d\", (num >> i) & 1);\n        if (i % 4 == 0 && i != 0) printf(\" \");\n    }\n    printf(\"\\n\");\n}\n\nint main(void) {\n    uint32_t val = 0xA3C5; // Hexadecimal literal\n    printf(\"Hex: 0x%X | Decimal: %u\\nBinary: \", val, val);\n    print_binary(val); // 0000 0000 0000 0000 1010 0011 1100 0101\n\n    printf(\"Word size of pointer on this system: %zu bytes (%zu bits)\\n\", \n           sizeof(void*), sizeof(void*) * 8);\n    return 0;\n}",
      "output": "Hex: 0xA3C5 | Decimal: 41925\nBinary: 0000 0000 0000 0000 1010 0011 1100 0101\nWord size of pointer on this system: 8 bytes (64 bits)"
    },
    "resources": [
      {
        "type": "tool",
        "title": "Float.exposed \u2014 IEEE 754 Floating Point Visualizer",
        "url": "https://float.exposed",
        "desc": "Interactive tool showing sign, exponent, and mantissa bit breakdown."
      },
      {
        "type": "gfg",
        "title": "Number Systems and Base Conversions",
        "url": "https://www.geeksforgeeks.org/number-system-in-digital-electronics/",
        "desc": "Detailed guide on binary, octal, decimal, and hexadecimal arithmetic."
      },
      {
        "type": "docs",
        "title": "Bit Twiddling Hacks by Sean Eron Anderson",
        "url": "https://graphics.stanford.edu/~seander/bithacks.html",
        "desc": "Stanford University collection of bit-manipulation algorithms."
      }
    ],
    "quiz": [
      {
        "id": "q2_1",
        "question": "How many distinct binary patterns can be stored in an n-bit storage location?",
        "options": [
          "2 * n",
          "n^2",
          "2^n",
          "2^(n-1)"
        ],
        "answer": 2,
        "explanation": "As stated on Slide 8, an n-bit storage location can represent up to 2^n distinct entities. For example, 3 bits can represent 2^3 = 8 distinct patterns."
      },
      {
        "id": "q2_2",
        "question": "What is the equivalent hexadecimal representation of the binary number 1001001010B?",
        "options": [
          "24AH",
          "4A2H",
          "92AH",
          "124H"
        ],
        "answer": 0,
        "explanation": "Grouping from the right in sets of 4 bits: 0010 0100 1010. 0010_2 = 2, 0100_2 = 4, 1010_2 = A (10). Thus, 1001001010B = 24AH (Slide 11)."
      },
      {
        "id": "q2_3",
        "question": "Why is a 32-bit CPU physically limited to addressing a maximum of 4 GB of RAM?",
        "options": [
          "Because hard drives cannot read faster than 4 GB/sec",
          "Because a 32-bit register can generate at most 2^32 unique memory byte addresses (4,294,967,296 bytes)",
          "Because operating systems prohibit using more than 4 GB for security",
          "Because DRAM capacitors discharge when accessing addresses above 4 GB"
        ],
        "answer": 1,
        "explanation": "A 32-bit register holds 32 bits. With 1 bit per byte reference, 2^32 addresses = 4,294,967,296 bytes = 4 GB of physical memory (Slide 26-27)."
      },
      {
        "id": "q2_4",
        "question": "What are the four fundamental steps in the CPU instruction cycle?",
        "options": [
          "Compile, Assemble, Link, Load",
          "Fetch, Decode, Execute, Write Back",
          "Read, Write, Erase, Verify",
          "Input, Process, Output, Store"
        ],
        "answer": 1,
        "explanation": "As detailed on Slide 30, the four core steps nearly all CPUs use are: Fetch (get instruction from memory), Decode (interpret opcode), Execute (perform calculation), and Write Back (store result)."
      },
      {
        "id": "q2_5",
        "question": "According to the storage units hierarchy on Slide 24, which is the highest named memory capacity unit?",
        "options": [
          "Yottabyte (YB)",
          "Brontobyte",
          "Geop Byte",
          "Exabyte (EB)"
        ],
        "answer": 2,
        "explanation": "Slide 24 specifically highlights: '1024 Brontobyte = 1 Geop Byte. Geop Byte is the Highest Memory.'"
      }
    ]
  },
  {
    "id": "m3",
    "num": 3,
    "title": "Hardware, Storage & Memory Hierarchy",
    "subtitle": "Primary vs Secondary Memory, RAM vs ROM, SRAM vs DRAM, Memory Pyramid",
    "slides": "Slides 15\u201323",
    "time": "30 mins",
    "content": "\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-layer-group\"></i> The Memory Pyramid: Speed vs. Cost vs. Size (Slide 21)</h3>\n        <p>Why can't our computers just have 1 Terabyte of super-fast CPU registers? Because ultra-fast memory is expensive and physically difficult to pack together. Computer architects solved this by organizing memory as a <strong>Pyramid</strong>:</p>\n\n        <div class=\"teacher-callout insight\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-mountain\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The Law of the Memory Pyramid</div>\n            <p><strong>Going UP the pyramid:</strong> Speed increases dramatically (nanoseconds!) and cost increases, but capacity shrinks.\n            <br><strong>Going DOWN the pyramid:</strong> Storage expands to massive Terabytes and Petabytes, but access becomes much slower.</p>\n          </div>\n        </div>\n\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Level</th><th>Memory Type</th><th>Technology</th><th>Speed Analogy</th><th>Primary Purpose</th></tr>\n            </thead>\n            <tbody>\n              <tr>\n                <td><strong>Level 0</strong></td>\n                <td>CPU Registers</td>\n                <td>Direct silicon latches in CPU</td>\n                <td>Like information already in your active thinking memory (&lt; 1 ns).</td>\n                <td>Holds numbers currently being calculated right this millisecond.</td>\n              </tr>\n              <tr>\n                <td><strong>Level 1</strong></td>\n                <td>Cache Memory (L1, L2, L3)</td>\n                <td>Static RAM (SRAM)</td>\n                <td>Like a notepad open right in front of you (1\u201310 ns).</td>\n                <td>Stores recently used instructions so the CPU doesn't wait on slow RAM.</td>\n              </tr>\n              <tr>\n                <td><strong>Level 2</strong></td>\n                <td>Main / Primary Memory</td>\n                <td>Dynamic RAM (DRAM)</td>\n                <td>Like walking to your desk drawer (50\u2013100 ns).</td>\n                <td>Holds your active programs, open browser tabs, and game data.</td>\n              </tr>\n              <tr>\n                <td><strong>Level 3</strong></td>\n                <td>Secondary / Mass Storage</td>\n                <td>Solid State Drive (SSD) / Hard Disk (HDD)</td>\n                <td>Like walking to a warehouse across town (milliseconds).</td>\n                <td>Stores saved files, installed apps, and Windows/Linux permanently.</td>\n              </tr>\n              <tr>\n                <td><strong>Level 4</strong></td>\n                <td>Offline / Archival Storage</td>\n                <td>Magnetic Tape, Optical Disks</td>\n                <td>Like ordering from an archive in another country.</td>\n                <td>Long-term historical company backups.</td>\n              </tr>\n            </tbody>\n          </table>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-code-compare\"></i> Primary Memory vs. Secondary Storage (Slide 23)</h3>\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Feature</th><th>Primary Memory (RAM)</th><th>Secondary Storage (SSD / Hard Drive)</th></tr>\n            </thead>\n            <tbody>\n              <tr><td><strong>Permanence</strong></td><td><strong>Temporary:</strong> Wiped clean the instant power is turned off.</td><td><strong>Permanent:</strong> Preserves data for years without electrical power.</td></tr>\n              <tr><td><strong>CPU Access</strong></td><td><strong>Direct:</strong> Connected directly to the CPU memory bus.</td><td><strong>Indirect:</strong> Must be copied into RAM before the CPU can read it.</td></tr>\n              <tr><td><strong>Volatility</strong></td><td>Volatile (RAM)</td><td>Non-Volatile (SSD, Hard Disk, Flash drive)</td></tr>\n              <tr><td><strong>Speed</strong></td><td>Super-fast electronic semiconductor memory.</td><td>Slower mechanical or flash access.</td></tr>\n              <tr><td><strong>Cost per GB</strong></td><td>High cost per gigabyte.</td><td>Very cheap cost per gigabyte.</td></tr>\n            </tbody>\n          </table>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-microchip\"></i> RAM vs. ROM: What's the Difference? (Slide 19)</h3>\n        <ul>\n          <li><strong>RAM (Random Access Memory):</strong> Read and Write. Fast, volatile, large (4 GB to 32 GB+). Stores apps you are actively running right now.\n            <br>&bull; <em>DRAM (Dynamic):</em> Uses tiny capacitors; must be refreshed with electricity thousands of times a second. Cheap, used for main system RAM.\n            <br>&bull; <em>SRAM (Static):</em> Uses flip-flops; doesn't need refreshing. Blazing fast, expensive, used for CPU cache!</li>\n          <li><strong>ROM (Read-Only Memory):</strong> Read-only during normal operation. Non-volatile, small (4 MB to 8 MB). Contains the firmware instructions (BIOS/UEFI) that wake the computer up when you press the power button!</li>\n        </ul>\n      </div>\n    ",
    "code": {
      "title": "Simulating Volatile Memory Allocation",
      "desc": "How C programs interact with primary memory and allocate memory dynamically.",
      "lang": "c",
      "snippet": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    // Variable in Primary Memory (RAM)\n    int stack_num = 100;\n    \n    // Dynamic allocation in RAM (Heap)\n    int *dynamic_array = (int*)malloc(5 * sizeof(int));\n    if (dynamic_array == NULL) {\n        printf(\"Out of primary memory!\\n\");\n        return 1;\n    }\n\n    for (int i = 0; i < 5; i++) {\n        dynamic_array[i] = (i + 1) * 10;\n    }\n\n    printf(\"Stack variable address: %p | Value: %d\\n\", (void*)&stack_num, stack_num);\n    printf(\"Heap allocated address: %p | First Value: %d\\n\", (void*)dynamic_array, dynamic_array[0]);\n\n    free(dynamic_array); // Always return memory to primary storage!\n    return 0;\n}",
      "output": "Stack variable address: 0x7ffd98... | Value: 100\nHeap allocated address: 0x55d7a2... | First Value: 10"
    },
    "resources": [
      {
        "type": "gfg",
        "title": "Memory Hierarchy in Computer Architecture",
        "url": "https://www.geeksforgeeks.org/memory-hierarchy-in-computer-architecture/",
        "desc": "In-depth guide covering Registers, Cache, Main Memory, and Disk."
      },
      {
        "type": "gfg",
        "title": "Differences Between RAM and ROM",
        "url": "https://www.geeksforgeeks.org/difference-between-ram-and-rom/",
        "desc": "Technical breakdown of semiconductor volatile vs non-volatile storage."
      },
      {
        "type": "docs",
        "title": "What Every Programmer Should Know About Memory (Ulrich Drepper)",
        "url": "https://people.freebsd.org/~lstewart/articles/cpumemory.pdf",
        "desc": "Seminal MIT/RedHat reference on modern memory systems and CPU caches."
      }
    ],
    "quiz": [
      {
        "id": "q3_1",
        "question": "What happens as you move UP the memory hierarchy pyramid towards the CPU registers?",
        "options": [
          "Capacity increases and cost decreases",
          "Speed increases, cost-per-bit increases, and capacity decreases",
          "Speed decreases and latency increases",
          "Volatility decreases to zero"
        ],
        "answer": 1,
        "explanation": "As clearly depicted on Slide 21, going up the pyramid increases speed and cost while decreasing storage capacity."
      },
      {
        "id": "q3_2",
        "question": "Which of the following memories is directly accessible by the central processing unit (CPU)?",
        "options": [
          "Magnetic Disk",
          "Secondary Storage",
          "Primary / Main Memory (RAM)",
          "Magnetic Tape"
        ],
        "answer": 2,
        "explanation": "Primary memory (RAM, cache, registers) is directly accessible by the CPU over the high-speed system bus. Secondary storage must first be transferred into primary memory before execution (Slide 23)."
      },
      {
        "id": "q3_3",
        "question": "Why is SRAM (Static RAM) used for CPU cache instead of DRAM (Dynamic RAM)?",
        "options": [
          "SRAM is cheaper and larger than DRAM",
          "SRAM uses flip-flops and does not require periodic electric refreshing, making it significantly faster",
          "SRAM is non-volatile and preserves data when powered off",
          "SRAM is magnetic while DRAM is optical"
        ],
        "answer": 1,
        "explanation": "SRAM uses bistable latching circuitry (flip-flops) and requires no refresh cycles, providing near-instantaneous access times ideal for CPU Level 1/2/3 caches, unlike DRAM which relies on discharging capacitors."
      },
      {
        "id": "q3_4",
        "question": "Where are the initial computer boot instructions (BIOS / UEFI) permanently stored?",
        "options": [
          "In the RAM text segment",
          "In Read-Only Memory (ROM)",
          "In the CPU ALU accumulator",
          "In the browser cache"
        ],
        "answer": 1,
        "explanation": "As noted on Slide 19, ROM is non-volatile and retains boot instructions (BIOS) even after the computer is turned off."
      },
      {
        "id": "q3_5",
        "question": "What is the primary difference between volatile and non-volatile storage?",
        "options": [
          "Volatile storage loses its contents when power is turned off; non-volatile retains data without power",
          "Volatile storage can only store text, while non-volatile stores images",
          "Volatile storage is slower than secondary storage",
          "Non-volatile storage can only be read once"
        ],
        "answer": 0,
        "explanation": "Volatility refers to data retention upon power loss. RAM is volatile (erased upon power-down), whereas hard drives and ROM are non-volatile (retain data without power) (Slide 22)."
      }
    ]
  },
  {
    "id": "m4",
    "num": 4,
    "title": "Problem Solving: Flowcharts & Pseudocode Made Simple",
    "subtitle": "The Recipe Analogy, Rosetta Stone Comparison, Rendered Flowcharts & Trace Tables",
    "slides": "Slides 31\u201345",
    "time": "40 mins",
    "content": "\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-cake-candles\"></i> What is an Algorithm? Think of a Recipe!</h3>\n        <p>Before you bake a cake, you need a recipe. If a recipe says <em>\"mix stuff and bake until it looks ready,\"</em> that's a terrible recipe because it's vague. But if it says:\n        <br>&emsp;<code>1. Take 2 eggs and 1 cup of flour</code>\n        <br>&emsp;<code>2. Whisk for 3 minutes until smooth</code>\n        <br>&emsp;<code>3. Bake at 350\u00b0F for exactly 25 minutes</code>\n        <br>Anyone following that recipe will get the exact same delicious cake!</p>\n\n        <div class=\"teacher-callout insight\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-lightbulb\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The 4 Rules of Every Good Algorithm (Slide 31)</div>\n            <p>&bull; <strong>Clear & Unambiguous:</strong> Every instruction has only one possible interpretation.\n            <br>&bull; <strong>Has Inputs & Outputs:</strong> Takes raw ingredients (input) and gives a specific result (output).\n            <br>&bull; <strong>Finiteness (Must Stop!):</strong> Must finish in a reasonable number of steps. It can never run forever.\n            <br>&bull; <strong>Language-Independent:</strong> Written in plain logic so it can be programmed in C, Python, or Java alike.</p>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-bridge\"></i> What is Pseudocode? The \"Bridge\" Between Thought and C</h3>\n        <p>When you start coding, trying to figure out the logic while simultaneously worrying about semicolons, braces, and C syntax gives you a headache. <strong>Pseudocode</strong> solves this!</p>\n        <p>Pseudocode is structured English. It looks like code, but has no strict syntax rules. Look at how cleanly logic translates across the <strong>Rosetta Stone Bridge</strong>:</p>\n\n        <div class=\"rosetta-bridge\">\n          <div class=\"rosetta-col\">\n            <div class=\"rosetta-header english\"><i class=\"fa-solid fa-user\"></i> 1. Human English Thought</div>\n            <div class=\"rosetta-body\">\n              \"Ask the user for four exam marks. Find their average. If the average is below 40, they failed; otherwise they passed.\"\n            </div>\n          </div>\n\n          <div class=\"rosetta-col\">\n            <div class=\"rosetta-header pseudocode\"><i class=\"fa-solid fa-file-lines\"></i> 2. Clean Pseudocode</div>\n            <div class=\"rosetta-body\">\n              <pre>READ m1, m2, m3, m4\navg = (m1 + m2 + m3 + m4) / 4\n\nIF avg < 40 THEN\n    PRINT \"Fail\"\nELSE\n    PRINT \"Pass\"\nENDIF</pre>\n            </div>\n          </div>\n\n          <div class=\"rosetta-col\">\n            <div class=\"rosetta-header c-code\"><i class=\"fa-solid fa-code\"></i> 3. Actual C Language</div>\n            <div class=\"rosetta-body\">\n              <pre>float m1, m2, m3, m4, avg;\nscanf(\"%f %f %f %f\", &m1, &m2, &m3, &m4);\navg = (m1 + m2 + m3 + m4) / 4.0;\n\nif (avg < 40) {\n    printf(\"Fail\\n\");\n} else {\n    printf(\"Pass\\n\");\n}</pre>\n            </div>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-shapes\"></i> Standard Flowchart Shapes: What Each Shape Means</h3>\n        <p>A <strong>Flowchart</strong> is simply drawing your algorithm with shapes and arrows so anyone can visually trace the flow of logic like water through a pipe:</p>\n\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Shape</th><th>Name</th><th>Color Meaning</th><th>Real-Life Role in Flowchart</th></tr>\n            </thead>\n            <tbody>\n              <tr>\n                <td><strong>Oval / Pill</strong></td>\n                <td>Terminal Symbol</td>\n                <td><span style=\"color: #10b981; font-weight: 700;\">GREEN</span></td>\n                <td>Marks where the program <strong>STARTS</strong> and where it <strong>STOPS</strong>.</td>\n              </tr>\n              <tr>\n                <td><strong>Parallelogram (Slanted)</strong></td>\n                <td>Input / Output</td>\n                <td><span style=\"color: #3b82f6; font-weight: 700;\">BLUE</span></td>\n                <td>Whenever the computer asks the user for data (<code>READ N</code>) or prints an answer on screen (<code>PRINT \"Pass\"</code>).</td>\n              </tr>\n              <tr>\n                <td><strong>Rectangle (Box)</strong></td>\n                <td>Process / Calculation</td>\n                <td><span style=\"color: #f59e0b; font-weight: 700;\">YELLOW</span></td>\n                <td>Any internal calculation or variable assignment (<code>Sum = 0</code>, <code>avg = total / 4</code>).</td>\n              </tr>\n              <tr>\n                <td><strong>Diamond</strong></td>\n                <td>Decision / Question</td>\n                <td><span style=\"color: #a855f7; font-weight: 700;\">PURPLE</span></td>\n                <td>Asks a Yes/No question with two exit arrows (e.g. <code>Is avg &lt; 40?</code> &rarr; Yes / No).</td>\n              </tr>\n              <tr>\n                <td><strong>Arrows</strong></td>\n                <td>Flowlines</td>\n                <td><span style=\"color: var(--text-muted); font-weight: 700;\">ARROWS</span></td>\n                <td>Show the exact direction instructions travel.</td>\n              </tr>\n            </tbody>\n          </table>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-diagram-project\"></i> Rendered Visual Flowchart: Student Grade Average (Slide 40\u201341)</h3>\n        <p>Here is the visual diagram for calculating student grades and deciding pass/fail:</p>\n\n        <div class=\"visual-flowchart\">\n          <div class=\"fc-node terminal\"><i class=\"fa-solid fa-circle-play\"></i> START</div>\n          <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n          <div class=\"fc-node io\"><i class=\"fa-solid fa-keyboard\"></i> READ m1, m2, m3, m4</div>\n          <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n          <div class=\"fc-node process\"><i class=\"fa-solid fa-calculator\"></i> avg = (m1 + m2 + m3 + m4) / 4</div>\n          <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n          <div class=\"fc-node decision\"><i class=\"fa-solid fa-question\"></i> Is avg &lt; 40?</div>\n\n          <div class=\"fc-decision-branches\">\n            <div class=\"fc-branch\">\n              <span class=\"fc-branch-tag true-tag\">TRUE (Yes)</span>\n              <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n              <div class=\"fc-node io\"><i class=\"fa-solid fa-print\"></i> PRINT \"Fail\"</div>\n            </div>\n            <div class=\"fc-branch\">\n              <span class=\"fc-branch-tag false-tag\">FALSE (No)</span>\n              <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n              <div class=\"fc-node io\"><i class=\"fa-solid fa-print\"></i> PRINT \"Pass\"</div>\n            </div>\n          </div>\n\n          <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n          <div class=\"fc-node terminal\"><i class=\"fa-solid fa-circle-stop\"></i> STOP (END)</div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-arrow-rotate-right\"></i> Rendered Visual Flowchart: Sum of Digits with Loop (Slide 42\u201344)</h3>\n        <p>How does a program sum up digits of a number like <code>1234</code>? It repeatedly chops off the rightmost digit using <code>N % 10</code> and accumulates it:</p>\n\n        <div class=\"visual-flowchart\">\n          <div class=\"fc-node terminal\"><i class=\"fa-solid fa-circle-play\"></i> START</div>\n          <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n          <div class=\"fc-node io\"><i class=\"fa-solid fa-keyboard\"></i> READ N (e.g. 1234)</div>\n          <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n          <div class=\"fc-node process\"><i class=\"fa-solid fa-gear\"></i> Set Sum = 0</div>\n          <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n          <div class=\"fc-node decision\"><i class=\"fa-solid fa-arrows-spin\"></i> Loop: Is N != 0?</div>\n\n          <div class=\"fc-decision-branches\">\n            <div class=\"fc-branch\" style=\"border-color: var(--accent-blue);\">\n              <span class=\"fc-branch-tag true-tag\">YES (Keep Looping)</span>\n              <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n              <div class=\"fc-node process\">Rem = N % 10 (get last digit)</div>\n              <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n              <div class=\"fc-node process\">Sum = Sum + Rem (add to total)</div>\n              <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n              <div class=\"fc-node process\">N = N / 10 (chop off last digit)</div>\n              <p style=\"font-size: 0.75rem; color: var(--accent-cyan); margin-top: 0.5rem;\">&uarr; Loop arrow flows back up to check N != 0</p>\n            </div>\n            <div class=\"fc-branch\" style=\"border-color: var(--accent-emerald);\">\n              <span class=\"fc-branch-tag false-tag\">NO (N reached 0)</span>\n              <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n              <div class=\"fc-node io\"><i class=\"fa-solid fa-print\"></i> PRINT Sum</div>\n              <div class=\"fc-arrow\"><i class=\"fa-solid fa-arrow-down\"></i></div>\n              <div class=\"fc-node terminal\"><i class=\"fa-solid fa-circle-stop\"></i> END</div>\n            </div>\n          </div>\n        </div>\n\n        <h4>Step-by-Step Execution Trace Table for N = 1234</h4>\n        <p>Watch exactly how variables change in each cycle of the loop:</p>\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Iteration</th><th>Current N</th><th>Rem = N % 10 (Extracted Digit)</th><th>Sum = Sum + Rem</th><th>New N = N / 10 (Remaining)</th></tr>\n            </thead>\n            <tbody>\n              <tr><td><strong>Before Loop</strong></td><td>1234</td><td>-</td><td>0</td><td>1234</td></tr>\n              <tr><td><strong>Turn 1</strong></td><td>1234</td><td>4</td><td>0 + 4 = <strong>4</strong></td><td>123</td></tr>\n              <tr><td><strong>Turn 2</strong></td><td>123</td><td>3</td><td>4 + 3 = <strong>7</strong></td><td>12</td></tr>\n              <tr><td><strong>Turn 3</strong></td><td>12</td><td>2</td><td>7 + 2 = <strong>9</strong></td><td>1</td></tr>\n              <tr><td><strong>Turn 4</strong></td><td>1</td><td>1</td><td>9 + 1 = <strong>10</strong></td><td><strong>0</strong> (Loop Exits!)</td></tr>\n            </tbody>\n          </table>\n        </div>\n        <p style=\"font-size: 0.95rem; font-weight: 700; color: var(--accent-emerald);\">Final Output: Sum = 10 (since 1 + 2 + 3 + 4 = 10)!</p>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-list-ol\"></i> Solutions to the 6 Practice Challenges (Slide 45)</h3>\n        <ol>\n          <li><strong>Sum of Multiples of 3 or 5 below 1000:</strong> Loop from 1 to 999. If $(i \\% 3 == 0 \\lor i \\% 5 == 0)$, add $i$ to sum. <strong>Answer = 233,168</strong>.</li>\n          <li><strong>Roots of Quadratic Equation $ax^2 + bx + c = 0$:</strong> Calculate discriminant $D = b^2 - 4ac$. If $D &gt; 0$, roots are $\\frac{-b \\pm \\sqrt{D}}{2a}$. If $D == 0$, root is $\\frac{-b}{2a}$. If $D &lt; 0$, roots are imaginary.</li>\n          <li><strong>Largest of 3 Numbers ($a, b, c$):</strong> Compare $a &gt; b$. If true, compare $a &gt; c$. If false, compare $b &gt; c$.</li>\n          <li><strong>Even or Odd:</strong> Check remainder: <code>if (N % 2 == 0)</code> &rarr; Even, else Odd.</li>\n          <li><strong>Quotient and Remainder:</strong> In C, <code>A / B</code> gives integer quotient, and <code>A % B</code> gives remainder.</li>\n          <li><strong>Even Numbers between 100 and 200:</strong> Loop $i$ starting at 102 up to 198 with step $+2$.</li>\n        </ol>\n      </div>\n    ",
    "code": {
      "title": "Sum of Digits in C (Slide 43)",
      "desc": "C implementation of the digit extraction and accumulation algorithm.",
      "lang": "c",
      "snippet": "#include <stdio.h>\n\nint main(void) {\n    int n = 12345;\n    int sum = 0;\n    int temp = n;\n\n    while (n != 0) {\n        int rem = n % 10;  // Extract rightmost digit\n        sum += rem;        // Add to sum\n        n = n / 10;        // Chop off rightmost digit\n    }\n\n    printf(\"Sum of digits of %d is: %d\\n\", temp, sum);\n    return 0;\n}",
      "output": "Sum of digits of 12345 is: 15"
    },
    "resources": [
      {
        "type": "gfg",
        "title": "Differences Between Algorithm and Flowchart",
        "url": "https://www.geeksforgeeks.org/difference-between-algorithm-and-flowchart/",
        "desc": "Tabular comparison of text vs pictorial problem solving."
      },
      {
        "type": "docs",
        "title": "ISO 5807 Information Processing Documentation Symbols",
        "url": "https://www.iso.org/standard/11955.html",
        "desc": "Official international standard for flowchart diagrams and data charts."
      },
      {
        "type": "tool",
        "title": "Draw.io / Diagrams.net Flowchart Builder",
        "url": "https://app.diagrams.net",
        "desc": "Interactive diagramming suite for creating ISO standard flowcharts."
      }
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
  },
  {
    "id": "m5",
    "num": 5,
    "title": "C Program Structure & GCC Compilation Pipeline",
    "subtitle": "The 4-Stage Conveyor Belt: Preprocessor, Compiler, Assembler, Linker",
    "slides": "Slides 46\u201361",
    "time": "40 mins",
    "content": "\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-industry\"></i> The Software Factory: The 4 Stages of GCC</h3>\n        <p>When you type <code>gcc main.c -o main</code>, your code goes through a <strong>4-station conveyor belt</strong>. Here is the visual pipeline:</p>\n\n        <div class=\"conveyor-pipeline\">\n          <div class=\"conveyor-step\">\n            <span class=\"conveyor-tool\">Source Code</span>\n            <span class=\"conveyor-name\">Your C Code</span>\n            <span class=\"conveyor-ext\">.c</span>\n          </div>\n          <div class=\"conveyor-arrow\"><i class=\"fa-solid fa-arrow-right\"></i></div>\n\n          <div class=\"conveyor-step\">\n            <span class=\"conveyor-tool\">1. Preprocessor (cpp)</span>\n            <span class=\"conveyor-name\">Text Expander</span>\n            <span class=\"conveyor-ext\">.i</span>\n          </div>\n          <div class=\"conveyor-arrow\"><i class=\"fa-solid fa-arrow-right\"></i></div>\n\n          <div class=\"conveyor-step\">\n            <span class=\"conveyor-tool\">2. Compiler (cc1)</span>\n            <span class=\"conveyor-name\">Assembly Gen</span>\n            <span class=\"conveyor-ext\">.s</span>\n          </div>\n          <div class=\"conveyor-arrow\"><i class=\"fa-solid fa-arrow-right\"></i></div>\n\n          <div class=\"conveyor-step\">\n            <span class=\"conveyor-tool\">3. Assembler (as)</span>\n            <span class=\"conveyor-name\">Object Machine Code</span>\n            <span class=\"conveyor-ext\">.o</span>\n          </div>\n          <div class=\"conveyor-arrow\"><i class=\"fa-solid fa-arrow-right\"></i></div>\n\n          <div class=\"conveyor-step\" style=\"border-color: var(--accent-emerald);\">\n            <span class=\"conveyor-tool\">4. Linker (ld)</span>\n            <span class=\"conveyor-name\">Executable Binary</span>\n            <span class=\"conveyor-ext\" style=\"background: rgba(16, 185, 129, 0.2); color: var(--accent-emerald);\">.exe / binary</span>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-wrench\"></i> What Each Station Does in Simple Terms</h3>\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Station</th><th>Tool & GCC Command</th><th>What It Does in Simple Words</th><th>Input &rarr; Output</th></tr>\n            </thead>\n            <tbody>\n              <tr>\n                <td><strong>1. Preprocessing</strong></td>\n                <td><code>gcc -E file.c -o file.i</code></td>\n                <td><strong>The Text Editor Assistant:</strong> Erases all comments (<code>/* */</code>), replaces all <code>#define</code> words with their actual values, and copies the entire content of header files (like <code>stdio.h</code>) directly into your file.</td>\n                <td><code>.c</code> &rarr; <code>.i</code></td>\n              </tr>\n              <tr>\n                <td><strong>2. Compilation</strong></td>\n                <td><code>gcc -S file.i -o file.s</code></td>\n                <td><strong>The Blueprint Translator:</strong> Checks grammar/syntax rules and translates the clean C code into human-readable <strong>Assembly Language</strong>.</td>\n                <td><code>.i</code> &rarr; <code>.s</code></td>\n              </tr>\n              <tr>\n                <td><strong>3. Assembly</strong></td>\n                <td><code>gcc -c file.s -o file.o</code></td>\n                <td><strong>The Machine Stamper:</strong> Translates assembly words into actual binary opcodes (0s and 1s) to produce a relocatable <strong>Object File</strong>.</td>\n                <td><code>.s</code> &rarr; <code>.o</code></td>\n              </tr>\n              <tr>\n                <td><strong>4. Linking</strong></td>\n                <td><code>gcc file.o -o file</code></td>\n                <td><strong>The Puzzle Solver:</strong> Merges your object file with precompiled library files (e.g. brings in <code>printf.o</code> from the C runtime library) and creates the final runnable program.</td>\n                <td><code>.o</code> &rarr; Executable</td>\n              </tr>\n            </tbody>\n          </table>\n        </div>\n\n        <div class=\"teacher-callout exam-alert\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-triangle-exclamation\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">Who Throws What Errors? (Slides 55, 104)</div>\n            <p>&bull; <strong>Syntax Errors:</strong> Caught by the <strong>Compiler (cc1)</strong> during stage 2 (e.g. missing semicolons, misspelled keywords).\n            <br>&bull; <strong>Linker Errors:</strong> Caught by the <strong>Linker (ld)</strong> during stage 4 (e.g. <code>undefined reference to 'main'</code> or <code>undefined reference to 'sqrt'</code> when a function is called but its body cannot be found!).</p>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-arrows-turn-to-dots\"></i> Transpilers: Source-to-Source Compilers (Slide 61)</h3>\n        <p>A <strong>Transpiler</strong> takes code written in one high-level language and translates it into another high-level language:</p>\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Source Language</th><th>Target Language</th><th>Historical Transpiler Name (Slide 61)</th></tr>\n            </thead>\n            <tbody>\n              <tr><td><strong>C++</strong></td><td><strong>C</strong></td><td><strong>CFRONT</strong> (Bjarne Stroustrup's original C++ compiler)</td></tr>\n              <tr><td><strong>C#</strong></td><td><strong>JavaScript</strong></td><td><strong>SCRIPTSHARP</strong></td></tr>\n              <tr><td><strong>PHP</strong></td><td><strong>C++</strong></td><td><strong>HIPHOP for PHP</strong> (developed by Facebook for speed)</td></tr>\n              <tr><td><strong>COBOL</strong></td><td><strong>C</strong></td><td><strong>Open COBOL</strong></td></tr>\n            </tbody>\n          </table>\n        </div>\n      </div>\n    ",
    "code": {
      "title": "Preprocessing Macro & Area of Circle (Slides 49\u201350)",
      "desc": "Demonstrating preprocessor #define macro replacement and standard formatted I/O.",
      "lang": "c",
      "snippet": "#include <stdio.h>\n#define PI 3.14159265\n#define GREETING \"Welcome to C Compilation Pipeline\"\n\nint main(void) {\n    float radius = 5.0f;\n    float area = PI * radius * radius;\n\n    printf(\"%s\\n\", GREETING);\n    printf(\"Radius: %.2f | Area of Circle: %.4f\\n\", radius, area);\n    return 0;\n}",
      "output": "Welcome to C Compilation Pipeline\nRadius: 5.00 | Area of Circle: 78.5398"
    },
    "resources": [
      {
        "type": "tool",
        "title": "Compiler Explorer (Godbolt)",
        "url": "https://godbolt.org",
        "desc": "Inspect interactive GCC assembly generation side-by-side with C code."
      },
      {
        "type": "video",
        "title": "How to Install TDM-GCC on Windows (YouTube)",
        "url": "https://www.youtube.com/watch?v=BgcygHaX7sA",
        "desc": "Official video referenced in Slide 47 showing Windows MinGW setup."
      },
      {
        "type": "gfg",
        "title": "Compiling a C Program: Behind the Scenes",
        "url": "https://www.geeksforgeeks.org/compiling-a-c-program-behind-the-scenes/",
        "desc": "Detailed breakdown of Preprocessor, Compiler, Assembler, and Linker."
      },
      {
        "type": "docs",
        "title": "Concept of Assembler, Compiler, Interpreter & Linker",
        "url": "https://www.efaculty.in/c-language/concept-of-assembler-compiler-interpreter-loader-and-linker/",
        "desc": "Curriculum reference on translation phases."
      }
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
  },
  {
    "id": "m6",
    "num": 6,
    "title": "Process Memory Layout in C",
    "subtitle": "The 5-Story Building Analogy: Text, Data, BSS, Heap, Stack & size Command",
    "slides": "Slides 62\u201369",
    "time": "35 mins",
    "content": "\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-building\"></i> The 5-Story Building Analogy (Slide 63)</h3>\n        <p>When you double-click your compiled C program, the Operating System rents an entire building of RAM addresses for your program to live in:</p>\n\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Building Floor</th><th>Memory Segment</th><th>What Lives Here in Plain Words</th><th>Direction</th></tr>\n            </thead>\n            <tbody>\n              <tr>\n                <td><strong>Top Floor (Penthouse)</strong></td>\n                <td><strong>Arguments & Environment</strong></td>\n                <td>Stores command line arguments (e.g. <code>argc, argv</code>) and OS environment settings.</td>\n                <td>Fixed at Highest Address (~0x7FFF...)</td>\n              </tr>\n              <tr>\n                <td><strong>4th Floor</strong></td>\n                <td><strong>Stack Segment</strong></td>\n                <td><strong>The Quick Notepad:</strong> Local variables declared inside functions. Fast and automatic! Every time a function is called, a stack frame is created; when the function finishes, everything is automatically tossed in the trash.</td>\n                <td><strong>Grows Downward &darr;</strong></td>\n              </tr>\n              <tr>\n                <td><em>Middle Space</em></td>\n                <td><em>Unallocated Free RAM</em></td>\n                <td>Empty space allowing Stack to grow down and Heap to grow up without crashing into each other.</td>\n                <td>-</td>\n              </tr>\n              <tr>\n                <td><strong>3rd Floor</strong></td>\n                <td><strong>Heap Segment</strong></td>\n                <td><strong>The Rental Storage Unit:</strong> Memory requested manually by you at runtime using <code>malloc()</code>. You are responsible for releasing it with <code>free()</code>!</td>\n                <td><strong>Grows Upward &uarr;</strong></td>\n              </tr>\n              <tr>\n                <td><strong>2nd Floor</strong></td>\n                <td><strong>Uninitialized Data (.bss)</strong></td>\n                <td>Global variables with no starting value (e.g. <code>int a;</code>). Automatically initialized to <strong>0</strong> by the OS kernel. Takes ZERO space in your disk file!</td>\n                <td>Fixed</td>\n              </tr>\n              <tr>\n                <td><strong>1st Floor</strong></td>\n                <td><strong>Initialized Data (.data)</strong></td>\n                <td>Global variables with starting values (e.g. <code>int count = 10;</code>) and text string literals.</td>\n                <td>Fixed</td>\n              </tr>\n              <tr>\n                <td><strong>Ground Floor / Bedrock</strong></td>\n                <td><strong>Text Segment (Code)</strong></td>\n                <td>The pure machine code instructions executed by the CPU. Marked <strong>Read-Only</strong> so a buggy program cannot accidentally overwrite its own code!</td>\n                <td>Fixed at Lowest Address (~0x0040...)</td>\n              </tr>\n            </tbody>\n          </table>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-terminal\"></i> The 'size' Command Experiment (Slides 68\u201369)</h3>\n        <div class=\"teacher-callout under-hood\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-microscope\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The Classroom Demonstration</div>\n            <p>Slide 68 shows a program with no globals: <code>size Memory.exe</code> &rarr; <strong>bss = 96</strong>.\n            <br>Slide 69 adds one global: <code>int a;</code> outside <code>main()</code>.\n            <br>Run again: <code>size Memory.exe</code> &rarr; <strong>bss = 100</strong>!\n            <br>Notice: <code>bss</code> increased by exactly <strong>4 bytes</strong> (the size of 1 integer)! Neither <code>text</code> nor <code>data</code> changed!</p>\n          </div>\n        </div>\n      </div>\n    ",
    "code": {
      "title": "Verifying Memory Segment Addresses in C",
      "desc": "Printing runtime memory addresses to prove how Text, BSS, Data, Heap, and Stack are positioned.",
      "lang": "c",
      "snippet": "#include <stdio.h>\n#include <stdlib.h>\n\nint global_initialized = 42;      // .data segment\nint global_uninitialized;          // .bss segment\n\nvoid demo_code(void) {}            // .text segment\n\nint main(void) {\n    static int static_initialized = 100; // .data segment\n    static int static_uninitialized;     // .bss segment\n    int stack_variable = 10;             // Stack segment\n    int *heap_pointer = (int*)malloc(sizeof(int)); // Heap segment\n\n    printf(\"=== Memory Layout Addresses ===\\n\");\n    printf(\"1. Text (Code)      : %p\\n\", (void*)&demo_code);\n    printf(\"2. Initialized Data : %p\\n\", (void*)&global_initialized);\n    printf(\"3. BSS (Uninit Data): %p\\n\", (void*)&global_uninitialized);\n    printf(\"4. Heap (Dynamic)   : %p\\n\", (void*)heap_pointer);\n    printf(\"5. Stack (Local)    : %p\\n\", (void*)&stack_variable);\n\n    free(heap_pointer);\n    return 0;\n}",
      "output": "1. Text (Code)      : 0x55b1c2... (Lowest)\n2. Initialized Data : 0x55b1c4...\n3. BSS (Uninit Data): 0x55b1c4...\n4. Heap (Dynamic)   : 0x55b1d8...\n5. Stack (Local)    : 0x7fffef... (Highest)"
    },
    "resources": [
      {
        "type": "gfg",
        "title": "Memory Layout of C Programs",
        "url": "https://www.geeksforgeeks.org/memory-layout-of-c-program/",
        "desc": "Curriculum link referenced in Slide 67 detailing BSS, Data, Heap, and Stack."
      },
      {
        "type": "gfg",
        "title": "Static Variables in C",
        "url": "https://www.geeksforgeeks.org/static-variables-in-c/",
        "desc": "Curriculum link referenced in Slide 67 explaining scope and lifetime of statics."
      },
      {
        "type": "tool",
        "title": "Python Tutor (C Memory Visualizer)",
        "url": "https://pythontutor.com/c.html",
        "desc": "Interactive diagramming of C stack frames, pointers, and heap blocks."
      }
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
        "question": "What happens in memory when an uninitialized global variable 'int a;' is added to a 32-bit C program, as demonstrated on Slides 68\u201369?",
        "options": [
          "The text segment size increases by 4 bytes",
          "The data segment size increases by 4 bytes",
          "The bss segment size increases by 4 bytes (from 96 to 100)",
          "The heap segment size doubles"
        ],
        "answer": 2,
        "explanation": "Slides 68\u201369 demonstrate with the `size` command that adding `int a;` increases only the `bss` column by exactly 4 bytes (96 bytes to 100 bytes)."
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
  },
  {
    "id": "m7",
    "num": 7,
    "title": "C Lexical Tokens: Keywords, Identifiers & Data Types",
    "subtitle": "The Building Blocks: 32 Keywords, Naming Rules, __func__, and Memory Containers",
    "slides": "Slides 70\u201380",
    "time": "35 mins",
    "content": "\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-graduation-cap\"></i> Teacher's Intro: The Vocabulary of C</h3>\n        <p class=\"lead-text\">\n          Just like human languages have words, punctuation, and grammar rules, a C program is constructed from tiny atomic units called <strong>Lexical Tokens</strong>.\n          Every single word or symbol you type into a <code>.c</code> source file belongs to one of these five categories:\n          <strong>Keywords</strong>, <strong>Identifiers</strong>, <strong>Constants</strong>, <strong>Operators</strong>, or <strong>Special Symbols</strong>.\n        </p>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-key\"></i> The 32 Reserved Keywords of ANSI C (Slide 70)</h3>\n        <p><strong>Keywords</strong> are words that have a fixed, permanent meaning to the C compiler. You cannot change their meaning, and you cannot use them as variable or function names.</p>\n        \n        <div class=\"teacher-callout analogy\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-traffic-light\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The Highway Traffic Sign Analogy</div>\n            <p>Keywords are like official traffic signs: <code>STOP</code>, <code>SPEED LIMIT</code>, <code>ONE WAY</code>. You cannot rename your pet dog \"STOP\" on the road without causing chaos! Similarly, C reserves exactly <strong>32 keywords</strong>. Because C is strictly case-sensitive, all 32 keywords are written in <strong>lowercase</strong>.</p>\n          </div>\n        </div>\n\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Classification</th><th>Keywords</th><th>Purpose</th></tr>\n            </thead>\n            <tbody>\n              <tr><td><strong>Data Types</strong></td><td><code>char</code>, <code>int</code>, <code>float</code>, <code>double</code>, <code>short</code>, <code>long</code>, <code>signed</code>, <code>unsigned</code>, <code>void</code></td><td>Specifies the type and size of memory containers.</td></tr>\n              <tr><td><strong>User-Defined Types</strong></td><td><code>struct</code>, <code>union</code>, <code>enum</code>, <code>typedef</code></td><td>Creates custom composite data structures.</td></tr>\n              <tr><td><strong>Storage Classes</strong></td><td><code>auto</code>, <code>register</code>, <code>static</code>, <code>extern</code></td><td>Controls lifetime, scope, and storage placement.</td></tr>\n              <tr><td><strong>Decision Making</strong></td><td><code>if</code>, <code>else</code>, <code>switch</code>, <code>case</code>, <code>default</code></td><td>Branches execution path based on conditions.</td></tr>\n              <tr><td><strong>Loops & Jumps</strong></td><td><code>for</code>, <code>do</code>, <code>while</code>, <code>break</code>, <code>continue</code>, <code>goto</code>, <code>return</code></td><td>Repeats code blocks or alters execution order.</td></tr>\n              <tr><td><strong>Type Qualifiers & Operators</strong></td><td><code>const</code>, <code>volatile</code>, <code>sizeof</code></td><td>Protects data, handles hardware I/O, weighs byte size.</td></tr>\n            </tbody>\n          </table>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-signature\"></i> Identifiers & The 5 Naming Rules (Slides 71\u201372)</h3>\n        <p><strong>Identifiers</strong> are the custom names <em>you</em> create for your variables, functions, and arrays. To prevent syntax errors, you must follow 5 golden rules:</p>\n        \n        <div class=\"comparison-card\">\n          <div class=\"comparison-header\">\n            <span><i class=\"fa-solid fa-list-check\"></i> 5 Rules for Naming C Identifiers</span>\n            <span class=\"badge\">Strictly Enforced</span>\n          </div>\n          <div class=\"comparison-grid\">\n            <div class=\"comparison-col\">\n              <h4>Rule</h4>\n              <p><strong>1. Allowed Characters:</strong> Only letters (<code>a-z</code>, <code>A-Z</code>), digits (<code>0-9</code>), and the underscore (<code>_</code>).</p>\n              <p><strong>2. First Character:</strong> Must be a letter or underscore. <em>Never a digit!</em></p>\n              <p><strong>3. Case Sensitive:</strong> Uppercase and lowercase are completely distinct.</p>\n              <p><strong>4. No Keywords:</strong> Cannot use any of the 32 reserved words.</p>\n              <p><strong>5. No Special Symbols or Spaces:</strong> No hyphens, spaces, commas, or dollar signs.</p>\n            </div>\n            <div class=\"comparison-col\">\n              <h4>Valid Examples &#10004;</h4>\n              <p><code>total_sum</code>, <code>count1</code>, <code>_index</code></p>\n              <p><code>student_age</code>, <code>_temp</code>, <code>MAX_VAL</code></p>\n              <p><code>age</code>, <code>Age</code>, and <code>AGE</code> are 3 different variables!</p>\n              <p><code>int_count</code>, <code>my_float</code>, <code>return_val</code></p>\n              <p><code>first_name</code>, <code>score_2026</code></p>\n            </div>\n            <div class=\"comparison-col\">\n              <h4>Invalid Traps &#10008; (Syntax Error!)</h4>\n              <p><code>total-sum</code> (hyphen is minus operator!), <code>total sum</code> (space!)</p>\n              <p><code>1st_number</code> (starts with digit '1'!), <code>9lives</code></p>\n              <p>Expecting <code>Total</code> to read <code>total</code> leads to \"undeclared identifier\".</p>\n              <p><code>int float;</code> or <code>int return;</code> (Keywords!)</p>\n              <p><code>emp$salary</code>, <code>user#id</code>, <code>test@mail</code></p>\n            </div>\n          </div>\n        </div>\n\n        <div class=\"teacher-callout insight\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-sparkles\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The C99/C11 Magic Identifier: __func__ (Slide 72)</div>\n            <p>C99 introduced a built-in predefined identifier: <code>__func__</code>. Whenever you reference it inside any function, the compiler treats it as:\n            <br><code>static const char __func__[] = \"name_of_current_function\";</code>\n            <br>Calling <code>printf(\"Inside: %s\\n\", __func__);</code> inside <code>main()</code> prints <code>\"Inside: main\"</code>. Systems programmers use it everywhere for debug logging!</p>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-boxes-stacked\"></i> Data Types: Memory Containers & Capacities (Slides 73\u201380)</h3>\n        <p>In C, a <strong>data type</strong> tells the compiler two critical facts: <strong>how many bytes of RAM to reserve</strong>, and <strong>how to interpret the bits inside</strong>.</p>\n        \n        <div class=\"teacher-callout analogy\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-mug-hot\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The Beverage Container Analogy</div>\n            <p>\n              &bull; <code>char</code> (1 byte) = An espresso cup (holds 1 character or tiny number -128 to 127).<br>\n              &bull; <code>short</code> (2 bytes) = A coffee mug (holds numbers -32,768 to 32,767).<br>\n              &bull; <code>int</code> (4 bytes) = A 1-liter water bottle (holds numbers up to $\\pm 2.14$ billion).<br>\n              &bull; <code>long long</code> (8 bytes) = A giant water gallon (holds quintillions up to $\\approx \\pm 9.22 \\times 10^{18}$).<br>\n              &bull; <code>float</code> / <code>double</code> = Containers equipped with a decimal measuring syringe!\n            </p>\n          </div>\n        </div>\n\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Data Type</th><th>Size (Bytes)</th><th>Bits</th><th>Value Range (32/64-bit GCC)</th><th>Format Specifier</th></tr>\n            </thead>\n            <tbody>\n              <tr><td><code>char</code></td><td>1 byte</td><td>8</td><td>-128 to 127 (signed)</td><td><code>%c</code> or <code>%d</code></td></tr>\n              <tr><td><code>unsigned char</code></td><td>1 byte</td><td>8</td><td>0 to 255</td><td><code>%c</code> or <code>%u</code></td></tr>\n              <tr><td><code>short int</code></td><td>2 bytes</td><td>16</td><td>-32,768 to 32,767</td><td><code>%hd</code></td></tr>\n              <tr><td><code>unsigned short</code></td><td>2 bytes</td><td>16</td><td>0 to 65,535</td><td><code>%hu</code></td></tr>\n              <tr><td><code>int</code></td><td>4 bytes</td><td>32</td><td>-2,147,483,648 to 2,147,483,647 ($-2^{31}$ to $2^{31}-1$)</td><td><code>%d</code> or <code>%i</code></td></tr>\n              <tr><td><code>unsigned int</code></td><td>4 bytes</td><td>32</td><td>0 to 4,294,967,295 ($0$ to $2^{32}-1$)</td><td><code>%u</code></td></tr>\n              <tr><td><code>long int</code></td><td>4 / 8 bytes</td><td>32 / 64</td><td>At least 32 bits ($-2^{31}$ to $2^{31}-1$)</td><td><code>%ld</code></td></tr>\n              <tr><td><code>long long int</code></td><td>8 bytes</td><td>64</td><td>$-2^{63}$ to $2^{63}-1$ ($\\approx \\pm 9.22 \\times 10^{18}$)</td><td><code>%lld</code></td></tr>\n              <tr><td><code>float</code></td><td>4 bytes</td><td>32</td><td>$\\pm 3.4 \\times 10^{-38}$ to $\\pm 3.4 \\times 10^{38}$ (6 decimals precision)</td><td><code>%f</code></td></tr>\n              <tr><td><code>double</code></td><td>8 bytes</td><td>64</td><td>$\\pm 1.7 \\times 10^{-308}$ to $\\pm 1.7 \\times 10^{308}$ (15 decimals precision)</td><td><code>%lf</code></td></tr>\n              <tr><td><code>void</code></td><td>0 bytes</td><td>0</td><td>Valueless / empty type (functions returning nothing or generic pointers)</td><td>N/A</td></tr>\n            </tbody>\n          </table>\n        </div>\n\n        <div class=\"teacher-callout exam-alert\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-scale-balanced\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">sizeof Operator & &lt;limits.h&gt; (Slide 80)</div>\n            <p><strong>Crucial Exam Fact:</strong> <code>sizeof</code> is NOT a function; it is a <strong>compile-time unary operator</strong>! The compiler calculates the byte size during compilation and replaces <code>sizeof(int)</code> with the literal number <code>4</code>.\n            To inspect host-specific numeric limits, include <code>&lt;limits.h&gt;</code> for constants like <code>INT_MAX</code>, <code>INT_MIN</code>, and <code>CHAR_BIT</code>.</p>\n          </div>\n        </div>\n      </div>\n    ",
    "code": {
      "title": "Verifying Data Types, Limits & __func__ in C",
      "desc": "Inspecting datatypes, compile-time sizeof evaluations, and the predefined identifier __func__.",
      "lang": "c",
      "snippet": "#include <stdio.h>\n#include <limits.h>\n\nvoid show_demo(void) {\n    // C99 __func__ magic identifier\n    printf(\"Executing inside function: %s\\n\", __func__);\n}\n\nint main(void) {\n    show_demo();\n\n    printf(\"sizeof(char)      = %zu byte  [Range: %d to %d]\\n\", sizeof(char), CHAR_MIN, CHAR_MAX);\n    printf(\"sizeof(short)     = %zu bytes [Range: %d to %d]\\n\", sizeof(short), SHRT_MIN, SHRT_MAX);\n    printf(\"sizeof(int)       = %zu bytes [Range: %d to %d]\\n\", sizeof(int), INT_MIN, INT_MAX);\n    printf(\"sizeof(long long) = %zu bytes\\n\", sizeof(long long));\n    printf(\"sizeof(float)     = %zu bytes\\n\", sizeof(float));\n    printf(\"sizeof(double)    = %zu bytes\\n\", sizeof(double));\n\n    return 0;\n}",
      "output": "Executing inside function: show_demo\nsizeof(char)      = 1 byte  [Range: -128 to 127]\nsizeof(short)     = 2 bytes [Range: -32768 to 32767]\nsizeof(int)       = 4 bytes [Range: -2147483648 to 2147483647]\nsizeof(long long) = 8 bytes\nsizeof(float)     = 4 bytes\nsizeof(double)    = 8 bytes"
    },
    "resources": [
      {
        "type": "gfg",
        "title": "C Data Types & Value Ranges",
        "url": "https://www.geeksforgeeks.org/data-types-in-c/",
        "desc": "Curriculum link referenced in Slide 73 detailing primitive, derived, and user types."
      },
      {
        "type": "gfg",
        "title": "The __func__ Predefined Identifier in C",
        "url": "https://www.geeksforgeeks.org/c-predefined-identifier-__func__/",
        "desc": "Curriculum link referenced in Slide 72 exploring C99 diagnostic logging."
      },
      {
        "type": "docs",
        "title": "GNU C Reference Manual: Keywords",
        "url": "https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html",
        "desc": "Official GNU documentation detailing ANSI and ISO C keywords."
      }
    ],
    "quiz": [
      {
        "id": "q7_1",
        "question": "Which of the following is a VALID identifier name according to ANSI C naming rules (Slide 71)?",
        "options": [
          "2nd_number",
          "_total_sum",
          "float",
          "user-name"
        ],
        "answer": 1,
        "explanation": "Identifiers can only contain alphanumeric characters and underscores, and cannot start with a digit or match a keyword. '_total_sum' is valid because starting with an underscore is permitted."
      },
      {
        "id": "q7_2",
        "question": "How many reserved keywords are specified in the ANSI C standard (Slide 70)?",
        "options": [
          "16",
          "32",
          "48",
          "64"
        ],
        "answer": 1,
        "explanation": "Slide 70 explicitly enumerates the 32 reserved keywords of ANSI C, including 'auto', 'int', 'return', 'switch', etc."
      },
      {
        "id": "q7_3",
        "question": "What is the nature of the 'sizeof' construct in C (Slide 80)?",
        "options": [
          "It is a runtime library function defined in <stdio.h>",
          "It is a compile-time operator whose value is evaluated by the compiler during translation",
          "It is a preprocessor macro directive",
          "It is a system call to the operating system kernel"
        ],
        "answer": 1,
        "explanation": "Slide 80 clarifies that sizeof is a compile-time operator, not a function. Its operand is evaluated at compilation to determine memory requirements."
      },
      {
        "id": "q7_4",
        "question": "What does the C99 predefined identifier '__func__' hold when evaluated inside a function (Slide 72)?",
        "options": [
          "A pointer to the function's machine code in the text segment",
          "A null-terminated string containing the name of the currently executing function",
          "The number of arguments passed into the function",
          "The return value of the function"
        ],
        "answer": 1,
        "explanation": "Slide 72 explains that C99/C11 injects '__func__' as a static const char array holding the function's name (e.g. \"main\")."
      },
      {
        "id": "q7_5",
        "question": "What is the typical memory size and value range of a standard signed 32-bit integer in C (Slide 78)?",
        "options": [
          "2 bytes: -32,768 to 32,767",
          "4 bytes: -2,147,483,648 to 2,147,483,647 (-2^31 to 2^31 - 1)",
          "8 bytes: 0 to 18 quintillion",
          "1 byte: -128 to 127"
        ],
        "answer": 1,
        "explanation": "On 32-bit and 64-bit systems, a signed 32-bit int occupies 4 bytes (32 bits) spanning from -2,147,483,648 to +2,147,483,647."
      }
    ]
  },
  {
    "id": "m8",
    "num": 8,
    "title": "Variables, Constants & Escape Sequences",
    "subtitle": "Scope, Shadowing, #define vs const, Escape Sequences & Syntax vs Semantic Errors",
    "slides": "Slides 81\u2013106",
    "time": "40 mins",
    "content": "\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-map-pin\"></i> Variable Scope: Local vs. Global (Slides 84\u201387)</h3>\n        <p>A variable's <strong>scope</strong> defines where in the program that variable is visible and accessible.</p>\n        \n        <div class=\"teacher-callout analogy\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-lightbulb\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The Desk Lamp vs. Street Lamp Analogy (Variable Shadowing)</div>\n            <p>\n              &bull; <strong>Global Variables:</strong> Declared outside all functions. Like a <strong>street lamp outside</strong>\u2014visible to everyone on the entire block.<br>\n              &bull; <strong>Local Variables:</strong> Declared inside a specific function or block <code>{ ... }</code>. Like a <strong>desk lamp inside your bedroom</strong>\u2014visible only to you inside your room.<br>\n              &bull; <strong>Variable Shadowing (Slide 87):</strong> What if your desk lamp and the street lamp have the same name? Inside your room, your local desk lamp <strong>takes priority and shadows</strong> the street lamp! The global variable remains completely untouched outside.\n            </p>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-lock\"></i> Constants: #define vs. const (Slide 88)</h3>\n        <p>A <strong>constant</strong> is an entity whose stored value cannot be modified during program execution. C provides two ways to declare constants:</p>\n\n        <div class=\"comparison-card\">\n          <div class=\"comparison-header\">\n            <span><i class=\"fa-solid fa-balance-scale\"></i> #define Macro vs const Variable (Slide 88)</span>\n            <span class=\"badge\">Architecture Comparison</span>\n          </div>\n          <div class=\"comparison-grid\">\n            <div class=\"comparison-col\">\n              <h4>Aspect</h4>\n              <p><strong>Stage Handled</strong></p>\n              <p><strong>Memory Allocated?</strong></p>\n              <p><strong>Type Safety</strong></p>\n              <p><strong>Scope</strong></p>\n              <p><strong>Syntax Example</strong></p>\n            </div>\n            <div class=\"comparison-col\">\n              <h4>#define (Preprocessor Macro)</h4>\n              <p>Handled during <strong>Preprocessing</strong> (Stage 1).</p>\n              <p><strong>No memory allocated</strong>; pure text find-and-replace.</p>\n              <p>No type checking (blind text substitution).</p>\n              <p>File-wide scope from definition onward.</p>\n              <p><code>#define PI 3.14159</code> (no semicolon!)</p>\n            </div>\n            <div class=\"comparison-col\">\n              <h4>const Variable (Compiler Enforced)</h4>\n              <p>Handled during <strong>Compilation</strong> (Stage 2).</p>\n              <p><strong>Allocates memory</strong> in the <code>.rodata</code> read-only segment.</p>\n              <p>Strict datatype checking enforced by compiler.</p>\n              <p>Respects block scope (local to its function).</p>\n              <p><code>const float PI = 3.14159f;</code></p>\n            </div>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-terminal\"></i> Escape Sequences: Non-Printable Characters (Slides 94\u201396)</h3>\n        <p>Escape sequences begin with a backslash (<code>\\</code>) and tell the terminal or printer to perform special formatting actions:</p>\n\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Sequence</th><th>Name</th><th>Action / Real-World Behavior</th></tr>\n            </thead>\n            <tbody>\n              <tr><td><code>\\n</code></td><td>Newline</td><td>Moves cursor down to the beginning of the next line.</td></tr>\n              <tr><td><code>\\t</code></td><td>Horizontal Tab</td><td>Advances cursor to the next tab stop (typically multiples of 8 columns).</td></tr>\n              <tr><td><code>\\r</code></td><td>Carriage Return</td><td>Moves cursor all the way back to the <strong>start of the current line</strong>! Subsequent characters overwrite existing ones.</td></tr>\n              <tr><td><code>\\b</code></td><td>Backspace</td><td>Moves cursor back by one character position without erasing.</td></tr>\n              <tr><td><code>\\\\</code></td><td>Backslash</td><td>Prints a literal backslash character <code>\\</code>.</td></tr>\n              <tr><td><code>\\\"</code></td><td>Double Quote</td><td>Prints a literal quote character <code>\"</code> inside a string literal.</td></tr>\n              <tr><td><code>\\072</code></td><td>Octal Escape</td><td>Interprets digits after <code>\\</code> as octal. <code>\\072</code> = decimal 58 = ASCII <code>':'</code> (Slide 94).</td></tr>\n              <tr><td><code>\\x4a</code></td><td>Hex Escape</td><td>Interprets digits after <code>\\x</code> as hex. <code>\\x4a</code> = decimal 74 = ASCII <code>'J'</code> (Slide 94).</td></tr>\n            </tbody>\n          </table>\n        </div>\n\n        <div class=\"teacher-callout insight\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-keyboard\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The Secret of Carriage Return (\\r)</div>\n            <p>On vintage mechanical typewriters, a physical carriage held the paper. Striking \"Carriage Return\" returned the carriage to the left margin without moving to the next line!\n            <br>In C: <code>printf(\"Hello friend\\rend\\n\");</code> prints <code>\"endlo friend\"</code> because <code>\\r</code> moves the cursor to column 0, where <code>\"end\"</code> overwrites <code>\"Hel\"</code>!</p>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-bug\"></i> Syntax Errors vs. Semantic Errors (Slides 102\u2013104)</h3>\n        <p>Every programmer must distinguish between grammar bugs and logic bugs:</p>\n        \n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Aspect</th><th>Syntax Error (Grammar)</th><th>Semantic Error (Meaning / Logic)</th></tr>\n            </thead>\n            <tbody>\n              <tr><td><strong>Definition</strong></td><td>Violation of the grammatical rules of the C programming language.</td><td>The code follows grammar rules, but the logic does not match programmer intent.</td></tr>\n              <tr><td><strong>Detection</strong></td><td>Caught at <strong>Compile Time</strong> by <code>cc1</code>; binary will NOT be built.</td><td>Compiles cleanly without errors, but produces wrong output at <strong>Runtime</strong>.</td></tr>\n              <tr><td><strong>Everyday Analogy</strong></td><td>\"Dog the barked loud.\" (Grammar order broken).</td><td>\"The dog flew to the moon.\" (Grammatically valid, but nonsense in reality!).</td></tr>\n              <tr><td><strong>Slide 103 Example</strong></td><td>Missing semicolon <code>;</code> or mismatched braces <code>{</code>.</td><td>Placing <code>return 0;</code> before <code>printf(\"Hello\");</code>! The function terminates before printing!</td></tr>\n            </tbody>\n          </table>\n        </div>\n      </div>\n    ",
    "code": {
      "title": "Variable Shadowing, Escape Sequences & Semantic Bug Demo (Slides 87, 94, 103)",
      "desc": "Testing variable shadowing, carriage return overwriting, octal/hex escapes, and unreachable statements.",
      "lang": "c",
      "snippet": "#include <stdio.h>\n\nint g = 20; // Global variable (Street lamp)\n\nint main(void) {\n    int g = 10; // Local variable (Desk lamp) shadows global!\n    printf(\"Local variable shadows global: g = %d\\n\", g);\n\n    // Escape sequences from Slide 94:\n    // Octal \\072 = 58 (':'), \\065 = 53 ('5')\n    char* s = \"A\\072\\065\";\n    // Hex \\x4a = 74 ('J')\n    char* y = \"B\\x4a\";\n    printf(\"Octal escape string: %s\\n\", s);\n    printf(\"Hex escape string  : %s\\n\", y);\n\n    // Carriage return demo\n    printf(\"Hello friend\\rend\\n\");\n\n    return 0;\n}",
      "output": "Local variable shadows global: g = 10\nOctal escape string: A:5\nHex escape string  : BJ\nendlo friend"
    },
    "resources": [
      {
        "type": "gfg",
        "title": "Differences Between Syntax and Semantics",
        "url": "https://www.geeksforgeeks.org/difference-between-syntax-and-semantics/",
        "desc": "Curriculum reference from Slide 102 exploring compiler vs runtime errors."
      },
      {
        "type": "tool",
        "title": "ASCII Table and Description",
        "url": "https://www.asciitable.com",
        "desc": "Reference table for character decimal, hex, and octal mappings."
      },
      {
        "type": "docs",
        "title": "TotalView: What Does a Debugger Do?",
        "url": "https://totalview.io/blog/what-does-debugger-do",
        "desc": "Curriculum link referenced in Slide 100 on analyzing bugs and breakpoints."
      }
    ],
    "quiz": [
      {
        "id": "q8_1",
        "question": "What happens when a local variable inside main() has the exact same name as a global variable declared outside main() (Slide 87)?",
        "options": [
          "The compiler issues a duplicate symbol error",
          "The local variable takes precedence within main(), hiding (shadowing) the global variable",
          "The global variable overrides the local variable",
          "Both values are added together"
        ],
        "answer": 1,
        "explanation": "Slide 87 explicitly states: 'A program can have same name for local and global variables but the value of local variable inside a function will take preference.'"
      },
      {
        "id": "q8_2",
        "question": "How is an octal integer constant designated in C source code (Slide 90)?",
        "options": [
          "By prefixing the number with '0x'",
          "By prefixing the number with a leading zero '0' (e.g. 045)",
          "By suffixing the number with 'O'",
          "By enclosing the digits in parentheses"
        ],
        "answer": 1,
        "explanation": "Slide 90: Octal integer constants use digits 0 to 7 and are designated by adding a leading '0' before the value (e.g. 045, 056, 067)."
      },
      {
        "id": "q8_3",
        "question": "What will printf(\"%s\", \"A\\072\\065\"); output on a standard terminal (Slide 94)?",
        "options": [
          "A072065",
          "A:5",
          "A\\072\\065",
          "Compilation Error"
        ],
        "answer": 1,
        "explanation": "In octal, 072 is decimal 58 (which corresponds to ASCII ':') and 065 is decimal 53 (ASCII '5'). Thus, it prints 'A:5' (Slide 94)."
      },
      {
        "id": "q8_4",
        "question": "Which of the following describes a Semantic Error in C programming (Slide 102\u2013104)?",
        "options": [
          "Omitting a semicolon at the end of a statement",
          "Typing 'pintf' instead of 'printf'",
          "Placing 'return 0;' before 'printf(\"Hello\");' causing the program to terminate prematurely without printing",
          "Using an uppercase 'INT' keyword"
        ],
        "answer": 2,
        "explanation": "Slide 103-104: A semantic error occurs when code obeys all grammatical syntax rules but fails to express the programmer's intended logical meaning, such as returning before printing."
      },
      {
        "id": "q8_5",
        "question": "What is the primary difference between #define and const in C (Slide 88)?",
        "options": [
          "#define is handled by the preprocessor via text substitution, whereas const is a typed, scoped variable enforced by the compiler",
          "#define only works for integers, while const only works for floats",
          "const values can be modified at runtime, while #define cannot",
          "There is no difference between them"
        ],
        "answer": 0,
        "explanation": "Slide 88 explains both mechanisms. #define is a textual preprocessor macro substitution, while const declares a typed, memory-aware read-only variable validated by the compiler."
      }
    ]
  },
  {
    "id": "m9",
    "num": 9,
    "title": "C Operators & Expressions Deep Dive",
    "subtitle": "No BODMAS in C, Precedence, Step-by-Step Bitwise Mastery & Two's Complement (~35 = -36)",
    "slides": "Slides 107\u2013133",
    "time": "45 mins",
    "content": "\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-bolt\"></i> The Crucial Myth: There is NO BODMAS in C! (Slide 107)</h3>\n        <p class=\"lead-text\">\n          In elementary school, you were taught the BODMAS rule (Brackets, Orders, Division, Multiplication, Addition, Subtraction).\n          <strong>Forget BODMAS when writing or reading C code!</strong>\n        </p>\n\n        <div class=\"teacher-callout pitfall\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-triangle-exclamation\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">Precedence and Associativity Dictate Evaluation (Slide 107)</div>\n            <p>Slide 107 emphasizes: <em>\"There is no BODMAS in C language. Precedence and Associativity are two characteristics of operators that determine the evaluation order of subexpressions in absence of brackets.\"</em></p>\n            <p>\n              &bull; <strong>Precedence:</strong> Determines <em>which</em> operator grabs its operands first when different operators compete (e.g. <code>*</code> binds before <code>+</code> in <code>3 + 4 * 5 = 23</code>).<br>\n              &bull; <strong>Associativity:</strong> Determines the evaluation direction (<strong>Left-to-Right</strong> or <strong>Right-to-Left</strong>) when multiple operators share the <em>same</em> precedence level!\n            </p>\n          </div>\n        </div>\n\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>Priority Tier</th><th>Operators</th><th>Description</th><th>Associativity</th></tr>\n            </thead>\n            <tbody>\n              <tr><td><strong>Tier 1 (Highest)</strong></td><td><code>()</code>, <code>[]</code>, <code>-&gt;</code>, <code>.</code></td><td>Parentheses, array subscript, structure access</td><td>Left-to-Right</td></tr>\n              <tr><td><strong>Tier 2 (Unary)</strong></td><td><code>++</code>, <code>--</code>, <code>+</code>, <code>-</code>, <code>!</code>, <code>~</code>, <code>*</code>, <code>&amp;</code>, <code>sizeof</code></td><td>Prefix inc/dec, logical/bitwise NOT, address-of, dereference</td><td><strong>Right-to-Left</strong></td></tr>\n              <tr><td><strong>Tier 3 (Multiplicative)</strong></td><td><code>*</code>, <code>/</code>, <code>%</code></td><td>Multiplication, division, modulo remainder</td><td>Left-to-Right</td></tr>\n              <tr><td><strong>Tier 4 (Additive)</strong></td><td><code>+</code>, <code>-</code></td><td>Addition and subtraction</td><td>Left-to-Right</td></tr>\n              <tr><td><strong>Tier 5 (Bitwise Shifts)</strong></td><td><code>&lt;&lt;</code>, <code>&gt;&gt;</code></td><td>Left shift (multiply by $2^k$), right shift (divide by $2^k$)</td><td>Left-to-Right</td></tr>\n              <tr><td><strong>Tier 6 (Relational)</strong></td><td><code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code>, <code>&gt;=</code></td><td>Relational inequalities</td><td>Left-to-Right</td></tr>\n              <tr><td><strong>Tier 7 (Equality)</strong></td><td><code>==</code>, <code>!=</code></td><td>Equal to, not equal to</td><td>Left-to-Right</td></tr>\n              <tr><td><strong>Tier 8 to 10 (Bitwise)</strong></td><td><code>&amp;</code>, <code>^</code>, <code>|</code></td><td>Bitwise AND, Bitwise XOR, Bitwise OR</td><td>Left-to-Right</td></tr>\n              <tr><td><strong>Tier 11 to 12 (Logical)</strong></td><td><code>&amp;&amp;</code>, <code>||</code></td><td>Logical AND, Logical OR (Short-circuiting!)</td><td>Left-to-Right</td></tr>\n              <tr><td><strong>Tier 13 (Ternary)</strong></td><td><code>? :</code></td><td>Conditional expression</td><td><strong>Right-to-Left</strong></td></tr>\n              <tr><td><strong>Tier 14 (Assignment)</strong></td><td><code>=</code>, <code>+=</code>, <code>-=</code>, <code>*=</code>, etc.</td><td>Simple & compound assignment</td><td><strong>Right-to-Left</strong></td></tr>\n              <tr><td><strong>Tier 15 (Lowest)</strong></td><td><code>,</code></td><td>Comma operator (sequence point)</td><td>Left-to-Right</td></tr>\n            </tbody>\n          </table>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-calculator\"></i> Arithmetic, Increment & Chaining Traps (Slides 111\u2013117)</h3>\n        <ul>\n          <li><strong>Integer Division (<code>/</code>):</strong> In C, <code>10 / 4</code> produces <code>2</code>, NOT <code>2.5</code>! Any fractional decimal is cleanly truncated toward zero. To preserve fractions, at least one operand must be a float: <code>10.0 / 4 = 2.5</code>.</li>\n          <li><strong>Modulo Division (<code>%</code>):</strong> Returns the integer remainder (e.g. <code>10 % 3 = 1</code>). Modulo is <strong>strictly prohibited</strong> on floating-point numbers! <code>10.5 % 3</code> is a fatal compiler error.</li>\n          <li><strong>Prefix Increment (<code>++x</code>):</strong> <em>\"Pay first, ride later.\"</em> Value increments immediately, and the newly incremented value is returned.</li>\n          <li><strong>Postfix Increment (<code>x++</code>):</strong> <em>\"Ride now, pay later.\"</em> Current value is returned for the expression first, and only incremented after the evaluation completes.</li>\n        </ul>\n\n        <div class=\"teacher-callout exam-alert\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-triangle-exclamation\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The Chaining Trap: d = a &gt; b &lt; c (Slide 117)</div>\n            <p>Suppose: <code>int a = 1, b = 2, c = 3; int d = a &gt; b &lt; c;</code></p>\n            <p>Because relational operators associate <strong>Left-to-Right</strong>:\n            <br>1. First evaluate: <code>(a &gt; b)</code> &rarr; <code>(1 &gt; 2)</code> evaluates to <strong>0 (False)</strong>.\n            <br>2. Next evaluate: <code>0 &lt; c</code> &rarr; <code>(0 &lt; 3)</code> evaluates to <strong>1 (True)</strong>!\n            <br>Therefore, <code>d</code> is assigned <strong>1</strong>! (Even though in mathematics $1 > 2 < 3$ is nonsense).</p>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-shield-halved\"></i> Short-Circuiting in Logical Operators (Slides 120\u2013123)</h3>\n        <p>In C, <code>&amp;&amp;</code> (Logical AND) and <code>||</code> (Logical OR) employ <strong>Short-Circuit Evaluation</strong> (Lazy Evaluation):</p>\n        <ul>\n          <li><strong>In <code>A &amp;&amp; B</code>:</strong> If <code>A</code> evaluates to <strong>0 (False)</strong>, the entire expression is already known to be False. The compiler <strong>skips evaluating B entirely</strong>! (Slide 122: in <code>(10 == 4) &amp;&amp; printf(\"Hi\")</code>, <code>printf</code> is never executed!).</li>\n          <li><strong>In <code>A || B</code>:</strong> If <code>A</code> evaluates to <strong>non-zero (True)</strong>, the expression is already known to be True. The compiler <strong>skips evaluating B entirely</strong>! (Slide 123: in <code>(10 != 4) || printf(\"Hi\")</code>, <code>printf</code> is never executed!).</li>\n        </ul>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-microchip\"></i> Bitwise Mastery: Step-by-Step Explanation Process (Slides 124\u2013129)</h3>\n        <p class=\"lead-text\">\n          Bitwise operators allow you to reach directly into the CPU registers and manipulate individual binary <code>0</code>s and <code>1</code>s in a single clock cycle. Follow this step-by-step masterclass:\n        </p>\n\n        <!-- STEP 1: The Core Mental Model -->\n        <div class=\"step-guide-card\">\n          <div class=\"step-badge\">STEP 1</div>\n          <div class=\"step-content\">\n            <h4>The Light Switch Foundation: What is a Bit?</h4>\n            <p>Imagine a light switch on the wall: it has only two states: <strong>0 (OFF / open circuit)</strong> and <strong>1 (ON / closed circuit)</strong>. In computer memory, an 8-bit number is literally a row of 8 tiny transistor switches. Bitwise operators evaluate these switches column-by-column with blazing speed.</p>\n          </div>\n        </div>\n\n        <!-- STEP 2: The 4 Core Gates Explained Step-by-Step -->\n        <div class=\"step-guide-card\">\n          <div class=\"step-badge\">STEP 2</div>\n          <div class=\"step-content\">\n            <h4>The 4 Core Bitwise Gates: Mental Models &amp; Truth Tables</h4>\n            <p>Every gate has a distinct physical circuit analogy and truth rule:</p>\n\n            <div class=\"bitwise-grid\">\n              <!-- AND -->\n              <div class=\"bitwise-card\">\n                <div class=\"bitwise-card-header and\">\n                  <span class=\"gate-symbol\">&amp;</span>\n                  <span class=\"gate-name\">Bitwise AND</span>\n                  <span class=\"gate-tag\">Series Circuit</span>\n                </div>\n                <div class=\"bitwise-card-body\">\n                  <p class=\"analogy-text\"><strong>Circuit Rule:</strong> Two switches in a row on the same wire. Current flows <strong>ONLY if BOTH switches are ON</strong> (1). If either is 0, the lamp is dark.</p>\n                  <table class=\"mini-truth-table\">\n                    <thead><tr><th>A</th><th>B</th><th>A &amp; B</th></tr></thead>\n                    <tbody>\n                      <tr><td>0</td><td>0</td><td class=\"res-0\">0</td></tr>\n                      <tr><td>0</td><td>1</td><td class=\"res-0\">0</td></tr>\n                      <tr><td>1</td><td>0</td><td class=\"res-0\">0</td></tr>\n                      <tr><td>1</td><td>1</td><td class=\"res-1\">1</td></tr>\n                    </tbody>\n                  </table>\n                  <div class=\"real-use\">\n                    <strong>Real-World Use:</strong> <em>Masking &amp; Clearing.</em>\n                    <br>Check if odd: <code>(num &amp; 1)</code> tests if the lowest bit is 1.\n                  </div>\n                </div>\n              </div>\n\n              <!-- OR -->\n              <div class=\"bitwise-card\">\n                <div class=\"bitwise-card-header or\">\n                  <span class=\"gate-symbol\">|</span>\n                  <span class=\"gate-name\">Bitwise OR</span>\n                  <span class=\"gate-tag\">Parallel Circuit</span>\n                </div>\n                <div class=\"bitwise-card-body\">\n                  <p class=\"analogy-text\"><strong>Circuit Rule:</strong> Two parallel wires. Current flows if <strong>EITHER switch (or both) is ON</strong> (1). Only turns off if both are 0.</p>\n                  <table class=\"mini-truth-table\">\n                    <thead><tr><th>A</th><th>B</th><th>A | B</th></tr></thead>\n                    <tbody>\n                      <tr><td>0</td><td>0</td><td class=\"res-0\">0</td></tr>\n                      <tr><td>0</td><td>1</td><td class=\"res-1\">1</td></tr>\n                      <tr><td>1</td><td>0</td><td class=\"res-1\">1</td></tr>\n                      <tr><td>1</td><td>1</td><td class=\"res-1\">1</td></tr>\n                    </tbody>\n                  </table>\n                  <div class=\"real-use\">\n                    <strong>Real-World Use:</strong> <em>Setting Flags / Turning Bits ON.</em>\n                    <br>Turn on permission bit without altering other bits: <code>perms |= 0x04;</code>\n                  </div>\n                </div>\n              </div>\n\n              <!-- XOR -->\n              <div class=\"bitwise-card\">\n                <div class=\"bitwise-card-header xor\">\n                  <span class=\"gate-symbol\">^</span>\n                  <span class=\"gate-name\">Bitwise XOR</span>\n                  <span class=\"gate-tag\">Difference Detector</span>\n                </div>\n                <div class=\"bitwise-card-body\">\n                  <p class=\"analogy-text\"><strong>Circuit Rule:</strong> Staircase 2-way switch. Lamp is ON <strong>ONLY when switches are in DIFFERENT directions</strong> (one UP, one DOWN)!</p>\n                  <table class=\"mini-truth-table\">\n                    <thead><tr><th>A</th><th>B</th><th>A ^ B</th></tr></thead>\n                    <tbody>\n                      <tr><td>0</td><td>0</td><td class=\"res-0\">0</td></tr>\n                      <tr><td>0</td><td>1</td><td class=\"res-1\">1</td></tr>\n                      <tr><td>1</td><td>0</td><td class=\"res-1\">1</td></tr>\n                      <tr><td>1</td><td>1</td><td class=\"res-0\">0</td></tr>\n                    </tbody>\n                  </table>\n                  <div class=\"real-use\">\n                    <strong>Real-World Use:</strong> <em>Toggling &amp; Variable Swapping.</em>\n                    <br>Swap two numbers without temp: <code>a^=b; b^=a; a^=b;</code>\n                  </div>\n                </div>\n              </div>\n\n              <!-- NOT -->\n              <div class=\"bitwise-card\">\n                <div class=\"bitwise-card-header not\">\n                  <span class=\"gate-symbol\">~</span>\n                  <span class=\"gate-name\">Bitwise NOT</span>\n                  <span class=\"gate-tag\">Inverter Mirror</span>\n                </div>\n                <div class=\"bitwise-card-body\">\n                  <p class=\"analogy-text\"><strong>Circuit Rule:</strong> Unary inverter gate. Flips every single <code>0</code> into <code>1</code>, and every single <code>1</code> into <code>0</code>.</p>\n                  <table class=\"mini-truth-table\">\n                    <thead><tr><th>A</th><th>~A</th><th>Action</th></tr></thead>\n                    <tbody>\n                      <tr><td>0</td><td class=\"res-1\">1</td><td>Flips to 1</td></tr>\n                      <tr><td>1</td><td class=\"res-0\">0</td><td>Flips to 0</td></tr>\n                    </tbody>\n                  </table>\n                  <div class=\"real-use\">\n                    <strong>Real-World Use:</strong> <em>One's Complement &amp; Bit Inversion.</em>\n                    <br>Creates inverse masks for zeroing bits: <code>x &amp;= ~FLAG;</code>\n                  </div>\n                </div>\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <!-- STEP 3: Real Numbers Step-by-Step Column Alignment -->\n        <div class=\"step-guide-card\">\n          <div class=\"step-badge\">STEP 3</div>\n          <div class=\"step-content\">\n            <h4>Bit-by-Bit Column Alignment: Computing A = 12 and B = 10</h4>\n            <p>Let's trace how the CPU calculates these operations bit-by-bit on two 8-bit integers: $A = 12$ ($0000\\ 1100_2$) and $B = 10$ ($0000\\ 1010_2$):</p>\n            \n            <div class=\"bit-matrix-card\">\n              <div class=\"bit-matrix-title\">\n                <i class=\"fa-solid fa-table-cells\"></i> Step-by-Step Bit Alignment Matrix\n              </div>\n              <table class=\"bit-matrix-table\">\n                <thead>\n                  <tr>\n                    <th class=\"row-label\">Operand / Operation</th>\n                    <th>b7 (128)</th><th>b6 (64)</th><th>b5 (32)</th><th>b4 (16)</th>\n                    <th>b3 (8)</th><th>b2 (4)</th><th>b1 (2)</th><th>b0 (1)</th>\n                    <th class=\"row-label\">Decimal Result</th>\n                  </tr>\n                </thead>\n                <tbody>\n                  <tr>\n                    <td class=\"row-label\">Operand A (12)</td>\n                    <td class=\"bit-cell zero\">0</td><td class=\"bit-cell zero\">0</td><td class=\"bit-cell zero\">0</td><td class=\"bit-cell zero\">0</td>\n                    <td class=\"bit-cell highlight\">1</td><td class=\"bit-cell highlight\">1</td><td class=\"bit-cell zero\">0</td><td class=\"bit-cell zero\">0</td>\n                    <td class=\"row-label\"><strong>12</strong></td>\n                  </tr>\n                  <tr>\n                    <td class=\"row-label\">Operand B (10)</td>\n                    <td class=\"bit-cell zero\">0</td><td class=\"bit-cell zero\">0</td><td class=\"bit-cell zero\">0</td><td class=\"bit-cell zero\">0</td>\n                    <td class=\"bit-cell highlight\">1</td><td class=\"bit-cell zero\">0</td><td class=\"bit-cell highlight\">1</td><td class=\"bit-cell zero\">0</td>\n                    <td class=\"row-label\"><strong>10</strong></td>\n                  </tr>\n                  <tr class=\"res-row\">\n                    <td class=\"row-label\">A &amp; B (AND: both 1)</td>\n                    <td class=\"bit-result-cell\">0</td><td class=\"bit-result-cell\">0</td><td class=\"bit-result-cell\">0</td><td class=\"bit-result-cell\">0</td>\n                    <td class=\"bit-result-cell highlight\">1</td><td class=\"bit-result-cell\">0</td><td class=\"bit-result-cell\">0</td><td class=\"bit-result-cell\">0</td>\n                    <td class=\"row-label\"><strong>8</strong> (Only bit 3 is 1 in both)</td>\n                  </tr>\n                  <tr class=\"res-row\">\n                    <td class=\"row-label\">A | B (OR: either 1)</td>\n                    <td class=\"bit-result-cell\">0</td><td class=\"bit-result-cell\">0</td><td class=\"bit-result-cell\">0</td><td class=\"bit-result-cell\">0</td>\n                    <td class=\"bit-result-cell highlight\">1</td><td class=\"bit-result-cell highlight\">1</td><td class=\"bit-result-cell highlight\">1</td><td class=\"bit-result-cell\">0</td>\n                    <td class=\"row-label\"><strong>14</strong> ($8 + 4 + 2 = 14$)</td>\n                  </tr>\n                  <tr class=\"res-row\">\n                    <td class=\"row-label\">A ^ B (XOR: different)</td>\n                    <td class=\"bit-result-cell\">0</td><td class=\"bit-result-cell\">0</td><td class=\"bit-result-cell\">0</td><td class=\"bit-result-cell\">0</td>\n                    <td class=\"bit-result-cell\">0</td><td class=\"bit-result-cell highlight\">1</td><td class=\"bit-result-cell highlight\">1</td><td class=\"bit-result-cell\">0</td>\n                    <td class=\"row-label\"><strong>6</strong> ($4 + 2 = 6$; matching bit 3 cancels out!)</td>\n                  </tr>\n                </tbody>\n              </table>\n            </div>\n          </div>\n        </div>\n\n        <!-- STEP 4: Two's Complement Decoded (~35 = -36) -->\n        <div class=\"step-guide-card\">\n          <div class=\"step-badge\">STEP 4</div>\n          <div class=\"step-content\">\n            <h4>The Mystery Solved: Why ~35 evaluates to -36! (Slides 126\u2013128)</h4>\n            <p>When you run <code>printf(\"%d\", ~35);</code> in C, beginners expect either 220 or an error. Instead, C outputs <strong>-36</strong>. Here is the exact 4-phase step-by-step reason why:</p>\n\n            <div class=\"twos-steps-container\">\n              <div class=\"twos-step-item\">\n                <div class=\"step-num-bubble\">1</div>\n                <div class=\"step-desc\">\n                  <strong>Write +35 in 8-bit binary:</strong>\n                  <br>Break into powers of two: $35 = 32 + 2 + 1 \\implies \\mathbf{0010\\ 0011_2}$.\n                </div>\n              </div>\n              <div class=\"twos-step-item\">\n                <div class=\"step-num-bubble\">2</div>\n                <div class=\"step-desc\">\n                  <strong>Apply Bitwise NOT (<code>~</code>):</strong>\n                  <br>Flip every 0 to 1 and every 1 to 0: $\\mathbf{0010\\ 0011_2} \\longrightarrow \\mathbf{1101\\ 1100_2}$.\n                </div>\n              </div>\n              <div class=\"twos-step-item\">\n                <div class=\"step-num-bubble\">3</div>\n                <div class=\"step-desc\">\n                  <strong>Check the Leftmost Sign Bit:</strong>\n                  <br>In C, signed integers use Two's Complement. The leftmost bit (bit 7) is the <strong>Sign Bit</strong>.\n                  <br>Because bit 7 is <strong>1</strong>, the computer knows this represents a <strong>NEGATIVE NUMBER</strong>!\n                </div>\n              </div>\n              <div class=\"twos-step-item\">\n                <div class=\"step-num-bubble\">4</div>\n                <div class=\"step-desc\">\n                  <strong>Decode the Negative Magnitude:</strong>\n                  <br>To find what negative quantity $\\mathbf{1101\\ 1100_2}$ represents, take its Two's Complement:\n                  <br>&bull; Invert bits back: $\\mathbf{0010\\ 0011_2}$ (which equals $35$).\n                  <br>&bull; Add 1: $35 + 1 = \\mathbf{36}$.\n                  <br>&bull; Add the negative sign: $\\mathbf{-36}$!\n                </div>\n              </div>\n            </div>\n\n            <!-- Golden Formula Box -->\n            <div class=\"golden-rule-box\">\n              <div class=\"rule-header\">\n                <i class=\"fa-solid fa-crown\"></i>\n                <span>Teacher's Golden Shortcut Formula (Slide 127)</span>\n              </div>\n              <div class=\"rule-formula\">\n                $$\\sim N = -(N + 1)$$\n              </div>\n              <div class=\"rule-examples\">\n                <span class=\"rule-chip\"><i class=\"fa-solid fa-arrow-right-long\" style=\"color: var(--accent-yellow)\"></i> $\\sim 35 = -(35 + 1) = \\mathbf{-36}$</span>\n                <span class=\"rule-chip\"><i class=\"fa-solid fa-arrow-right-long\" style=\"color: var(--accent-yellow)\"></i> $\\sim 0 = -(0 + 1) = \\mathbf{-1}$</span>\n                <span class=\"rule-chip\"><i class=\"fa-solid fa-arrow-right-long\" style=\"color: var(--accent-yellow)\"></i> $\\sim (-12) = -(-12 + 1) = \\mathbf{+11}$</span>\n                <span class=\"rule-chip\"><i class=\"fa-solid fa-arrow-right-long\" style=\"color: var(--accent-yellow)\"></i> $\\sim 100 = -(100 + 1) = \\mathbf{-101}$</span>\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <!-- STEP 5: High-Speed Shifts -->\n        <div class=\"step-guide-card\">\n          <div class=\"step-badge\">STEP 5</div>\n          <div class=\"step-content\">\n            <h4>Bit Shift Operators as Hardware Multipliers &amp; Dividers (Slide 129)</h4>\n            <p>Shifting bits left or right is the fastest mathematical operation a CPU can perform\u2014it takes only 1 hardware clock cycle!</p>\n            \n            <div class=\"shifts-grid\">\n              <div class=\"shift-card left\">\n                <div class=\"shift-title\"><i class=\"fa-solid fa-angles-left\"></i> Left Shift (<code>x &lt;&lt; k</code>)</div>\n                <p><strong>Action:</strong> Bits slide left by $k$ slots; zeroes fill in from the right.</p>\n                <div class=\"shift-math\">Formula: $\\text{Result} = x \\times 2^k$</div>\n                <div class=\"shift-example\">\n                  <code>int x = 5; // 0000 0101</code><br>\n                  <code>x &lt;&lt; 3; // 0010 1000 = 40 (5 * 2^3 = 5 * 8 = 40!)</code>\n                </div>\n              </div>\n\n              <div class=\"shift-card right\">\n                <div class=\"shift-title\"><i class=\"fa-solid fa-angles-right\"></i> Right Shift (<code>x &gt;&gt; k</code>)</div>\n                <p><strong>Action:</strong> Bits slide right by $k$ slots; rightmost bits fall off the edge.</p>\n                <div class=\"shift-math\">Formula: $\\text{Result} = x / 2^k$ (integer division)</div>\n                <div class=\"shift-example\">\n                  <code>int y = 40; // 0010 1000</code><br>\n                  <code>y &gt;&gt; 2;  // 0000 1010 = 10 (40 / 2^2 = 40 / 4 = 10!)</code>\n                </div>\n              </div>\n            </div>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-code-branch\"></i> Ternary &amp; Comma Operators (Slides 130\u2013133)</h3>\n        <ul>\n          <li><strong>Ternary Operator (<code>? :</code>):</strong> The compact one-line if-else. Syntax: <code>condition ? expr_true : expr_false;</code>\n            <br>Finding maximum of 3 numbers (Slide 131):\n            <br><code>max = a &gt; b ? (a &gt; c ? a : c) : (b &gt; c ? b : c);</code>\n          </li>\n          <li><strong>Comma Operator (<code>,</code>):</strong> Lowest precedence in all of C! Evaluates expressions strictly from Left to Right and returns the value of the <em>rightmost</em> expression.\n            <br>Example: <code>int x = (10, 20, 30);</code> &rarr; <code>x</code> receives <strong>30</strong>!\n          </li>\n        </ul>\n      </div>\n    ",
    "code": {
      "title": "Bitwise Operations, ~35 = -36 & Relational Chaining Demo",
      "desc": "Testing ~35 = -36, relational chaining d = a > b < c, bit shifts, and short-circuit evaluation.",
      "lang": "c",
      "snippet": "#include <stdio.h>\n#include <stdbool.h>\n\nint main(void) {\n    // 1. Bitwise NOT theorem: ~N = -(N + 1)\n    int n = 35;\n    printf(\"~35 = %d | ~(-12) = %d\\n\", ~n, ~(-12));\n\n    // 2. Relational Chaining: left-to-right associativity\n    int a = 1, b = 2, c = 3;\n    int d = a > b < c; // (1 > 2) is 0; then (0 < 3) is 1!\n    printf(\"Result of (1 > 2 < 3): d = %d\\n\", d);\n\n    // 3. Bit Shifts as powers of 2\n    int x = 5;\n    printf(\"5 << 3 (5 * 8) = %d\\n\", x << 3);\n    printf(\"40 >> 2 (40 / 4) = %d\\n\", 40 >> 2);\n\n    // 4. Nested Ternary: Maximum of 3 numbers\n    int p = 14, q = 42, r = 27;\n    int max = p > q ? (p > r ? p : r) : (q > r ? q : r);\n    printf(\"Max of %d, %d, %d is: %d\\n\", p, q, r, max);\n\n    // 5. Short-Circuiting in &&\n    int u = 10, v = 4;\n    bool res = ((u == v) && printf(\"This won't print!\\n\"));\n    printf(\"Short-circuit result: %d\\n\", res);\n\n    return 0;\n}",
      "output": "~35 = -36 | ~(-12) = 11\nResult of (1 > 2 < 3): d = 1\n5 << 3 (5 * 8) = 40\n40 >> 2 (40 / 4) = 10\nMax of 14, 42, 27 is: 42\nShort-circuit result: 0"
    },
    "resources": [
      {
        "type": "gfg",
        "title": "Operator Precedence and Associativity in C",
        "url": "https://www.geeksforgeeks.org/operator-precedence-and-associativity-in-c/",
        "desc": "Curriculum link referenced in Slide 107 with complete precedence tables."
      },
      {
        "type": "gfg",
        "title": "Left Shift and Right Shift Operators in C",
        "url": "https://www.geeksforgeeks.org/left-shift-right-shift-operators-c-cpp/",
        "desc": "Curriculum link referenced in Slide 129 detailing multiplication/division via shifts."
      },
      {
        "type": "gfg",
        "title": "The Comma Operator in C",
        "url": "https://www.geeksforgeeks.org/a-comma-operator-question/",
        "desc": "Curriculum link referenced in Slide 132 exploring evaluation order."
      },
      {
        "type": "gfg",
        "title": "Typecasting in C",
        "url": "https://www.geeksforgeeks.org/typecasting-in-c/",
        "desc": "Curriculum link referenced in Slide 133 detailing implicit vs explicit conversion."
      }
    ],
    "quiz": [
      {
        "id": "q9_1",
        "question": "What is the value of the bitwise complement of 35 (~35) in C programming, and why (Slides 126\u2013127)?",
        "options": [
          "220, because all 8 bits are inverted",
          "-36, because signed integers are stored in two's complement form where ~N = -(N + 1)",
          "-35, because only the sign bit is changed",
          "0, because bitwise NOT is not allowed on integers"
        ],
        "answer": 1,
        "explanation": "Slides 126\u2013127 explain that in two's complement representation, ~N = -(N + 1). Hence, ~35 evaluates to -(35 + 1) = -36."
      },
      {
        "id": "q9_2",
        "question": "Given 'int a = 1, b = 2, c = 3; int d = a > b < c;', what is the value stored in d (Slide 117)?",
        "options": [
          "0 (False)",
          "1 (True)",
          "2",
          "Compilation Error"
        ],
        "answer": 1,
        "explanation": "Relational operators associate left-to-right. First, (a > b) -> (1 > 2) evaluates to 0. Then, (0 < c) -> (0 < 3) evaluates to 1 (True). Thus d = 1."
      },
      {
        "id": "q9_3",
        "question": "In the statement 'bool res = (a == b) && printf(\"C Language\");', under what condition is the printf() function NEVER executed (Slide 122)?",
        "options": [
          "When (a == b) is True",
          "When (a == b) is False (0), due to short-circuit evaluation of logical AND",
          "printf() is always executed regardless of condition",
          "Only when b equals 0"
        ],
        "answer": 1,
        "explanation": "Slide 122: In logical AND (&&), if the first operand is False (0), the entire expression can never be True, so the second operand is short-circuited and not evaluated."
      },
      {
        "id": "q9_4",
        "question": "Which of the following operations is strictly ILLEGAL in C?",
        "options": [
          "int rem = 10 % 3;",
          "float rem = 10.5 % 3.2;",
          "int res = 10 << 2;",
          "int a = (1, 2, 3);"
        ],
        "answer": 1,
        "explanation": "As stated on Slide 114 and 125, the modulo operator (%) and bitwise operators can ONLY be applied to integer and char operands, never floating-point types."
      },
      {
        "id": "q9_5",
        "question": "What is the result of shifting an integer x left by 3 positions (x << 3) (Slide 129)?",
        "options": [
          "x + 3",
          "x * 3",
          "x * 2^3 = x * 8",
          "x / 8"
        ],
        "answer": 2,
        "explanation": "Slide 129: 'Left shift is useful in implementing multiplication with powers of 2.' Shifting left by 3 positions multiplies x by 2^3 = 8."
      },
      {
        "id": "q9_6",
        "question": "What value is assigned to variable x in: 'int x = (10, 20, 30);' (Slide 132)?",
        "options": [
          "10",
          "20",
          "30",
          "Compilation Error"
        ],
        "answer": 2,
        "explanation": "The comma operator evaluates expressions from left to right and returns the value of the rightmost expression (30) (Slide 132)."
      }
    ]
  },
  {
    "id": "m10",
    "num": 10,
    "title": "Decision Control: If-Else & Switch-Case Mastery",
    "subtitle": "The Crossroads: Branching, Jump Tables, Unreachable Switch Trap & Strict Case Rules",
    "slides": "Slides 134\u2013146",
    "time": "40 mins",
    "content": "\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-code-fork\"></i> Decision Making: The Fork in the Road (Slides 134\u2013141)</h3>\n        <p class=\"lead-text\">\n          By default, computers execute code sequentially, one line after another.\n          <strong>Decision control statements</strong> act as forks in the road, inspecting conditions and routing execution down different paths.\n        </p>\n\n        <div class=\"teacher-callout analogy\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-traffic-light\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The Truthy vs Falsy Rule in C (Slide 138)</div>\n            <p>Unlike languages that require a strict <code>true</code> or <code>false</code> boolean keyword, C evaluates every integer expression natively:\n            <br>&bull; <strong>Zero (<code>0</code>)</strong> is <strong>FALSE</strong>.\n            <br>&bull; <strong>ANY non-zero value</strong> (positive, negative like <code>-1</code>, or fractional like <code>3.14</code>) is <strong>TRUE</strong>!\n            <br>Exam favorite from Slide 138: <code>if (-1) printf(\"Hello\");</code> &rarr; Prints <code>\"Hello\"</code> because <code>-1</code> is non-zero, hence TRUE!</p>\n          </div>\n        </div>\n\n        <div class=\"comparison-card\">\n          <div class=\"comparison-header\">\n            <span><i class=\"fa-solid fa-diagram-project\"></i> The If Family Tree</span>\n            <span class=\"badge\">Control Patterns</span>\n          </div>\n          <div class=\"comparison-grid\">\n            <div class=\"comparison-col\">\n              <h4>Simple if</h4>\n              <p>One-way branch: executes the block only if true; otherwise skips past it.</p>\n              <code>if (score &gt;= 50) { pass(); }</code>\n            </div>\n            <div class=\"comparison-col\">\n              <h4>if ... else</h4>\n              <p>Two-way fork: executes block A if true, or block B if false. Exactly one executes.</p>\n              <code>if (x % 2 == 0) even(); else odd();</code>\n            </div>\n            <div class=\"comparison-col\">\n              <h4>if-else-if Ladder</h4>\n              <p>Multi-way sequential tests: tests conditions top-to-bottom until the first match.</p>\n              <code>if (m &gt; 90) 'A'; else if (m &gt; 80) 'B'; else 'C';</code>\n            </div>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-toggle-on\"></i> The Switch-Case Statement & The Jump Table (Slides 142\u2013146)</h3>\n        <p>The <code>switch</code> statement tests an expression against a series of constant case labels. Why do systems programmers use it instead of a long <code>if-else-if</code> ladder?</p>\n\n        <div class=\"teacher-callout analogy\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-elevator\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The Hallway vs. Express Elevator Analogy (Slide 143)</div>\n            <p>\n              &bull; <strong><code>if-else-if</code> Ladder:</strong> Walking down a long hotel hallway and knocking on Room 1, then Room 2, then Room 3, until you find your room ($O(N)$ sequential search).<br>\n              &bull; <strong><code>switch</code> Statement:</strong> An <strong>Express Elevator with a Jump Table</strong>! The C compiler synthesizes an array of code memory addresses indexed by the switch value. The CPU jumps directly to the target case in <strong>$O(1)$ constant time</strong>, regardless of whether there are 3 cases or 300 cases!\n            </p>\n          </div>\n        </div>\n\n        <h4>The 5 Golden Rules of C Switch Statements (Slides 144\u2013146)</h4>\n        <div class=\"table-responsive\">\n          <table class=\"curriculum-table\">\n            <thead>\n              <tr><th>#</th><th>Rule (Slides 144\u2013146)</th><th>Valid Example</th><th>Invalid Example (Compiler Rejection!)</th></tr>\n            </thead>\n            <tbody>\n              <tr>\n                <td>1</td>\n                <td><strong>Integral Expressions Only:</strong> Switch expression must evaluate to an integer type (<code>int</code>, <code>char</code>, <code>enum</code>). Floats and doubles are strictly forbidden! (You cannot press button 3.14 in an elevator!).</td>\n                <td><code>switch(choice)</code> where <code>choice</code> is <code>int</code> or <code>char</code></td>\n                <td><code>float x = 2.5; switch(x)</code> &rarr; <em>Error: switch quantity not an integer</em></td>\n              </tr>\n              <tr>\n                <td>2</td>\n                <td><strong>Constant Case Labels:</strong> Each case label must be a compile-time constant integer expression. Variables are strictly illegal!</td>\n                <td><code>case 1:</code> or <code>case 'A':</code> or <code>case 2 + 3:</code></td>\n                <td><code>int k = 5; switch(x) { case k: ... }</code> &rarr; <em>Error: case label does not reduce to an integer constant</em></td>\n              </tr>\n              <tr>\n                <td>3</td>\n                <td><strong>Unique Case Labels:</strong> Two case labels cannot have identical values.</td>\n                <td><code>case 1: ... case 2:</code></td>\n                <td><code>case 2: ... case 1 + 1:</code> &rarr; <em>Error: duplicate case value '2'</em></td>\n              </tr>\n              <tr>\n                <td>4</td>\n                <td><strong>The Unreachable Code Trap:</strong> Any code written inside the switch block <em>before</em> the very first <code>case</code> label will <strong>never execute</strong>! The jump table bypasses it entirely!</td>\n                <td>Place statements inside the case labels.</td>\n                <td><code>switch(x) { printf(\"Hi\"); case 1: ... }</code> &rarr; <code>printf(\"Hi\")</code> is permanently skipped! (Slide 146)</td>\n              </tr>\n              <tr>\n                <td>5</td>\n                <td><strong>Fallthrough & break:</strong> If you omit <code>break;</code>, execution does not stop; it falls through and runs every subsequent case regardless of label!</td>\n                <td>Always end each case with <code>break;</code> unless intentional fallthrough is desired.</td>\n                <td>Missing break cascades execution into subsequent cases.</td>\n              </tr>\n            </tbody>\n          </table>\n        </div>\n      </div>\n    ",
    "code": {
      "title": "Switch Unreachable Code & Fallthrough Mechanics (Slides 145\u2013146)",
      "desc": "Demonstrating how statements placed before the first case are skipped, and intentional break termination.",
      "lang": "c",
      "snippet": "#include <stdio.h>\n\nint main(void) {\n    int choice = 1;\n\n    switch (choice) {\n        printf(\"I am unreachable and never execute!\\n\"); // SLIDE 146 TRAP!\n\n        case 1:\n            printf(\"Choice is 1\\n\");\n            break;\n        case 2:\n            printf(\"Choice is 2\\n\");\n            break;\n        default:\n            printf(\"Default choice\\n\");\n            break;\n    }\n\n    // Truthy test with negative number (Slide 138)\n    if (-1) {\n        printf(\"In C, -1 is non-zero, hence TRUE!\\n\");\n    }\n\n    return 0;\n}",
      "output": "Choice is 1\nIn C, -1 is non-zero, hence TRUE!"
    },
    "resources": [
      {
        "type": "gfg",
        "title": "Switch Statement in C",
        "url": "https://www.geeksforgeeks.org/switch-statement-in-c/",
        "desc": "GeeksforGeeks detailed guide on switch-case rules and jump table mechanics."
      },
      {
        "type": "docs",
        "title": "Compiler Explorer: Jump Table Disassembly",
        "url": "https://godbolt.org",
        "desc": "Write a dense switch case and view the emitted assembly jump table (jmp *%rax)."
      }
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
  },
  {
    "id": "m11",
    "num": 11,
    "title": "Iteration: Loops & Advanced I/O Quirks",
    "subtitle": "The Loops: While, For, Do-While, Continue Traps, and Return Values of printf & scanf",
    "slides": "Slides 147\u2013162",
    "time": "45 mins",
    "content": "\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-repeat\"></i> The Three Loops: Repetition Without Redundancy (Slides 147\u2013154)</h3>\n        <p class=\"lead-text\">\n          Loops allow running a block of statements repeatedly until a specified termination condition becomes False.\n          C provides three primary loop constructs:\n        </p>\n\n        <div class=\"comparison-card\">\n          <div class=\"comparison-header\">\n            <span><i class=\"fa-solid fa-arrows-spin\"></i> The Three C Loop Constructs</span>\n            <span class=\"badge\">Execution Comparison</span>\n          </div>\n          <div class=\"comparison-grid\">\n            <div class=\"comparison-col\">\n              <h4>while Loop</h4>\n              <p><strong>\"The Nightclub Bouncer\"</strong></p>\n              <p><strong>Entry-Controlled:</strong> Tests the condition <em>before</em> entering the loop.</p>\n              <p>If the condition is initially False, the body executes <strong>0 times</strong>!</p>\n              <code>while (count &lt; 5) { count++; }</code>\n            </div>\n            <div class=\"comparison-col\">\n              <h4>for Loop</h4>\n              <p><strong>\"The Lap Counter\"</strong></p>\n              <p><strong>Entry-Controlled:</strong> Compact syntax packing initialization, condition, and update in one line with 2 semicolons.</p>\n              <p>Ideal when the number of iterations is known in advance.</p>\n              <code>for (int i=0; i&lt;5; i++) { ... }</code>\n            </div>\n            <div class=\"comparison-col\">\n              <h4>do-while Loop</h4>\n              <p><strong>\"The Rollercoaster Ride\"</strong></p>\n              <p><strong>Exit-Controlled:</strong> You get to ride once first; ticket is checked at the exit!</p>\n              <p>Guaranteed to execute <strong>at least once</strong>! Must end with a semicolon <code>;</code>!</p>\n              <code>do { work(); } while (more);</code>\n            </div>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-infinity\"></i> Infinite Loops & The continue Trap (Slides 155\u2013159)</h3>\n        <p>An <strong>Infinite Loop</strong> runs forever because its condition never evaluates to False:</p>\n        <ul>\n          <li><code>for ( ; ; ) { /* infinite loop */ }</code></li>\n          <li><code>while (1) { /* infinite loop */ }</code></li>\n        </ul>\n\n        <h4>Loop Control Statements (Slide 158)</h4>\n        <ul>\n          <li><strong><code>break</code>:</strong> Instantly breaks out of the loop and jumps to the code following the loop.</li>\n          <li><strong><code>continue</code>:</strong> Skips the rest of the current iteration and jumps directly to the next iteration.</li>\n        </ul>\n\n        <div class=\"teacher-callout pitfall\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-bomb\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">The Sneaky continue Trap in while vs. for</div>\n            <p>\n              &bull; In a <strong><code>for</code> loop</strong>: <code>continue</code> jumps to the <strong>update step</strong> (<code>i++</code>) before checking the condition. The counter increments safely.<br>\n              &bull; In a <strong><code>while</code> loop</strong>: <code>continue</code> jumps directly to the <strong>condition check</strong>! If your counter update (<code>i++</code>) was located at the bottom of the loop body, it is completely skipped, trapping your program in an <strong>accidental infinite loop</strong>!\n            </p>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"teaching-block\">\n        <h3><i class=\"fa-solid fa-receipt\"></i> High-Yield Exam Topic: Return Values of printf() & scanf() (Slides 160\u2013162)</h3>\n        <p>Both <code>printf()</code> and <code>scanf()</code> are functions that return valuable status information. Think of their return values as <strong>store receipts</strong>!</p>\n\n        <div class=\"comparison-card\">\n          <div class=\"comparison-header\">\n            <span><i class=\"fa-solid fa-file-invoice\"></i> The Store Receipt Analogy for I/O Functions</span>\n            <span class=\"badge\">Return Value Rules</span>\n          </div>\n          <div class=\"comparison-grid\">\n            <div class=\"comparison-col\">\n              <h4>Function</h4>\n              <p><strong>printf(...)</strong></p>\n              <br>\n              <p><strong>scanf(...)</strong></p>\n            </div>\n            <div class=\"comparison-col\">\n              <h4>What It Returns (Slide 160)</h4>\n              <p>Returns the total number of <strong>characters successfully printed</strong> to the screen.</p>\n              <p>Returns the total number of <strong>input items successfully matched and assigned</strong> into memory variables.</p>\n            </div>\n            <div class=\"comparison-col\">\n              <h4>Classic Exam Code Trace</h4>\n              <p>\n                <code>printf(\" %d\", printf(\"geeksforgeeks\"));</code><br>\n                1. Inner <code>printf(\"geeksforgeeks\")</code> prints 13 characters and returns <strong>13</strong>.<br>\n                2. Outer <code>printf</code> prints <code>\" 13\"</code>.<br>\n                <strong>Screen Output: <code>geeksforgeeks 13</code></strong>!\n              </p>\n              <p>\n                <code>char a[50]; printf(\" %d\", scanf(\"%s\", a));</code><br>\n                Regardless of the word entered (e.g. \"Computer\"), exactly 1 item was assigned, so <code>scanf</code> returns <strong>1</strong> (Slide 161).\n              </p>\n            </div>\n          </div>\n        </div>\n\n        <div class=\"teacher-callout insight\">\n          <div class=\"callout-icon\"><i class=\"fa-solid fa-keyboard\"></i></div>\n          <div class=\"callout-body\">\n            <div class=\"callout-title\">Reading Strings with Spaces using Scansets (Slide 162)</div>\n            <p>Normal <code>scanf(\"%s\", str);</code> terminates at the first whitespace character (space, tab, or newline).\n            <br>To read an entire line including spaces, use a <strong>Scanset</strong>:\n            <br><code>scanf(\"%[^\\\\n]s\", str);</code>\n            <br>The <code>^\\\\n</code> tells <code>scanf</code>: <em>\"Accept and read every character until you encounter a newline!\"</em></p>\n          </div>\n        </div>\n      </div>\n    ",
    "code": {
      "title": "Return Values of printf() and scanf() in C (Slides 160\u2013161)",
      "desc": "Demonstrating nested printf character counts, empty printf return, and do-while guaranteed execution.",
      "lang": "c",
      "snippet": "#include <stdio.h>\n\nint main(void) {\n    // 1. Nested printf return value (Slide 160)\n    // Inner prints \"geeksforgeeks\" (13 chars) and returns 13\n    // Outer prints \" 13\"\n    printf(\" %d\\n\", printf(\"geeksforgeeks\"));\n\n    // 2. Empty printf returns 0 characters\n    printf(\"Empty printf returned: %d\\n\", printf(\"\"));\n\n    // 3. do-while loop executing at least once (Slide 153-154)\n    int i = 2;\n    do {\n        printf(\"do-while body executed with i = %d\\n\", i);\n        i++;\n    } while (i < 1); // condition false initially, but executed once!\n\n    return 0;\n}",
      "output": "geeksforgeeks 13\nEmpty printf returned: 0\ndo-while body executed with i = 2"
    },
    "resources": [
      {
        "type": "gfg",
        "title": "Scansets in C",
        "url": "https://www.geeksforgeeks.org/scansets-in-c/",
        "desc": "Curriculum link from Slide 162 on using %[^\\n]s to read spaces."
      },
      {
        "type": "gfg",
        "title": "Taking String Input with Spaces in C",
        "url": "https://www.geeksforgeeks.org/taking-string-input-space-c-3-different-methods/",
        "desc": "Curriculum link comparing scanf scansets, fgets, and gets."
      },
      {
        "type": "docs",
        "title": "TutorialsPoint: C continue Statement",
        "url": "https://www.tutorialspoint.com/cprogramming/c_continue_statement.htm",
        "desc": "Curriculum link referenced in Slide 159 on loop control."
      }
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
        "question": "What does scanf() return when successfully reading user input into variables (Slide 160\u2013161)?",
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
  }
];
const CAPSTONE_EXAM = [
  {
    "id": "exam_1",
    "question": "Who created the C programming language, in what year, and at which facility?",
    "options": [
      "Bjarne Stroustrup in 1979 at Bell Labs",
      "Dennis Ritchie in 1972 at AT&T Bell Laboratories",
      "Ken Thompson in 1969 at MIT",
      "James Gosling in 1995 at Sun Microsystems"
    ],
    "answer": 1,
    "explanation": "Dennis Ritchie developed C in 1972 at AT&T Bell Laboratories to construct the UNIX operating system."
  },
  {
    "id": "exam_2",
    "question": "What is the maximum theoretical memory addressable by a 32-bit CPU register?",
    "options": [
      "2 GB",
      "4 GB (4,294,967,296 bytes)",
      "8 GB",
      "16 Exabytes"
    ],
    "answer": 1,
    "explanation": "A 32-bit register references 2^32 unique byte addresses, equaling exactly 4 GB."
  },
  {
    "id": "exam_3",
    "question": "Convert the binary number 1000001110B to Octal (Base 8) as solved on Slide 12:",
    "options": [
      "(1016)base 8",
      "(2016)base 8",
      "(416)base 8",
      "(527)base 8"
    ],
    "answer": 0,
    "explanation": "Group from right by 3 bits: 001 000 001 110 -> 1 0 1 6 in octal = (1016)base 8."
  },
  {
    "id": "exam_4",
    "question": "Which memory type occupies Level 1 of the computer memory hierarchy pyramid?",
    "options": [
      "CPU Registers",
      "Cache Memory (SRAMs)",
      "Main Memory (DRAMs)",
      "Magnetic Hard Disk"
    ],
    "answer": 1,
    "explanation": "Level 0 is CPU Registers, Level 1 is Cache Memory (SRAMs), Level 2 is Main Memory (DRAMs)."
  },
  {
    "id": "exam_5",
    "question": "What does a Parallelogram symbol signify in standard ISO flowcharts (Slide 33)?",
    "options": [
      "Decision conditional test",
      "Computation / Assignment",
      "Input or Output operation",
      "Start or Stop"
    ],
    "answer": 2,
    "explanation": "A parallelogram represents a point where data is input to or output from the program."
  },
  {
    "id": "exam_6",
    "question": "Which phase of the GCC compilation pipeline produces the assembly language file (.s)?",
    "options": [
      "Preprocessing (gcc -E)",
      "Proper Compilation (gcc -S via cc1)",
      "Assembly (gcc -c via as)",
      "Linking (gcc via ld)"
    ],
    "answer": 1,
    "explanation": "Proper compilation (cc1) translates preprocessed code (.i) into assembly language (.s)."
  },
  {
    "id": "exam_7",
    "question": "In which memory segment are uninitialized global variables stored, and to what value are they initialized by the OS kernel?",
    "options": [
      "Stack segment, initialized to garbage",
      "Heap segment, initialized to NULL",
      "Uninitialized Data segment (.bss), initialized to 0",
      "Text segment, initialized to 1"
    ],
    "answer": 2,
    "explanation": "Uninitialized global/static variables go to .bss and are automatically initialized to arithmetic zero by the OS kernel."
  },
  {
    "id": "exam_8",
    "question": "Which predefined identifier was introduced in C99/C11 to represent the current function's name as a string?",
    "options": [
      "__LINE__",
      "__func__",
      "__FILE__",
      "__DATE__"
    ],
    "answer": 1,
    "explanation": "C99/C11 introduced __func__, which acts as `static const char __func__[] = \"function_name\";`."
  },
  {
    "id": "exam_9",
    "question": "What is the result of evaluating the bitwise complement ~35 in C (Slide 126)?",
    "options": [
      "220",
      "-36",
      "-35",
      "0"
    ],
    "answer": 1,
    "explanation": "Due to two's complement representation, ~N = -(N + 1). Hence ~35 = -36."
  },
  {
    "id": "exam_10",
    "question": "What is printed on the screen by: `printf(\" %d\", printf(\"geeksforgeeks\"));` (Slide 160)?",
    "options": [
      "13 geeksforgeeks",
      "geeksforgeeks 13",
      "geeksforgeeks 0",
      "Compilation Error"
    ],
    "answer": 1,
    "explanation": "The inner printf outputs 'geeksforgeeks' and returns 13 (character count). The outer printf then outputs ' 13'."
  },
  {
    "id": "exam_11",
    "question": "What happens if code statements are placed inside a switch block BEFORE the first case label?",
    "options": [
      "They execute before every case",
      "They are never executed (bypassed completely)",
      "They cause an immediate segmentation fault",
      "They execute only on default"
    ],
    "answer": 1,
    "explanation": "Statements placed before the first case label in a switch are unreachable and never executed."
  },
  {
    "id": "exam_12",
    "question": "In C, what is the result of the expression: `10 / 4`?",
    "options": [
      "2.5",
      "2",
      "2.0",
      "3"
    ],
    "answer": 1,
    "explanation": "When both operands are integers, C performs integer division and truncates the fractional part, yielding 2."
  },
  {
    "id": "exam_13",
    "question": "Which statement about the `do-while` loop is TRUE?",
    "options": [
      "It evaluates its test condition before executing the loop body",
      "It is guaranteed to execute its body at least once regardless of whether the condition is true or false",
      "It cannot be nested",
      "It does not require a semicolon at the end"
    ],
    "answer": 1,
    "explanation": "Because do-while is exit-controlled, the loop body always executes at least once before checking the condition."
  },
  {
    "id": "exam_14",
    "question": "What is the difference between a Syntax error and a Semantic error in C?",
    "options": [
      "Syntax errors occur at runtime; Semantic errors occur at compile time",
      "Syntax errors violate grammatical rules and prevent compilation; Semantic errors compile cleanly but produce incorrect logical behavior",
      "There is no difference",
      "Syntax errors only occur in loops"
    ],
    "answer": 1,
    "explanation": "Syntax errors are grammatical violations caught by the compiler. Semantic errors are logical flaws that compile but behave unexpectedly at runtime."
  },
  {
    "id": "exam_15",
    "question": "What scanset format specifier allows scanf() to read a complete line containing spaces until Enter is pressed (Slide 162)?",
    "options": [
      "scanf(\"%s\", str);",
      "scanf(\"%[^\\n]s\", str);",
      "scanf(\"%text\", str);",
      "scanf(\"%line\", str);"
    ],
    "answer": 1,
    "explanation": "Using `%[^\\n]s` specifies a scanset that reads all characters until a newline character is encountered."
  },
  {
    "id": "exam_16",
    "question": "Which of the following is NOT one of Donald Knuth's five mandatory criteria for an algorithm (Slide 26)?",
    "options": [
      "Finiteness (terminates after finite steps)",
      "Definiteness (each step is clear and unambiguous)",
      "Platform-Dependence (written strictly for a specific CPU architecture)",
      "Effectiveness (operations are basic enough to be carried out exactly)"
    ],
    "answer": 2,
    "explanation": "Donald Knuth's 5 algorithmic criteria are Finiteness, Definiteness, Input, Output, and Effectiveness. Algorithms are abstract logic independent of hardware platform."
  },
  {
    "id": "exam_17",
    "question": "In standard ISO flowchart conventions, which geometric symbol represents a conditional Decision test, and how many exit paths can it have?",
    "options": [
      "Rectangle with 1 exit path",
      "Diamond (Rhombus) with 2 or 3 exit branches",
      "Oval with unlimited exit paths",
      "Circle with 0 exit paths"
    ],
    "answer": 1,
    "explanation": "A Diamond (Rhombus) represents a decision test and has either 2 branches (True/False, Yes/No) or 3 branches (<0, =0, >0)."
  },
  {
    "id": "exam_18",
    "question": "To which Programming Language Generation does Assembly Language belong (Slide 22)?",
    "options": [
      "1GL (First Generation - Pure Binary Machine Code)",
      "2GL (Second Generation - Mnemonic symbolic opcodes)",
      "3GL (Third Generation - High-level procedural languages like C)",
      "4GL (Fourth Generation - Query languages like SQL)"
    ],
    "answer": 1,
    "explanation": "Assembly language with mnemonics (MOV, ADD, SUB) is classified as 2GL (Second Generation Language)."
  },
  {
    "id": "exam_19",
    "question": "What is the final value stored in variable `d` after evaluating: `int a = 1, b = 2, c = 3; int d = a > b < c;` in C (Slide 117)?",
    "options": [
      "0 (false)",
      "1 (true)",
      "2",
      "Undefined Behavior"
    ],
    "answer": 1,
    "explanation": "Relational operators associate Left-to-Right: `(a > b) < c` -> `(1 > 2) < 3` -> `0 < 3` -> evaluates to 1 (True)."
  },
  {
    "id": "exam_20",
    "question": "What is printed by: `int a = 0, b = 5; if (a && ++b) { } printf(\"b = %d\\n\", b);` due to short-circuiting?",
    "options": [
      "b = 6",
      "b = 5",
      "b = 0",
      "Compilation Error"
    ],
    "answer": 1,
    "explanation": "In logical AND `&&`, because the left operand `a` is 0 (False), the right operand `++b` is skipped completely, leaving `b = 5`."
  },
  {
    "id": "exam_21",
    "question": "Given integer `x = 6` (binary 0000 0110), what are the results of `x << 2` and `x >> 1` respectively (Slide 126)?",
    "options": [
      "12 and 2",
      "24 and 3",
      "18 and 1",
      "24 and 1"
    ],
    "answer": 1,
    "explanation": "Left shift multiplies by 2^k (`6 << 2 = 6 * 4 = 24`). Right shift divides by 2^k (`6 >> 1 = 6 / 2 = 3`)."
  },
  {
    "id": "exam_22",
    "question": "Which mathematical property of Bitwise XOR (`^`) makes swapping two numbers possible without temporary storage (Slide 126)?",
    "options": [
      "x ^ 0 = 0",
      "x ^ x = 0 and x ^ 0 = x (self-inverse and identity)",
      "x ^ 1 = 0",
      "x ^ y = x * y"
    ],
    "answer": 1,
    "explanation": "XOR cancels out identical bit patterns (`x ^ x = 0`) and preserves bits against zeros (`x ^ 0 = x`)."
  },
  {
    "id": "exam_23",
    "question": "Which of the following is a completely VALID variable identifier according to ANSI C rules (Slide 78)?",
    "options": [
      "2nd_rank",
      "switch",
      "_total_score_2024",
      "student-name"
    ],
    "answer": 2,
    "explanation": "Identifiers must start with a letter or underscore, cannot contain hyphens, and cannot be keywords. `_total_score_2024` satisfies all rules."
  },
  {
    "id": "exam_24",
    "question": "How many total reserved keywords are specified in the ANSI C (C89/C90) standard (Slide 80)?",
    "options": [
      "24 keywords",
      "32 keywords",
      "48 keywords",
      "64 keywords"
    ],
    "answer": 1,
    "explanation": "ANSI C89 specifies exactly 32 reserved keywords (e.g., auto, break, case, char, const, continue, default, do, int, return, while...)."
  },
  {
    "id": "exam_25",
    "question": "What are the decimal integer values of the literals `025` and `0x25` in C (Slide 94)?",
    "options": [
      "25 and 25",
      "21 and 37",
      "25 and 37",
      "17 and 37"
    ],
    "answer": 1,
    "explanation": "`025` is octal: 2*8^1 + 5*8^0 = 16 + 5 = 21. `0x25` is hexadecimal: 2*16^1 + 5*16^0 = 32 + 5 = 37."
  },
  {
    "id": "exam_26",
    "question": "Which escape sequence generates an audible alert / bell sound on the console terminal (Slide 94)?",
    "options": [
      "\\b",
      "\\a",
      "\\r",
      "\\v"
    ],
    "answer": 1,
    "explanation": "`\\a` is the alert/bell escape sequence. `\\b` is backspace, `\\r` is carriage return, and `\\v` is vertical tab."
  },
  {
    "id": "exam_27",
    "question": "What is printed by: `int a = 10; printf(\"%zu, %d\", sizeof(a++), a);` in C?",
    "options": [
      "4, 11",
      "4, 10",
      "8, 11",
      "Compilation Error"
    ],
    "answer": 1,
    "explanation": "`sizeof` is a compile-time operator that only determines expression type. Its operand `a++` is never executed at runtime, so `a` remains 10."
  },
  {
    "id": "exam_28",
    "question": "What is the value of `x` after evaluating: `int x; x = (10, 20, 30);` in C?",
    "options": [
      "10",
      "20",
      "30",
      "60"
    ],
    "answer": 2,
    "explanation": "The comma operator evaluates from left to right and produces the value of the rightmost operand, which is 30."
  },
  {
    "id": "exam_29",
    "question": "In the statement `double result = 5 / 2;`, what is the final numeric value stored in `result`?",
    "options": [
      "2.5",
      "2.0",
      "2",
      "0.0"
    ],
    "answer": 1,
    "explanation": "`5 / 2` evaluates as integer division = 2, which is subsequently converted to `2.0` upon assignment to the `double` variable."
  },
  {
    "id": "exam_30",
    "question": "Where are non-static local variables stored, and what is their default initial content (Slide 64)?",
    "options": [
      "Stack segment, initialized to indeterminate (garbage) values",
      "BSS segment, initialized to 0",
      "Heap segment, initialized to NULL",
      "Data segment, initialized to 0"
    ],
    "answer": 0,
    "explanation": "Local automatic variables are allocated in the function's Stack frame and retain whatever indeterminate garbage data was previously in that memory."
  }
];

// Code Sandbox Pre-configured Programs
const SANDBOX_PROGRAMS = {
  hello: {
    title: "1. Hello World (Slide 46)",
    code: `#include <stdio.h>

/* Author: XYZ
   Date: 16-08-2017
   Description: Writes 'Hello, World!' on screen */
int main(void) {
    /* first C program */
    printf("Hello, World!\\n");
    return 0;
}`,
    output: `$ gcc -Wall hello.c -o hello
$ ./hello
Hello, World!`
  },
  compilation: {
    title: "2. Compilation 4-Stages Demo (Slides 51-57)",
    code: `#include <stdio.h>
#define SOMETHING "Hello World"

int main(void) {
    // 1. Preprocessor expands SOMETHING & inlines stdio.h
    printf("Hi\\n");
    printf(SOMETHING "\\n");
    return 0;
}`,
    output: `$ gcc -E -o demo.i demo.c   # Stage 1: Preprocess (macros expanded)
$ gcc -S demo.i -o demo.s   # Stage 2: Compile to assembly (cc1)
$ gcc -c demo.s -o demo.o   # Stage 3: Assemble to object (as)
$ gcc demo.o -o demo        # Stage 4: Link with libc (ld)
$ ./demo
Hi
Hello World`
  },
  product: {
    title: "3. Formatted Product I/O (Slide 106)",
    code: `#include <stdio.h>

int main(void) {
    char pname[20] = "Laptop";
    int pid = 123;
    int qty = 23;
    char mname[50] = "Dell";
    char category[50] = "Electronics";

    printf("Product Name is: %s\\n", pname);
    printf("Product id is: %d\\n", pid);
    printf("Product quantity is: %d\\n", qty);
    printf("Manufacturer name is: %s\\n", mname);
    printf("Category name is: %s\\n", category);
    return 0;
}`,
    output: `$ gcc product.c -o product
$ ./product
Product Name is: Laptop
Product id is: 123
Product quantity is: 23
Manufacturer name is: Dell
Category name is: Electronics`
  },
  relational: {
    title: "4. Relational Chaining (Slide 117)",
    code: `#include <stdio.h>

int main(void) {
    int a = 1, b = 2, c = 3;
    int d;

    // Evaluates Left-to-Right: (a > b) is 0; then (0 < c) is 1!
    d = a > b < c;
    printf("The Value of d is: %d\\n", d);
    return 0;
}`,
    output: `$ gcc -Wall relational.c -o relational
relational.c: In function 'main':
relational.c:8:11: warning: comparisons like 'X<=Y<=Z' do not have their mathematical meaning [-Wparentheses]
    d = a > b < c;
          ^
$ ./relational
The Value of d is: 1`
  },
  escape: {
    title: "5. Octal & Hex Escape Sequences (Slide 94)",
    code: `#include <stdio.h>

int main(void) {
    printf("Hello fri\\rend\\n"); // \\r carriage return overwrites start of line
    printf("a\\\\b\\n");            // literal backslash

    char* s = "A\\072\\065";       // \\072 is octal 72 = 58 = ':', \\065 is octal 65 = 53 = '5'
    printf("%s\\n", s);

    char* y = "B\\x4a";           // \\x4a is hex 4A = 74 = 'J'
    printf("%s\\n", y);
    return 0;
}`,
    output: `$ gcc escape.c -o escape
$ ./escape
endlo fri
a\\b
A:5
BJ`
  },
  switch: {
    title: "6. Switch Unreachable Trap (Slide 146)",
    code: `#include <stdio.h>

int main(void) {
    int x = 1;
    switch (x) {
        x = x + 1; // WARNING: Unreachable code before first case!

        case 1:
            printf("Choice is 1\\n");
            break;
        case 2:
            printf("Choice is 2\\n");
            break;
        default:
            printf("Default\\n");
            break;
    }
    return 0;
}`,
    output: `$ gcc -Wall switch.c -o switch
switch.c: In function 'main':
switch.c:6:11: warning: statement will never be executed [-Wswitch-unreachable]
        x = x + 1;
          ^
$ ./switch
Choice is 1`
  },
  sum_digits: {
    title: "7. Sum of Digits While Loop (Slide 43)",
    code: `#include <stdio.h>

int main(void) {
    int N = 1234;
    int Sum = 0;
    int Rem;

    while (N != 0) {
        Rem = N % 10;
        Sum = Sum + Rem;
        N = N / 10;
    }

    printf("Sum of digits = %d\\n", Sum);
    return 0;
}`,
    output: `$ gcc sum_digits.c -o sum_digits
$ ./sum_digits
Sum of digits = 10`
  },
  printf_ret: {
    title: "8. printf() Return Value (Slide 160)",
    code: `#include <stdio.h>

int main(void) {
    // printf returns the number of characters printed
    printf(" %d\\n", printf("geeksforgeeks"));
    printf("Empty return: %d\\n", printf(""));
    return 0;
}`,
    output: `$ gcc printf_ret.c -o printf_ret
$ ./printf_ret
geeksforgeeks 13
Empty return: 0`
  }
};

// Precedence Playground Presets
const PRECEDENCE_DATA = {
  relational: {
    expr: "d = a > b < c",
    explanation: `<h4>Relational Chaining Analysis: <code>d = a &gt; b &lt; c</code> (where a=1, b=2, c=3)</h4>
      <p>1. In C, relational operators (<code>&gt;</code> and <code>&lt;</code>) have <strong>equal precedence</strong> and associate <strong>Left-to-Right</strong>.</p>
      <p>2. First, the subexpression <code>(a &gt; b)</code> is evaluated: <code>(1 &gt; 2)</code> evaluates to <strong>0 (False)</strong>.</p>
      <p>3. Next, the remaining expression becomes <code>0 &lt; c</code>: <code>(0 &lt; 3)</code> evaluates to <strong>1 (True)</strong>!</p>
      <p>4. Finally, assignment assigns <strong>1</strong> to <code>d</code>. Notice that GCC issues a warning: <em>'comparisons like X&lt;=Y&lt;=Z do not have their mathematical meaning'</em>.</p>`
  },
  arithmetic: {
    expr: "3 + 4 * 5",
    explanation: `<h4>Arithmetic Precedence: <code>3 + 4 * 5</code></h4>
      <p>1. In C, multiplication (<code>*</code>) has higher precedence than addition (<code>+</code>).</p>
      <p>2. <code>4 * 5</code> evaluates first to <strong>20</strong>.</p>
      <p>3. <code>3 + 20</code> evaluates to <strong>23</strong> (NOT 35!). This is why BODMAS does not apply in C—operators have strict binary priority tiers.</p>`
  },
  shift: {
    expr: "x << 2 + 1 (where x=10)",
    explanation: `<h4>Shift vs Arithmetic: <code>x &lt;&lt; 2 + 1</code></h4>
      <p>1. Addition (<code>+</code>) has <strong>higher precedence</strong> than bitwise left shift (<code>&lt;&lt;</code>)!</p>
      <p>2. The subexpression <code>2 + 1</code> is evaluated first, producing <strong>3</strong>.</p>
      <p>3. The expression becomes <code>x &lt;&lt; 3</code> &rarr; 10 * 8 = <strong>80</strong>.</p>
      <p>4. Many programmers falsely assume <code>(x &lt;&lt; 2) + 1 = 41</code>, causing critical low-level bugs!</p>`
  },
  shortcircuit: {
    expr: "(a == b) && printf(\"C\")",
    explanation: `<h4>Logical AND Short-Circuiting: <code>(a == b) &amp;&amp; printf(\"C\")</code></h4>
      <p>1. Logical AND (<code>&amp;&amp;</code>) guarantees left-to-right evaluation.</p>
      <p>2. If the left-hand operand is False (0), the entire expression can never be true.</p>
      <p>3. Therefore, C <strong>short-circuits</strong> and skips evaluation of the right-hand operand entirely. <code>printf(\"C\")</code> is NEVER called!</p>`
  },
  comma: {
    expr: "a = (1, 2, 3)",
    explanation: `<h4>The Comma Operator: <code>a = (1, 2, 3)</code></h4>
      <p>1. The comma operator (<code>,</code>) has the lowest precedence in the entire C language.</p>
      <p>2. Inside parentheses, it evaluates its operands sequentially from left to right, discarding previous results.</p>
      <p>3. It returns the value of the <strong>rightmost expression</strong> (<code>3</code>), which is assigned to <code>a</code>.</p>`
  },
  bitwise_not: {
    expr: "~35",
    explanation: `<h4>Bitwise NOT / One's Complement: <code>~35 = -36</code></h4>
      <p>1. Binary of 35 is <code>00000000 00000000 00000000 00100011</code>.</p>
      <p>2. Inverting all 32 bits gives <code>11111111 11111111 11111111 11011100</code>.</p>
      <p>3. In Two's Complement representation, any bit pattern with a leading 1 represents a negative number -M where M = invert(pattern) + 1.</p>
      <p>4. Inverting back gives 35 + 1 = 36. With negative sign, the result is <strong>-36</strong>.</p>
      <p>5. <strong>Universal Theorem:</strong> For any integer N, <strong>~N = -(N + 1)</strong>.</p>`
  }
};

// Memory Segment Details Data
const MEMORY_SEGMENTS_INFO = {
  args: {
    title: "Command-Line Arguments & Environment Variables",
    addr: "Highest Virtual Memory Addresses (~0x7fffffffffff)",
    desc: "Stores program command-line arguments (argc, argv[]) and environment variables passed by the OS kernel when launching the process."
  },
  stack: {
    title: "Stack Segment (Automatic Memory)",
    addr: "Grows downward from high to low memory",
    desc: "Stores local variables, function stack frames, parameter values, and return addresses. Managed automatically by the CPU via push/pop instructions. Extremely fast, but limited in size (prone to Stack Overflow with deep recursion)."
  },
  heap: {
    title: "Heap Segment (Dynamic Memory)",
    addr: "Grows upward towards the Stack",
    desc: "Stores memory requested dynamically at runtime via malloc(), calloc(), and realloc(). Must be explicitly freed by the programmer via free(). Slower allocation and susceptible to memory leaks and heap fragmentation."
  },
  bss: {
    title: "Uninitialized Data Segment (.bss)",
    addr: "Block Started by Symbol (Above .data)",
    desc: "Stores global and static variables that are either uninitialized or explicitly initialized to zero. Does NOT take disk space in the binary file; the OS kernel zeroes this memory block at process load."
  },
  data: {
    title: "Initialized Data Segment (.data)",
    addr: "Above Text Segment",
    desc: "Stores global and static variables initialized with non-zero values by the programmer (e.g. static int x = 10;). Split into read-write area for mutable globals and read-only area for string literals."
  },
  text: {
    title: "Text Segment (Code Segment)",
    addr: "Lowest Virtual Memory Addresses (~0x00400000)",
    desc: "Contains the compiled machine language instructions executed by the CPU. Marked Read-Only and Executable to prevent programs from accidentally or maliciously modifying their own code."
  }
};

// ============================================================================
// Core Application State & Storage
// ============================================================================
class CourseEngine {
  constructor() {
    this.modules = COURSE_MODULES;
    this.completedModules = new Set(JSON.parse(localStorage.getItem('c_unit1_completed') || '[]'));
    this.quizScores = JSON.parse(localStorage.getItem('c_unit1_scores') || '{}');
    this.theme = localStorage.getItem('c_unit1_theme') || 'dark';

    // Deep linking via URL hash (#m2, #m4, #m9) or query params (?m=2)
    const hash = window.location.hash.replace('#', '').toLowerCase();
    const urlParams = new URLSearchParams(window.location.search);
    const modParam = urlParams.get('m') || urlParams.get('module') || (hash.startsWith('m') ? hash : '');
    let initialIdx = 0;
    if (modParam) {
      const found = this.modules.findIndex(m => m.id.toLowerCase() === modParam || `m${m.num}`.toLowerCase() === modParam || String(m.num) === modParam);
      if (found !== -1) initialIdx = found;
    }
    this.currentModuleIndex = initialIdx;

    const completedParam = urlParams.get('completed');
    if (completedParam) {
      completedParam.split(',').forEach(id => this.completedModules.add(id));
    }

    this.initElements();
    this.initTheme();
    this.initTimeline();
    this.initSyllabus();
    this.initToolsLab();
    this.initEvents();
    this.renderCurrentModule();
    this.updateOverallProgress();
    if (hash === 'tools') this.openModal('tools-modal');
    if (hash === 'exam') this.openExamModal();
    if (hash === 'sidebar') this.sidebar.classList.add('open');

    if (urlParams.get('modal') === 'tools' || hash === 'tools') {
      setTimeout(() => this.openModal('tools-modal'), 100);
    } else if (urlParams.get('modal') === 'exam' || hash === 'exam') {
      setTimeout(() => this.openExamModal(), 100);
    }
  }

  initElements() {
    this.viewport = document.getElementById('lesson-viewport');
    this.timelineNodes = document.getElementById('timeline-nodes-container');
    this.timelineFill = document.getElementById('timeline-progress-line');
    this.stepIndicator = document.getElementById('timeline-step-indicator');
    this.progressText = document.getElementById('overall-progress-text');
    this.progressFill = document.getElementById('overall-progress-fill');
    this.scrollProgressBar = document.getElementById('scroll-progress-bar');
    this.markCompleteBtn = document.getElementById('mark-complete-btn');
    this.markCompleteText = document.getElementById('mark-complete-text');
    this.footerPrevBtn = document.getElementById('footer-prev-btn');
    this.footerNextBtn = document.getElementById('footer-next-btn');
    this.prevStepBtn = document.getElementById('prev-step-btn');
    this.nextStepBtn = document.getElementById('next-step-btn');
    this.sidebar = document.getElementById('syllabus-sidebar');
    this.syllabusList = document.getElementById('syllabus-nav-list');
  }

  initTheme() {
    document.documentElement.setAttribute('data-theme', this.theme);
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) {
      themeBtn.innerHTML = this.theme === 'dark' ? '<i class="fa-solid fa-sun"></i>' : '<i class="fa-solid fa-moon"></i>';
    }
  }

  toggleTheme() {
    this.theme = this.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', this.theme);
    localStorage.setItem('c_unit1_theme', this.theme);
    this.initTheme();
  }

  initTimeline() {
    this.timelineNodes.innerHTML = '';
    this.modules.forEach((mod, idx) => {
      const node = document.createElement('div');
      node.className = `timeline-node ${idx === this.currentModuleIndex ? 'active' : ''} ${this.completedModules.has(mod.id) ? 'completed' : ''}`;
      node.setAttribute('data-index', idx);
      node.innerHTML = `
        <div class="node-bullet">${this.completedModules.has(mod.id) ? '<i class="fa-solid fa-check"></i>' : mod.num}</div>
        <div class="node-label">M${mod.num}</div>
      `;
      node.addEventListener('click', () => this.jumpToModule(idx));
      this.timelineNodes.appendChild(node);
    });
    this.updateTimelineTrack();
  }

  updateTimelineTrack() {
    const total = this.modules.length;
    const progressPercent = (this.currentModuleIndex / (total - 1)) * 100;
    this.timelineFill.style.width = `${progressPercent}%`;
    this.stepIndicator.textContent = `Milestone ${this.currentModuleIndex + 1} of ${total}`;

    const nodes = this.timelineNodes.querySelectorAll('.timeline-node');
    nodes.forEach((n, idx) => {
      n.classList.toggle('active', idx === this.currentModuleIndex);
      n.classList.toggle('completed', this.completedModules.has(this.modules[idx].id));
      const bullet = n.querySelector('.node-bullet');
      if (bullet) {
        bullet.innerHTML = this.completedModules.has(this.modules[idx].id) 
          ? '<i class="fa-solid fa-check"></i>' 
          : this.modules[idx].num;
      }
    });

    const activeNode = nodes[this.currentModuleIndex];
    if (activeNode) {
      activeNode.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
    }
  }

  initSyllabus() {
    this.syllabusList.innerHTML = '';
    this.modules.forEach((mod, idx) => {
      if (idx === 0) {
        const div1 = document.createElement('div');
        div1.className = 'syllabus-unit-divider';
        div1.innerHTML = '<span class="unit-tag">UNIT 1</span> <span>Introduction to Computing (Slides 1–45)</span>';
        this.syllabusList.appendChild(div1);
      } else if (idx === 4) {
        const div2 = document.createElement('div');
        div2.className = 'syllabus-unit-divider';
        div2.innerHTML = '<span class="unit-tag">UNIT 2</span> <span>C Programming Fundamentals (Slides 46–162)</span>';
        this.syllabusList.appendChild(div2);
      }

      const item = document.createElement('button');
      item.className = `syllabus-item ${idx === this.currentModuleIndex ? 'active' : ''} ${this.completedModules.has(mod.id) ? 'completed' : ''}`;
      item.innerHTML = `
        <div class="item-icon">${this.completedModules.has(mod.id) ? '<i class="fa-solid fa-check"></i>' : mod.num}</div>
        <div class="item-content">
          <div class="item-title">${mod.title}</div>
          <div class="item-subtitle">${mod.slides} &bull; ${mod.time}</div>
        </div>
      `;
      item.addEventListener('click', () => {
        this.jumpToModule(idx);
        this.sidebar.classList.remove('open');
      });
      this.syllabusList.appendChild(item);
    });
  }

  updateSyllabusActiveState() {
    const items = this.syllabusList.querySelectorAll('.syllabus-item');
    items.forEach((item, idx) => {
      item.classList.toggle('active', idx === this.currentModuleIndex);
      item.classList.toggle('completed', this.completedModules.has(this.modules[idx].id));
      const icon = item.querySelector('.item-icon');
      if (icon) {
        icon.innerHTML = this.completedModules.has(this.modules[idx].id) 
          ? '<i class="fa-solid fa-check"></i>' 
          : this.modules[idx].num;
      }
    });
  }

  jumpToModule(index, updateHash = true) {
    if (index < 0 || index >= this.modules.length) return;
    this.currentModuleIndex = index;
    if (updateHash) {
      try {
        history.replaceState(null, '', `#${this.modules[index].id}`);
      } catch (e) {}
    }
    this.renderCurrentModule();
    this.updateTimelineTrack();
    this.updateSyllabusActiveState();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  renderCurrentModule() {
    const mod = this.modules[this.currentModuleIndex];
    const isCompleted = this.completedModules.has(mod.id);

    this.footerPrevBtn.disabled = this.currentModuleIndex === 0;
    this.footerNextBtn.disabled = this.currentModuleIndex === this.modules.length - 1;
    this.prevStepBtn.disabled = this.currentModuleIndex === 0;
    this.nextStepBtn.disabled = this.currentModuleIndex === this.modules.length - 1;

    this.markCompleteBtn.classList.toggle('is-completed', isCompleted);
    this.markCompleteText.textContent = isCompleted ? 'Mastered / Understood' : 'Mark as Understood';
    this.markCompleteBtn.querySelector('i').className = isCompleted ? 'fa-solid fa-circle-check' : 'fa-regular fa-circle-check';

    this.viewport.innerHTML = `
      <article class="lesson-card">
        <header class="lesson-hero">
          <div class="lesson-badges">
            <span class="badge unit-pill">${mod.num <= 4 ? '<i class="fa-solid fa-microchip"></i> Unit 1: Computing' : '<i class="fa-solid fa-code"></i> Unit 2: C Fundamentals'}</span>
            <span class="badge module-num">Module ${mod.num} of ${this.modules.length}</span>
            <span class="badge slides-range">${mod.slides}</span>
            <span class="badge status-pill">${isCompleted ? '<i class="fa-solid fa-check"></i> Completed' : '<i class="fa-regular fa-clock"></i> In Progress'}</span>
          </div>
          <h1 class="lesson-title">${mod.title}</h1>
          <p class="lesson-subtitle">${mod.subtitle}</p>
        </header>

        <div class="lesson-body">
          ${mod.content}
        </div>

        <div class="teaching-block">
          <h3><i class="fa-solid fa-code"></i> Professor's Verified C Workbench</h3>
          <p>${mod.code.desc}</p>
          <div class="code-container">
            <div class="code-header">
              <span class="code-lang-tag"><i class="fa-solid fa-file-code"></i> ${mod.code.title}</span>
              <button class="code-copy-btn" onclick="copySnippet(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre><code class="language-c">${escapeHtml(mod.code.snippet)}</code></pre>
            <div class="code-output-preview">
              <span class="output-label">Compiled Execution Output:</span>
              <pre>${escapeHtml(mod.code.output)}</pre>
            </div>
          </div>
        </div>

        <div class="teaching-block">
          <h3><i class="fa-solid fa-compass"></i> Curated Learning Resources & References</h3>
          <p>Carefully vetted external guides, standards documentation, and video lectures corresponding to this lesson:</p>
          <div class="resources-grid">
            ${mod.resources.map(res => `
              <a href="${res.url}" target="_blank" rel="noopener noreferrer" class="resource-card">
                <div class="resource-header ${res.type}">
                  <i class="fa-solid ${res.type === 'video' ? 'fa-circle-play' : res.type === 'tool' ? 'fa-screwdriver-wrench' : 'fa-book'}"></i>
                  <span>${res.type.toUpperCase()}</span>
                </div>
                <div class="resource-title">${res.title}</div>
                <div class="resource-desc">${res.desc}</div>
                <div class="resource-link-text">Open Resource <i class="fa-solid fa-arrow-up-right-from-square"></i></div>
              </a>
            `).join('')}
          </div>
        </div>

        <section class="quiz-section" id="module-quiz-section">
          <div class="quiz-header">
            <div class="quiz-title-wrap">
              <span class="quiz-tag"><i class="fa-solid fa-spell-check"></i> KNOWLEDGE CHECKPOINT</span>
              <h3>Module ${mod.num} Practice Quiz (Multiple Choice Only)</h3>
            </div>
            <div class="quiz-score-badge" id="quiz-score-badge-${mod.id}">
              Score: ${this.quizScores[mod.id] !== undefined ? this.quizScores[mod.id] + '/' + mod.quiz.length : 'Not Taken'}
            </div>
          </div>

          <div class="quiz-questions-list">
            ${mod.quiz.map((q, qIdx) => `
              <div class="quiz-card" id="card-${q.id}">
                <div class="quiz-question-text"><strong>Q${qIdx + 1}.</strong> ${q.question}</div>
                <div class="quiz-options">
                  ${q.options.map((opt, optIdx) => `
                    <button class="quiz-option-btn" data-qid="${q.id}" data-opt="${optIdx}" onclick="engine.handleQuizOption('${mod.id}', '${q.id}', ${optIdx})">
                      <span class="opt-prefix">${String.fromCharCode(65 + optIdx)}</span>
                      <span class="opt-text">${opt}</span>
                    </button>
                  `).join('')}
                </div>
                <div class="quiz-explanation-box hidden" id="exp-${q.id}"></div>
              </div>
            `).join('')}
          </div>
        </section>
      </article>
    `;

    const renderMath = () => {
      if (window.renderMathInElement) {
        try {
          renderMathInElement(this.viewport, {
            delimiters: [
              {left: "$$", right: "$$", display: true},
              {left: "$", right: "$", display: false}
            ],
            throwOnError: false,
            ignoredClasses: ["language-c", "code-output-preview", "code-copy-btn"]
          });
        } catch (e) {}
      }
    };
    renderMath();
    setTimeout(renderMath, 150);
  }

  handleQuizOption(modId, qId, selectedOpt) {
    const mod = this.modules.find(m => m.id === modId);
    if (!mod) return;
    const question = mod.quiz.find(q => q.id === qId);
    if (!question) return;

    const card = document.getElementById(`card-${qId}`);
    const expBox = document.getElementById(`exp-${qId}`);
    const buttons = card.querySelectorAll('.quiz-option-btn');

    buttons.forEach((btn, idx) => {
      btn.disabled = true;
      if (idx === question.answer) {
        btn.classList.add('correct');
      } else if (idx === selectedOpt) {
        btn.classList.add('incorrect');
      }
    });

    const isCorrect = selectedOpt === question.answer;
    expBox.className = `quiz-explanation-box ${isCorrect ? 'correct' : 'incorrect'}`;
    expBox.innerHTML = `
      <div class="explanation-title ${isCorrect ? 'correct' : 'incorrect'}">
        <i class="fa-solid ${isCorrect ? 'fa-circle-check' : 'fa-circle-xmark'}"></i>
        ${isCorrect ? 'Correct! Excellent Reasoning.' : "Incorrect. Let's Analyze Why:"}
      </div>
      <p>${question.explanation}</p>
    `;
    expBox.classList.remove('hidden');

    this.recalculateModuleQuizScore(mod);
  }

  recalculateModuleQuizScore(mod) {
    let answered = 0;
    let correct = 0;
    mod.quiz.forEach(q => {
      const card = document.getElementById(`card-${q.id}`);
      if (card) {
        const correctBtn = card.querySelector('.quiz-option-btn.correct');
        const incorrectBtn = card.querySelector('.quiz-option-btn.incorrect');
        if (correctBtn && !incorrectBtn) {
          correct++;
          answered++;
        } else if (incorrectBtn) {
          answered++;
        }
      }
    });

    if (answered === mod.quiz.length) {
      this.quizScores[mod.id] = correct;
      localStorage.setItem('c_unit1_scores', JSON.stringify(this.quizScores));
      const badge = document.getElementById(`quiz-score-badge-${mod.id}`);
      if (badge) badge.textContent = `Score: ${correct}/${mod.quiz.length}`;
      
      if (correct >= Math.ceil(mod.quiz.length * 0.6)) {
        this.markModuleCompleted(mod.id, true);
      }
      this.updateOverallProgress();
    }
  }

  toggleCurrentModuleCompleted() {
    const mod = this.modules[this.currentModuleIndex];
    if (this.completedModules.has(mod.id)) {
      this.completedModules.delete(mod.id);
    } else {
      this.completedModules.add(mod.id);
    }
    localStorage.setItem('c_unit1_completed', JSON.stringify(Array.from(this.completedModules)));
    this.renderCurrentModule();
    this.updateTimelineTrack();
    this.updateSyllabusActiveState();
    this.updateOverallProgress();
  }

  markModuleCompleted(modId, state) {
    if (state) {
      this.completedModules.add(modId);
    } else {
      this.completedModules.delete(modId);
    }
    localStorage.setItem('c_unit1_completed', JSON.stringify(Array.from(this.completedModules)));
    this.updateTimelineTrack();
    this.updateSyllabusActiveState();
    this.updateOverallProgress();
  }

  updateOverallProgress() {
    const total = this.modules.length;
    const completed = this.completedModules.size;
    const pct = Math.round((completed / total) * 100);

    this.progressText.textContent = `${pct}%`;
    this.progressFill.style.width = `${pct}%`;
  }

  initToolsLab() {
    const decInput = document.getElementById('calc-dec');
    const binInput = document.getElementById('calc-bin');
    const hexInput = document.getElementById('calc-hex');
    const octInput = document.getElementById('calc-oct');

    const updateAllBases = (decimalVal) => {
      if (isNaN(decimalVal)) return;
      const d = parseInt(decimalVal, 10);
      decInput.value = d;
      binInput.value = (d >>> 0).toString(2).padStart(16, '0');
      hexInput.value = '0x' + (d >>> 0).toString(16).toUpperCase();
      octInput.value = '0' + (d >>> 0).toString(8);

      document.getElementById('bit-twos-comp').textContent = (-d).toString();
      document.getElementById('bit-not-val').textContent = `${(~d)} (Notice ~${d} = ${(~d)}!)`;
      document.getElementById('bit-lshift').textContent = (d << 1).toString();
      document.getElementById('bit-rshift').textContent = (d >> 1).toString();

      const bitContainer = document.getElementById('bit-visualizer-display');
      if (bitContainer) {
        bitContainer.innerHTML = '';
        const binStr = (d >>> 0).toString(2).padStart(16, '0');
        for (let i = 0; i < 16; i++) {
          const bitBox = document.createElement('div');
          bitBox.className = `bit-box ${binStr[i] === '1' ? 'one' : ''}`;
          bitBox.textContent = binStr[i];
          bitContainer.appendChild(bitBox);
        }
      }
    };

    if (decInput) {
      decInput.addEventListener('input', (e) => updateAllBases(parseInt(e.target.value, 10) || 0));
      binInput.addEventListener('input', (e) => updateAllBases(parseInt(e.target.value, 2) || 0));
      hexInput.addEventListener('input', (e) => updateAllBases(parseInt(e.target.value.replace(/^0x/i, ''), 16) || 0));
      octInput.addEventListener('input', (e) => updateAllBases(parseInt(e.target.value, 8) || 0));
      updateAllBases(35);
    }

    const memBlocks = document.querySelectorAll('.memory-block');
    const memDetails = document.getElementById('memory-segment-details');
    const renderMemDetails = (segKey) => {
      const info = MEMORY_SEGMENTS_INFO[segKey] || MEMORY_SEGMENTS_INFO['text'];
      memBlocks.forEach(b => b.classList.toggle('selected', b.getAttribute('data-segment') === segKey));
      if (memDetails) {
        memDetails.innerHTML = `
          <h4><i class="fa-solid fa-layer-group"></i> ${info.title}</h4>
          <p><strong>Virtual Address Range:</strong> <code>${info.addr}</code></p>
          <p>${info.desc}</p>
        `;
      }
    };
    memBlocks.forEach(b => {
      b.addEventListener('click', () => renderMemDetails(b.getAttribute('data-segment')));
    });
    renderMemDetails('text');

    const precSelect = document.getElementById('precedence-preset-select');
    const precBox = document.getElementById('precedence-explanation-box');
    const renderPrec = (key) => {
      const item = PRECEDENCE_DATA[key] || PRECEDENCE_DATA['relational'];
      if (precBox) precBox.innerHTML = item.explanation;
    };
    if (precSelect) {
      precSelect.addEventListener('change', (e) => renderPrec(e.target.value));
      renderPrec('relational');
    }

    const codeSelect = document.getElementById('sandbox-code-select');
    const codeDisplay = document.getElementById('sandbox-code-display');
    const termOutput = document.getElementById('sandbox-terminal-output');
    const runBtn = document.getElementById('sandbox-run-btn');

    const loadSandboxSample = (sampleKey) => {
      const sample = SANDBOX_PROGRAMS[sampleKey] || SANDBOX_PROGRAMS['hello'];
      if (codeDisplay) codeDisplay.textContent = sample.code;
      if (termOutput) {
        termOutput.innerHTML = `
          $ gcc program.c -o program<br>
          $ ./program<br>
          <span class="term-dim">Click "Run in GCC" to execute...</span>
        `;
      }
    };

    if (codeSelect) {
      codeSelect.addEventListener('change', (e) => loadSandboxSample(e.target.value));
      loadSandboxSample('hello');
    }

    if (runBtn) {
      runBtn.addEventListener('click', () => {
        const sampleKey = codeSelect ? codeSelect.value : 'hello';
        const sample = SANDBOX_PROGRAMS[sampleKey] || SANDBOX_PROGRAMS['hello'];
        if (termOutput) {
          termOutput.innerHTML = `<span style="color: #10b981;">Compiling with GCC 13.2.0...</span><br>`;
          setTimeout(() => {
            termOutput.innerHTML = sample.output.replace(/\\n/g, '<br>');
          }, 250);
        }
      });
    }

    const modalTabs = document.querySelectorAll('.modal-tab');
    modalTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        modalTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        const targetId = tab.getAttribute('data-tab');
        document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
        const targetPanel = document.getElementById(targetId);
        if (targetPanel) targetPanel.classList.add('active');
      });
    });
  }

  initEvents() {
    document.getElementById('theme-toggle-btn')?.addEventListener('click', () => this.toggleTheme());
    document.getElementById('syllabus-toggle-btn')?.addEventListener('click', () => this.sidebar.classList.toggle('open'));
    document.getElementById('sidebar-close-btn')?.addEventListener('click', () => this.sidebar.classList.remove('open'));
    document.getElementById('tools-modal-btn')?.addEventListener('click', () => this.openModal('tools-modal'));
    document.getElementById('exam-jump-btn')?.addEventListener('click', () => this.openExamModal());

    this.prevStepBtn?.addEventListener('click', () => this.jumpToModule(this.currentModuleIndex - 1));
    this.nextStepBtn?.addEventListener('click', () => this.jumpToModule(this.currentModuleIndex + 1));
    this.footerPrevBtn?.addEventListener('click', () => this.jumpToModule(this.currentModuleIndex - 1));
    this.footerNextBtn?.addEventListener('click', () => this.jumpToModule(this.currentModuleIndex + 1));
    this.markCompleteBtn?.addEventListener('click', () => this.toggleCurrentModuleCompleted());

    document.getElementById('jump-quiz-btn')?.addEventListener('click', () => {
      const qSec = document.getElementById('module-quiz-section');
      if (qSec) qSec.scrollIntoView({ behavior: 'smooth' });
    });

    const resetProgress = () => {
      if (confirm('Are you sure you want to reset your learning progress and quiz scores?')) {
        localStorage.removeItem('c_unit1_completed');
        localStorage.removeItem('c_unit1_scores');
        this.completedModules.clear();
        this.quizScores = {};
        this.renderCurrentModule();
        this.updateTimelineTrack();
        this.updateSyllabusActiveState();
        this.updateOverallProgress();
      }
    };
    document.getElementById('reset-progress-btn')?.addEventListener('click', resetProgress);

    document.querySelectorAll('[data-close-modal]').forEach(btn => {
      btn.addEventListener('click', () => {
        const modalId = btn.getAttribute('data-close-modal');
        this.closeModal(modalId);
      });
    });

    document.getElementById('print-cert-btn')?.addEventListener('click', () => window.print());

    window.addEventListener('scroll', () => {
      const scrollable = document.documentElement.scrollHeight - window.innerHeight;
      const scrolled = window.scrollY;
      const progressPercentage = scrollable > 0 ? (scrolled / scrollable) : 0;
      if (this.scrollProgressBar) {
        this.scrollProgressBar.style.transform = `scaleX(${progressPercentage})`;
      }
    });

    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') return;
      if (e.key === 'ArrowLeft') this.jumpToModule(this.currentModuleIndex - 1);
      if (e.key === 'ArrowRight') this.jumpToModule(this.currentModuleIndex + 1);
    });

    window.addEventListener('hashchange', () => {
      const h = window.location.hash.replace('#', '').toLowerCase();
      if (h === 'tools') {
        this.openModal('tools-modal');
      } else if (h === 'exam') {
        this.openExamModal();
      } else if (h === 'sidebar') {
        this.sidebar.classList.add('open');
      } else {
        const foundIdx = this.modules.findIndex(m => m.id.toLowerCase() === h || `m${m.num}`.toLowerCase() === h || String(m.num) === h);
        if (foundIdx !== -1 && foundIdx !== this.currentModuleIndex) {
          this.jumpToModule(foundIdx, false);
        }
      }
    });
  }

  openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) modal.classList.remove('hidden');
  }

  closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) modal.classList.add('hidden');
  }

  openExamModal() {
    this.openModal('exam-modal');
    this.renderExamView();
  }

  renderExamView() {
    const body = document.getElementById('exam-modal-body');
    if (!body) return;

    body.innerHTML = `
      <div class="tool-intro">
        <h3>Units 1 & 2 Comprehensive Assessment</h3>
        <p>This exam consists of ${CAPSTONE_EXAM.length} multiple-choice questions testing your comprehensive understanding of Computer Organization, Number Systems, Flowcharts, Compilation Pipelines, Memory Layout, Data Types, and C Control Structures across Units 1 & 2. Score 80% (${Math.ceil(CAPSTONE_EXAM.length * 0.8)}/${CAPSTONE_EXAM.length}) or higher to earn your <strong>Course Completion Certificate</strong>!</p>
      </div>

      <div class="exam-form" id="exam-form">
        ${CAPSTONE_EXAM.map((q, idx) => `
          <div class="quiz-card" id="exam-card-${q.id}">
            <div class="quiz-question-text"><strong>${idx + 1}.</strong> ${q.question}</div>
            <div class="quiz-options">
              ${q.options.map((opt, optIdx) => `
                <button class="quiz-option-btn" data-qid="${q.id}" data-opt="${optIdx}" onclick="engine.handleExamOption('${q.id}', ${optIdx})">
                  <span class="opt-prefix">${String.fromCharCode(65 + optIdx)}</span>
                  <span class="opt-text">${opt}</span>
                </button>
              `).join('')}
            </div>
            <div class="quiz-explanation-box hidden" id="exam-exp-${q.id}"></div>
          </div>
        `).join('')}
      </div>

      <div class="exam-submit-bar" style="margin-top: 2rem; display: flex; justify-content: space-between; align-items: center;">
        <div id="exam-score-display" style="font-weight: 700; font-size: 1.1rem; color: var(--accent-cyan);"></div>
        <button id="exam-cert-btn" class="action-btn next hidden" onclick="engine.openCertificateModal()">
          <i class="fa-solid fa-certificate"></i> Claim Course Certificate
        </button>
      </div>
    `;
  }

  handleExamOption(qId, selectedOpt) {
    const question = CAPSTONE_EXAM.find(q => q.id === qId);
    if (!question) return;

    const card = document.getElementById(`exam-card-${qId}`);
    const expBox = document.getElementById(`exam-exp-${qId}`);
    const buttons = card.querySelectorAll('.quiz-option-btn');

    buttons.forEach((btn, idx) => {
      btn.disabled = true;
      if (idx === question.answer) btn.classList.add('correct');
      else if (idx === selectedOpt) btn.classList.add('incorrect');
    });

    const isCorrect = selectedOpt === question.answer;
    expBox.className = `quiz-explanation-box ${isCorrect ? 'correct' : 'incorrect'}`;
    expBox.innerHTML = `
      <div class="explanation-title ${isCorrect ? 'correct' : 'incorrect'}">
        <i class="fa-solid ${isCorrect ? 'fa-circle-check' : 'fa-circle-xmark'}"></i>
        ${isCorrect ? 'Correct!' : 'Incorrect.'}
      </div>
      <p>${question.explanation}</p>
    `;
    expBox.classList.remove('hidden');

    this.checkExamFinished();
  }

  checkExamFinished() {
    let answered = 0;
    let score = 0;
    CAPSTONE_EXAM.forEach(q => {
      const card = document.getElementById(`exam-card-${q.id}`);
      if (card) {
        const correctBtn = card.querySelector('.quiz-option-btn.correct');
        const incorrectBtn = card.querySelector('.quiz-option-btn.incorrect');
        if (correctBtn && !incorrectBtn) score++;
        if (correctBtn || incorrectBtn) answered++;
      }
    });

    const display = document.getElementById('exam-score-display');
    const certBtn = document.getElementById('exam-cert-btn');

    if (display) {
      display.textContent = `Completed: ${answered} / ${CAPSTONE_EXAM.length} | Score: ${score} / ${CAPSTONE_EXAM.length} (${Math.round((score / CAPSTONE_EXAM.length) * 100)}%)`;
    }

    if (answered === CAPSTONE_EXAM.length) {
      const pct = Math.round((score / CAPSTONE_EXAM.length) * 100);
      const passingScore = Math.ceil(CAPSTONE_EXAM.length * 0.8);
      if (score >= passingScore) {
        display.innerHTML = `<span style="color: #10b981;">🎉 Outstanding! You Passed with ${score}/${CAPSTONE_EXAM.length} (${pct}%)!</span>`;
        if (certBtn) certBtn.classList.remove('hidden');
      } else {
        display.innerHTML = `<span style="color: #f59e0b;">Score: ${score}/${CAPSTONE_EXAM.length} (${pct}%). You need 80% (${passingScore}/${CAPSTONE_EXAM.length}) to claim the certificate. Review modules and try again!</span>`;
      }
    }
  }

  openCertificateModal() {
    this.closeModal('exam-modal');
    this.openModal('certificate-modal');

    const wrapper = document.getElementById('certificate-canvas-wrapper');
    if (!wrapper) return;

    const studentName = prompt('Enter your full name for the certificate:', 'Computer Science Scholar') || 'Computer Science Scholar';
    const dateStr = new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });

    wrapper.innerHTML = `
      <div class="cert-title">Certificate of Completion</div>
      <div class="cert-sub">This certifies that</div>
      <div class="cert-name">${escapeHtml(studentName)}</div>
      <p class="cert-desc">has successfully demonstrated comprehensive theoretical mastery and practical problem-solving competence in <strong>Units 1 & 2: Overview of Computer Organization and C Programming Fundamentals</strong>, including Computer Architecture, Number Systems, Flowcharts, GCC Compilation Pipelines, Process Memory Layouts, and C Language Syntax.</p>
      <div class="cert-meta-row">
        <div><strong>Course:</strong> C Programming Masterclass</div>
        <div><strong>Date:</strong> ${dateStr}</div>
        <div><strong>Instructor:</strong> Prof. Uday Kumar M</div>
        <div><strong>Status:</strong> Verified & Certified</div>
      </div>
    `;
  }
}

// Utilities
function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

function copySnippet(btn) {
  const pre = btn.closest('.code-container').querySelector('code');
  if (pre) {
    navigator.clipboard.writeText(pre.textContent).then(() => {
      const originalText = btn.innerHTML;
      btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
      setTimeout(() => { btn.innerHTML = originalText; }, 2000);
    });
  }
}

// Boot Engine on DOM Ready
let engine;
document.addEventListener('DOMContentLoaded', () => {
  engine = new CourseEngine();
});
