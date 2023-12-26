from flask import Flask, redirect ,render_template, request,make_response ,session,jsonify
from Interest import Interest
from db import SMDBHandler
app = Flask(__name__)
@app.route('/')
def start():
    print("........kl")
    return render_template("Sign in.html")

@app.route('/login', methods=['GET', 'POST'])
def log():
    try:
        if request.method == 'POST':
            uname = request.form.get('username')
            password = request.form.get('password')

            dhlr = SMDBHandler("localhost", "root", "12345678", "es")
            intrst = dhlr.check(uname, password)

            print(intrst)
            
            if intrst:
                print("Login successful")
                return redirect("/s")
            else:
                return render_template("Sign in.html",error="Please enter correct login info")
        else:
            # Handle the case when the request method is not POST
            return render_template("Sign in.html")
    except Exception as e:
        return render_template("Sign in.html", error=str(e))

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    try:
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            dhlr = SMDBHandler("localhost", "root", "12345678", "es")
            is_successful = dhlr.ins(username, password)

            if is_successful:
                print("Sign up successful")
                return redirect("/")
            else:
                print("Username already exists")
                return render_template("Sign up.html", error="Username already exists")

        # Handle GET request or other methods
        return render_template("Sign up.html", error="")
    except Exception as e:
        print(str(e))
        return render_template("Sign up.html", error=str(e))






@app.route('/s')
def hello_world():
    try:
        dhlr = SMDBHandler("localhost", "root", "12345678", "es")
        interests = dhlr.getInterests()

        return render_template("addStudent.html", interests=interests)

    except Exception as e:
        return render_template("addStudent.html", error=str(e))
@app.route("/addInterest",methods=["POST"])
def addContacts():
    try:
       if request.method == 'POST':
        rollNo = request.form['rollNo']
        name = request.form['name']
        email = request.form['email']
        gender = request.form['gender']
        dob = request.form['dob']
        city = request.form['city']
        interest = request.form['interest']
        department = request.form['department']
        degree = request.form['degree']
        subject = request.form['subject']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        if interest == "other":
                new_interest = request.form['newInterest']
                interest = new_interest
        interest= Interest(rollNo, name, email, gender, dob, city, interest, department, degree, subject, startDate, endDate)
        dhlr=SMDBHandler("localhost","root","12345678","es")
        intrst=dhlr.addInterest(interest)
        print(intrst)
        if intrst == True:
            return render_template("addStudent.html",error="Interest Added SuccessFully :_)")
        else :
              return render_template("addStudent.html", error="Please login to add contacts")
    except Exception as e:
        return render_template("addStudent.html", error=str(e))
@app.route('/provincial_distribution_data')
def provincial_distribution_data():
    try:
        dhlr = SMDBHandler("localhost", "root", "12345678", "es")
        provincial_distribution = dhlr.get_provincial_distribution()
        return jsonify(provincial_distribution)
    except Exception as e:
        return jsonify({'error': str(e)})
@app.route('/gender_distribution')
def gender_distribution():
    try:
        dhlr = SMDBHandler("localhost", "root", "12345678", "es")
        gender_distribution = dhlr.get_gender_distribution()
        return jsonify( gender_distribution)
    except Exception as e:
        return jsonify({'error': str(e)})
@app.route('/degree_distribution')
def degree_distribution():
    try:
        dhlr = SMDBHandler("localhost", "root", "12345678", "es")
        degree_distribution = dhlr.get_degree_distribution()
        return jsonify( degree_distribution)
    except Exception as e:
        return jsonify({'error': str(e)})
@app.route("/age_distribution_data")
def age_distribution_data():
    try:
        dhlr = SMDBHandler("localhost", "root", "12345678", "es")
        age_distribution_data = dhlr.get_age_distribution()
        return jsonify(age_distribution_data)

    except Exception as e:
        return jsonify(error=str(e))
