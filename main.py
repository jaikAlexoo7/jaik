import flet
from flet import *
# IMPORT YOU CREATE TABLE 
from myaction import create_table
from datatable import mytable,tb,calldb
import sqlite3
conn = sqlite3.connect("db/dbone.db",check_same_thread=False)

def main(page:Page):

# AND RUN SCRIPT FOR CREATE TABLE WHEN FLET FIRST RUN
#1stly we create database in here
	create_table()

	page.scroll = "auto"

	def showInput(e):
		inputcon.offset = transform.Offset(0,0)
		page.update()
#this will show the inputcon here inputcon is a card item in here


	def hidecon(e):
		inputcon.offset = transform.Offset(2,0)
		page.update()
#this will hide the inputcon card in here


	def savedata(e):
		try:
# INPUT TO DATABASE
			c = conn.cursor()
			c.execute("INSERT INTO users (name,age,contact,email,address,gender) VALUES(?,?,?,?,?,?)",(name.value,age.value,contact.value,email.value,address.value,gender.value))
			conn.commit()
			print("success")

# AND SLIDE RIGHT AGAIN IF FINAL INPUT SUUCESS
			inputcon.offset = transform.Offset(2,0)

# ADD SNACKBAR IF SUCCESS INPUT TO DATABASE

#it is a notification message that appear briefly at the bottom screen to provide feedback to the user below line is the creation o
#of the snack bar in the app
			page.snack_bar = SnackBar(
				Text("success INPUT"),
				bgcolor="green"
				)
#this line here shows the visible of snack bar in here
			page.snack_bar.open = True


# i donot clearly knows this code but refresh the page and the database in here
# REFRESH TABLE
			tb.rows.clear()
#this line in here shows the existing values in the database in here
			calldb()
			tb.update()
			page.update()


		except Exception as e:
			print(e)

#CREATE FIELD FOR INPUT
#IT CREATES THE tables input for the database in here
	name = TextField(label="name")
	age = TextField(label="age")
	contact = TextField(label="contact")
	email = TextField(label="email")
	address = TextField(label="address")
	gender = RadioGroup(content=Column([
		Radio(value="man",label="man"),
		Radio(value="woman",label="woman")
		]))

	# CREATE MODAL INPUT FOR ADD NEW DATA 
	inputcon = Card(
		# ADD SLIDE LEFT EFFECT
		# on calling the card this card would appear from the side
		offset = transform.Offset(2,0),
       # it is the design how card would appear in the front of the page
		animate_offset = animation.Animation(600,curve="easeIn"),
		elevation=30,

#the UI element from its current position(the offset) over a duration of 600  milliseconds.The movement follows an "easeIn"
# curve, starting slowly and accelerating towards the end.Simultaneously, the element's elevation is set to 30,
# potentially creating a shadow effect that might enhance the visual appeal of the animation

		content=Container(
			content=Column([
				Row([
				Text("Add new data",size=20,weight="bold"),
				IconButton(icon="close",icon_size=30,
				on_click=hidecon
					),
					]),
				name,
				age,
				contact,
				email,
				gender,
				address,
				FilledButton("save data",
				on_click=savedata
					)

			])

		)

	)


	page.add(
#column is used to arrange the element one above another so Text would come at the top
#the button below it then comes the button

	Column([
		Text("SCHO0L APP",size=30,weight="bold"),
		ElevatedButton("add new data",
		on_click=showInput
		),
		mytable,
		# AND DIALOG FOR ADD DATA
		inputcon 


		# NOTICE IF YOU ERROR
		# DISABLE import Datatable like this
		])
		)

flet.app(target=main)
