from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}, too!'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f'The {adjective} {noun} ate too much dessert!'

@app.route('/multiply/<number1>/<number2>')
def multiply_numbers(number1,number2):
    return f"{number1} times {number2} is {int(number1)* int(number2)}!"

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    if n.isdigit():
        n = int(n)
        return " ".join([word for _ in range(n)])
    else:
        return "Invalid input. Please enter a number for n."


@app.route('/dicegame')
def dicegame():
    n = random.randint(1,6)
    if n < 6:
        return f"You rolled a {n}. You lost!"
    return f"You rolled a 6. You won!"

####################
if __name__ == '__main__':
    app.run(debug=True)
