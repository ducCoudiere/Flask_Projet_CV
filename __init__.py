from flask import Flask,render_template

app = Flask(__name__) #creating flask app name

@app.route('/')
def home():
    return render_template("index.html")
 
@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_3')
def resume_3():
    return render_template("resume_3.html")

@app.route('/resume_4')
def resume_4():
    return render_template("resume_4.html")

@app.route('/resume_5')
def resume_5():
    return render_template("resume_5.html")

@app.route('/resume_6')
def resume_6():
    return render_template("resume_6.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

if(__name__ == "__main__"):
    app.run()
