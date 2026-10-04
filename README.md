# Tower of Hanoi

## 📌 Description

This project is a simple Python implementation of the **Tower of Hanoi** problem using **recursion**.

The program takes the number of disks as input and displays the step-by-step moves required to transfer all disks from the source tower to the target tower while following the rules of the Tower of Hanoi problem.

## 🎯 Objective

The main objective of this program is to understand:

* Recursion in Python
* Function calls
* Problem-solving using recursive algorithms
* The Tower of Hanoi algorithm

## 🧠 What is Tower of Hanoi?

Tower of Hanoi is a mathematical puzzle consisting of three towers and a number of disks of different sizes.

The goal is to move all disks from the **source tower** to the **target tower** using the **helper tower**.

### Rules

1. Only one disk can be moved at a time.
2. Only the top disk of a tower can be moved.
3. A larger disk cannot be placed on top of a smaller disk.
4. All disks must be moved from the source tower to the target tower.

## ⚙️ How the Program Works

The program uses a recursive function called `tower()`.

```python
def tower(n, source, helper, target):
```

The function receives:

* `n` – Number of disks
* `source` – Starting tower
* `helper` – Auxiliary tower
* `target` – Destination tower

The recursive process is:

1. Move `n-1` disks from the source tower to the helper tower.
2. Move the largest disk from the source tower to the target tower.
3. Move the `n-1` disks from the helper tower to the target tower.

The recursion stops when `n == 0`.

## 💻 Program

```python
def tower(n:int, source:str, helper:str,target:str):
    if n==0:
        return
    tower(n-1, source,target,helper)
    print(f"Move disk {n} from {source} -> {target}")
    tower(n-1,helper,source,target)

if __name__ == "__main__":
    n=int(input("Enter the number of disks:"))
    print(f"\n Steps to solve Tower for {n} disks")
    tower(n,"A","B","C")
```

## ▶️ How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open Command Prompt or Terminal.
4. Navigate to the project folder.
5. Run:

```bash
python "tower of hanoi.py"
```

6. Enter the number of disks when prompted.

## 📝 Example

### Input

```text
Enter the number of disks: 3
```

### Output

```text
Steps to solve Tower for 3 disks
Move disk 1 from A -> C
Move disk 2 from A -> B
Move disk 1 from C -> B
Move disk 3 from A -> C
Move disk 1 from B -> A
Move disk 2 from B -> C
Move disk 1 from A -> C
```

## ⏱️ Complexity

For `n` disks:

* **Time Complexity:** O(2^n)
* **Space Complexity:** O(n)

The minimum number of moves required is:

```text
2^n - 1
```

For example:

| Number of Disks | Minimum Moves |
| --------------: | ------------: |
|               1 |             1 |
|               2 |             3 |
|               3 |             7 |
|               4 |            15 |
|               5 |            31 |

## 🛠️ Technologies Used

* Python
* Recursion

## 🎓 Learning Outcome

By completing this project, you can understand how recursive functions work and how a complex problem can be divided into smaller subproblems.

## 📂 File Structure

```text
Tower-of-Hanoi/
│
└── tower of hanoi.py
```

## 👩‍💻 Author

Created as a Python programming practice project.

## 📄 License

This project is created for educational and learning purposes.
