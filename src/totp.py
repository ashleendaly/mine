import pyotp
import qrtools

class TotpHandler:

    def __init__(self, path_to_qr):
        self.totp = pyotp.TOTP(self.get_secret_from_qr(path_to_qr))
        self.qr = qrtools.QR()
        
    def get_passcode(self):
        return self.totp.now()

    def get_secret_from_qr(self, path_to_qr):
        return self.qr.decode(path_to_qr)