# Python Basic Questions and Answers

This folder contains simple, correct Python programs for the given basic programming questions.

## Questions covered

1. Algorithm and flowchart for finding the largest of 3 numbers
2. Identify `int`, `float`, and `string` data types
3. Output of `print("213" + "214")`
4. Output of `print(213 + 214)`
5. Use of the `input()` function
6. Check whether a number is prime
7. Check whether a number is even or odd
8. Print Grade A, B, or C based on a 10th-mark input
9. `for` loop from 20 to 60
10. Print each item in a list using a `for` loop
11. Add two numbers using a function and arguments
12. Create 10 fruits and print the 6th fruit
13. Change the 2nd fruit to Mango
14. Difference between list and tuple
15. Check whether a year is a leap year
16. Calculator using `input()`
17. Find the factorial of a number

## 1. Algorithm: Largest of Three Numbers

1. Start
2. Input three numbers `a`, `b`, and `c`
3. Check whether `a >= b` and `a >= c`
4. If true, set `largest = a`
5. Otherwise, check whether `b >= a` and `b >= c`
6. If true, set `largest = b`
7. Otherwise, set `largest = c`
8. Print `largest`
9. Stop

### Standard flowchart symbols

- **Oval (Terminator):** Start / Stop
- **Parallelogram (Input/Output):** Input / Print
- **Rectangle (Process):** Calculation / Assignment
- **Diamond (Decision):** Condition such as `if`
- **Arrow:** Flow direction

### Flowchart in text form

```text
             ( START )
                 |
                 v
        / Input a, b, c /
                 |
                 v
        < a >= b and a >= c? >
             /           \
          Yes             No
           |               |
           v               v
   [ largest = a ]   < b >= a and b >= c? >
           |             /            \
           |          Yes              No
           |           |                |
           |           v                v
           |    [ largest = b ]   [ largest = c ]
           |           \                /
           |            \              /
           +-------------+-------------+
                         |
                         v
                  / Print largest /
                         |
                         v
                      ( STOP )
```

## 2. Data Types

```python
x = "hello"   # str
y = 12        # int
z = 1.4       # float
```

Answer:

- `x` → `str` (string)
- `y` → `int` (integer)
- `z` → `float`

## 3. Output

```python
print("213" + "214")
```

Output:

```text
213214
```

Because both values are strings, they are concatenated.

## 4. Output

```python
print(213 + 214)
```

Output:

```text
427
```

## 5. Use of input()

The `input()` function is used to take data from the user during program execution. By default, it returns the input as a string.

Example:

```python
name = input("Enter your name: ")
```

For numeric input, type conversion can be used:

```python
age = int(input("Enter your age: "))
```

## 6. Prime Number

A prime number is a number greater than 1 that has only two factors: 1 and itself.

See `06_prime_number.py`.

## 7. Even or Odd

A number is even if it is exactly divisible by 2. Otherwise, it is odd.

See `07_even_or_odd.py`.

## 8. Grade A, B, or C

The program assumes:

- 90 to 100 → A
- 60 to 89 → B
- 0 to 59 → C

If your teacher uses different grade ranges, change the conditions.

See `08_grade_from_10th_mark.py`.

## 9. for loop from 20 to 60

```python
for i in range(20, 61):
    print(i)
```

`range()` excludes its ending value, so `61` is used to include `60`.

## 10. Print list items using a for loop

```python
for item in my_list:
    print(item)
```

See `10_for_loop_list_items.py`.

## 11. Function to add two numbers

A function can receive values through parameters and the function can be called with arguments.

```python
def add(a, b):
    return a + b
```

See `11_function_add_two_numbers.py`.

## 12. Print the 6th fruit

Python list indexing starts from 0.

Therefore:
- 1st item → index 0
- 2nd item → index 1
- ...
- 6th item → index 5

See `12_fruits_print_6th.py`.

## 13. Change the 2nd fruit to Mango

The 2nd item has index `1`.

```python
fruits[1] = "Mango"
```

See `13_change_2nd_fruit_to_mango.py`.

## 14. List vs Tuple

| List | Tuple |
|---|---|
| Written using `[]` | Written using `()` |
| Mutable | Immutable |
| Elements can be changed | Elements cannot be changed |
| Example: `[1, 2, 3]` | Example: `(1, 2, 3)` |

## 15. Leap Year

A year is a leap year when:

```text
(year divisible by 400)
OR
(year divisible by 4 AND not divisible by 100)
```

See `15_leap_year.py`.

## 16. Calculator

The calculator program takes two numbers and an operator from the user and performs `+`, `-`, `*`, or `/`.

See `16_calculator.py`.

## 17. Factorial

The factorial of `n` is:

```text
n! = n × (n-1) × (n-2) × ... × 1
```

For example:

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

See `17_factorial.py`.

## How to use in VS Code

1. Extract this folder.
2. Open the folder in VS Code.
3. Open any `.py` file.
4. Run it using the Run button or the Python terminal command.
5. Upload the folder/files to your GitHub repository.
