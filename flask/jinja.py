from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return '<html><h1>welcome to flask</h1></html>'

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

# @app.route('/submit',methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name']
#         return f"HELLO {name}"
#     return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    if score>=50:
        res='Passed'
    else:
        res='Failed'
    
    return render_template('result.html',result=res)

@app.route('/successres/<int:score>')
def successres(score):
    if score>=50:
        res='Passed'
    else:
        res='Failed'
    
    exp={'score':score,'result':res}

    return render_template('result1.html',result=exp)

@app.route('/successif/<int:score>')
def successif(score):
    
    return render_template('result.html',result=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',result=score)

@app.route('/submit',methods=['GET','POST'])
def submit():
    total=0
    if request.method=='POST':
        science=float(request.form['science'])
        math=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total=(science+math+c+data_science)/4
    else:
        return render_template('getresult.html')

    return redirect(url_for('successres',score=total))

if __name__ == '__main__':
    app.run(debug=True)