from Database.database import conn,cursor
class Appointment:
    def __init__(self):
        self.conn=conn
        self.cursor=cursor
    
    def book_appointment(self, patient_id, doctor_id, appointment_date):
        self.cursor.execute(
            "SELECT * FROM patients WHERE patient_id=%s",
            (patient_id,)
        )

        if not self.cursor.fetchone():
            print("Patient not found")
            return False

        
        self.cursor.execute(
            "SELECT * FROM doctors WHERE doctor_id=%s",
            (doctor_id,)
        )

        if not self.cursor.fetchone():
            print("Doctor not found")
            return False

    
        self.cursor.execute(
            """
            SELECT * FROM appointments
            WHERE doctor_id=%s AND appointment_date=%s
            """,
            (doctor_id, appointment_date)
        )

        if self.cursor.fetchone():
            return False

    
        query = """
        INSERT INTO appointments
        (patient_id, doctor_id, appointment_date)
        VALUES (%s, %s, %s)
        """

        values = (patient_id, doctor_id, appointment_date)

        self.cursor.execute(query, values)
        self.conn.commit()

        return True
    
    def view_appointments(self):
        query="select * from appointments"
        self.cursor.execute(query)
        results=self.cursor.fetchall()
        return results

    def update_appointment(self, appointment_id, patient_id, doctor_id, appointment_date):
        query="update appointments set patient_id=%s,doctor_id=%s,appointment_date=%s where appointment_id=%s"
        values=(patient_id,doctor_id,appointment_date,appointment_id)
        self.cursor.execute(query,values)
        self.conn.commit()
        return True

    def cancel_appointment(self, appointment_id):
        query="delete from appointments where appointment_id=%s"
        value=(appointment_id,)
        self.cursor.execute(query,value)
        self.conn.commit()
        return True
