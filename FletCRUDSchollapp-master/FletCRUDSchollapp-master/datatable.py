from flet import *
import sqlite3
conn = sqlite3.connect('db/dbone.db',check_same_thread=False)

tb = DataTable(
	columns=[
		DataColumn(Text("actions")),
		DataColumn(Text("name")),
		DataColumn(Text("age")),
		DataColumn(Text("contact")),
		DataColumn(Text("email")),
		DataColumn(Text("address")),
		DataColumn(Text("gender")),
	],
	rows=[]

	)


def showdelete(e):
	try:
		myid = int(e.control.data)
		c = conn.cursor()
		c.execute("DELETE FROM users WHERE id=?", (myid,))
		conn.commit()
		print("success delete")
		# we donot use datacell or cell it conatins only one values like one particular ropw
		tb.rows.clear()	
		calldb()
		tb.update()

	except Exception as e:
		print(e)


id_edit = Text()
name_edit = TextField(label="name")
age_edit = TextField(label="age")
contact_edit = TextField(label="contact")
gender_edit = RadioGroup(content=Column([
		Radio(value="man",label="man"),
        Radio(value="woman",label="woman"),

	]))
email_edit = TextField(label="email")
address_edit = TextField(label="address")


def hidedlg(e):
	dlg.visible = False
	dlg.update()


def updateandsave(e):
	try:
		myid = id_edit.value
		c = conn.cursor()
		c.execute("UPDATE users SET name=?, contact=?, age=?, gender=?, email=?, address=? WHERE id=?", (name_edit.value, contact_edit.value, age_edit.value, gender_edit.value, email_edit.value, address_edit.value, myid))
		conn.commit()
		print("success Edit ")
		tb.rows.clear()	
		calldb()
		dlg.visible = False
		dlg.update()
		tb.update()
	except Exception as e:
		print(e)

dlg = Container(
	bgcolor="blue200",
	padding=10,
			content=Column([
				Row([
				Text("Edit Form",size=30,weight="bold"),
				IconButton(icon="close",on_click=hidedlg),
					],alignment="spaceBetween"),
				name_edit,
				age_edit,
				contact_edit,
				Text("Select Gender",size=20,weight="bold"),
				gender_edit,
				email_edit,
				address_edit,
				ElevatedButton("Update",on_click=updateandsave)

				])
)




def showedit(e):
	data_edit = e.control.data
	id_edit.value = data_edit['id']
	name_edit.value = data_edit['name']
	age_edit.value = data_edit['age']
	contact_edit.value = data_edit['contact']
	gender_edit.value = data_edit['gender']
	email_edit.value = data_edit['email']
	address_edit.value = data_edit['address']

	dlg.visible = True
	dlg.update()



#this is the function which they calls to display all the values in the database
def calldb():
	c = conn.cursor()
	c.execute("SELECT * FROM users")
	#users here is fetching all the data from the database in here
	users = c.fetchall()
	#this code here is fecting all tyhe values from the database
	print(users)
	if not users == "":
	#in here the values are not empty then
		keys = ['id', 'name', 'contact', 'age', 'gender', 'email', 'address']
		result = [dict(zip(keys, values)) for values in users]
	#in here keys are values are zipping together to get a values for the
		for x in result:
			#tb is the database table in here
			tb.rows.append(
				#Each DataRow in this table would represent a single customer, containing their specific name, age, and email address values.
				#it is usually from the database
				DataRow(
					#cell holds the entire row value
                    cells=[
						#here datacell takes only one value from that row
                        DataCell(Row([
                        	IconButton(icon="create",icon_color="blue",
                        		data=x,

                        		on_click=showedit

                        		),

                        	IconButton(icon="delete",icon_color="red",
                        		data=x['id'],
                        	on_click=showdelete

                        		),
                        	])),
                        DataCell(Text(x['name'])),
                        DataCell(Text(x['age'])),
                        DataCell(Text(x['contact'])),
                        DataCell(Text(x['email'])),
                        DataCell(Text(x['address'])),
                        DataCell(Text(x['gender'])),
                    ],
                ),

		)


calldb()





dlg.visible = False
mytable = Column([
	dlg,
	Row([tb],scroll="always")
	])

# he code creates a Row container.Inside the Row, it includes the tb element within a list.
# This ensures that even though there's only one element, Flet treats it as a proper item within the horizontal layout.
# The scroll="always" property tells Flet to enable horizontal scrolling within the Row.
# This means if the table content (including its columns and data) overflows the available width,
# the user can horizontally scroll to view the entire table.