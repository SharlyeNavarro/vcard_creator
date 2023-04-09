from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory
import vobject
import qrcode
from qrcode import QRCode, constants
from PIL import Image


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vcards', methods=['GET', 'POST'])
def vcards():
    if request.method == 'POST':
        # Recopilar los datos del formulario
        nombre = request.form['nombre']
        correo = request.form['correo']
        celular = request.form['celular']
        trabajo = request.form['trabajo']
        casa = request.form['casa']
        facebook = request.form['facebook']
        twitter = request.form['twitter']
        linkedin = request.form['linkedin']
        instagram = request.form['instagram']
        youtube = request.form['youtube']
        
        # Crear el archivo contacto.vcf
        with open('static/vcards/contacto.vcf', 'w') as vcard:
            vcard.write(f'BEGIN:VCARD\nVERSION:3.0\nN:{nombre};;;;\nFN:{nombre}\nTEL;TYPE=CELL:{celular}\nTEL;TYPE=WORK:{trabajo}\nTEL;TYPE=HOME:{casa}\nEMAIL;TYPE=PREF,INTERNET:{correo}\nURL;TYPE=FACEBOOK:{facebook}\nURL;TYPE=TWITTER:{twitter}\nURL;TYPE=LINKEDIN:{linkedin}\nURL;TYPE=INSTAGRAM:{instagram}\nURL;TYPE=YOUTUBE:{youtube}\nEND:VCARD')

        # Crear el código QR correspondiente al archivo contacto.vcf
        qr = qrcode.QRCode(version=None, box_size=10, border=4)
        qr.add_data(open('static/vcards/contacto.vcf', 'r').read())
        qr.make(fit=True)

        # Generar el archivo PNG del código QR
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('static/img/qr_contacto.png')

        # Mostrar el código QR en la página vcard_complete.html
        return render_template('vcard_complete.html')

    else:
        return render_template('vcards.html')

@app.route('/qr')
def qr():
    # Descargar el archivo PNG del código QR
    return send_from_directory('static/img', 'qr_contacto.png')


@app.route('/prueba')
def prueba():
    return render_template('menulateral.html')

if __name__ == '__main__':
    app.run(debug=True)

