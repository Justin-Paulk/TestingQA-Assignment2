import os
from funTimes import *
from flask import Flask
from flask import render_template
from flask import request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/bmiCalc.html', methods=["GET", "POST"])
    def bmi_site():
        if request.method == "POST":
            if(request.form['feet'] and request.form['inches'] and request.form['pounds']):
                try:
                    feet = int(request.form.get('feet'))
                    inches = int(request.form.get('inches'))
                    pounds = float(request.form.get('pounds'))
                    res = bmi_calc(feet, inches, pounds)
                    resString = "You are " + str(res[0]) + " with a BMI of " + str(res[1])
                    return render_template("bmiCalc.html", resString=resString, errString="")
                except:
                    return render_template("bmiCalc.html", errString="Please enter valid numbers")

        return render_template("bmiCalc.html")


    @app.route('/retirementCalc.html', methods=["GET", "POST"])
    def retirement_site():
        if request.method == "POST":
            if(request.form['age'] and request.form['goal'] and request.form['salary'] and request.form['prc_saved']):
                try:
                    age = float(request.form.get('age'))
                    salary = float(request.form.get('salary'))
                    prc_saved = float(request.form.get('prc_saved'))
                    if prc_saved > 100:
                        return render_template("retirementCalc.html", errString="Please enter valid numbers")
                    prc_saved *= 1/100
                    goal = float(request.form.get('goal'))
                    res = round(float(retirement_calc(age, salary, prc_saved, goal)), 2)
                    print(res)
                    if res > 100.0:
                        newRes = "The goal would be reached at " + str(res) + ".\nThe goal will not be met."
                    else:
                        newRes = "The goal would be reached at " + str(res) + ".\nThe goal will be met."
                    print("here")
                    return render_template("retirementCalc.html", resString=newRes)
                except:
                    return render_template("retirementCalc.html", errString="Please enter valid numbers")

        return render_template("retirementCalc.html")

    return app
