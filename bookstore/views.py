from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import subprocess
import json

from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello_world.html')

@csrf_exempt
@require_POST
def update_server(request):
    """Webhook que atualiza o servidor após um push no GitHub"""
    try:
        # Pega os dados do webhook
        payload = json.loads(request.body)
        
        # Faz pull das últimas alterações
        subprocess.run(['git', 'pull', 'origin', 'main'], cwd='/home/kellzero/BookStore', check=True)
        
        # Roda as migrações se houver
        subprocess.run(['source', '/home/kellzero/BookStore/env/bin/activate', '&&', 'python', 'manage.py', 'migrate'], 
                      cwd='/home/kellzero/BookStore', shell=True, executable='/bin/bash')
        
        # Coleta arquivos estáticos
        subprocess.run(['source', '/home/kellzero/BookStore/env/bin/activate', '&&', 'python', 'manage.py', 'collectstatic', '--noinput'],
                      cwd='/home/kellzero/BookStore', shell=True, executable='/bin/bash')
        
        return JsonResponse({'status': 'success', 'message': 'Deploy realizado com sucesso!'})
    
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
