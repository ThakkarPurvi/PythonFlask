from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = '2121212121212121212121'

class BasicForm(FlaskForm):
    submit = SubmitField('Add Name')
    date_of_birth = DateField('Date of Birth', format='%d/%m/%Y')
    number = IntegerField('Favourite Number')
    food = SelectField('Favourite Food',
        choices=[
            ('pizza', 'Pizza'),
            ('chilli', 'Chilli'), 
            ('spaghetti', 'Spaghetti')
            ]
        )
    submit = SubmitField('Generate Username')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
          message = f"{form.number.data}{form.food.data}{form.date_of_birth.data}"

    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')