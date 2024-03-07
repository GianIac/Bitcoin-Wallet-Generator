import qrcode
from bitcoinlib.wallets import Wallet

class Generator:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet.create(name)
        self.private_key = ""
        self.public_key = ""
        self.private_key_converted = ""
        self.public_key_converted = ""

    def generate_keys(self):
        key = self.wallet.new_key()
        self.private_key = key.key_private
        self.public_key = key.key_public
        self.private_key_converted = self.private_key.hex()
        self.public_key_converted = self.public_key.hex()

    def generate_qr(self, key, file_name):
        img = qrcode.make(key)
        img.save(f'static/img/{file_name}')