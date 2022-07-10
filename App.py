from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)

@app.route ('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html',my_name=name)
    

@app.route('/home/<value>')
def home(value):
    return f"Hello {value}"
    #return redirect(url_for('index'))


@app.route('/new', methods=['POST'])
def new_value():
    data = request.get_json()
    data['body'] = "Mayeesha Maimuna"
    return data
    

if __name__ == "__main__":
    app.run()