from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, SubmitField
from wtforms import DecimalField
from flask_wtf import FlaskForm
from wtforms.fields import DecimalField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class DiagnosisForm(FlaskForm):
    diagnosis = SelectField('Diagnosis',choices=[('Schizophrenia','Schizophrenia'), ('Depression','Depression')])
    submit = SubmitField('Submit')

class DepressionDrugForm(FlaskForm):
    drug = SelectField('Prescribed Drug', choices=[('Citalopram',
        'Citalopram'), ('Escitalopram', 'Escitalopram'), ('Fluoxetine',
        'Fluoxetine'), ('Fluvoxamine', 'Fluvoxamine'), ('Paroxetine',
        'Paroxetine'), ('Sertraline', 'Sertraline'),
        ('Duloxetine','Duloxetine'), ('Venlafaxine', 'Venlafaxine'),
        ('Desvenlafaxine', 'Desvenlafaxine'), ('Duloxetine', 'Duloxetine'),
        ('Milnacipran','Milnacipran'), ('Venlafaxine','Venlafaxine'),
        ('Amineptine','Amineptine'), ('Bupropion', 'Bupropion'),
        ('Methylphenidate', 'Methylphenidate'), ('Nomifensine',
            'Nomifensine')])
    submit = SubmitField('Submit')

class SchizophreniaDrugForm(FlaskForm):
    drug = SelectField('Prescribed Drug',
    choices=[('Aripiprazole','Aripiprazole'), ('Clozapine', 'Clozapine'),
    ('Olanzapine', 'Olanzapine'), ('Paliperidone', 'Paliperdone'),
    ('Perospirone', 'Perospirone'), ('Risperidone', 'Risperidone'),
    ('Cariprazine', 'Cariprazine'), ('Quetiapine', 'Quetiapine'), ('Zotepine',
        'Zotepine')])
    submit = SubmitField('Submit')

class SymptomsForm(FlaskForm):
    cognitive_symptoms = DecimalField('Cognitive Symptoms')
    negative_symptoms = DecimalField('Negative Symptoms')
    avolition = DecimalField('Avolition')
    extrapyramidal = DecimalField('Extrapyramidal')
    positive_symptoms_psychosis = DecimalField('Positive Symptoms Psychosis')
    depression = DecimalField('Depression')
    insomnia = DecimalField('Insomnia')
    anxiety = DecimalField('Anxiety')
    weight_gain = DecimalField('Weight Gain')
    apathy = DecimalField('Apathy')
    motivation = DecimalField('Motivation')
    stress = DecimalField('Stress')
    fatigue = DecimalField('Fatigue')
    suicidal_thoughts = DecimalField('Suicidal Thoughts')
    agitation = DecimalField('Agitation')
    submit = SubmitField('Submit')

class ProceedForm(FlaskForm):
    submit = SubmitField('Go')
