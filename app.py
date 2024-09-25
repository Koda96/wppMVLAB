from flask import Flask, request, render_template
import pywhatkit as kit
import os

app = Flask(__name__)

# Crear la carpeta 'uploads' si no existe
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_whatsapp', methods=['POST'])
def send_whatsapp():
    number = request.form.get('number')
    file = request.files['file']  # Captura el archivo PDF cargado
    pdf_path = os.path.join('uploads', file.filename)  # Define la ruta para guardar el archivo

    # Guarda el archivo en la carpeta uploads
    file.save(pdf_path)
    
    if number.startswith("0"):
        number = number[1:]  # Elimina el primer cero si está presente
    formatted_number = f"+54{number}"  # Agrega el código de país

    message = "Aquí está tu resultado de laboratorio."

    try:
        # Envía un mensaje de texto
        kit.sendwhatmsg_instantly(f"{formatted_number}", message, 10, tab_close=False)

        return "Mensaje enviado correctamente"
    except Exception as e:
        return f"Error al enviar mensaje: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
