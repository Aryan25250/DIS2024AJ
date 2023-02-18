from flask import Flask, render_template, request
from registration import Registration

app = Flask(__name__)
app.config["SECRET_KEY"] = "utfhukigy789y0uipojuhiopuyg8u9i[ko;lmjilkoh;"

@app.route('/')
def hello_form():
    form = Registration()
    return render_template('registration.html',form=form)


@app.route('/registration',methods=['GET','POST'])

def RegisterUser():
    form = Registration()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('registration.html',form=form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('registration.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)