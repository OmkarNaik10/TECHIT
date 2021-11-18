#SJSU CMPE 138 Fall 2021 TEAM3

#file that establishes default data
import sqlite3
from tkinter.constants import NONE
from passwordHash import hashPassword
import logging

logging.basicConfig(filename='TECHitLog.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(lineno)d:%(funcName)s:%(message)s')

connection = sqlite3.connect('login.db')
connection.execute("PRAGMA foreign_keys = 1")
cursor = connection.cursor()

# added two technicians, one DBA, one engineer, one ticket, and one project managed by one manager

def addDefDepartments():
    cursor.execute("INSERT INTO Department VALUES (?,?,?)",(1,'Engineering',25))
    cursor.execute("INSERT INTO Department VALUES (?,?,?)",(2,'Science',50))
    cursor.execute("INSERT INTO Department VALUES (?,?,?)",(3,'Research',30))
    cursor.execute("INSERT INTO Department_Locations Values (?,?,?)",(1,'Engineering','San Jose'))
    cursor.execute("INSERT INTO Department_Locations Values (?,?,?)",(2,'Science','San Fransisco'))
    cursor.execute("INSERT INTO Department_Locations Values (?,?,?)",(3,'Research','Mountain View'))
    cursor.execute("INSERT INTO Department_Phone_Number Values (?,?,?)",(1,'Engineering','4087823583'))
    cursor.execute("INSERT INTO Department_Phone_Number Values (?,?,?)",(2,'Science','401419847'))
    cursor.execute("INSERT INTO Department_Phone_Number Values (?,?,?)",(3,'Research','408362923'))

def addDefProjects():
    cursor.execute("INSERT INTO Project Values (?,?,?)",('Valk','Jetpack',3))
    cursor.execute("INSERT INTO Project Values (?,?,?)",('AI','Car path detection',3))
    cursor.execute("INSERT INTO Project Values (?,?,?)",('Gold','Research into gold',3))

def addDefAdmin():
    cursor.execute("INSERT INTO EMPLOYEE Values (?,?,?,?,?,?,?,?,?,?)",('Joe','Smith',30,1,'JOEY',hashPassword('password123'),'1','Engineering','07/06/2014',None))
    cursor.execute("INSERT INTO Database_Administrator Values (1)")
    logging.info('Registration: {} {} ({}) has been added as {} to database '.format('Joe','Smith','JOEY','DBA',))
    

def addDefEngineer():
    cursor.execute("INSERT INTO Employee Values (?,?,?,?,?,?,?,?,?,?)",('Anna','Gram',23,2,'Anny',hashPassword('123456789'),'1','Engineering','04/05/2015',None))
    cursor.execute("INSERT INTO Employee Values (?,?,?,?,?,?,?,?,?,?)",('Steve','Job',23,10,'steve123',hashPassword('abcd'),'1','Engineering','09/05/2015',None))
    cursor.execute("INSERT INTO Engineer Values (?,?)",(2,'AI'))
    cursor.execute("INSERT INTO Engineer Values (?,?)",(10,None))
    logging.info('Registration: {} {} ({}) has been added as {} to database '.format('Anna','Gram','Anny','Engineer',))
    logging.info('Registration: {} {} ({}) has been added as {} to database '.format('Steve','Job','steve123','Engineer',))
    
def addDefManager():
    cursor.execute("INSERT INTO Employee Values (?,?,?,?,?,?,?,?,?,?)",('Hugh','Mungus',25,3,'Huge15',hashPassword('mypassword'),'1','Engineering','09/02/2015',None))
    cursor.execute("INSERT INTO Dept_manager Values (3)")
    logging.info('Registration: {} {} ({}) has been added as {} to database '.format('Hugh','Mungus','Huge15','Manager',))

def addDefTechnicians():
    cursor.execute("INSERT INTO Employee Values (?,?,?,?,?,?,?,?,?,?)",('Kenny','Ant',28,4,'KAnt',hashPassword('thisismypw'),'1','Engineering','08/04/2014',None))
    cursor.execute("INSERT INTO Technician Values (4)")
    cursor.execute("INSERT INTO Level_A_Technician Values (4)")
    logging.info('Registration: {} {} ({}) has been added as {} to database '.format('Kenny','Ant','KAnt','Technician Level A',))
    cursor.execute("INSERT INTO Employee Values (?,?,?,?,?,?,?,?,?,?)",('Timmy','Turn',28,5,'TimT',hashPassword('p@ssword101'),'1','Engineering','11/23/2015',None))
    cursor.execute("INSERT INTO Technician Values (5)")
    cursor.execute("INSERT INTO Level_B_Technician Values (5)")
    logging.info('Registration: {} {} ({}) has been added as {} to database '.format('Timmy','Turn','TimT','Technician Level B',))
    
def addDefTicket():
    cursor.execute("INSERT INTO Ticket Values (?,?,?,?,?,?,?,?,?)",(1,'Open','A','high','Conflict in accesing','Engineering',2,None,'11/9/2021')) 
    cursor.execute("INSERT INTO Level_A_Ticket Values (?,?)",(1,None))
    logging.info('Engineer with ID {} added ticket with ID {}'.format('2','1'))   
    

def addAllData():
    addDefDepartments()
    addDefManager()
    addDefProjects()
    addDefAdmin()
    addDefEngineer()
    addDefTechnicians()
    addDefTicket()
    
    connection.commit()
    connection.close()