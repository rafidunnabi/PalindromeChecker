from flask import Flask, redirect, url_for, request, render_template
from sklearn.neighbors import KNeighborsClassifier
import pickle

app = Flask(__name__)



@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/', defaults={'result': "Unavailable!"})
@app.route('/<result>')
def mainpage(result):
    return render_template("index.html", result = result)


@app.route('/submit',methods = ['GET'])
def submit():
    if request.method == 'GET':
        n1 = request.args['N1']
        num = int(n1)
        temp = num       
        
        rev=0
        while (num>0) :
            dig=num%10
            rev=rev*10+dig
            num=num//10
    
        if (temp == rev):
            ans =  str(n1) + " is Palindrome"
        else:
            ans = str(n1) + " is not Palindrome"  

        return redirect(url_for('mainpage',result = ans))
    else:
        return redirect(url_for('mainpage',result = "Something went wrong!"))

if __name__ == '__main__':
    app.run()
