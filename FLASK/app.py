#INTEGRATE HTML WITH FLASK
#HTTP VERB GET AND POST

#BUILDING URL DYNAMICALLY
#VARIABLE RULES AND URL BUILDING

from flask import Flask ,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html')

@app.route('/results/<int:marks>')
def results(marks):
    res=""
    if(marks>=50):
        res='success'
    
    else:
        res='fail'
    return redirect(url_for(res,score=marks))

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        cs=float(request.form['cs'])
        dsa=float(request.form['dsa'])

        total_score=(science+maths+cs+dsa)/4
    return redirect(url_for('success',score=total_score))


if __name__=='__main__':
    app.run(debug=True)