@app.route('/department_distribution_data')
def get_department_distribution_data():
    try:
        dhlr = SMDBHandler("localhost", "root", "12345678", "es")
        department_distribution = dhlr.get_department_distribution()
        return jsonify(department_distribution)
    except Exception as e:
        return jsonify({'error': str(e)})
@app.route("/showalll")
def showalll():

    try:
        dhlr = SMDBHandler("localhost", "root", "12345678", "es")
        list=[]
        data = dhlr.show_all()
        for id in data:
            list.append({
                "RollNo": id[0],
                "Name": id[1],
                "Email": id[2],
                "Gender": id[3],
                "Dob": id[4],
                "City": id[5],
                "Interest": id[6],
                "Department": id[7],
                "Degree": id[8],
                "Subject": id[9],
                "StartDate": id[10],
                "EndDate": id[11]
            })
        return list
    except Exception as e:
        return render_template("addStudent.html", error=str(e))
@app.route("/showall")
def showall():
    try:
        dhlr = SMDBHandler("localhost", "root", "12345678", "es")

        data = dhlr.show_all()
        if data != None:
            return render_template("jquery.html", datas=data)
        else:
            er = "Hello you didn't add any data "
            return render_template("jquery.html", error=er)
    except Exception as e:
        return render_template("addStudent.html", error=str(e))
@app.route("/view/<int:id>")
def view_detail(id):
    try:
        dhlr = SMDBHandler("localhost", "root", "12345678", "es")
        data = dhlr.get_record_by_id(id) 
        if data:
            return render_template("viewStudent.html", data=data)
        else:
            return "Record not found."
    except Exception as e:
            print("hhhhhhey")
            return render_template("addStudent.html", error=str(e))
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_record(id):
    try:
        dhlr = SMDBHandler("localhost", "root", "12345678", "es")
        record = dhlr.get_record_by_id(id)

        if request.method == 'POST':
            updated_name = request.form['name']
            updated_email = request.form['email']
            updated_gender = request.form['gender']
            updated_dob = request.form['dob']
            updated_city = request.form['city']
            updated_interest = request.form['interest']
            updated_department = request.form['department']
            updated_degree = request.form['degree']
            updated_subject = request.form['subject']
            updated_startDate = request.form['startDate']
            updated_endDate = request.form['endDate']
            dhlr.update_record(id, updated_name, updated_email, updated_gender, updated_dob,
                               updated_city, updated_interest, updated_department, updated_degree, updated_subject,
                               updated_startDate, updated_endDate)
            return redirect("/showall")

        return render_template("update.html", record=record)

    except Exception as e:
        return render_template("addStudent.html", error=str(e))
@app.route("/delete/<int:id>")
def delete_record(id):
    try:
        dhlr = SMDBHandler("localhost", "root", "12345678", "es")
        dhlr.delete_record(id)
        return redirect("/showall")

    except Exception as e:
        return render_template("addStudent.html", error=str(e))
@app.route("/dash", methods=["GET", "POST"])
def dashboard():
    try:
        dhlr = SMDBHandler("localhost", "root", "12345678", "es")
        top_interests = dhlr.get_top_interests(5)
        bottom_interests = dhlr.get_bottom_interests(5)
        distinct_interests_count = dhlr.get_distinct_interests_count()
        provincial_distribution = dhlr.get_provincial_distribution()
        submission_chart_data = dhlr.get_submission_chart_data(30)
        age_distribution = dhlr.get_age_distribution()
        department_distribution = dhlr.get_department_distribution()
        degree_distribution = dhlr.get_degree_distribution()
        gender_distribution = dhlr.get_gender_distribution()
        return render_template(
            "dashboard.html",
            top_interests=top_interests,
            bottom_interests=bottom_interests,
            distinct_interests_count=distinct_interests_count,
            provincial_distribution=provincial_distribution,
            submission_chart_data=submission_chart_data,
            age_distribution=age_distribution,
            department_distribution=department_distribution,
            degree_distribution=degree_distribution,
            gender_distribution=gender_distribution,
        )
    except Exception as e:
        return render_template("addStudent.html", error=str(e))
if __name__ == '__main__':
    app.run()