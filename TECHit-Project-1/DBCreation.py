#SJSU CMPE 138 Fall 2021 TEAM3
import sqlite3
import sys
#from sqlite3.dbapi2 import Cursor


def BuildDB():
	# connection and cursor
	connection = sqlite3.connect('login.db')
	connection.execute("PRAGMA foreign_keys = 1")
	cursor = connection.cursor()


	## Creating tables
	#Might want to add constraints to make sure employees cant manage themselves, etc...

	# Creating department and department related tables
	command1 = """CREATE TABLE IF NOT EXISTS Department (
		d_no INTEGER,
		d_name TEXT,
		number_employees INTEGER,
		Primary KEY (d_no,d_name)
	);"""
	cursor.execute(command1)

	command2 = """CREATE TABLE IF NOT EXISTS Department_Locations (
		d_no INTEGER,
		d_name TEXT,
		locations TEXT PRIMARY KEY,
		FOREIGN KEY (d_no,d_name)
			REFERENCES Department (d_no,d_name)
				ON UPDATE CASCADE
				ON DELETE CASCADE
	);"""
	cursor.execute(command2)

	command3 = """CREATE TABLE IF NOT EXISTS Department_Phone_Number (
		d_no INTEGER NOT NULL,
		d_name TEXT NOT NULL,
		phone_number TEXT PRIMARY KEY,
		FOREIGN KEY (d_no,d_name)
			REFERENCES Department (d_no,d_name)
				ON UPDATE CASCADE
				ON DELETE CASCADE
	);"""
	cursor.execute(command3)

	# Creating employee and employee related tables
	command4 = """CREATE TABLE IF NOT EXISTS Employee  (
		F_name TEXT NOT NULL,
		L_name TEXT NOT NULL,
		age INTEGER NOT NULL,
		e_id INTEGER Primary Key,
		username TEXT Unique,
		password TEXT NOT NULL,
		d_no INTEGER NOT NULL,
		d_name TEXT NOT NULL,
		start_date TEXT NOT NULL,
		db_authorized_id INTEGER,
		FOREIGN KEY (db_authorized_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE SET NULL
   
		FOREIGN KEY (d_no,d_name)
		REFERENCES Department (d_no,d_name)
			ON UPDATE CASCADE
			ON DELETE CASCADE
		
	);"""
	cursor.execute(command4)

	command5 = """CREATE TABLE IF NOT EXISTS Dept_manager (
		m_id Integer,
		FOREIGN KEY (m_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE CASCADE
	);
	"""
	cursor.execute(command5)

	command6 = """CREATE TABLE IF NOT EXISTS Dept_employee (
		emp_id Integer,
		m_id Integer,
		FOREIGN KEY (emp_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE CASCADE
		FOREIGN KEY (m_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE SET NULL
	);"""
	cursor.execute(command6)

	command7 = """CREATE TABLE IF NOT EXISTS Engineer (
		engr_id Integer,
		proj_name TEXT,
		FOREIGN KEY (engr_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE CASCADE
		FOREIGN KEY (proj_name)
		REFERENCES Project (proj_name)
			ON UPDATE CASCADE
			ON DELETE SET NULL
	);"""
	cursor.execute(command7)

	command8 = """CREATE TABLE IF NOT EXISTS Technician (
		tech_id Integer,
		FOREIGN KEY (tech_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE CASCADE
	);"""
	cursor.execute(command8)

	command9 = """CREATE TABLE IF NOT EXISTS Database_Administrator (
		dba_id INTEGER, 
		FOREIGN KEY (dba_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE CASCADE
	);"""
	cursor.execute(command9)

	command10 = """CREATE TABLE IF NOT EXISTS Level_A_Technician (
		techA_id INTEGER,
		FOREIGN KEY (techA_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE CASCADE
	);"""
	cursor.execute(command10)

	command11 = """CREATE TABLE IF NOT EXISTS Level_B_Technician (
		techB_id Integer,
		FOREIGN KEY (techB_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE CASCADE
	);"""
	cursor.execute(command11)

	command12 = """CREATE TABLE IF NOT EXISTS Salaried_Employee (
		e_id Integer,
		Salary REAL ,
		FOREIGN KEY (e_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE CASCADE
	);"""
	cursor.execute(command12)

	command13 = """CREATE TABLE IF NOT EXISTS Hourly_Employee (
		e_id Integer,
		Payscale REAL ,
		FOREIGN KEY (e_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE CASCADE
	);"""
	cursor.execute(command13)

	# Creating project table
	command14 = """CREATE TABLE IF NOT EXISTS Project (
		proj_name TEXT PRIMARY KEY, 
  		description TEXT NOT NULL,
		manager_id INTEGER,
  
		FOREIGN KEY (manager_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE SET NULL
	);"""
	cursor.execute(command14)

	# Creating Ticket related tables
	#Should there be foreign key to department here??
	command15 = """CREATE TABLE IF NOT EXISTS Ticket (
		t_id INTEGER PRIMARY KEY AUTOINCREMENT,
		status TEXT NOT NULL,
		level TEXT NOT NULL,
		priority TEXT NOT NULL,
		description TEXT NOT NULL,
		department TEXT NOT NULL,
		engr_id Integer,
		tech_id Integer,
		submitted_on TEXT NOT NULL,
		FOREIGN KEY (engr_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE SET NULL,
		FOREIGN KEY (tech_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE SET NULL
	);"""
	cursor.execute(command15)

	command16 = """CREATE TABLE IF NOT EXISTS Level_A_Ticket (
		ticketA_id Integer,
		techA_id Integer,
		FOREIGN KEY (ticketA_id)
		REFERENCES Ticket (t_id)
			ON UPDATE CASCADE
			ON DELETE CASCADE,
		FOREIGN KEY (techA_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE SET NULL
	);"""
	cursor.execute(command16)

	command17 = """CREATE TABLE IF NOT EXISTS Level_B_Ticket (
		ticketB_id Integer,
		techB_id Integer,
		FOREIGN KEY (ticketB_id)
		REFERENCES Ticket (t_id)
			ON UPDATE CASCADE
			ON DELETE CASCADE,
		FOREIGN KEY (techB_id)
		REFERENCES Employee (e_id)
			ON UPDATE CASCADE
			ON DELETE SET NULL
	);"""
	cursor.execute(command17)


	connection.commit()
	connection.close()