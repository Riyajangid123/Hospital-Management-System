from Database.database import conn,cursor
class Doctor:
    def __init__(self):
        self.conn=conn
        self.cursor=cursor
    
    def add_doctor(self, name, specialization):
        try:
            query="insert into doctors (name,specialization) values (%s,%s)"
            values=(name,specialization)
            self.cursor.execute(query,values)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
        
    
    def view_doctors(self):
        query="select * from doctors"
        self.cursor.execute(query)
        return self.cursor.fetchall()
        
    def update_doctors(self, doctor_id, name, specialization):
        self.cursor.execute(
            "SELECT * FROM doctors WHERE doctor_id=%s",
            (doctor_id,)
        )

        if not self.cursor.fetchone():
            return False
        query="update doctors set name=%s,specialization=%s where doctor_id=%s"
        values=(name,specialization,doctor_id)
        self.cursor.execute(query,values)
        self.conn.commit()
        return True

    def delete_doctors(self, doctor_id):
        self.cursor.execute(
            "SELECT * FROM doctors WHERE doctor_id=%s",
            (doctor_id,)
        )

        if not self.cursor.fetchone():
            return False
        query="delete from doctors where doctor_id=%s"
        value=(doctor_id,)
        self.cursor.execute(query,value)
        self.conn.commit()
        return True
    def search_by_specialization(self, specialization):
        query = """
        SELECT * FROM doctors
        WHERE specialization=%s
        """

        self.cursor.execute(query, (specialization,))

        return self.cursor.fetchall()