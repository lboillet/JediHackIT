import sqlite3

db = sqlite3.connect('db/MercyCorps4.db')

# Get a cursor object
cursor = db.cursor()


with open("test_data/Schools_test_data.csv", "r") as mySchool:
    
    for line in mySchool:
        id, name, address, phone = line.split(",")
        
        cursor.execute('''INSERT INTO School(id, name, address, phone)
                  VALUES(?,?,?,?)''', (id, name, address, phone))
                  
        print(' %s, %s, %s, %s'% (id, name, address, phone))

        
with open("test_data/Person_test_data.csv", "r") as myPerson:
    
    for line in myPerson:
        firstname,lastname,nationalid,id,phone,email,address, att_percent, payment = line.split(",")
        
        cursor.execute('''INSERT INTO Person(firstname, lastname, nationalid, id, phone, email, address, att_percent, payment)
                  VALUES(?,?,?,?,?,?,?,?,?)''', (firstname, lastname, nationalid, id, phone, email, address, att_percent, payment))
                  
        print(' %s, %s, %s, %s, %s, %s, %s, %s, %s '% (firstname, lastname, nationalid, id, phone, email, address, att_percent, payment))        
        

with open("test_data/Legal_Rep_test_data.csv", "r") as myLegal_Rep:
    
    for line in myLegal_Rep:
        id,personid,studentid = line.split(",")
        
        cursor.execute('''INSERT INTO Legal_rep('id','personid','studentid')
                  VALUES(?,?,?)''', (id,personid,studentid))
                  
        print(' %s, %s, %s'% (id,personid,studentid))
    

with open("test_data/Students_test_data.csv", "r") as myStudent:
    
    for line in myStudent:
        id,personid,legal_rep = line.split(",")
        
        cursor.execute('''INSERT INTO Student('id','personid','legal_rep')
                  VALUES(?,?,?)''', (id,personid,legal_rep))
                  
        print(' %s, %s, %s'% (id,personid,legal_rep))
        
    


  

db.commit()

db.close()
