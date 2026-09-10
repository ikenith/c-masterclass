import json

modules = []

# Module 7
modules.append({
    "id": "m7",
    "num": 7,
    "title": "C Lexical Tokens: Keywords, Identifiers & Data Types",
    "subtitle": "The Building Blocks: 32 Keywords, Naming Rules, __func__, and Memory Containers",
    "slides": "Slides 70–80",
    "time": "35 mins",
    "content": r"""
      <div class="teaching-block">
        <h3><i class="fa-solid fa-graduation-cap"></i> Teacher's Intro: The Vocabulary of C</h3>
        <p class="lead-text">
          Just like human languages have words, punctuation, and grammar rules, a C program is constructed from tiny atomic units called <strong>Lexical Tokens</strong>.
          Every single word or symbol you type into a <code>.c</code> source file belongs to one of these five categories:
          <strong>Keywords</strong>, <strong>Identifiers</strong>, <strong>Constants</strong>, <strong>Operators</strong>, or <strong>Special Symbols</strong>.
        </p>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-key"></i> The 32 Reserved Keywords of ANSI C (Slide 70)</h3>
        <p><strong>Keywords</strong> are words that have a fixed, permanent meaning to the C compiler. You cannot change their meaning, and you cannot use them as variable or function names.</p>
        
        <div class="teacher-callout analogy">
          <div class="callout-icon"><i class="fa-solid fa-traffic-light"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Highway Traffic Sign Analogy</div>
            <p>Keywords are like official traffic signs: <code>STOP</code>, <code>SPEED LIMIT</code>, <code>ONE WAY</code>. You cannot rename your pet dog "STOP" on the road without causing chaos! Similarly, C reserves exactly <strong>32 keywords</strong>. Because C is strictly case-sensitive, all 32 keywords are written in <strong>lowercase</strong>.</p>
          </div>
        </div>

        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Classification</th><th>Keywords</th><th>Purpose</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Data Types</strong></td><td><code>char</code>, <code>int</code>, <code>float</code>, <code>double</code>, <code>short</code>, <code>long</code>, <code>signed</code>, <code>unsigned</code>, <code>void</code></td><td>Specifies the type and size of memory containers.</td></tr>
              <tr><td><strong>User-Defined Types</strong></td><td><code>struct</code>, <code>union</code>, <code>enum</code>, <code>typedef</code></td><td>Creates custom composite data structures.</td></tr>
              <tr><td><strong>Storage Classes</strong></td><td><code>auto</code>, <code>register</code>, <code>static</code>, <code>extern</code></td><td>Controls lifetime, scope, and storage placement.</td></tr>
              <tr><td><strong>Decision Making</strong></td><td><code>if</code>, <code>else</code>, <code>switch</code>, <code>case</code>, <code>default</code></td><td>Branches execution path based on conditions.</td></tr>
              <tr><td><strong>Loops & Jumps</strong></td><td><code>for</code>, <code>do</code>, <code>while</code>, <code>break</code>, <code>continue</code>, <code>goto</code>, <code>return</code></td><td>Repeats code blocks or alters execution order.</td></tr>
              <tr><td><strong>Type Qualifiers & Operators</strong></td><td><code>const</code>, <code>volatile</code>, <code>sizeof</code></td><td>Protects data, handles hardware I/O, weighs byte size.</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-signature"></i> Identifiers & The 5 Naming Rules (Slides 71–72)</h3>
        <p><strong>Identifiers</strong> are the custom names <em>you</em> create for your variables, functions, and arrays. To prevent syntax errors, you must follow 5 golden rules:</p>
        
        <div class="comparison-card">
          <div class="comparison-header">
            <span><i class="fa-solid fa-list-check"></i> 5 Rules for Naming C Identifiers</span>
            <span class="badge">Strictly Enforced</span>
          </div>
          <div class="comparison-grid">
            <div class="comparison-col">
              <h4>Rule</h4>
              <p><strong>1. Allowed Characters:</strong> Only letters (<code>a-z</code>, <code>A-Z</code>), digits (<code>0-9</code>), and the underscore (<code>_</code>).</p>
              <p><strong>2. First Character:</strong> Must be a letter or underscore. <em>Never a digit!</em></p>
              <p><strong>3. Case Sensitive:</strong> Uppercase and lowercase are completely distinct.</p>
              <p><strong>4. No Keywords:</strong> Cannot use any of the 32 reserved words.</p>
              <p><strong>5. No Special Symbols or Spaces:</strong> No hyphens, spaces, commas, or dollar signs.</p>
            </div>
            <div class="comparison-col">
              <h4>Valid Examples &#10004;</h4>
              <p><code>total_sum</code>, <code>count1</code>, <code>_index</code></p>
              <p><code>student_age</code>, <code>_temp</code>, <code>MAX_VAL</code></p>
              <p><code>age</code>, <code>Age</code>, and <code>AGE</code> are 3 different variables!</p>
              <p><code>int_count</code>, <code>my_float</code>, <code>return_val</code></p>
              <p><code>first_name</code>, <code>score_2026</code></p>
            </div>
            <div class="comparison-col">
              <h4>Invalid Traps &#10008; (Syntax Error!)</h4>
              <p><code>total-sum</code> (hyphen is minus operator!), <code>total sum</code> (space!)</p>
              <p><code>1st_number</code> (starts with digit '1'!), <code>9lives</code></p>
              <p>Expecting <code>Total</code> to read <code>total</code> leads to "undeclared identifier".</p>
              <p><code>int float;</code> or <code>int return;</code> (Keywords!)</p>
              <p><code>emp$salary</code>, <code>user#id</code>, <code>test@mail</code></p>
            </div>
          </div>
        </div>

        <div class="teacher-callout insight">
          <div class="callout-icon"><i class="fa-solid fa-sparkles"></i></div>
          <div class="callout-body">
            <div class="callout-title">The C99/C11 Magic Identifier: __func__ (Slide 72)</div>
            <p>C99 introduced a built-in predefined identifier: <code>__func__</code>. Whenever you reference it inside any function, the compiler treats it as:
            <br><code>static const char __func__[] = "name_of_current_function";</code>
            <br>Calling <code>printf("Inside: %s\n", __func__);</code> inside <code>main()</code> prints <code>"Inside: main"</code>. Systems programmers use it everywhere for debug logging!</p>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-boxes-stacked"></i> Data Types: Memory Containers & Capacities (Slides 73–80)</h3>
        <p>In C, a <strong>data type</strong> tells the compiler two critical facts: <strong>how many bytes of RAM to reserve</strong>, and <strong>how to interpret the bits inside</strong>.</p>
        
        <div class="teacher-callout analogy">
          <div class="callout-icon"><i class="fa-solid fa-mug-hot"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Beverage Container Analogy</div>
            <p>
              &bull; <code>char</code> (1 byte) = An espresso cup (holds 1 character or tiny number -128 to 127).<br>
              &bull; <code>short</code> (2 bytes) = A coffee mug (holds numbers -32,768 to 32,767).<br>
              &bull; <code>int</code> (4 bytes) = A 1-liter water bottle (holds numbers up to $\pm 2.14$ billion).<br>
              &bull; <code>long long</code> (8 bytes) = A giant water gallon (holds quintillions up to $\approx \pm 9.22 \times 10^{18}$).<br>
              &bull; <code>float</code> / <code>double</code> = Containers equipped with a decimal measuring syringe!
            </p>
          </div>
        </div>

        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Data Type</th><th>Size (Bytes)</th><th>Bits</th><th>Value Range (32/64-bit GCC)</th><th>Format Specifier</th></tr>
            </thead>
            <tbody>
              <tr><td><code>char</code></td><td>1 byte</td><td>8</td><td>-128 to 127 (signed)</td><td><code>%c</code> or <code>%d</code></td></tr>
              <tr><td><code>unsigned char</code></td><td>1 byte</td><td>8</td><td>0 to 255</td><td><code>%c</code> or <code>%u</code></td></tr>
              <tr><td><code>short int</code></td><td>2 bytes</td><td>16</td><td>-32,768 to 32,767</td><td><code>%hd</code></td></tr>
              <tr><td><code>unsigned short</code></td><td>2 bytes</td><td>16</td><td>0 to 65,535</td><td><code>%hu</code></td></tr>
              <tr><td><code>int</code></td><td>4 bytes</td><td>32</td><td>-2,147,483,648 to 2,147,483,647 ($-2^{31}$ to $2^{31}-1$)</td><td><code>%d</code> or <code>%i</code></td></tr>
              <tr><td><code>unsigned int</code></td><td>4 bytes</td><td>32</td><td>0 to 4,294,967,295 ($0$ to $2^{32}-1$)</td><td><code>%u</code></td></tr>
              <tr><td><code>long int</code></td><td>4 / 8 bytes</td><td>32 / 64</td><td>At least 32 bits ($-2^{31}$ to $2^{31}-1$)</td><td><code>%ld</code></td></tr>
              <tr><td><code>long long int</code></td><td>8 bytes</td><td>64</td><td>$-2^{63}$ to $2^{63}-1$ ($\approx \pm 9.22 \times 10^{18}$)</td><td><code>%lld</code></td></tr>
              <tr><td><code>float</code></td><td>4 bytes</td><td>32</td><td>$\pm 3.4 \times 10^{-38}$ to $\pm 3.4 \times 10^{38}$ (6 decimals precision)</td><td><code>%f</code></td></tr>
              <tr><td><code>double</code></td><td>8 bytes</td><td>64</td><td>$\pm 1.7 \times 10^{-308}$ to $\pm 1.7 \times 10^{308}$ (15 decimals precision)</td><td><code>%lf</code></td></tr>
              <tr><td><code>void</code></td><td>0 bytes</td><td>0</td><td>Valueless / empty type (functions returning nothing or generic pointers)</td><td>N/A</td></tr>
            </tbody>
          </table>
        </div>

        <div class="teacher-callout exam-alert">
          <div class="callout-icon"><i class="fa-solid fa-scale-balanced"></i></div>
          <div class="callout-body">
            <div class="callout-title">sizeof Operator & &lt;limits.h&gt; (Slide 80)</div>
            <p><strong>Crucial Exam Fact:</strong> <code>sizeof</code> is NOT a function; it is a <strong>compile-time unary operator</strong>! The compiler calculates the byte size during compilation and replaces <code>sizeof(int)</code> with the literal number <code>4</code>.
            To inspect host-specific numeric limits, include <code>&lt;limits.h&gt;</code> for constants like <code>INT_MAX</code>, <code>INT_MIN</code>, and <code>CHAR_BIT</code>.</p>
          </div>
        </div>
      </div>
    """,
    "code": {
        "title": "Verifying Data Types, Limits & __func__ in C",
        "desc": "Inspecting datatypes, compile-time sizeof evaluations, and the predefined identifier __func__.",
        "lang": "c",
        "snippet": """#include <stdio.h>
#include <limits.h>

void show_demo(void) {
    // C99 __func__ magic identifier
    printf("Executing inside function: %s\\n", __func__);
}

int main(void) {
    show_demo();

    printf("sizeof(char)      = %zu byte  [Range: %d to %d]\\n", sizeof(char), CHAR_MIN, CHAR_MAX);
    printf("sizeof(short)     = %zu bytes [Range: %d to %d]\\n", sizeof(short), SHRT_MIN, SHRT_MAX);
    printf("sizeof(int)       = %zu bytes [Range: %d to %d]\\n", sizeof(int), INT_MIN, INT_MAX);
    printf("sizeof(long long) = %zu bytes\\n", sizeof(long long));
    printf("sizeof(float)     = %zu bytes\\n", sizeof(float));
    printf("sizeof(double)    = %zu bytes\\n", sizeof(double));

    return 0;
}""",
        "output": "Executing inside function: show_demo\nsizeof(char)      = 1 byte  [Range: -128 to 127]\nsizeof(short)     = 2 bytes [Range: -32768 to 32767]\nsizeof(int)       = 4 bytes [Range: -2147483648 to 2147483647]\nsizeof(long long) = 8 bytes\nsizeof(float)     = 4 bytes\nsizeof(double)    = 8 bytes"
    },
    "resources": [
        {"type": "gfg", "title": "C Data Types & Value Ranges", "url": "https://www.geeksforgeeks.org/data-types-in-c/", "desc": "Curriculum link referenced in Slide 73 detailing primitive, derived, and user types."},
        {"type": "gfg", "title": "The __func__ Predefined Identifier in C", "url": "https://www.geeksforgeeks.org/c-predefined-identifier-__func__/", "desc": "Curriculum link referenced in Slide 72 exploring C99 diagnostic logging."},
        {"type": "docs", "title": "GNU C Reference Manual: Keywords", "url": "https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html", "desc": "Official GNU documentation detailing ANSI and ISO C keywords."}
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
})

# Module 8
modules.append({
    "id": "m8",
    "num": 8,
    "title": "Variables, Constants & Escape Sequences",
    "subtitle": "Scope, Shadowing, #define vs const, Escape Sequences & Syntax vs Semantic Errors",
    "slides": "Slides 81–106",
    "time": "40 mins",
    "content": r"""
      <div class="teaching-block">
        <h3><i class="fa-solid fa-map-pin"></i> Variable Scope: Local vs. Global (Slides 84–87)</h3>
        <p>A variable's <strong>scope</strong> defines where in the program that variable is visible and accessible.</p>
        
        <div class="teacher-callout analogy">
          <div class="callout-icon"><i class="fa-solid fa-lightbulb"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Desk Lamp vs. Street Lamp Analogy (Variable Shadowing)</div>
            <p>
              &bull; <strong>Global Variables:</strong> Declared outside all functions. Like a <strong>street lamp outside</strong>—visible to everyone on the entire block.<br>
              &bull; <strong>Local Variables:</strong> Declared inside a specific function or block <code>{ ... }</code>. Like a <strong>desk lamp inside your bedroom</strong>—visible only to you inside your room.<br>
              &bull; <strong>Variable Shadowing (Slide 87):</strong> What if your desk lamp and the street lamp have the same name? Inside your room, your local desk lamp <strong>takes priority and shadows</strong> the street lamp! The global variable remains completely untouched outside.
            </p>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-lock"></i> Constants: #define vs. const (Slide 88)</h3>
        <p>A <strong>constant</strong> is an entity whose stored value cannot be modified during program execution. C provides two ways to declare constants:</p>

        <div class="comparison-card">
          <div class="comparison-header">
            <span><i class="fa-solid fa-balance-scale"></i> #define Macro vs const Variable (Slide 88)</span>
            <span class="badge">Architecture Comparison</span>
          </div>
          <div class="comparison-grid">
            <div class="comparison-col">
              <h4>Aspect</h4>
              <p><strong>Stage Handled</strong></p>
              <p><strong>Memory Allocated?</strong></p>
              <p><strong>Type Safety</strong></p>
              <p><strong>Scope</strong></p>
              <p><strong>Syntax Example</strong></p>
            </div>
            <div class="comparison-col">
              <h4>#define (Preprocessor Macro)</h4>
              <p>Handled during <strong>Preprocessing</strong> (Stage 1).</p>
              <p><strong>No memory allocated</strong>; pure text find-and-replace.</p>
              <p>No type checking (blind text substitution).</p>
              <p>File-wide scope from definition onward.</p>
              <p><code>#define PI 3.14159</code> (no semicolon!)</p>
            </div>
            <div class="comparison-col">
              <h4>const Variable (Compiler Enforced)</h4>
              <p>Handled during <strong>Compilation</strong> (Stage 2).</p>
              <p><strong>Allocates memory</strong> in the <code>.rodata</code> read-only segment.</p>
              <p>Strict datatype checking enforced by compiler.</p>
              <p>Respects block scope (local to its function).</p>
              <p><code>const float PI = 3.14159f;</code></p>
            </div>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-terminal"></i> Escape Sequences: Non-Printable Characters (Slides 94–96)</h3>
        <p>Escape sequences begin with a backslash (<code>\</code>) and tell the terminal or printer to perform special formatting actions:</p>

        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Sequence</th><th>Name</th><th>Action / Real-World Behavior</th></tr>
            </thead>
            <tbody>
              <tr><td><code>\n</code></td><td>Newline</td><td>Moves cursor down to the beginning of the next line.</td></tr>
              <tr><td><code>\t</code></td><td>Horizontal Tab</td><td>Advances cursor to the next tab stop (typically multiples of 8 columns).</td></tr>
              <tr><td><code>\r</code></td><td>Carriage Return</td><td>Moves cursor all the way back to the <strong>start of the current line</strong>! Subsequent characters overwrite existing ones.</td></tr>
              <tr><td><code>\b</code></td><td>Backspace</td><td>Moves cursor back by one character position without erasing.</td></tr>
              <tr><td><code>\\</code></td><td>Backslash</td><td>Prints a literal backslash character <code>\</code>.</td></tr>
              <tr><td><code>\"</code></td><td>Double Quote</td><td>Prints a literal quote character <code>"</code> inside a string literal.</td></tr>
              <tr><td><code>\072</code></td><td>Octal Escape</td><td>Interprets digits after <code>\</code> as octal. <code>\072</code> = decimal 58 = ASCII <code>':'</code> (Slide 94).</td></tr>
              <tr><td><code>\x4a</code></td><td>Hex Escape</td><td>Interprets digits after <code>\x</code> as hex. <code>\x4a</code> = decimal 74 = ASCII <code>'J'</code> (Slide 94).</td></tr>
            </tbody>
          </table>
        </div>

        <div class="teacher-callout insight">
          <div class="callout-icon"><i class="fa-solid fa-keyboard"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Secret of Carriage Return (\r)</div>
            <p>On vintage mechanical typewriters, a physical carriage held the paper. Striking "Carriage Return" returned the carriage to the left margin without moving to the next line!
            <br>In C: <code>printf("Hello friend\rend\n");</code> prints <code>"endlo friend"</code> because <code>\r</code> moves the cursor to column 0, where <code>"end"</code> overwrites <code>"Hel"</code>!</p>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-bug"></i> Syntax Errors vs. Semantic Errors (Slides 102–104)</h3>
        <p>Every programmer must distinguish between grammar bugs and logic bugs:</p>
        
        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Aspect</th><th>Syntax Error (Grammar)</th><th>Semantic Error (Meaning / Logic)</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Definition</strong></td><td>Violation of the grammatical rules of the C programming language.</td><td>The code follows grammar rules, but the logic does not match programmer intent.</td></tr>
              <tr><td><strong>Detection</strong></td><td>Caught at <strong>Compile Time</strong> by <code>cc1</code>; binary will NOT be built.</td><td>Compiles cleanly without errors, but produces wrong output at <strong>Runtime</strong>.</td></tr>
              <tr><td><strong>Everyday Analogy</strong></td><td>"Dog the barked loud." (Grammar order broken).</td><td>"The dog flew to the moon." (Grammatically valid, but nonsense in reality!).</td></tr>
              <tr><td><strong>Slide 103 Example</strong></td><td>Missing semicolon <code>;</code> or mismatched braces <code>{</code>.</td><td>Placing <code>return 0;</code> before <code>printf("Hello");</code>! The function terminates before printing!</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    "code": {
        "title": "Variable Shadowing, Escape Sequences & Semantic Bug Demo (Slides 87, 94, 103)",
        "desc": "Testing variable shadowing, carriage return overwriting, octal/hex escapes, and unreachable statements.",
        "lang": "c",
        "snippet": """#include <stdio.h>

int g = 20; // Global variable (Street lamp)

int main(void) {
    int g = 10; // Local variable (Desk lamp) shadows global!
    printf("Local variable shadows global: g = %d\\n", g);

    // Escape sequences from Slide 94:
    // Octal \\072 = 58 (':'), \\065 = 53 ('5')
    char* s = "A\\072\\065";
    // Hex \\x4a = 74 ('J')
    char* y = "B\\x4a";
    printf("Octal escape string: %s\\n", s);
    printf("Hex escape string  : %s\\n", y);

    // Carriage return demo
    printf("Hello friend\\rend\\n");

    return 0;
}""",
        "output": "Local variable shadows global: g = 10\nOctal escape string: A:5\nHex escape string  : BJ\nendlo friend"
    },
    "resources": [
        {"type": "gfg", "title": "Differences Between Syntax and Semantics", "url": "https://www.geeksforgeeks.org/difference-between-syntax-and-semantics/", "desc": "Curriculum reference from Slide 102 exploring compiler vs runtime errors."},
        {"type": "tool", "title": "ASCII Table and Description", "url": "https://www.asciitable.com", "desc": "Reference table for character decimal, hex, and octal mappings."},
        {"type": "docs", "title": "TotalView: What Does a Debugger Do?", "url": "https://totalview.io/blog/what-does-debugger-do", "desc": "Curriculum link referenced in Slide 100 on analyzing bugs and breakpoints."}
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
            "question": "Which of the following describes a Semantic Error in C programming (Slide 102–104)?",
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
})

# Module 9
modules.append({
    "id": "m9",
    "num": 9,
    "title": "C Operators & Expressions Deep Dive",
    "subtitle": "No BODMAS in C, Precedence, Step-by-Step Bitwise Mastery & Two's Complement (~35 = -36)",
    "slides": "Slides 107–133",
    "time": "45 mins",
    "content": r"""
      <div class="teaching-block">
        <h3><i class="fa-solid fa-bolt"></i> The Crucial Myth: There is NO BODMAS in C! (Slide 107)</h3>
        <p class="lead-text">
          In elementary school, you were taught the BODMAS rule (Brackets, Orders, Division, Multiplication, Addition, Subtraction).
          <strong>Forget BODMAS when writing or reading C code!</strong>
        </p>

        <div class="teacher-callout pitfall">
          <div class="callout-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
          <div class="callout-body">
            <div class="callout-title">Precedence and Associativity Dictate Evaluation (Slide 107)</div>
            <p>Slide 107 emphasizes: <em>"There is no BODMAS in C language. Precedence and Associativity are two characteristics of operators that determine the evaluation order of subexpressions in absence of brackets."</em></p>
            <p>
              &bull; <strong>Precedence:</strong> Determines <em>which</em> operator grabs its operands first when different operators compete (e.g. <code>*</code> binds before <code>+</code> in <code>3 + 4 * 5 = 23</code>).<br>
              &bull; <strong>Associativity:</strong> Determines the evaluation direction (<strong>Left-to-Right</strong> or <strong>Right-to-Left</strong>) when multiple operators share the <em>same</em> precedence level!
            </p>
          </div>
        </div>

        <div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr><th>Priority Tier</th><th>Operators</th><th>Description</th><th>Associativity</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Tier 1 (Highest)</strong></td><td><code>()</code>, <code>[]</code>, <code>-&gt;</code>, <code>.</code></td><td>Parentheses, array subscript, structure access</td><td>Left-to-Right</td></tr>
              <tr><td><strong>Tier 2 (Unary)</strong></td><td><code>++</code>, <code>--</code>, <code>+</code>, <code>-</code>, <code>!</code>, <code>~</code>, <code>*</code>, <code>&amp;</code>, <code>sizeof</code></td><td>Prefix inc/dec, logical/bitwise NOT, address-of, dereference</td><td><strong>Right-to-Left</strong></td></tr>
              <tr><td><strong>Tier 3 (Multiplicative)</strong></td><td><code>*</code>, <code>/</code>, <code>%</code></td><td>Multiplication, division, modulo remainder</td><td>Left-to-Right</td></tr>
              <tr><td><strong>Tier 4 (Additive)</strong></td><td><code>+</code>, <code>-</code></td><td>Addition and subtraction</td><td>Left-to-Right</td></tr>
              <tr><td><strong>Tier 5 (Bitwise Shifts)</strong></td><td><code>&lt;&lt;</code>, <code>&gt;&gt;</code></td><td>Left shift (multiply by $2^k$), right shift (divide by $2^k$)</td><td>Left-to-Right</td></tr>
              <tr><td><strong>Tier 6 (Relational)</strong></td><td><code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code>, <code>&gt;=</code></td><td>Relational inequalities</td><td>Left-to-Right</td></tr>
              <tr><td><strong>Tier 7 (Equality)</strong></td><td><code>==</code>, <code>!=</code></td><td>Equal to, not equal to</td><td>Left-to-Right</td></tr>
              <tr><td><strong>Tier 8 to 10 (Bitwise)</strong></td><td><code>&amp;</code>, <code>^</code>, <code>|</code></td><td>Bitwise AND, Bitwise XOR, Bitwise OR</td><td>Left-to-Right</td></tr>
              <tr><td><strong>Tier 11 to 12 (Logical)</strong></td><td><code>&amp;&amp;</code>, <code>||</code></td><td>Logical AND, Logical OR (Short-circuiting!)</td><td>Left-to-Right</td></tr>
              <tr><td><strong>Tier 13 (Ternary)</strong></td><td><code>? :</code></td><td>Conditional expression</td><td><strong>Right-to-Left</strong></td></tr>
              <tr><td><strong>Tier 14 (Assignment)</strong></td><td><code>=</code>, <code>+=</code>, <code>-=</code>, <code>*=</code>, etc.</td><td>Simple & compound assignment</td><td><strong>Right-to-Left</strong></td></tr>
              <tr><td><strong>Tier 15 (Lowest)</strong></td><td><code>,</code></td><td>Comma operator (sequence point)</td><td>Left-to-Right</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-calculator"></i> Arithmetic, Increment & Chaining Traps (Slides 111–117)</h3>
        <ul>
          <li><strong>Integer Division (<code>/</code>):</strong> In C, <code>10 / 4</code> produces <code>2</code>, NOT <code>2.5</code>! Any fractional decimal is cleanly truncated toward zero. To preserve fractions, at least one operand must be a float: <code>10.0 / 4 = 2.5</code>.</li>
          <li><strong>Modulo Division (<code>%</code>):</strong> Returns the integer remainder (e.g. <code>10 % 3 = 1</code>). Modulo is <strong>strictly prohibited</strong> on floating-point numbers! <code>10.5 % 3</code> is a fatal compiler error.</li>
          <li><strong>Prefix Increment (<code>++x</code>):</strong> <em>"Pay first, ride later."</em> Value increments immediately, and the newly incremented value is returned.</li>
          <li><strong>Postfix Increment (<code>x++</code>):</strong> <em>"Ride now, pay later."</em> Current value is returned for the expression first, and only incremented after the evaluation completes.</li>
        </ul>

        <div class="teacher-callout exam-alert">
          <div class="callout-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
          <div class="callout-body">
            <div class="callout-title">The Chaining Trap: d = a &gt; b &lt; c (Slide 117)</div>
            <p>Suppose: <code>int a = 1, b = 2, c = 3; int d = a &gt; b &lt; c;</code></p>
            <p>Because relational operators associate <strong>Left-to-Right</strong>:
            <br>1. First evaluate: <code>(a &gt; b)</code> &rarr; <code>(1 &gt; 2)</code> evaluates to <strong>0 (False)</strong>.
            <br>2. Next evaluate: <code>0 &lt; c</code> &rarr; <code>(0 &lt; 3)</code> evaluates to <strong>1 (True)</strong>!
            <br>Therefore, <code>d</code> is assigned <strong>1</strong>! (Even though in mathematics $1 > 2 < 3$ is nonsense).</p>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-shield-halved"></i> Short-Circuiting in Logical Operators (Slides 120–123)</h3>
        <p>In C, <code>&amp;&amp;</code> (Logical AND) and <code>||</code> (Logical OR) employ <strong>Short-Circuit Evaluation</strong> (Lazy Evaluation):</p>
        <ul>
          <li><strong>In <code>A &amp;&amp; B</code>:</strong> If <code>A</code> evaluates to <strong>0 (False)</strong>, the entire expression is already known to be False. The compiler <strong>skips evaluating B entirely</strong>! (Slide 122: in <code>(10 == 4) &amp;&amp; printf("Hi")</code>, <code>printf</code> is never executed!).</li>
          <li><strong>In <code>A || B</code>:</strong> If <code>A</code> evaluates to <strong>non-zero (True)</strong>, the expression is already known to be True. The compiler <strong>skips evaluating B entirely</strong>! (Slide 123: in <code>(10 != 4) || printf("Hi")</code>, <code>printf</code> is never executed!).</li>
        </ul>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-microchip"></i> Bitwise Mastery: Step-by-Step Explanation Process (Slides 124–129)</h3>
        <p class="lead-text">
          Bitwise operators allow you to reach directly into the CPU registers and manipulate individual binary <code>0</code>s and <code>1</code>s in a single clock cycle. Follow this step-by-step masterclass:
        </p>

        <!-- STEP 1: The Core Mental Model -->
        <div class="step-guide-card">
          <div class="step-badge">STEP 1</div>
          <div class="step-content">
            <h4>The Light Switch Foundation: What is a Bit?</h4>
            <p>Imagine a light switch on the wall: it has only two states: <strong>0 (OFF / open circuit)</strong> and <strong>1 (ON / closed circuit)</strong>. In computer memory, an 8-bit number is literally a row of 8 tiny transistor switches. Bitwise operators evaluate these switches column-by-column with blazing speed.</p>
          </div>
        </div>

        <!-- STEP 2: The 4 Core Gates Explained Step-by-Step -->
        <div class="step-guide-card">
          <div class="step-badge">STEP 2</div>
          <div class="step-content">
            <h4>The 4 Core Bitwise Gates: Mental Models &amp; Truth Tables</h4>
            <p>Every gate has a distinct physical circuit analogy and truth rule:</p>

            <div class="bitwise-grid">
              <!-- AND -->
              <div class="bitwise-card">
                <div class="bitwise-card-header and">
                  <span class="gate-symbol">&amp;</span>
                  <span class="gate-name">Bitwise AND</span>
                  <span class="gate-tag">Series Circuit</span>
                </div>
                <div class="bitwise-card-body">
                  <p class="analogy-text"><strong>Circuit Rule:</strong> Two switches in a row on the same wire. Current flows <strong>ONLY if BOTH switches are ON</strong> (1). If either is 0, the lamp is dark.</p>
                  <table class="mini-truth-table">
                    <thead><tr><th>A</th><th>B</th><th>A &amp; B</th></tr></thead>
                    <tbody>
                      <tr><td>0</td><td>0</td><td class="res-0">0</td></tr>
                      <tr><td>0</td><td>1</td><td class="res-0">0</td></tr>
                      <tr><td>1</td><td>0</td><td class="res-0">0</td></tr>
                      <tr><td>1</td><td>1</td><td class="res-1">1</td></tr>
                    </tbody>
                  </table>
                  <div class="real-use">
                    <strong>Real-World Use:</strong> <em>Masking &amp; Clearing.</em>
                    <br>Check if odd: <code>(num &amp; 1)</code> tests if the lowest bit is 1.
                  </div>
                </div>
              </div>

              <!-- OR -->
              <div class="bitwise-card">
                <div class="bitwise-card-header or">
                  <span class="gate-symbol">|</span>
                  <span class="gate-name">Bitwise OR</span>
                  <span class="gate-tag">Parallel Circuit</span>
                </div>
                <div class="bitwise-card-body">
                  <p class="analogy-text"><strong>Circuit Rule:</strong> Two parallel wires. Current flows if <strong>EITHER switch (or both) is ON</strong> (1). Only turns off if both are 0.</p>
                  <table class="mini-truth-table">
                    <thead><tr><th>A</th><th>B</th><th>A | B</th></tr></thead>
                    <tbody>
                      <tr><td>0</td><td>0</td><td class="res-0">0</td></tr>
                      <tr><td>0</td><td>1</td><td class="res-1">1</td></tr>
                      <tr><td>1</td><td>0</td><td class="res-1">1</td></tr>
                      <tr><td>1</td><td>1</td><td class="res-1">1</td></tr>
                    </tbody>
                  </table>
                  <div class="real-use">
                    <strong>Real-World Use:</strong> <em>Setting Flags / Turning Bits ON.</em>
                    <br>Turn on permission bit without altering other bits: <code>perms |= 0x04;</code>
                  </div>
                </div>
              </div>

              <!-- XOR -->
              <div class="bitwise-card">
                <div class="bitwise-card-header xor">
                  <span class="gate-symbol">^</span>
                  <span class="gate-name">Bitwise XOR</span>
                  <span class="gate-tag">Difference Detector</span>
                </div>
                <div class="bitwise-card-body">
                  <p class="analogy-text"><strong>Circuit Rule:</strong> Staircase 2-way switch. Lamp is ON <strong>ONLY when switches are in DIFFERENT directions</strong> (one UP, one DOWN)!</p>
                  <table class="mini-truth-table">
                    <thead><tr><th>A</th><th>B</th><th>A ^ B</th></tr></thead>
                    <tbody>
                      <tr><td>0</td><td>0</td><td class="res-0">0</td></tr>
                      <tr><td>0</td><td>1</td><td class="res-1">1</td></tr>
                      <tr><td>1</td><td>0</td><td class="res-1">1</td></tr>
                      <tr><td>1</td><td>1</td><td class="res-0">0</td></tr>
                    </tbody>
                  </table>
                  <div class="real-use">
                    <strong>Real-World Use:</strong> <em>Toggling &amp; Variable Swapping.</em>
                    <br>Swap two numbers without temp: <code>a^=b; b^=a; a^=b;</code>
                  </div>
                </div>
              </div>

              <!-- NOT -->
              <div class="bitwise-card">
                <div class="bitwise-card-header not">
                  <span class="gate-symbol">~</span>
                  <span class="gate-name">Bitwise NOT</span>
                  <span class="gate-tag">Inverter Mirror</span>
                </div>
                <div class="bitwise-card-body">
                  <p class="analogy-text"><strong>Circuit Rule:</strong> Unary inverter gate. Flips every single <code>0</code> into <code>1</code>, and every single <code>1</code> into <code>0</code>.</p>
                  <table class="mini-truth-table">
                    <thead><tr><th>A</th><th>~A</th><th>Action</th></tr></thead>
                    <tbody>
                      <tr><td>0</td><td class="res-1">1</td><td>Flips to 1</td></tr>
                      <tr><td>1</td><td class="res-0">0</td><td>Flips to 0</td></tr>
                    </tbody>
                  </table>
                  <div class="real-use">
                    <strong>Real-World Use:</strong> <em>One's Complement &amp; Bit Inversion.</em>
                    <br>Creates inverse masks for zeroing bits: <code>x &amp;= ~FLAG;</code>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- STEP 3: Real Numbers Step-by-Step Column Alignment -->
        <div class="step-guide-card">
          <div class="step-badge">STEP 3</div>
          <div class="step-content">
            <h4>Bit-by-Bit Column Alignment: Computing A = 12 and B = 10</h4>
            <p>Let's trace how the CPU calculates these operations bit-by-bit on two 8-bit integers: $A = 12$ ($0000\ 1100_2$) and $B = 10$ ($0000\ 1010_2$):</p>
            
            <div class="bit-matrix-card">
              <div class="bit-matrix-title">
                <i class="fa-solid fa-table-cells"></i> Step-by-Step Bit Alignment Matrix
              </div>
              <table class="bit-matrix-table">
                <thead>
                  <tr>
                    <th class="row-label">Operand / Operation</th>
                    <th>b7 (128)</th><th>b6 (64)</th><th>b5 (32)</th><th>b4 (16)</th>
                    <th>b3 (8)</th><th>b2 (4)</th><th>b1 (2)</th><th>b0 (1)</th>
                    <th class="row-label">Decimal Result</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="row-label">Operand A (12)</td>
                    <td class="bit-cell zero">0</td><td class="bit-cell zero">0</td><td class="bit-cell zero">0</td><td class="bit-cell zero">0</td>
                    <td class="bit-cell highlight">1</td><td class="bit-cell highlight">1</td><td class="bit-cell zero">0</td><td class="bit-cell zero">0</td>
                    <td class="row-label"><strong>12</strong></td>
                  </tr>
                  <tr>
                    <td class="row-label">Operand B (10)</td>
                    <td class="bit-cell zero">0</td><td class="bit-cell zero">0</td><td class="bit-cell zero">0</td><td class="bit-cell zero">0</td>
                    <td class="bit-cell highlight">1</td><td class="bit-cell zero">0</td><td class="bit-cell highlight">1</td><td class="bit-cell zero">0</td>
                    <td class="row-label"><strong>10</strong></td>
                  </tr>
                  <tr class="res-row">
                    <td class="row-label">A &amp; B (AND: both 1)</td>
                    <td class="bit-result-cell">0</td><td class="bit-result-cell">0</td><td class="bit-result-cell">0</td><td class="bit-result-cell">0</td>
                    <td class="bit-result-cell highlight">1</td><td class="bit-result-cell">0</td><td class="bit-result-cell">0</td><td class="bit-result-cell">0</td>
                    <td class="row-label"><strong>8</strong> (Only bit 3 is 1 in both)</td>
                  </tr>
                  <tr class="res-row">
                    <td class="row-label">A | B (OR: either 1)</td>
                    <td class="bit-result-cell">0</td><td class="bit-result-cell">0</td><td class="bit-result-cell">0</td><td class="bit-result-cell">0</td>
                    <td class="bit-result-cell highlight">1</td><td class="bit-result-cell highlight">1</td><td class="bit-result-cell highlight">1</td><td class="bit-result-cell">0</td>
                    <td class="row-label"><strong>14</strong> ($8 + 4 + 2 = 14$)</td>
                  </tr>
                  <tr class="res-row">
                    <td class="row-label">A ^ B (XOR: different)</td>
                    <td class="bit-result-cell">0</td><td class="bit-result-cell">0</td><td class="bit-result-cell">0</td><td class="bit-result-cell">0</td>
                    <td class="bit-result-cell">0</td><td class="bit-result-cell highlight">1</td><td class="bit-result-cell highlight">1</td><td class="bit-result-cell">0</td>
                    <td class="row-label"><strong>6</strong> ($4 + 2 = 6$; matching bit 3 cancels out!)</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- STEP 4: Two's Complement Decoded (~35 = -36) -->
        <div class="step-guide-card">
          <div class="step-badge">STEP 4</div>
          <div class="step-content">
            <h4>The Mystery Solved: Why ~35 evaluates to -36! (Slides 126–128)</h4>
            <p>When you run <code>printf("%d", ~35);</code> in C, beginners expect either 220 or an error. Instead, C outputs <strong>-36</strong>. Here is the exact 4-phase step-by-step reason why:</p>

            <div class="twos-steps-container">
              <div class="twos-step-item">
                <div class="step-num-bubble">1</div>
                <div class="step-desc">
                  <strong>Write +35 in 8-bit binary:</strong>
                  <br>Break into powers of two: $35 = 32 + 2 + 1 \implies \mathbf{0010\ 0011_2}$.
                </div>
              </div>
              <div class="twos-step-item">
                <div class="step-num-bubble">2</div>
                <div class="step-desc">
                  <strong>Apply Bitwise NOT (<code>~</code>):</strong>
                  <br>Flip every 0 to 1 and every 1 to 0: $\mathbf{0010\ 0011_2} \longrightarrow \mathbf{1101\ 1100_2}$.
                </div>
              </div>
              <div class="twos-step-item">
                <div class="step-num-bubble">3</div>
                <div class="step-desc">
                  <strong>Check the Leftmost Sign Bit:</strong>
                  <br>In C, signed integers use Two's Complement. The leftmost bit (bit 7) is the <strong>Sign Bit</strong>.
                  <br>Because bit 7 is <strong>1</strong>, the computer knows this represents a <strong>NEGATIVE NUMBER</strong>!
                </div>
              </div>
              <div class="twos-step-item">
                <div class="step-num-bubble">4</div>
                <div class="step-desc">
                  <strong>Decode the Negative Magnitude:</strong>
                  <br>To find what negative quantity $\mathbf{1101\ 1100_2}$ represents, take its Two's Complement:
                  <br>&bull; Invert bits back: $\mathbf{0010\ 0011_2}$ (which equals $35$).
                  <br>&bull; Add 1: $35 + 1 = \mathbf{36}$.
                  <br>&bull; Add the negative sign: $\mathbf{-36}$!
                </div>
              </div>
            </div>

            <!-- Golden Formula Box -->
            <div class="golden-rule-box">
              <div class="rule-header">
                <i class="fa-solid fa-crown"></i>
                <span>Teacher's Golden Shortcut Formula (Slide 127)</span>
              </div>
              <div class="rule-formula">
                $$\sim N = -(N + 1)$$
              </div>
              <div class="rule-examples">
                <span class="rule-chip"><i class="fa-solid fa-arrow-right-long" style="color: var(--accent-yellow)"></i> $\sim 35 = -(35 + 1) = \mathbf{-36}$</span>
                <span class="rule-chip"><i class="fa-solid fa-arrow-right-long" style="color: var(--accent-yellow)"></i> $\sim 0 = -(0 + 1) = \mathbf{-1}$</span>
                <span class="rule-chip"><i class="fa-solid fa-arrow-right-long" style="color: var(--accent-yellow)"></i> $\sim (-12) = -(-12 + 1) = \mathbf{+11}$</span>
                <span class="rule-chip"><i class="fa-solid fa-arrow-right-long" style="color: var(--accent-yellow)"></i> $\sim 100 = -(100 + 1) = \mathbf{-101}$</span>
              </div>
            </div>
          </div>
        </div>

        <!-- STEP 5: High-Speed Shifts -->
        <div class="step-guide-card">
          <div class="step-badge">STEP 5</div>
          <div class="step-content">
            <h4>Bit Shift Operators as Hardware Multipliers &amp; Dividers (Slide 129)</h4>
            <p>Shifting bits left or right is the fastest mathematical operation a CPU can perform—it takes only 1 hardware clock cycle!</p>
            
            <div class="shifts-grid">
              <div class="shift-card left">
                <div class="shift-title"><i class="fa-solid fa-angles-left"></i> Left Shift (<code>x &lt;&lt; k</code>)</div>
                <p><strong>Action:</strong> Bits slide left by $k$ slots; zeroes fill in from the right.</p>
                <div class="shift-math">Formula: $\text{Result} = x \times 2^k$</div>
                <div class="shift-example">
                  <code>int x = 5; // 0000 0101</code><br>
                  <code>x &lt;&lt; 3; // 0010 1000 = 40 (5 * 2^3 = 5 * 8 = 40!)</code>
                </div>
              </div>

              <div class="shift-card right">
                <div class="shift-title"><i class="fa-solid fa-angles-right"></i> Right Shift (<code>x &gt;&gt; k</code>)</div>
                <p><strong>Action:</strong> Bits slide right by $k$ slots; rightmost bits fall off the edge.</p>
                <div class="shift-math">Formula: $\text{Result} = x / 2^k$ (integer division)</div>
                <div class="shift-example">
                  <code>int y = 40; // 0010 1000</code><br>
                  <code>y &gt;&gt; 2;  // 0000 1010 = 10 (40 / 2^2 = 40 / 4 = 10!)</code>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="teaching-block">
        <h3><i class="fa-solid fa-code-branch"></i> Ternary &amp; Comma Operators (Slides 130–133)</h3>
        <ul>
          <li><strong>Ternary Operator (<code>? :</code>):</strong> The compact one-line if-else. Syntax: <code>condition ? expr_true : expr_false;</code>
            <br>Finding maximum of 3 numbers (Slide 131):
            <br><code>max = a &gt; b ? (a &gt; c ? a : c) : (b &gt; c ? b : c);</code>
          </li>
          <li><strong>Comma Operator (<code>,</code>):</strong> Lowest precedence in all of C! Evaluates expressions strictly from Left to Right and returns the value of the <em>rightmost</em> expression.
            <br>Example: <code>int x = (10, 20, 30);</code> &rarr; <code>x</code> receives <strong>30</strong>!
          </li>
        </ul>
      </div>
    """,
    "code": {
        "title": "Bitwise Operations, ~35 = -36 & Relational Chaining Demo",
        "desc": "Testing ~35 = -36, relational chaining d = a > b < c, bit shifts, and short-circuit evaluation.",
        "lang": "c",
        "snippet": """#include <stdio.h>
#include <stdbool.h>

int main(void) {
    // 1. Bitwise NOT theorem: ~N = -(N + 1)
    int n = 35;
    printf("~35 = %d | ~(-12) = %d\\n", ~n, ~(-12));

    // 2. Relational Chaining: left-to-right associativity
    int a = 1, b = 2, c = 3;
    int d = a > b < c; // (1 > 2) is 0; then (0 < 3) is 1!
    printf("Result of (1 > 2 < 3): d = %d\\n", d);

    // 3. Bit Shifts as powers of 2
    int x = 5;
    printf("5 << 3 (5 * 8) = %d\\n", x << 3);
    printf("40 >> 2 (40 / 4) = %d\\n", 40 >> 2);

    // 4. Nested Ternary: Maximum of 3 numbers
    int p = 14, q = 42, r = 27;
    int max = p > q ? (p > r ? p : r) : (q > r ? q : r);
    printf("Max of %d, %d, %d is: %d\\n", p, q, r, max);

    // 5. Short-Circuiting in &&
    int u = 10, v = 4;
    bool res = ((u == v) && printf("This won't print!\\n"));
    printf("Short-circuit result: %d\\n", res);

    return 0;
}""",
        "output": "~35 = -36 | ~(-12) = 11\nResult of (1 > 2 < 3): d = 1\n5 << 3 (5 * 8) = 40\n40 >> 2 (40 / 4) = 10\nMax of 14, 42, 27 is: 42\nShort-circuit result: 0"
    },
    "resources": [
        {"type": "gfg", "title": "Operator Precedence and Associativity in C", "url": "https://www.geeksforgeeks.org/operator-precedence-and-associativity-in-c/", "desc": "Curriculum link referenced in Slide 107 with complete precedence tables."},
        {"type": "gfg", "title": "Left Shift and Right Shift Operators in C", "url": "https://www.geeksforgeeks.org/left-shift-right-shift-operators-c-cpp/", "desc": "Curriculum link referenced in Slide 129 detailing multiplication/division via shifts."},
        {"type": "gfg", "title": "The Comma Operator in C", "url": "https://www.geeksforgeeks.org/a-comma-operator-question/", "desc": "Curriculum link referenced in Slide 132 exploring evaluation order."},
        {"type": "gfg", "title": "Typecasting in C", "url": "https://www.geeksforgeeks.org/typecasting-in-c/", "desc": "Curriculum link referenced in Slide 133 detailing implicit vs explicit conversion."}
    ],
    "quiz": [
        {
            "id": "q9_1",
            "question": "What is the value of the bitwise complement of 35 (~35) in C programming, and why (Slides 126–127)?",
            "options": [
                "220, because all 8 bits are inverted",
                "-36, because signed integers are stored in two's complement form where ~N = -(N + 1)",
                "-35, because only the sign bit is changed",
                "0, because bitwise NOT is not allowed on integers"
            ],
            "answer": 1,
            "explanation": "Slides 126–127 explain that in two's complement representation, ~N = -(N + 1). Hence, ~35 evaluates to -(35 + 1) = -36."
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
})

with open("/home/hinazu/.gemini/antigravity/scratch/c-unit1-course/modules_7_9.json", "w", encoding="utf-8") as f:
    json.dump(modules, f, indent=2)
print("Modules 7 to 9 written to modules_7_9.json successfully!")
