from flask import request, jsonify
import requests    
import json

class ReporteModelo():

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBza3pydWd1enhreGRzZ3B3ZnZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEyMDM2MjgsImV4cCI6MjAyNjc3OTYyOH0.hDnMerhhIbKtNXxG2kVoqUXztXITbi4yqZocUlARQvM',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBza3pydWd1enhreGRzZ3B3ZnZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEyMDM2MjgsImV4cCI6MjAyNjc3OTYyOH0.hDnMerhhIbKtNXxG2kVoqUXztXITbi4yqZocUlARQvM',
        'Content-Type' : 'application/json'
        }

    # Realizar una solicitud POST a la API de SUPABASE
    def crear_reporte(self, id):
            
        descripcion = request.json.get('descripcion')
        sintomas =  request.json.get('sintomas')
        enfermedad = request.json.get('enfermedad')
        id_paciente = request.json.get('idPaciente')

        datos_crear_reportes = {
            'descripcion': descripcion,
            'sintomas': sintomas,
            'enfermedad': enfermedad,
            'id_paciente' : id_paciente
        }

        datos_reportes= json.dumps(datos_crear_reportes)

        try:
            res = requests.post(f'https://pskzruguzxkxdsgpwfvi.supabase.co/rest/v1/REPORTES?id_paciente=eq.{id}', 
            data = datos_reportes,
            headers = self.headers)

            print(res.text)

            return jsonify({"Reporte creado para el usuario": id})

        except requests.exceptions.HTTPError as err:
            print(err)

        return 201
    
    def obtener_reporte(self):
        try:
            id_paciente = request.json.get('id_paciente')
            response = requests.get('https://pskzruguzxkxdsgpwfvi.supabase.co/rest/v1/REPORTES?id_paciente=eq.'+str(id_paciente),
                                   headers = self.headers)
            lista_reportes = []

            for reportes in response.json():
                lista_reportes.append(reportes)
            
            return jsonify({"reportes": lista_reportes})

        except requests.exceptions.HTTPError as err:
            print(err)
        return 201
