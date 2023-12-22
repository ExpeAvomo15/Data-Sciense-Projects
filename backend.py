import os
import convertapi
import openai
import tempfile

convertapi.api_secret = "lmkKcfJttQx1pMgM"

openai.api_type = "azure"
openai.api_base = "https://lawyersavomoia.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = "f98fd9417e1e47198e2fa65e84ee6de9"

def responder_pregunta_usuario(pregunta, documento):
    # Obtener el contenido del archivo PDF
    contenido_pdf = documento.read()

    # Guardar el contenido del archivo en un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(contenido_pdf)
        temp_pdf_path = temp_pdf.name

    try:
        # Extracción de datos con OCR
        convertapi.convert('txt', {'File': temp_pdf_path}).save_files('documento.txt')

        # Resto del código...
        with open('documento.txt', 'r', encoding='utf-8') as text_file:
            prompt = text_file.read()

        # Petición a Azure OpenAI
        respuesta = openai.ChatCompletion.create(
            engine="AvLawyers",
            messages=[{"role": "system", "content": "Eres un experto en analizar documentos legales de los clientes de un despacho de abogados. Debes responder a la siguiente pregunta: " + pregunta},
                      {"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None)

        # Devolver la respuesta en lugar de imprimir
        respuesta_final = respuesta['choices'][0]['message']['content']
        return respuesta_final

    finally:
        # Eliminar el archivo temporal después de su uso
        os.remove(temp_pdf_path)