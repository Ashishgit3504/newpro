from studentreg.serviceimpl.StudentImplInfo import StudentImpl
from studentreg.model.StudentInfo import myapp,Student
from flask import request,render_template

simpl = StudentImpl()

dummy = Student(id=0,fname='',lname='',age=0,email='',address='')

@myapp.route('/index/', methods=['GET'])
def appStandingPage():
    return render_template('Students.html',student = dummy,students=simpl.getAllStudents(),savg=simpl.getStudentsAgeAvg())


@myapp.route('/student/', methods=['POST'])
def addOrUpdateStudent():
    print(request.form['id'],request.form['fname'],request.form['lname'],request.form['age'],request.form['email'],request.form['address'])
    sid = int(request.form['id'])

    if sid==0:
        st = Student(fname=request.form['fname'], lname=request.form['lname'], age=request.form['age'], email=request.form['email'], address=request.form['address'])
        simpl.addStudent(st)
        emsg = "Student Added Successfully...!"
    else:
        st = Student(fname=request.form['fname'], lname=request.form['lname'], age=request.form['age'],
                     email=request.form['email'], address=request.form['address'],id=sid)
        simpl.updateStudent(st)
        emsg = "Student Updated Successfully...!"
    return render_template('Students.html',student=dummy,msg=emsg,students=simpl.getAllStudents(),savg=simpl.getStudentsAgeAvg())

@myapp.route('/edit/<id>', methods=['GET'])
def aaaaaa(id):
    stud = simpl.getStudent(id)
    #return 'inside edit student'+str(id)
    return render_template('Students.html', student=stud, students=simpl.getAllStudents(),savg=simpl.getStudentsAgeAvg())

@myapp.route('/delete/<id>', methods=['GET'])
def deleteStudent(id):
    #return 'inside delete student'+str(id)
    simpl.deleteStudent(id)
    return render_template('Students.html', student=dummy, students=simpl.getAllStudents(),msg="Student deleted Successfully...!",savg=simpl.getStudentsAgeAvg())

if __name__ == '__main__':
    myapp.run(debug=True)