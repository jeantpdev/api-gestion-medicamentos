from flask import request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import supabase

class Usuario():

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBza3pydWd1enhreGRzZ3B3ZnZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEyMDM2MjgsImV4cCI6MjAyNjc3OTYyOH0.hDnMerhhIbKtNXxG2kVoqUXztXITbi4yqZocUlARQvM',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBza3pydWd1enhreGRzZ3B3ZnZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEyMDM2MjgsImV4cCI6MjAyNjc3OTYyOH0.hDnMerhhIbKtNXxG2kVoqUXztXITbi4yqZocUlARQvM',
        'Content-Type' : 'application/json'
        }

    def login(self):
        user = request.json.get('usuario')
        password = request.json.get('contrasena')

        SUPABASE_URL = 'https://pskzruguzxkxdsgpwfvi.supabase.co'
        SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBza3pydWd1enhreGRzZ3B3ZnZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEyMDM2MjgsImV4cCI6MjAyNjc3OTYyOH0.hDnMerhhIbKtNXxG2kVoqUXztXITbi4yqZocUlARQvM'
        client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

        query = client.table('USUARIOS').select('*').eq('usuario', user).eq('contrasena', password)
        res = query.execute()
        # Si el usuario existe y la contraseña es correcta, se devuelve un token JWT
        if len(res.data) == 1:
            json_data = res.data
            access_token = create_access_token(identity=user)
            id_paciente = json_data[0]['id_paciente']
            rol = json_data[0]['rol']
            usuario = json_data[0]['usuario']
            return jsonify({"acceso": True, "id_paciente": id_paciente, "access_token": access_token, "rol": rol, 'usuario': usuario})
        else:
            return jsonify({"acceso": "ACCESO A LA CUENTA NO AUTORIZADO"})