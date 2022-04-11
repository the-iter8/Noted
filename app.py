from flask import Flask, redirect, request
from flask import render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def form():
    f = open("test.txt","a+")
    if request.method == 'POST':
        content = request.form['content']
        try:
            f.write(content + "\n")
            return redirect('/')
        except:
            return "There was an issue adding the text. "

    else:
        f = open("test.txt","r")
        tasklist = f.readlines()
        
        return render_template("index.html", tasklist = tasklist)

# Just a way to save files 
'''
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
       f = request.files['file']
       f.save(secure_filename(f.filename))
       return 'file uploaded successfully'
'''


@app.route('/delete}')
def delete():
    return "Hello world. "

if __name__ == '__main__':
    app.run(debug = True)