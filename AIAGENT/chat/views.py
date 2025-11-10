import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Simple in-memory viewer counter
VIEWER_COUNT = 0

def index(request):
    global VIEWER_COUNT
    VIEWER_COUNT += 1
    return render(request, 'chat/index.html', {'viewer_count': VIEWER_COUNT})

@csrf_exempt
@require_http_methods(["POST"])
def chat(request):
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({'error': 'Message is required'}, status=400)
        
        # Gemini API only
        try:
            api_key = "AIzaSyCHeOd0Ls1C5UZIIyHTCCkSGWf8hu1UEvY"
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')
            prompt = f"""Convert this text to natural Bengali. Match the tone of the input - if casual, be casual; if formal, be less formal but still natural.

Rules:
- Use "আমি" and natural Bengali words
- Use "টা", "গুলা" moderately
- Keep the same meaning and tone as input
- Sound natural but not overly casual
- Don't add extra words or change the message

Text: {user_message}

Natural Bengali:"""
            response = model.generate_content(prompt)
            ai_response = response.text.strip()
        except Exception as e:
            return JsonResponse({'error': f'Translation failed: {str(e)}'}, status=500)
        
        return JsonResponse({
            'response': ai_response, 
            'status': 'success'
        })
        
    except Exception as e:
        return JsonResponse({'error': f'Error: {str(e)}'}, status=500)