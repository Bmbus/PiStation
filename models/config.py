class Config:
    def __init__(self, name:str=None, username:str=None, pin:int=2, email:str=None, password:str=None, set_password:bool=False, set_email_notify:bool=False):
        self.name = name
        self.username = username
        self.pin = pin
        self.email = email
        self.password = password
        self.set_password = set_password
        self.set_email_notify = set_email_notify