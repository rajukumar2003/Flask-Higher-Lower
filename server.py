from flask import Flask, request, render_template
import random

app = Flask(__name__)

random_num = random.randint(0, 9)


@app.route('/')
def guess():
    return render_template('index.html')


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
               '<img src= "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif",width=200>'

    else:
        return f'{user_num} is high, Try Again!'\
                '<br>' \
               '<img src= "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif",width=200>'


if __name__ == '__main__':
    app.run(debug=True)
