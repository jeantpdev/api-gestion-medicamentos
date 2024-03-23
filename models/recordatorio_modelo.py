from flask import request, jsonify
import requests    
import json

class RecordatorioModelo():

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBza3pydWd1enhreGRzZ3B3ZnZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEyMDM2MjgsImV4cCI6MjAyNjc3OTYyOH0.hDnMerhhIbKtNXxG2kVoqUXztXITbi4yqZocUlARQvM',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBza3pydWd1enhreGRzZ3B3ZnZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEyMDM2MjgsImV4cCI6MjAyNjc3OTYyOH0.hDnMerhhIbKtNXxG2kVoqUXztXITbi4yqZocUlARQvM',
        'Content-Type' : 'application/json'
        }
    
    def crear_recordatorio(self):
            
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        medicamento = request.json.get('medicamento')
        informacion = request.json.get('informacion')
        id_paciente = request.json.get('id_paciente')

        datos_crear_recordatorios = {
            'fecha': fecha,
            'hora': hora,
            'medicamento': medicamento,
            'informacion': informacion,
            'id_paciente': id_paciente
        }

        datos_recordatorio = json.dumps(datos_crear_recordatorios)

        try:
            requests.post('https://pskzruguzxkxdsgpwfvi.supabase.co/rest/v1/RECORDATORIOS_MEDICINAS', 
            data = datos_recordatorio, 
            headers = self.headers)

            return jsonify({"Recordatorio creado para el usuario": id_paciente})

        except requests.exceptions.HTTPError as err:
            print(err)

        return 201
    
    def obtener_recordatorio(self, id):

        try:
            response = requests.get(f'https://pskzruguzxkxdsgpwfvi.supabase.co/rest/v1/RECORDATORIOS_MEDICINAS?id_paciente=eq.{id}',
            headers= self.headers)

            print(response)

            lista_recordatorios = []
            for recordatorios in response.json():
                lista_recordatorios.append(recordatorios)

            return jsonify({"recordatorios": lista_recordatorios})
        except requests.exceptions.HTTPError as err:
            print(err)
        return 201

    def eliminar_recordatorio(self, id_recordatorio_eliminar):

        try:
            requests.delete(f'https://pskzruguzxkxdsgpwfvi.supabase.co/rest/v1/RECORDATORIOS_MEDICINAS?id_recordatorio=eq.{id_recordatorio_eliminar}', 
            headers = self.headers)

            return jsonify({"Recordatorio eliminado": "Exitoso"})

        except requests.exceptions.HTTPError as err:
            print(err)

        return 201









             