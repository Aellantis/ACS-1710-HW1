from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/desserts/<users_desserts>')
def favorite_dessert(users_desserts):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_desserts}, too!'

@app.route('/multiply/<number1>/<number2>')
def multiply_numbers(number1,number2):
    return f"{number1} times {number2} is {int(number1)* int(number2)}!"

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    n = int(n)
    return " ".join([word for _ in range(n)])


if __name__ == '__main__':
    app.run(debug=True)
