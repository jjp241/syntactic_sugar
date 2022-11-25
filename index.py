from flask import Flask,\
                  render_template,\
                  url_for,\
                  request,\
                  flash,\
                  redirect
import time

from lib.token_authentication import is_token_file_present, get_goldman_token_value

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = "2b3f12f3ef12a6c86b"


# What to do, when we receive GET or POST at index
@app.route('/', methods=['GET', 'POST'])
def index():
   some_text = "Hello World!"
   return render_template('init.html',
                          sample_text=some_text)


@app.route('/test1', methods=['GET'])
def test1():
   return render_template('test1.html')


@app.route('/test2', methods=['GET'])
def test2():
   return render_template('test2.html')

@app.route('/forward', methods=['GET', 'POST'])
def forward():
   print('here')
   if is_token_file_present():
      print('token present')
      token = get_goldman_token_value()
      print('token')
      return render_template('test2.html', token=token)
   else:
      return redirect('/')



if __name__ == "__main__":
   app.run(debug=True)
