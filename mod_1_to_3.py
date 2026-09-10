import json

modules = []

# Module 1
modules.append({
    "id": "m1",
    "num": 1,
    "title": "Genesis of Computing, Architecture & C",
    "subtitle": "Computer Organization, 5 Generations of Languages, Dennis Ritchie & Standards",
    "slides": "Slides 1–7, 15, 25",
    "time": "25 mins",
    "content": """
      <div class="teaching-block">
        <h3><i class="fa-solid fa-chalkboard-user"></i> Professor's Welcome: What is a Computer System?</h3>
        <p>Hello and welcome! Think of a computer not as a magic black box, but as an <strong>orchestra of interconnected parts</strong> working together:</p>
        
        <div class="teacher-callout insight">
          <div class="callout-icon"><i class="fa-solid fa-lightbulb"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Master Philosophy of C</div>
            <p>Dennis Ritchie created C in 1972 at Bell Labs to write the <strong>UNIX operating system</strong>. Most languages hide how the computer works; C gives you direct control over CPU memory addresses, individual bits, and raw hardware speed. That's why Windows, Linux, macOS, iOS, Android, and car engine controllers are still powered by C today!</p>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-sitemap"></i> The 4 Layers: How You Talk to the Silicon (Slide 25)</h3>
        <p>Whenever you tap an app on your phone or computer, instructions pass through four distinct layers:</p>
        
        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Layer</th><th>Simple Real-World Role</th><th>Examples</th></tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1. User</strong></td>
                <td>The human being directing the action.</td>
                <td>You, a gamer, a software developer.</td>
              </tr>
              <tr>
                <td><strong>2. Application Software</strong></td>
                <td>The tool designed to do a specific job for the user.</td>
                <td>Chrome browser, WhatsApp, VS Code, VLC player.</td>
              </tr>
              <tr>
                <td><strong>3. Operating System (OS)</strong></td>
                <td>The <strong>Master Manager</strong>. It translates what the app wants into commands the physical hardware understands, while managing memory and security.</td>
                <td>Linux, Windows 11, macOS, Android, UNIX.</td>
              </tr>
              <tr>
                <td><strong>4. Hardware</strong></td>
                <td>The physical electronics and chips that execute electric pulses.</td>
                <td>CPU (Processor), RAM (Memory), Motherboard, SSD/HDD.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-clock-rotate-left"></i> The Five Generations of Programming Languages</h3>
        <p>How did programming evolve from tedious electric wiring to human-readable code?</p>
        <ul>
          <li><strong>1GL (Machine Language):</strong> Pure binary (<code>01010011</code>). Only the CPU understands it directly. Painful for humans to read or write!</li>
          <li><strong>2GL (Assembly Language):</strong> Short human codes called <em>mnemonics</em> (e.g., <code>ADD</code>, <code>MOV</code>). Requires an <strong>Assembler</strong> to convert into machine code. Still tied to a specific processor model.</li>
          <li><strong>3GL (High-Level Procedural Languages):</strong> Readable, English-like code using math expressions. <strong>C, FORTRAN, Pascal, BASIC</strong> belong here. Programs can run on any computer once compiled!</li>
          <li><strong>4GL (Declarative Languages):</strong> Tell the computer <em>what</em> you want, not <em>how</em> to calculate it (e.g. <strong>SQL</strong> database queries: <code>SELECT * FROM Students</code>).</li>
          <li><strong>5GL (AI & Constraint Languages):</strong> Problem-solving through rules and neural logic (e.g. Prolog, Mercury, modern AI systems).</li>
        </ul>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-timeline"></i> The Evolution of C Standards</h3>
        <p>Over the decades, international committees created official standards so C programs run consistently everywhere:</p>
        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Standard</th><th>Year</th><th>Why It Matters to You</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>K&R C</strong></td><td>1978</td><td>The original book by Brian Kernighan & Dennis Ritchie. Set the de-facto baseline.</td></tr>
              <tr><td><strong>ANSI C (C89)</strong></td><td>1989</td><td>The first official ANSI standard. Introduced function prototypes and standard library headers (<code>stdio.h</code>).</td></tr>
              <tr><td><strong>ISO C (C90)</strong></td><td>1990</td><td>The international ISO edition of C89. <strong>C89 and C90 are identical!</strong></td></tr>
              <tr><td><strong>C99</strong></td><td>1999</td><td>Modernized C: added <code>//</code> single-line comments, <code>long long int</code>, <code>stdbool.h</code>, and <code>__func__</code>.</td></tr>
              <tr><td><strong>C11</strong></td><td>2011</td><td>Added built-in multithreading (<code>threads.h</code>) and atomic memory operations.</td></tr>
              <tr><td><strong>C17 / C18</strong></td><td>2018</td><td>Defect corrections and clarifications (the standard used in modern university courses).</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    "code": {
        "title": "The Historic First C Program",
        "desc": "The canonical 'Hello, World!' program written by Dennis Ritchie and Brian Kernighan.",
        "lang": "c",
        "snippet": """#include <stdio.h>

/* Written by Dennis Ritchie at Bell Labs (1972)
   The canonical entry point for all C software */
int main(void) {
    printf("Hello, World!\\n");
    return 0;
}""",
        "output": "Hello, World!"
    },
    "resources": [
        {"type": "gfg", "title": "Introduction to Programming Languages", "url": "https://www.geeksforgeeks.org/introduction-to-programming-languages/", "desc": "GeeksforGeeks overview of programming paradigms and abstraction levels."},
        {"type": "gfg", "title": "The Evolution of Programming Languages", "url": "https://www.geeksforgeeks.org/the-evolution-of-programming-languages/", "desc": "Chronological history from machine code to modern compiled systems."},
        {"type": "docs", "title": "ISO/IEC 9899 C Standard Working Group", "url": "https://www.open-std.org/jtc1/sc22/wg14/", "desc": "The official international committee governing the C programming language specification."}
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
})

# Module 2 - SIMPLIFIED WITH INTUITIVE ANALOGIES & DIAGRAMS
modules.append({
    "id": "m2",
    "num": 2,
    "title": "Number Systems & Architecture Mathematics",
    "subtitle": "Binary, Octal, Hexadecimal, 3-bit/4-bit Grouping, 32-bit vs 64-bit & CPU Cycles",
    "slides": "Slides 8–14, 24, 26–30",
    "time": "35 mins",
    "content": """
      <div class="teaching-block">
        <h3><i class="fa-solid fa-lightbulb"></i> The Light Switch Secret: Why Computers Use Binary</h3>
        <p>Imagine a light switch on the wall. It can only be in one of two states: <strong>OFF (0)</strong> or <strong>ON (1)</strong>. That's a <strong>Bit</strong> (binary digit)!</p>
        <p>A computer doesn't know letters, colors, or decimal numbers. Inside, it has billions of microscopic switches (transistors). By combining switches together, we can represent numbers, text, and music:</p>
        
        <div class="teacher-callout insight">
          <div class="callout-icon"><i class="fa-solid fa-calculator"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Fundamental Rule: 2ⁿ Patterns (Slide 8)</div>
            <p>Every time you add 1 bit, you <strong>double</strong> the number of things you can represent:
            <br>&bull; <strong>1 bit:</strong> 2 patterns ($2^1$) &rarr; <code>0, 1</code>
            <br>&bull; <strong>2 bits:</strong> 4 patterns ($2^2$) &rarr; <code>00, 01, 10, 11</code>
            <br>&bull; <strong>3 bits:</strong> 8 patterns ($2^3$) &rarr; <code>000, 001, 010, 011, 100, 101, 110, 111</code>
            <br>&bull; <strong>8 bits (1 Byte):</strong> 256 patterns ($2^8$) &rarr; enough for every key on your keyboard!
            <br>&bull; <strong>n bits:</strong> can represent up to <strong>2ⁿ distinct entities</strong>!
            </p>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-layer-group"></i> Visual Diagram: The Power-of-2 Weight Buckets</h3>
        <p>How does a computer convert binary into a number you understand? Think of 8 buckets, where each bucket holds a fixed power of 2:</p>

        <div class="weight-buckets">
          <div class="bucket-col">
            <span class="bucket-power">2⁷</span>
            <span class="bucket-weight">128</span>
            <div class="bucket-bit">0</div>
          </div>
          <div class="bucket-col">
            <span class="bucket-power">2⁶</span>
            <span class="bucket-weight">64</span>
            <div class="bucket-bit">0</div>
          </div>
          <div class="bucket-col">
            <span class="bucket-power">2⁵</span>
            <span class="bucket-weight">32</span>
            <div class="bucket-bit active-one">1</div>
          </div>
          <div class="bucket-col">
            <span class="bucket-power">2⁴</span>
            <span class="bucket-weight">16</span>
            <div class="bucket-bit">0</div>
          </div>
          <div class="bucket-col">
            <span class="bucket-power">2³</span>
            <span class="bucket-weight">8</span>
            <div class="bucket-bit">0</div>
          </div>
          <div class="bucket-col">
            <span class="bucket-power">2²</span>
            <span class="bucket-weight">4</span>
            <div class="bucket-bit">0</div>
          </div>
          <div class="bucket-col">
            <span class="bucket-power">2¹</span>
            <span class="bucket-weight">2</span>
            <div class="bucket-bit active-one">1</div>
          </div>
          <div class="bucket-col">
            <span class="bucket-power">2⁰</span>
            <span class="bucket-weight">1</span>
            <div class="bucket-bit active-one">1</div>
          </div>
        </div>

        <p><strong>To find the value of binary <code>00100011</code>:</strong> Just add the active buckets where bit is 1!
        <br>&rarr; $32 + 2 + 1 = \\mathbf{35}$! It's that simple!</p>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-shapes"></i> The Four Number Bases Compared</h3>
        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>System</th><th>Base (Radix)</th><th>Digits Used</th><th>Why Humans & Computers Use It</th><th>C Notation</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Binary</strong></td><td>2</td><td>0, 1</td><td>Directly matches physical on/off electric voltages.</td><td>Suffix <code>B</code> (or <code>0b</code>)</td></tr>
              <tr><td><strong>Octal</strong></td><td>8</td><td>0 to 7</td><td>Shortens binary by grouping bits into sets of <strong>3 bits</strong> ($2^3 = 8$). Used in UNIX file permissions (e.g. <code>chmod 755</code>).</td><td>Prefix <code>0</code> (e.g. <code>0527</code>)</td></tr>
              <tr><td><strong>Decimal</strong></td><td>10</td><td>0 to 9</td><td>Human standard counting system (based on our 10 fingers).</td><td>Default (e.g. <code>735</code>)</td></tr>
              <tr><td><strong>Hexadecimal</strong></td><td>16</td><td>0–9 and A–F (A=10, B=11, C=12, D=13, E=14, F=15)</td><td><strong>The Programmer's Best Friend!</strong> Groups binary into sets of <strong>4 bits (1 nibble)</strong> ($2^4 = 16$). Represents huge binary addresses compactly.</td><td>Prefix <code>0x</code> (e.g. <code>0xA3C5</code>)</td></tr>
            </tbody>
          </table>
        </div>

        <div class="teacher-callout insight">
          <div class="callout-icon"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
          <div class="callout-body">
            <div class="callout-title">The 4-Bit Hex Secret (Slides 10–11)</div>
            <p>Reading <code>1010001111000101</code> makes your eyes hurt. But notice how clean it becomes when split into 4-bit nibbles:
            <br>&emsp;<code>1010</code> = <strong>A</strong> (10)
            <br>&emsp;<code>0011</code> = <strong>3</strong>
            <br>&emsp;<code>1100</code> = <strong>C</strong> (12)
            <br>&emsp;<code>0101</code> = <strong>5</strong>
            <br>&rarr; Together: <strong>0xA3C5</strong>! Hexadecimal is not a separate math; it is just friendly shorthand nicknames for 4-bit binary chunks!</p>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-pen-ruler"></i> Visual Step-by-Step Radix Conversions (Slide 14)</h3>
        <p>Let's look at the exact handwritten examples from Slide 14 broken down into clear visual steps:</p>

        <div class="conversion-ladder">
          <div class="ladder-col">
            <h5><i class="fa-solid fa-arrow-down-9-1"></i> Example 1: Convert (108.78)₁₀ to Octal</h5>
            <p style="font-size: 0.8rem; color: var(--text-muted);"><strong>Integer Part (108):</strong> Successive division by 8, reading remainders from bottom to top:</p>
            <div class="ladder-step"><span class="calc">108 &divide; 8 = 13</span><span class="rem">Remainder 4 &uarr; (LSD)</span></div>
            <div class="ladder-step"><span class="calc">13 &divide; 8 = 1</span><span class="rem">Remainder 5 &uarr;</span></div>
            <div class="ladder-step"><span class="calc">1 &divide; 8 = 0</span><span class="rem">Remainder 1 &uarr; (MSD)</span></div>
            <p style="font-size: 0.82rem; margin-top: 0.4rem;">&rarr; Integer part = <strong>154₈</strong></p>

            <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.75rem;"><strong>Fractional Part (0.78):</strong> Successive multiplication by 8, taking the integer part from top to bottom:</p>
            <div class="ladder-step"><span class="calc">0.78 &times; 8 = 6.24</span><span class="rem">Take 6 &darr;</span></div>
            <div class="ladder-step"><span class="calc">0.24 &times; 8 = 1.92</span><span class="rem">Take 1 &darr;</span></div>
            <div class="ladder-step"><span class="calc">0.92 &times; 8 = 7.36</span><span class="rem">Take 7 &darr;</span></div>
            <div class="ladder-step"><span class="calc">0.36 &times; 8 = 2.88</span><span class="rem">Take 2 &darr;</span></div>
            <p style="font-size: 0.82rem; margin-top: 0.4rem;">&rarr; Fractional part = <strong>.6172...₈</strong></p>
            <p style="font-size: 0.88rem; font-weight: 700; color: var(--accent-emerald); margin-top: 0.5rem;">Result: (108.78)₁₀ &approx; (154.6172)₈</p>
          </div>

          <div class="ladder-col">
            <h5><i class="fa-solid fa-arrow-right-arrow-left"></i> Example 2 & 3: Hex & Binary to Octal</h5>
            <p style="font-size: 0.8rem; color: var(--text-muted);"><strong>Example 2: Convert (FE.4A)₁₆ to Decimal:</strong></p>
            <div class="ladder-step"><span class="calc">F &times; 16¹ = 15 &times; 16</span><span class="rem">240</span></div>
            <div class="ladder-step"><span class="calc">E &times; 16⁰ = 14 &times; 1</span><span class="rem">14</span></div>
            <div class="ladder-step"><span class="calc">4 &times; 16⁻¹ = 4 / 16</span><span class="rem">0.25</span></div>
            <div class="ladder-step"><span class="calc">A &times; 16⁻² = 10 / 256</span><span class="rem">0.0390625</span></div>
            <p style="font-size: 0.88rem; font-weight: 700; color: var(--accent-emerald); margin-top: 0.5rem;">Total = 240 + 14 + 0.25 + 0.039 = 254.289₁₀</p>

            <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 1rem;"><strong>Example 3: Convert (101010111)₂ to Octal:</strong></p>
            <p style="font-size: 0.85rem;">Group binary digits by 3 bits from right:</p>
            <div class="ladder-step"><span class="calc">101 | 010 | 111</span><span class="rem">5 | 2 | 7</span></div>
            <p style="font-size: 0.88rem; font-weight: 700; color: var(--accent-emerald); margin-top: 0.5rem;">Result: (527)₈</p>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-microchip"></i> 32-bit vs. 64-bit Processors: Why the 4 GB Limit? (Slides 26–29)</h3>
        <p>A CPU register is like a notepad where the processor scribbles memory addresses. The bit-width tells us how big of an address the processor can write:</p>
        <ul>
          <li><strong>32-bit Processor:</strong> Can write up to $2^{32}$ distinct addresses. Since each address points to 1 byte, $2^{32}\\text{ bytes} = \\mathbf{4\\text{ GB}}$! Even if you physically plug 16 GB of RAM into a 32-bit machine, the CPU physically cannot address beyond ~3.5 to 4 GB.</li>
          <li><strong>64-bit Processor:</strong> Can write up to $2^{64}$ addresses = <strong>18 Quintillion bytes (16 Exabytes)</strong>! It can effortlessly handle 8 GB, 32 GB, 128 GB, or Terabytes of RAM.</li>
        </ul>

        <div class="teacher-callout exam-alert">
          <div class="callout-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Teacher's Takeaway</div>
            <p>If your computer has 8 GB of RAM or more, it <em>must</em> have a 64-bit processor and a 64-bit operating system to use that memory (Slide 28).</p>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-arrows-spin"></i> The 4-Step CPU Heartbeat (Slide 30)</h3>
        <p>Every single millisecond, your CPU loops through four fundamental steps to execute instructions:</p>
        <ol>
          <li><strong>1. Fetch:</strong> Grabs the next instruction from RAM into the CPU.</li>
          <li><strong>2. Decode:</strong> Figures out what the instruction means (e.g. "Add two numbers" or "Move data").</li>
          <li><strong>3. Execute:</strong> The ALU (Arithmetic Logic Unit) actually computes the math or logic.</li>
          <li><strong>4. Write Back:</strong> Saves the result into a register or RAM so you can see it.</li>
        </ol>
      </div>
    """,
    "code": {
        "title": "Inspecting Binary and Bit-Width in C",
        "desc": "Demonstrating how numbers are stored and how bitwise operations inspect architecture representation.",
        "lang": "c",
        "snippet": """#include <stdio.h>
#include <stdint.h>

void print_binary(uint32_t num) {
    for (int i = 31; i >= 0; i--) {
        printf("%d", (num >> i) & 1);
        if (i % 4 == 0 && i != 0) printf(" ");
    }
    printf("\\n");
}

int main(void) {
    uint32_t val = 0xA3C5; // Hexadecimal literal
    printf("Hex: 0x%X | Decimal: %u\\nBinary: ", val, val);
    print_binary(val); // 0000 0000 0000 0000 1010 0011 1100 0101

    printf("Word size of pointer on this system: %zu bytes (%zu bits)\\n", 
           sizeof(void*), sizeof(void*) * 8);
    return 0;
}""",
        "output": "Hex: 0xA3C5 | Decimal: 41925\nBinary: 0000 0000 0000 0000 1010 0011 1100 0101\nWord size of pointer on this system: 8 bytes (64 bits)"
    },
    "resources": [
        {"type": "tool", "title": "Float.exposed — IEEE 754 Floating Point Visualizer", "url": "https://float.exposed", "desc": "Interactive tool showing sign, exponent, and mantissa bit breakdown."},
        {"type": "gfg", "title": "Number Systems and Base Conversions", "url": "https://www.geeksforgeeks.org/number-system-in-digital-electronics/", "desc": "Detailed guide on binary, octal, decimal, and hexadecimal arithmetic."},
        {"type": "docs", "title": "Bit Twiddling Hacks by Sean Eron Anderson", "url": "https://graphics.stanford.edu/~seander/bithacks.html", "desc": "Stanford University collection of bit-manipulation algorithms."}
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
})

# Module 3
modules.append({
    "id": "m3",
    "num": 3,
    "title": "Hardware, Storage & Memory Hierarchy",
    "subtitle": "Primary vs Secondary Memory, RAM vs ROM, SRAM vs DRAM, Memory Pyramid",
    "slides": "Slides 15–23",
    "time": "30 mins",
    "content": """
      <div class="teaching-block">
        <h3><i class="fa-solid fa-layer-group"></i> The Memory Pyramid: Speed vs. Cost vs. Size (Slide 21)</h3>
        <p>Why can't our computers just have 1 Terabyte of super-fast CPU registers? Because ultra-fast memory is expensive and physically difficult to pack together. Computer architects solved this by organizing memory as a <strong>Pyramid</strong>:</p>

        <div class="teacher-callout insight">
          <div class="callout-icon"><i class="fa-solid fa-mountain"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Law of the Memory Pyramid</div>
            <p><strong>Going UP the pyramid:</strong> Speed increases dramatically (nanoseconds!) and cost increases, but capacity shrinks.
            <br><strong>Going DOWN the pyramid:</strong> Storage expands to massive Terabytes and Petabytes, but access becomes much slower.</p>
          </div>
        </div>

        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Level</th><th>Memory Type</th><th>Technology</th><th>Speed Analogy</th><th>Primary Purpose</th></tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Level 0</strong></td>
                <td>CPU Registers</td>
                <td>Direct silicon latches in CPU</td>
                <td>Like information already in your active thinking memory (&lt; 1 ns).</td>
                <td>Holds numbers currently being calculated right this millisecond.</td>
              </tr>
              <tr>
                <td><strong>Level 1</strong></td>
                <td>Cache Memory (L1, L2, L3)</td>
                <td>Static RAM (SRAM)</td>
                <td>Like a notepad open right in front of you (1–10 ns).</td>
                <td>Stores recently used instructions so the CPU doesn't wait on slow RAM.</td>
              </tr>
              <tr>
                <td><strong>Level 2</strong></td>
                <td>Main / Primary Memory</td>
                <td>Dynamic RAM (DRAM)</td>
                <td>Like walking to your desk drawer (50–100 ns).</td>
                <td>Holds your active programs, open browser tabs, and game data.</td>
              </tr>
              <tr>
                <td><strong>Level 3</strong></td>
                <td>Secondary / Mass Storage</td>
                <td>Solid State Drive (SSD) / Hard Disk (HDD)</td>
                <td>Like walking to a warehouse across town (milliseconds).</td>
                <td>Stores saved files, installed apps, and Windows/Linux permanently.</td>
              </tr>
              <tr>
                <td><strong>Level 4</strong></td>
                <td>Offline / Archival Storage</td>
                <td>Magnetic Tape, Optical Disks</td>
                <td>Like ordering from an archive in another country.</td>
                <td>Long-term historical company backups.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-code-compare"></i> Primary Memory vs. Secondary Storage (Slide 23)</h3>
        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Feature</th><th>Primary Memory (RAM)</th><th>Secondary Storage (SSD / Hard Drive)</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Permanence</strong></td><td><strong>Temporary:</strong> Wiped clean the instant power is turned off.</td><td><strong>Permanent:</strong> Preserves data for years without electrical power.</td></tr>
              <tr><td><strong>CPU Access</strong></td><td><strong>Direct:</strong> Connected directly to the CPU memory bus.</td><td><strong>Indirect:</strong> Must be copied into RAM before the CPU can read it.</td></tr>
              <tr><td><strong>Volatility</strong></td><td>Volatile (RAM)</td><td>Non-Volatile (SSD, Hard Disk, Flash drive)</td></tr>
              <tr><td><strong>Speed</strong></td><td>Super-fast electronic semiconductor memory.</td><td>Slower mechanical or flash access.</td></tr>
              <tr><td><strong>Cost per GB</strong></td><td>High cost per gigabyte.</td><td>Very cheap cost per gigabyte.</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-microchip"></i> RAM vs. ROM: What's the Difference? (Slide 19)</h3>
        <ul>
          <li><strong>RAM (Random Access Memory):</strong> Read and Write. Fast, volatile, large (4 GB to 32 GB+). Stores apps you are actively running right now.
            <br>&bull; <em>DRAM (Dynamic):</em> Uses tiny capacitors; must be refreshed with electricity thousands of times a second. Cheap, used for main system RAM.
            <br>&bull; <em>SRAM (Static):</em> Uses flip-flops; doesn't need refreshing. Blazing fast, expensive, used for CPU cache!</li>
          <li><strong>ROM (Read-Only Memory):</strong> Read-only during normal operation. Non-volatile, small (4 MB to 8 MB). Contains the firmware instructions (BIOS/UEFI) that wake the computer up when you press the power button!</li>
        </ul>
      </div>
    """,
    "code": {
        "title": "Simulating Volatile Memory Allocation",
        "desc": "How C programs interact with primary memory and allocate memory dynamically.",
        "lang": "c",
        "snippet": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    // Variable in Primary Memory (RAM)
    int stack_num = 100;
    
    // Dynamic allocation in RAM (Heap)
    int *dynamic_array = (int*)malloc(5 * sizeof(int));
    if (dynamic_array == NULL) {
        printf("Out of primary memory!\\n");
        return 1;
    }

    for (int i = 0; i < 5; i++) {
        dynamic_array[i] = (i + 1) * 10;
    }

    printf("Stack variable address: %p | Value: %d\\n", (void*)&stack_num, stack_num);
    printf("Heap allocated address: %p | First Value: %d\\n", (void*)dynamic_array, dynamic_array[0]);

    free(dynamic_array); // Always return memory to primary storage!
    return 0;
}""",
        "output": "Stack variable address: 0x7ffd98... | Value: 100\nHeap allocated address: 0x55d7a2... | First Value: 10"
    },
    "resources": [
        {"type": "gfg", "title": "Memory Hierarchy in Computer Architecture", "url": "https://www.geeksforgeeks.org/memory-hierarchy-in-computer-architecture/", "desc": "In-depth guide covering Registers, Cache, Main Memory, and Disk."},
        {"type": "gfg", "title": "Differences Between RAM and ROM", "url": "https://www.geeksforgeeks.org/difference-between-ram-and-rom/", "desc": "Technical breakdown of semiconductor volatile vs non-volatile storage."},
        {"type": "docs", "title": "What Every Programmer Should Know About Memory (Ulrich Drepper)", "url": "https://people.freebsd.org/~lstewart/articles/cpumemory.pdf", "desc": "Seminal MIT/RedHat reference on modern memory systems and CPU caches."}
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
})

with open("modules_1_3.json", "w", encoding="utf-8") as f:
    json.dump(modules, f, indent=2)
print("Updated modules_1_3.json with simplified binary explanations and weight bucket diagrams!")
