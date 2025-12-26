from flask import Flask,request,render_template
import db_st
app = Flask(__name__)
@app.route('/', methods=["GET","POST"])
def add():
    if request.method=="POST":
        student=request.form.get("student")
        db_st.students.append(student)
        print("added succes")
    return render_template("index2.html",students=db_st.students)
@app.route('/edit', methods=["GET","POST"])
def edit():
    if request.method=="POST":
        if request.form.get("delete_student"):
            student=request.form.get("delete_student")
            db_st.students.remove(student)
            if student in db_st.present:
                db_st.present.remove(student)
                print("removed succes")
        if request.method=="POST":
                student=request.form.get("xyz")
                db_st.present.append(student)
    return render_template("index1.html", students=db_st.students , present=db_st.present)


if __name__ == "__main__":
    app.run(debug=True)

