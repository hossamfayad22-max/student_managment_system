# Student Management System (Flask)

A simple backend-based student management system built with Flask for learning purposes.

## Features
- Add students
- Delete students
- Mark students as present
- Display students and attendance list
- HTML templates rendering

## Project Structure
student_managment_system/
│
├── app.py
├── db_st.py
├── main.py
├── templates/
│ ├── index1.html
│ └── index2.html

bash
Copy code

## Requirements
- Python 3.9+
- Flask

## How to Run Locally

```bash
git clone https://github.com/hossamfayad22-max/student_managment_system.git
cd student_managment_system
python -m venv venv
venv\Scripts\activate
pip install flask
python app.py
Then open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000/
Notes
This project runs locally only.

GitHub Pages is NOT used.

Data is stored temporarily in memory (lists).

This project is for learning purposes.

yaml
Copy code

---

## 2️⃣ `.gitignore` (نفس اللي قبل كده)

لو مش عامل واحد، اعمله وحط:

```txt
venv/
__pycache__/
*.pyc
.env
