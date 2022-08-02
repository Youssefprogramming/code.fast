from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'passsword'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("home.html")

@app.route('/nav')
def nav():
    return render_template("navbar.html")


@app.route('/Advanced')
def Advanced():
    flash('You are now in the python tutorial page!', category='success')
    return render_template("tutorial.html")

@app.route('/book', methods=['GET', 'POST'])
def book():
    return render_template("book.html")

@app.route('/project')
def project():
    return render_template("project.html")



@app.route('/courses', methods=['GET', 'POST'])
def courses():
    return render_template("courses.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")



@app.route('/Intermidiate', methods=['GET', 'POST'])
def index4():
    if request.method == 'POST':
        return redirect(url_for('advanced'))
    return render_template("project4.html")

@app.route('/advanced')
def advanced():
    return render_template("project5.html")

@app.route('/advanced', methods=['GET', 'POST'])
def index5():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template("project5.html")

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)