# Python Fundamentals

[Home](../README.md) · **Python Fundamentals**

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Course](https://img.shields.io/badge/Course-CCCS%20102-blue)

Exercises, lab activities and small programs from **CCCS 102: Fundamentals of Programming**. They are grouped by topic. The dates in the table below come from the file timestamps (the last time each file was saved), so they are approximate.

Each script runs on its own and most of them ask for input in the terminal:

```bash
python3 <file>.py
```

The exercise files note Python 3.11.5, but any recent Python 3 should work. No extra packages are needed.

## Contents

| Folder | Topic | Dates |
|---|---|---|
| [prog-exercises/](prog-exercises/) | [Operators](#1-operators-prog-exercises) | 26 Sep 2023 |
| [coding-tasks/](coding-tasks/) | [Classes and input validation](#2-classes-and-input-validation-coding-tasks) | 4 May 2024 |
| [string-manipulation/](string-manipulation/) | [Counting characters in a string](#3-string-manipulation-string-manipulation) | 19 Nov 2023 |
| [labs-lists-tuples-sets-dicts/](labs-lists-tuples-sets-dicts/) | [Lists, tuples, sets and dictionaries](#4-collections-labs-lists-tuples-sets-dicts) | 18 Feb – 11 Mar 2024 |
| [file-handling/](file-handling/) | [Reading and writing files](#5-file-handling-file-handling) | 28 – 29 Nov 2023 |
| [taxation-spreadsheets/](taxation-spreadsheets/) | [Excel workbooks](#6-spreadsheets-taxation-spreadsheets) | 21 Nov – 1 Dec 2023 |

## 1. Operators (`prog-exercises`)

| File | What it does |
|---|---|
| `ORIAS_MARKJOSEPH_prog_exer_1.py` | Reads two numbers and prints the results of arithmetic, comparison, bitwise and logical operators |
| `ORIAS_MARKJOSEPH_prog_exer_2.py` | Reads two integers, swaps them, then prints parity checks, a sum, a left shift, a logical result and a remainder |

These exercises cover how `and`, `or`, `&` and `|` behave differently, and that `int()` drops the decimal part before a bitwise operation. A run of exercise 1 with `4.6` and `3.8`:

```text
Addition result:  8.399999999999999
Subtraction result:  0.7999999999999998
Multiplication result:  17.479999999999997
Division result:  1.2105263157894737
Equal result:  False
Greater result:  True
Less or equal result:  True
Bitwise AND result:  0
Bitwise OR result:  7
Logical AND result: False
Logical OR result:  True
```

The long decimals in the first three lines come from floating-point arithmetic. The bitwise lines use `int(4.6) = 4` and `int(3.8) = 3`, so `4 & 3 = 0` and `4 | 3 = 7`.

Looking back at the code, the "less or equal" line compares `num2 <= num2` (the same variable on both sides), so it always prints `True`. It should be `num1 <= num2`.

## 2. Classes and input validation (`coding-tasks`)

| File | What it does |
|---|---|
| `TASK1_ORIAS_1A.py` | `stud_info` class that collects and prints a student's name, age, address, year, section and program |
| `TASK2_ORIAS_1A.py` | Instrument rental: asks for the type, price and availability, then rents or returns the instrument |
| `TASK3_ORIAS_1A.py` | `student` class that records a name and age and asks again until the input is valid |

These programs use classes and `while True` loops that keep asking until the user gives valid input. Task 2 follows the sample run written in the comments at the top of the file:

```text
Enter instrument type: Guitar
Enter rental price: 500
Is the instrument available? (True/False): True
Guitar rental created with price PHP500.00
Do you want to rent or return the instrument? (Rent/Return): Rent
A Guitar has been rented for ₱500.00
```

## 3. String manipulation (`string-manipulation`)

Counts the letters, digits, spaces and special symbols in a string entered by the user.

| File | Notes |
|---|---|
| `ORIAS_MARKJOSEPH_A_STRINGMANIP.py` | The program |
| `STRINGMANIP.txt` | A sample input string |

The program loops over each character and uses `isalpha()`, `isdigit()` and `isspace()`. Anything that does not match one of those counts as a special symbol. A run with `Hello World 2023!`:

```text
Enter a string: Hello World 2023!
Letters:  10
Digits:  4
Spaces:  2
Special Symbols:  1
```

The order of the checks matters. Each character must be tested for only one category, which is why I used `if` / `elif` instead of separate `if` statements.

## 4. Collections (`labs-lists-tuples-sets-dicts`)

| File | Topic |
|---|---|
| `ORIAS_LAB1_List.py` | One example for each list method |
| `ORIAS_LAB2_Tuples.py` | Tuple methods (`count`, `index`) |
| `ORIAS_LAB3_Sets.py` | Set methods |
| `ORIAS_LAB4_Dictionary.py` | Dictionary methods |
| `ORIAS_LAB5_Act.List.py` | Activity: sort a list of fruits |
| `ORIAS_LAB6_Act.Sets.py` | Activity: check whether a smartphone brand is in a set |
| `ORIAS_LAB7_Act.Dictionary.py` | Activity: build and print a table of student names and averages |
| `ORIAS_LAB8.py` | Activity: collect colleges and their programs into a dictionary |

Labs 1 to 4 are one small example for each built-in method, so they work as a quick reference. Labs 5 to 8 are the activities that combine what I learned. Lab 8 is the most involved: it asks how many colleges there are, then the programs for each college, stores them as `{college: [programs]}`, and lets the user search for a college by name.

## 5. File handling (`file-handling`)

Reads student grades from `grades.txt` and writes each student's average to `average_grades.txt`, as described in the activity sheet (`activity file handling.jpg`).

| File | Role |
|---|---|
| `file_handling_ORIAS_MARKJOSEPH.py` | The script |
| `grades.txt` | Input: one line per student, a name followed by three scores |
| `average_grades.txt` | Output generated by the script |
| `activity file handling.jpg` | The activity instructions |

Run it from inside the `file-handling` folder so the relative file names resolve:

```bash
cd file-handling
python3 file_handling_ORIAS_MARKJOSEPH.py
```

For each line, the script splits the text, converts the scores to integers and divides their sum by how many there are. For the ten students in `grades.txt`, the output starts like this:

```text
Alice 89.0
Bob 82.33333333333333
Charlie 91.66666666666667
Dave 86.66666666666667
...
```

The first three lines match the sample output in the activity sheet. One thing I noticed when reviewing it: the script writes `file.close` without parentheses, so that line does not actually close the file. It still works because Python closes the file when the program ends, but a `with open(...)` block would be the proper way.

## 6. Spreadsheets (`taxation-spreadsheets`)

Excel workbooks for an income-tax topic:

- `ORIAS_INCOME_TAX_COMPUTATION.xlsx`: income tax computation
- `ORIAS_TAX_QUIZ.xlsx` and `#NEW_ORIAS_TAX_QUIZ.xlsx`: tax quiz workbooks (the second one is the newer version)

## What I learned

- Reading input and checking it with `while` loops and `try`/`except` before using it
- Using the built-in methods of lists, tuples, sets and dictionaries
- Writing simple classes with `__init__`
- Reading and writing text files
- Comparing my output against the sample outputs in the instructions, and reading old code again to find mistakes like the `num2 <= num2` one above

## Related

The string handling, file handling and input validation from these exercises were used again in the group final project, which is in its own repository, `jejemon-text-corrector` (see its "Project development" section).

[← Back to the main README](../README.md)
