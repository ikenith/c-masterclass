import json

with open("modules_1_3.json", "r", encoding="utf-8") as f:
    m1_3 = json.load(f)
with open("modules_4_6.json", "r", encoding="utf-8") as f:
    m4_6 = json.load(f)
with open("modules_7_9.json", "r", encoding="utf-8") as f:
    m7_9 = json.load(f)
with open("modules_10_11.json", "r", encoding="utf-8") as f:
    m10_11 = json.load(f)

all_modules = m1_3 + m4_6 + m7_9 + m10_11
print(f"Total modules merged: {len(all_modules)}")

capstone_exam = [
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
]

# Write js file using template replacement
js_template = r"""/**
 * C Programming Masterclass: Unit 1 — Application Engine
 * Curated from Unit 1: Overview of Computer Organization & Programming Fundamentals
 * Author: Prof. Uday Kumar M Courseware
 */

// Global Course Curriculum Dataset
const COURSE_MODULES = __MODULES_DATA__;
const CAPSTONE_EXAM = __EXAM_DATA__;

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

    if (window.updateBitwiseLiveCalc) {
      setTimeout(() => window.updateBitwiseLiveCalc(), 50);
    }
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

// Bitwise Interactive Visualizer
window.setBitwisePreset = function(a, b) {
  const inpA = document.getElementById('bw-op-a');
  const inpB = document.getElementById('bw-op-b');
  if (inpA && inpB) {
    inpA.value = a;
    inpB.value = b;
    window.updateBitwiseLiveCalc();
  }
};

window.updateBitwiseLiveCalc = function() {
  const container = document.getElementById('bw-live-results');
  if (!container) return;
  const aRaw = parseInt(document.getElementById('bw-op-a')?.value || '0', 10);
  const bRaw = parseInt(document.getElementById('bw-op-b')?.value || '0', 10);
  const aVal = isNaN(aRaw) ? 0 : Math.max(0, Math.min(255, aRaw));
  const bVal = isNaN(bRaw) ? 0 : Math.max(0, Math.min(255, bRaw));

  const toBin = (n, bits = 8) => {
    let s = (n >>> 0).toString(2);
    while (s.length < bits) s = '0' + s;
    return s.slice(-bits);
  };

  const andRes = aVal & bVal;
  const orRes = aVal | bVal;
  const xorRes = aVal ^ bVal;
  const notARes = (~aVal);
  const shlRes = (aVal << 1) & 0x1FF;
  const shrRes = aVal >> 1;

  container.innerHTML = `
    <div class="bw-res-box">
      <div class="bw-res-header">
        <span>Bitwise AND (&)</span>
        <span class="bitwise-sym-pill and" style="width:24px;height:24px;font-size:0.75rem;">&amp;</span>
      </div>
      <div class="bw-res-bin">${toBin(andRes)}</div>
      <div class="bw-res-dec">Decimal: ${andRes}</div>
      <div style="font-size:0.75rem;color:var(--text-muted);">${aVal} &amp; ${bVal} = ${andRes}</div>
    </div>

    <div class="bw-res-box">
      <div class="bw-res-header">
        <span>Bitwise OR (|)</span>
        <span class="bitwise-sym-pill or" style="width:24px;height:24px;font-size:0.75rem;">|</span>
      </div>
      <div class="bw-res-bin">${toBin(orRes)}</div>
      <div class="bw-res-dec">Decimal: ${orRes}</div>
      <div style="font-size:0.75rem;color:var(--text-muted);">${aVal} | ${bVal} = ${orRes}</div>
    </div>

    <div class="bw-res-box">
      <div class="bw-res-header">
        <span>Bitwise XOR (^)</span>
        <span class="bitwise-sym-pill xor" style="width:24px;height:24px;font-size:0.75rem;">^</span>
      </div>
      <div class="bw-res-bin">${toBin(xorRes)}</div>
      <div class="bw-res-dec">Decimal: ${xorRes}</div>
      <div style="font-size:0.75rem;color:var(--text-muted);">${aVal} ^ ${bVal} = ${xorRes}</div>
    </div>

    <div class="bw-res-box">
      <div class="bw-res-header">
        <span>Bitwise NOT (~A)</span>
        <span class="bitwise-sym-pill not" style="width:24px;height:24px;font-size:0.75rem;">~</span>
      </div>
      <div class="bw-res-bin">${toBin(notARes & 0xFF)}</div>
      <div class="bw-res-dec">Signed: ${notARes}</div>
      <div style="font-size:0.75rem;color:var(--text-muted);">Formula: -(${aVal} + 1) = ${notARes}</div>
    </div>

    <div class="bw-res-box">
      <div class="bw-res-header">
        <span>Left Shift (A &lt;&lt; 1)</span>
        <span class="bitwise-sym-pill shift" style="width:24px;height:24px;font-size:0.75rem;">&lt;&lt;</span>
      </div>
      <div class="bw-res-bin">${toBin(shlRes, 9)}</div>
      <div class="bw-res-dec">Decimal: ${shlRes}</div>
      <div style="font-size:0.75rem;color:var(--text-muted);">${aVal} &times; 2 = ${shlRes}</div>
    </div>

    <div class="bw-res-box">
      <div class="bw-res-header">
        <span>Right Shift (A &gt;&gt; 1)</span>
        <span class="bitwise-sym-pill shift" style="width:24px;height:24px;font-size:0.75rem;">&gt;&gt;</span>
      </div>
      <div class="bw-res-bin">${toBin(shrRes)}</div>
      <div class="bw-res-dec">Decimal: ${shrRes}</div>
      <div style="font-size:0.75rem;color:var(--text-muted);">${aVal} / 2 = ${shrRes}</div>
    </div>
  `;
};

// Boot Engine on DOM Ready
let engine;
document.addEventListener('DOMContentLoaded', () => {
  engine = new CourseEngine();
});
"""

full_js = js_template.replace("__MODULES_DATA__", json.dumps(all_modules, indent=2))
full_js = full_js.replace("__EXAM_DATA__", json.dumps(capstone_exam, indent=2))

with open("app.js", "w", encoding="utf-8") as f:
    f.write(full_js)

print("app.js successfully created via template substitution!")
