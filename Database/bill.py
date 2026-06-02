from Database.database import conn,cursor
class Bill:
    def __init__(self):
        self.conn=conn
        self.cursor=cursor
    
    def generate_bill(self, patient_id, consultation_fee,medicine_charges,room_charges,amount):
        self.cursor.execute(
            "SELECT * FROM patients WHERE patient_id=%s",
            (patient_id,)
        )

        if not self.cursor.fetchone():
            print("Patient not found")
            return False
    
        amount=consultation_fee+medicine_charges+room_charges
        query="insert into bills (patient_id,consultation_fee,medicine_charges,room_charges,amount) values (%s,%s,%s,%s,%s)"
        values=(patient_id,consultation_fee,medicine_charges,room_charges,amount)
        self.cursor.execute(query,values)
        self.conn.commit()
        return True

    def view_bills(self):
        query="select * from bills"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def search_bills(self, patient_id):
        query="select * from bills where patient_id=%s"
        value=(patient_id,)
        self.cursor.execute(query,value)
        return self.cursor.fetchall()
        
