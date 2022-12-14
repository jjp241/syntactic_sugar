from flask import Flask,\
                  render_template,\
                  url_for,\
                  request,\
                  flash,\
                  redirect

import json

from lib.token_authentication import is_token_file_present, get_goldman_token_value

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = "2b3f12f3ef12a6c86b"

# mock user token to just global variable
session_user_token = None

#collect user analytics data of which teams they are viewing
def collect_data(team):
   json_result = {
         "token-id": session_user_token,
         "team": team
      }

   with open('db.json', 'r') as open_file:
      json_object = json.load(open_file)
      json_object["user_analytics_data"].append(json_result)
      
      with open('db.json', 'w') as db_file:
         json.dump(json_object, db_file, indent=4)

   return

# What to do, when we receive GET or POST at index
@app.route('/', methods=['GET', 'POST'])
def index():
   global session_user_token

   if request.method == 'POST':    
      # Check if physical token is present, if not try to read from text input
      if is_token_file_present():
         print('Token present!')

         token_id = get_goldman_token_value()
         session_user_token = token_id
         print(token_id)
         return redirect('/login_form')
      else:
         token_id = request.form['user-token']
         if token_id and len(token_id) == 8:
            session_user_token = token_id
            return redirect('/login_form')
         
      print('No token found!')
      return redirect('/')
   else:
      return render_template('welcome_page.html')

   
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
         "sex": request.form["sex"],
         "event": "Job fair University of Warsaw"
      }

      with open('db.json', 'r') as open_file:
         json_object = json.load(open_file)
         json_object["user_data"].append(json_result)
         
         with open('db.json', 'w') as db_file:
            json.dump(json_object, db_file, indent=4)

      return redirect('/choose_team')

   return render_template('login_form.html', user_token=session_user_token)


@app.route('/team_content', methods=['GET'])
def team_content():
   collect_data("quant")
   return render_template('team_content.html')

@app.route('/choose_team', methods=['GET'])
def choose_team():
   collect_data("quant")
   return render_template('choose_team.html')

@app.route('/admin_panel', methods=['GET'])
def admin_panel():
   with open('db.json', 'r') as open_file:
         json_object = json.load(open_file)

   return render_template('admin_panel.html', users_data=json_object)

@app.route('/quant_quiz', methods=['GET'])
def quant_quiz():
   collect_data("quant")
   return render_template('quant_quiz.html')

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
   return render_template('leaderboard.html')

if __name__ == "__main__":
   app.run(debug=True)
