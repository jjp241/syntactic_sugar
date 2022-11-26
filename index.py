from flask import Flask,\
                  render_template,\
                  url_for,\
                  request,\
                  flash,\
                  redirect

import json

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = "2b3f12f3ef12a6c86b"

# What to do, when we receive GET or POST at index
@app.route('/', methods=['GET', 'POST'])
def index():
   some_text = "Hello World!"
   return render_template('init.html',
                          sample_text=some_text)

@app.route('/login_form', methods=['GET', 'POST'])
def login_form():
   if request.method == 'POST':    
      json_result = {
         "token-id": "test1",
         "first_name": request.form["first_name"],
         "last_name": request.form["last_name"],
         "email": request.form["email"],
         "uni_name": request.form["university"],
         "major": request.form["major"],
         "sex": request.form["sex"]
      }

      with open('db.json', 'r') as open_file:
         json_object = json.load(open_file)
         print(json_object)
         json_object["user_data"].append(json_result)
         
         with open('db.json', 'w') as db_file:
            json.dump(json_object, db_file, indent=4)

   return render_template('login_form.html')

@app.route('/test1', methods=['GET'])
def test1():
   return render_template('test1.html')


@app.route('/test2', methods=['GET'])
def test2():
   return render_template('test2.html')


if __name__ == "__main__":
   app.run(debug=True)
