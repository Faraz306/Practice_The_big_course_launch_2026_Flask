from flask import Flask, render_template, request

yf_app = Flask(__name__)


@yf_app.route('/', methods=['GET', 'POST'])
def home():
    user = None
    if request.method == 'POST':
        print("--- BUTTON CLICKED! ---")  # Look for this in PyCharm!
        email = request.form.get('input-1')
        password = request.form.get('input-2')

        if email and password:
            user = {"email": email, "password": password}
            print(f"Data Captured: {email}")

    return render_template('home.html', user=user)


# The other simple routes
@yf_app.route('/about/')
def about(): return render_template('about.html')


@yf_app.route('/contact/')
def contact(): return render_template('contact.html')


@yf_app.route('/learnpython/')
def learnpython(): return render_template('learnpython.html')


if __name__ == "__main__":
    yf_app.run(debug=True)