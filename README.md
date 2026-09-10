# 🎓 C Programming Masterclass: Units 1 & 2 Interactive Platform

An interactive, responsive single-page web application designed from a pedagogical standpoint to teach the complete university curriculum of **Units 1 & 2: Overview of Computer Organization and C Programming Fundamentals** (based on the 162-slide courseware by Prof. Uday Kumar M).

Designed with a **minimalist, distraction-free monochrome aesthetic**, featuring high-contrast academic typography, semantic color cues, and responsive mobile-first architecture.

---

## 🌟 Live Demo & Deployment

Deployable instantly to **GitHub Pages** with zero backend dependencies!

- **Live URL:** `https://<username>.github.io/<repository-name>/`
- **Pure Client-Side:** Vanilla HTML5, CSS3, ES6+ JavaScript, FontAwesome 6, Google Fonts (`Outfit`, `Inter`, `Fira Code`).

---

## 🚀 Quick Start (Local Development)

To run locally on any machine:

```bash
# Clone the repository
git clone git@github.com:ikenith/c-masterclass.git
cd c-masterclass

# Launch any static HTTP server (e.g. Python)
python3 -m http.server 8000

# Open in your browser
# http://localhost:8000
```

---

## 📚 Complete Curriculum Overview (Units 1 & 2)

The curriculum spans **11 interactive milestones** across 162 university slides:

### Unit 1: Introduction to Computing (Slides 1–45)
1. **Milestone 1: Genesis of Computing, Architecture & C** (Slides 1–7, 15, 25)
   - 4-layer computing stack (User, App, OS, Hardware), 5 language generations (1GL to 5GL), Dennis Ritchie & UNIX history, C standards evolution (K&R, C89, C99, C11, C17).
2. **Milestone 2: Number Systems & Architecture Math** (Slides 8–14, 24, 26–30)
   - Radix conversion algorithms (Decimal, Binary, Octal, Hexadecimal), grouping rules, Two's Complement arithmetic, CPU register word widths (32-bit vs 64-bit address space).
3. **Milestone 3: Hardware, Storage & Memory Hierarchy** (Slides 15–23)
   - Primary vs Secondary storage, SRAM vs DRAM, Memory Pyramid (Registers, Cache, RAM, Magnetic/Solid State Storage).
4. **Milestone 4: Problem Solving: Flowcharts & Pseudocode** (Slides 31–45)
   - Donald Knuth's 5 algorithmic criteria, ISO flowchart symbols (Oval, Rectangle, Parallelogram, Diamond, Connector), pseudocode conventions.

### Unit 2: C Programming Fundamentals (Slides 46–162)
5. **Milestone 5: C Program Structure & GCC Compilation Pipeline** (Slides 46–61)
   - Canonical `main()` structure, the 4 compilation phases (`gcc -E` Preprocessing, `gcc -S` Compilation via `cc1`, `gcc -c` Assembly via `as`, `gcc` Linking via `ld`).
6. **Milestone 6: Process Memory Layout in C** (Slides 62–69)
   - Text/Code (read-only), Initialized Data (`.data`), Uninitialized Data (`.bss`), Heap (dynamic expansion upward), Stack (stack frames expanding downward).
7. **Milestone 7: C Lexical Tokens: Keywords, Identifiers & Data Types** (Slides 70–80)
   - 32 ANSI C reserved keywords, identifier naming rules, primitive data types (`char`, `int`, `float`, `double`), standard type sizes and byte ranges.
8. **Milestone 8: Variables, Constants & Escape Sequences** (Slides 81–106)
   - Variable declarations, octal (`0...`) and hex (`0x...`) integer literals, ASCII escape sequences (`\n`, `\t`, `\a`, `\b`, `\0`), formatted I/O (`printf`/`scanf` specifiers).
9. **Milestone 9: C Operators & Expressions Deep Dive** (Slides 107–133)
   - Arithmetic, Relational chaining quirks (`1 > 2 < 3 = 1`), Logical short-circuiting (`&&`, `||`), Bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`), assignment, conditional ternary, `sizeof`, comma operator, full precedence & associativity hierarchy (NO BODMAS in C!).
10. **Milestone 10: Decision Control: If-Else & Switch-Case Mastery** (Slides 134–146)
    - Two-way selection (`if`, `if-else`), nested branches, multi-way `switch` statement mechanics, fallthrough quirks, break requirement, unreachable statement traps.
11. **Milestone 11: Iteration: Loops & Advanced I/O Quirks** (Slides 147–162)
    - Entry-controlled (`while`, `for`) vs Exit-controlled (`do-while`) loops, `break` and `continue` semantics, `printf` character return values, scansets (`%[^\n]s`).

---

## 🛠️ Interactive Features & Diagnostic Tools

### 1. Curriculum Roadmap & Progress Stepper
- 11-node horizontal timeline with completed emerald bullets, active highlighted focus, and automated progress bar calculation.
- Zero bleed-through opaque nodes with smooth scrolling.
- Keyboard navigation (`ArrowLeft` / `ArrowRight`).

### 2. Interactive Tools Lab (`#tools`)
- **Radix & Bitwise Converter:** Real-time bidirectional conversion between Decimal, Binary, Hexadecimal, and Octal with 32-bit cell visualizer, bit shift multipliers, and Two's Complement diagnostics.
- **Process Memory Inspector:** Interactive high/low memory diagram illustrating Text, Data, BSS, Heap, and Stack segments with live technical descriptions.
- **Precedence Evaluator:** Visual interactive walkthrough of tricky C expressions without parentheses.
- **GCC Code Sandbox:** 8 verified C programs with integrated GCC simulation and terminal output.

### 3. Practice Quizzes & Capstone Mastery Exam (`#exam`)
- **42 In-Lesson MCQs:** Instant feedback with thorough explanations for every option.
- **30-Question Final Exam:** Comprehensive assessment spanning Units 1 & 2.
- **Dynamic Grading & Certification:** Score $\ge 80\%$ (24/30) to unlock the official printable/PDF Course Completion Certificate.

---

## 🗂️ Project Structure

```text
├── index.html              # Main application shell & UI layouts
├── style.css               # Minimalist high-contrast stylesheet (dark/light themes)
├── app.js                  # Complete application engine, modules dataset & quiz logic
├── assemble_app.py         # Python builder for modular curriculum compilation
├── modules_1_3.json        # Curated content for Modules 1–3
├── modules_4_6.json        # Curated content for Modules 4–6
├── modules_7_9.json        # Curated content for Modules 7–9
├── modules_10_11.json      # Curated content for Modules 10–11
├── test_verification.py    # Automated test suite (GCC syntax & dataset validation)
├── .gitignore              # Git ignore configuration
└── README.md               # Project documentation
```

---

## 📜 Academic Attribution

- **Curriculum:** Unit 1 & Unit 2 Courseware (Slides 1–162)
- **Instructor:** Prof. Uday Kumar M, Department of Computer Science
- **Platform Architecture:** Antigravity AI Engineering
