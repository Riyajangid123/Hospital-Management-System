from Database.database import conn,cursor
class Patient:

    def __init__(self):
        self.conn = conn
        self.cursor = cursor

    def add_patients(self, name, age, gender):
        try:
            query="insert into patients (name,age,gender) values (%s,%s,%s)"
            values=(name,age,gender)
            self.cursor.execute(query,values)
            self.conn.commit()
            return True
    

        except Exception as e:
            print(f"Error occurred: {e}")
            return False
    def view_patients(self):

        query="select * from patients"
        self.cursor.execute(query)
        return self.cursor.fetchall()
        
        
    def update_patients(self, patient_id, name, age, gender):
        query="update patients set name=%s,age=%s,gender=%s where patient_id=%s"
        values=(name,age,gender,patient_id)
        self.cursor.execute(query,values)
        self.conn.commit()
        if self.cursor.rowcount>0:
            return True
        return False
    
    def delete_patients(self, patient_id):
        query="delete from patients where patient_id=%s"
        value=(patient_id,)
        self.cursor.execute(query,value)
        self.conn.commit()
        if self.cursor.rowcount>0:
            return True
        return False

    def search_patients(self, name):
        query="select * from patients where name=%s"
        value=(name,)
        self.cursor.execute(query,value)
        return self.cursor.fetchall()