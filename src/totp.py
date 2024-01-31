import pyotp

class TotpHandler:

    def __init__(self, secret):
        self.totp = pyotp.TOTP(secret)
        
    def get_passcode(self):
        return self.totp.now()