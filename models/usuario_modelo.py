from flask import jsonify
import requests    

class UsuarioModelo():

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBza3pydWd1enhreGRzZ3B3ZnZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEyMDM2MjgsImV4cCI6MjAyNjc3OTYyOH0.hDnMerhhIbKtNXxG2kVoqUXztXITbi4yqZocUlARQvM',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBza3pydWd1enhreGRzZ3B3ZnZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEyMDM2MjgsImV4cCI6MjAyNjc3OTYyOH0.hDnMerhhIbKtNXxG2kVoqUXztXITbi4yqZocUlARQvM',
        'Content-Type' : 'application/json'
        }
    
    def obtener_datos_usuario(self, id):

        print(id)

        try:
            response = requests.get(f'https://pskzruguzxkxdsgpwfvi.supabase.co/rest/v1/PACIENTES?id_paciente=eq.{id}',
            headers= self.headers)

            datos = response.json()

            datos_usuario = datos[0]

            return jsonify({"datos_usuario": datos_usuario})
        except requests.exceptions.HTTPError as err:
            print(err)
        return 201


    def notificaciones_usuario(self, id):

        try:
            response = requests.get(f'https://pskzruguzxkxdsgpwfvi.supabase.co/rest/v1/ENTREGAS_MEDICAMENTOS?id_paciente=eq.{id}',
            headers= self.headers)

            datos = response.json()

            return jsonify({"datos_notificaciones": datos})

        except requests.exceptions.HTTPError as err:
            print(err)
        return 201



             