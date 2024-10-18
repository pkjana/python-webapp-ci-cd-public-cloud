from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = "Hello, World from Flask!"
    return render_template('index.html', message=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = ''
    if request.method == 'POST':
      # Perform login authentication
      username = request.form['username']
      password = request.form['password']
      # Add your authentication logic here
      if username == 'admin' and password == 'password':
        return 'Login successful!'
      else:
        return 'Invalid username or password'

    # If the request method is GET, render the login template
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
