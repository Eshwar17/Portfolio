from flask import Flask,render_template, request, redirect
app=Flask(__name__)
@app.route("/")
def home_page():
    return render_template('index.html')
@app.route("/index.html")
def index_page():
    return render_template('index.html')
@app.route("/about.html")
def about_page():
    return render_template('about.html')
@app.route("/contact.html")
def contact_page():
    return render_template('contact.html')
@app.route("/work.html")
def work_page():
    return render_template('work.html')
@app.route("/works.html")
def works_page():
    return render_template('works.html')
@app.route('/thankyou.html')
def thankyou_page():
    return render_template('thankyou.html')

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form',methods=['POST', "GET"])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong'