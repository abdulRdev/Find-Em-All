import mysql.connector
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import InputRequired, Length

#TOTALPOKEMON = 151

app= Flask (__name__)

#this key is to configure flask application for form!
app.config['SECRET_KEY']='secretkey'

#establishing connection to database
mydb= mysql.connector.connect(
    host="localhost",
    user="Abdul",
    passwd="rootdatabase",
    database="maindatabase"
)

#cursor interacts with mysql server
mycursor= mydb.cursor()

@app.route("/")
def home():
    return render_template("base.html")


class DisplayData (FlaskForm):
    submit = SubmitField("Display all")


@app.route("/display", methods=['GET','POST'])
def display():

    form = DisplayData()
    mycursor.execute("SELECT * FROM POKECHALLENGE")
    allData = mycursor.fetchall()
    if form.is_submitted():
        displayForm=True
        return render_template("display.html", form=form, allData=allData, displayForm=displayForm)
    displayForm=False
    return render_template("display.html", form=form, allData=allData,displayForm=displayForm)



class AddEntry (FlaskForm):
    name = StringField("Pokemon Name", validators=[InputRequired()])
    type = StringField("Pokemon Type", validators=[InputRequired()])
    type2 = StringField("Secondary Type")
    trainer = StringField("Your Name", validators=[InputRequired(), Length(2, 30)])
    submit = SubmitField("Add Pokemon Entry")

@app.route("/add", methods=['GET','POST'])
def add():
    form = AddEntry()
    mycursor.execute("SELECT * FROM POKEGEN1")
    allData= mycursor.fetchall()
    print(allData)
    if form.validate_on_submit():

       if hasBeenEntered(form.name.data, "POKECHALLENGE"):
           flash(form.name.data.upper()+" has already been entered!")
           return render_template("add.html",form=form)

       for row in allData:
            if form.name.data.casefold()==row[1].casefold():
                insertFormula= "INSERT INTO POKECHALLENGE (DexNumber,Pokemon,TypeMain,TypeSec,Adder) VALUES (%s,%s,%s,%s,%s)"
                newEntry=(row[0],row[1],row[2],row[3],form.trainer.data)

                mycursor.execute(insertFormula,newEntry)
                mydb.commit()

                flash(form.name.data.upper()+" was added!")
                return render_template("add.html",form=form)

       flash(form.name.data.upper() + " is not in the list! The Pokemon must be 1st Gen")
       return render_template("add.html",form=form)
    return render_template("add.html",form=form)



class ClearData (FlaskForm):
    submit = SubmitField("Clear all")


@app.route("/clear", methods=['GET','POST'])
def clear():
    form = ClearData()
    if form.is_submitted():
        mycursor.execute("DELETE FROM POKECHALLENGE")
        mydb.commit()
        flash("All previously entred data has been erased.")
    return render_template("Clear.html",form=form)

#to check whether entry has already been entered
def hasBeenEntered(name, table):
    mycursor.execute("SELECT * FROM "+table)
    tableInfo = mycursor.fetchall()
    for row in tableInfo:
        if name.casefold()==row[1].casefold(): #pokemon has already been entered
            return True
    return False

if __name__ == "__main__":
    app.debug=True
    app.run()
