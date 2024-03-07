from flask import Flask, render_template, request, flash, redirect, url_for
from generator import Generator
from bitcoinlib.wallets import WalletError
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        wallet_name = request.form.get('wallet_name')
        try:
            generator = Generator(wallet_name)
            generator.generate_keys()
            generator.generate_qr(generator.private_key_converted, 'private_key_qr.png')
            generator.generate_qr(generator.public_key_converted, 'public_key_qr.png')
            flash('Wallet successfully created!','success')
        except WalletError as e:
            flash(str(e),'error')
        return render_template('index.html', wallet=generator if 'generator' in locals() else None)
    return render_template('index.html', wallet=None)

if __name__ == '__main__':
    app.run(debug=True)