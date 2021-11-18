#SJSU CMPE 138 Fall 2021 TEAM3

#This works by hashing the password combined with a salt.
#The salt generated is random. 
#So a password is not always hashed to the same value. 
#But how the verification works is bcrypt gets the salt from the stored hashed password and uses that salt to the user entered password suring and hashes it.
#So now the passwords should match.

import bcrypt
#This function is to hash the password entered by the user during registration. The hashed password is needed to be stored in the database.
def hashPassword(password):
	password_bytes=password.encode() #encoding the password string to bytes
	salt = bcrypt.gensalt(14) #generating the salt to use with the password
	password_hash_bytes = bcrypt.hashpw(password_bytes, salt) #hashing the combination of password and salt usign bcrypt
	password_hash = password_hash_bytes.decode() #converting the password bytes to string
	return password_hash

#This function is to verify the password entered by the user during login
def verifyPassword(password,hashed_password):
	password_bytes = password.encode() #encode the password string to bytes
	hash_bytes = hashed_password.encode() #encode the hashed password stored in the database to bytes
	does_match = bcrypt.checkpw(password_bytes, hash_bytes) #check if both the above passwords match
	return does_match