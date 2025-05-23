# 🧩 Reeborg's World: Maze Challenge

[🔗 Try the Maze Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)

## 🧠 Objective

Guide **Reeborg**, the virtual robot, through a maze to reach the goal using Python.

---

## 📚 Key Commands

Reeborg uses a limited set of commands:

- `move()` – Move one step forward
- `turn_left()` – Turn left
- `front_is_clear()` – Check if there's no wall in front
- `wall_in_front()` – Check if there's a wall ahead
- `at_goal()` – Check if Reeborg has reached the goal

---

## 🧭 Strategy: Right-Hand Rule

The **right-hand rule** is a classic maze-solving technique. It involves always keeping your right hand on the wall:

1. If there's a path to the right, turn and take it.
2. If not, go forward if possible.
3. If blocked, turn left.

---

## 🧪 Python Code Solution

```python
def turn_right():
    for _ in range(3):
        turn_left()

def right_is_clear():
    turn_right()
    clear = front_is_clear()
    turn_left()
    return clear

def maze_move():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

while not at_goal():
    maze_move()
