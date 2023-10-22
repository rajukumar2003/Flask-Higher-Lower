from flask import Flask, request, render_template
import random

app = Flask(__name__)

random_num = random.randint(0, 9)


@app.route('/')
def guess():
    return render_template('index.html')


# Python Decorator Function
def text_color(func):
    def wrapper():
        return f"<h1 style='color:violet'> {func()} </h1>"
    return wrapper


@app.route('/guess')
@text_color
def guess_num():
    user_num = int(request.args.get('user_guess'))
    if user_num == random_num:
        return '<em> You found me!! </em>'\
                '<br>'\
                '<img src= "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif",width=200>'

    elif user_num < random_num:
        return f'<em>{user_num} is low, Try Again!</em>' \
               '<br>' \
               '<img src= "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif",width=200>'\
                '<button onclick="location.href=\'/\'"  \
                style="background-color: #4CAF50; color: white; border: none; padding: 10px 20px; \
                text-align: center; text-decoration: none; display: inline-block; font-size: 16px; \
                margin: 4px 2px; cursor: pointer;">Try Again</button>'

    else:
        return f'{user_num} is high, Try Again!'\
                '<br>' \
               '<img src= "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif",width=200>'\
                '<button onclick="location.href=\'/\'"  \
                style="background-color: #4CAF50; color: white; border: none; padding: 10px 20px; \
                text-align: center; text-decoration: none; display: inline-block; font-size: 16px; \
                margin: 4px 2px; cursor: pointer;">Try Again</button>'



if __name__ == '__main__':
    app.run(debug=True)
