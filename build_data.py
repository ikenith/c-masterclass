import json
import sys

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
        <h3><i class="fa-solid fa-chalkboard-user"></i> Professor's Welcome & Mental Model</h3>
        <p>Welcome to Unit 1 of our Computer Science journey! Before you write a single line of C, you must understand a profound truth: <strong>a computer is not an isolated calculator, but an integrated system</strong>. Everything we do in C—manipulating pointers, passing arguments, allocating memory—directly mirrors the physical architecture of the machine.</p>
        
        <div class="teacher-callout insight">
          <div class="callout-icon"><i class="fa-solid fa-lightbulb"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Master Philosophy of C</div>
            <p>Dennis Ritchie designed C in 1972 at Bell Labs to build the <strong>UNIX operating system</strong>. Most languages wrap you in safety blankets; C gives you the keys to the machine. You get direct access to CPU memory addresses via pointers, bit-level manipulation, and raw hardware speed. That is why Windows, Linux, macOS, iOS, Android kernels, and device drivers remain powered by C.</p>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-sitemap"></i> Computer System Architecture & Layers</h3>
        <p>A computer system takes raw data as <strong>Input</strong> (keyboard, mouse, joystick, scanner), processes it through the <strong>Processing Unit (ALU + Control Unit + Memory)</strong>, delivers results via <strong>Output Units</strong> (monitors, printers, plotters, speakers), and stores it for future retrieval in <strong>Secondary Storage</strong>.</p>
        
        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Layer</th><th>Role & Description</th><th>Concrete Real-World Examples</th></tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>User</strong></td>
                <td>A human being or external network service utilizing computing capabilities.</td>
                <td>Student, software engineer, data analyst.</td>
              </tr>
              <tr>
                <td><strong>Application Software</strong></td>
                <td>Programs designed to perform user-facing tasks and workflows.</td>
                <td>Web browsers, WhatsApp, media players, IDEs.</td>
              </tr>
              <tr>
                <td><strong>Operating System (OS)</strong></td>
                <td>System software acting as the intermediary bridge between applications and hardware.</td>
                <td>Linux, Windows, macOS, UNIX, iOS.</td>
              </tr>
              <tr>
                <td><strong>Hardware</strong></td>
                <td>The physical digital electronic components executing instructions and storing bits.</td>
                <td>CPU (ALU, CU, Registers), Motherboard, RAM, SSD/HDD.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-clock-rotate-left"></i> The Five Generations of Programming Languages</h3>
        <p>To appreciate why C was such a monumental revolution, let's trace how programming evolved:</p>
        <ul>
          <li><strong>1GL (First Generation - Machine Language):</strong> Raw binary sequences (0s and 1s) executed directly by CPU logic circuits. Extremely fast, but excruciatingly error-prone and non-portable.</li>
          <li><strong>2GL (Second Generation - Assembly Language):</strong> Replaced binary opcodes with human-readable mnemonics (e.g., <code>MOV</code>, <code>ADD</code>, <code>JMP</code>). Required an <em>Assembler</em> to produce machine code. Still tied to specific CPU architectures.</li>
          <li><strong>3GL (Third Generation - High-Level Languages):</strong> Human-friendly syntax resembling algebra and English sentences. Introduces compilers and interpreters. <strong>C, FORTRAN, Pascal, COBOL, BASIC</strong> belong here. Programs written in 3GL can be compiled across diverse CPU architectures.</li>
          <li><strong>4GL (Fourth Generation - Declarative Languages):</strong> Focuses on <em>what</em> result is wanted rather than <em>how</em> to compute it. Examples include <strong>SQL</strong> and report generation tools.</li>
          <li><strong>5GL (Fifth Generation - Constraint & AI Languages):</strong> Programs based on constraints, declarative logic, and neural networks (e.g., Prolog, Mercury).</li>
        </ul>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-timeline"></i> The Evolution of C Standards</h3>
        <p>C has evolved through rigorous international standards to ensure cross-platform compatibility:</p>
        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Standard</th><th>Year</th><th>Key Significance & Additions</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>K&R C</strong></td><td>1978</td><td>Brian Kernighan & Dennis Ritchie published "The C Programming Language" (1st ed.), serving as the original de-facto specification.</td></tr>
              <tr><td><strong>ANSI C (C89)</strong></td><td>1989</td><td>Standardized as ANSI X3.159-1989. Introduced function prototypes, <code>void*</code>, standard library headers, and standardized keyword definitions.</td></tr>
              <tr><td><strong>ISO C (C90)</strong></td><td>1990</td><td>Identical standard adopted globally by ISO as ISO/IEC 9899:1990. Terms "C89" and "C90" refer to the exact same language.</td></tr>
              <tr><td><strong>C99</strong></td><td>1999</td><td>ISO/IEC 9899:1999: Added <code>//</code> comments, inline functions, variable-length arrays (VLAs), <code>long long int</code>, <code>stdbool.h</code>, and <code>__func__</code>.</td></tr>
              <tr><td><strong>C11</strong></td><td>2011</td><td>ISO/IEC 9899:2011: Added standardized multithreading (<code>threads.h</code>), atomic operations (<code>stdatomic.h</code>), and anonymous structs.</td></tr>
              <tr><td><strong>C17 / C18</strong></td><td>2018</td><td>ISO/IEC 9899:2018: Technical bug fixes and defect clarifications without adding major new syntax.</td></tr>
            </tbody>
          </table>
        </div>

        <div class="teacher-callout exam-alert">
          <div class="callout-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
          <div class="callout-body">
            <div class="callout-title">Exam & Interview Alert!</div>
            <p>University exams frequently ask: <em>"Are C89 and C90 different?"</em> Answer: <strong>No!</strong> C89 was published by ANSI in 1989, and ISO adopted it in 1990 with only formatting/editorial changes under ISO/IEC 9899:1990. They specify the identical programming language.</p>
          </div>
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
        {"type": "gfg", "title": "Generations of Programming Languages", "url": "https://www.geeksforgeeks.org/generation-programming-languages/", "desc": "1GL to 5GL comparative characteristics and features."},
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
            "explanation": "In 1989, ANSI established the standard X3.159-1989 (C89). In 1990, ISO adopted it as ISO/IEC 9899:1990 (C90). Hence, C89 and C90 denote the exact same language standard."
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

print("Module 1 ready.")
