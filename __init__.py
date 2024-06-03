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

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

@app.route('/resume_D')
def resume_D():
    return render_template("resume_D.html")

if(__name__ == "__main__"):
    app.run()
