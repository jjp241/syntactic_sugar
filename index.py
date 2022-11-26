from flask import Flask,\
                  render_template,\
                  url_for,\
                  request,\
                  flash,\
                  redirect


app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = "2b3f12f3ef12a6c86b"

# What to do, when we receive GET or POST at index
@app.route('/', methods=['GET', 'POST'])
def index():
   some_text = "Hello World!"
   return render_template('init.html',
                          sample_text=some_text)

@app.route('/login_form', methods=['GET'])
def login():
   return render_template('login_form.html')

@app.route('/test1', methods=['GET'])
def test1():
   return render_template('test1.html')


@app.route('/test2', methods=['GET'])
def test2():
   return render_template('test2.html')


if __name__ == "__main__":
   app.run(debug=True)
