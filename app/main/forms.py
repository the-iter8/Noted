from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class ListForm(FlaskForm):
    # HTML tag parameters for content field
    content_html_params = {'id':'content',
                           'class':'form-input',
                           'placeholder':'New Note'}

    # HTML tag parameters for submit field
    submit_html_params = {'id':'add-task-btn',
                          'value':'add task'}

    content = StringField(validators=[DataRequired()],
                          render_kw=content_html_params)

    submit = SubmitField(render_kw=submit_html_params)

class LoginForm(FlaskForm):
    email_id = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired(), Length(8)])
    submit = SubmitField()
