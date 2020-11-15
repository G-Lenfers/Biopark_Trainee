# -*- coding: utf-8 -*-
"""
Programa de Trainee Biopark

Código desenvolvido para receber solicitação de agendamento de envio de
comunicação.

Leia as informações apresentadas no arquivo READ_ME.txt para saber mais sobre
esta aplicação, suas funcionalidades e instruções de uso.

Autor: Guilherme Lenfers Dornelles
Data: 15/11/2020
"""

#Import the required packages
from flask import (Flask,             #Server handling
                    render_template,  #For HTML templates
                    request,          #Allow posts of data
                    redirect)         #redirect links
from flask_sqlalchemy import SQLAlchemy #Link with database
import datetime         #Dates and time manipulations

#Create our application
app = Flask(__name__)

####################
###   Database   ###
####################

#We are using sqlite temporarily
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedules.db'
#Creating our database
db = SQLAlchemy(app)

#Structure the data in our database
class SchedulePlatform(db.Model):

    #Defining unique id
    #primary_key means that this id will be the main distinguisher between rows
    id = db.Column(db.Integer, primary_key=True)

    #Date time initially will be string type
    #Nullable equals false means that it is a required field
    date_time =db.Column(db.DateTime, nullable=False)

    #Addressee (limit of 100 characters)
    addressee = db.Column(db.String(100), nullable=False)

    #message
    message = db.Column(db.Text, nullable=False)

    #Defining what we print out when we call data from database
    def __repr__(self):
        return 'Agendamento' + str(self.id)


#If it is your first run, need create the database files
#Use the following commands (must be at 'Biopark' folder's directory):
#from app import db
#db.create_all()
#It goes through our model and create the database based on our configuration


##########################
###   Our app routes   ###
##########################

#Our home page
@app.route('/home')
def homepage():
    #Our Home Page
    return render_template('home.html')

#Define our schedule route
@app.route('/schedule', methods = ['GET','POST'])
def agenda():
    #we add a check here
    #If we fill the form and hit submit button, add it to the database
    #Need to import request package for this
    if request.method == 'POST':

        #read our data from form filled out by user
        schedule_year =  request.form['year']      #0
        schedule_month = request.form['month']     #1
        schedule_day = request.form['day']         #2
        schedule_hour = request.form['hour']       #3
        schedule_minutes = request.form['minutes'] #4
        schedule_addressee = request.form['addressee']
        schedule_message = request.form['message']

        #Joining date values into a single list
        schedule_date_str = [schedule_year,
                            schedule_month,
                            schedule_day,
                            schedule_hour,
                            schedule_minutes]

        #But datetime function requires int type
        schedule_date_int = [int(i) for i in schedule_date_str]

        #And finally converting it to datetime format
        schedule_date = datetime.datetime(schedule_date_int[0],
                                        schedule_date_int[1],
                                        schedule_date_int[2],
                                        schedule_date_int[3],
                                        schedule_date_int[4])


        #Then we create a variable containing all the required information
        new_post = SchedulePlatform(date_time = schedule_date,
                                    addressee = schedule_addressee,
                                    message = schedule_message)

        #Saving data into our database
        db.session.add(new_post)

        #Take whatever it is in our session and commit it to the database
        db.session.commit()

        #After we hit submit button, redirect to
        return redirect('/schedule')
    else:
        #Get all of Schedules from database
        all_schedules = SchedulePlatform.query.order_by(SchedulePlatform.id).all()

        #render the web page with all our schedule requests
        return render_template('schedule.html', schedules = all_schedules)

    return render_template('schedule.html', schedules = all_schedules)

#Define our web page for posting new schedules
@app.route('/schedule/new')
def agenda_novo():

    #If we have just arrived on the web page for posting, we are GETting
    return render_template('new_schedule.html')


#Defining a route for delete function
@app.route('/schedule/delete/<int:id>')
def delete(id):

    #getor404: if it doesn't exist, we don't want it to break
    #Assigning our schedule we want to delete
    schedule_to_delete = SchedulePlatform.query.get_or_404(id)

    #And delete it from database
    db.session.delete(schedule_to_delete)
    db.session.commit()

    #Return to the previous page
    return redirect('/schedule')


#If running this file directly, it's good practice to turn on debug mode
if __name__ == "__main__":
        app.run(debug=True)
