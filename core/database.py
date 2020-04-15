import mysql.connector as mysql


class Database:
    def __init__(self):
        try:
            self.connector = mysql.connect(
                host: "127.0.0.1",
                user: "root",
                database: "Tomato",
                #password: "your_passwrd"
            )
            self.cursor = self.connector.cursor()
            self.connector.commit()
        except Exception as err:
            print(f"<DATABASE>-Error {err}")
    
    def check_connection(self):
        return self.connector is not None and self.connector.is_connected()
    
    def setup(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS data (
            id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
            humidity INT NOT NULL,
            temperature INT NOT NULL,
            created_at DATETIME NOT NULL
        );""")
        self.connector.commit()
    
    def execute(self, query, values=()):
        try:
            self.cursor.execute(query, values)
        except Exception as err:
            print(f"<DATABASE>-Error: {err}")