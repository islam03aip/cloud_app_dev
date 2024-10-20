import functions_framework

@functions_framework.http
def add_task(request):
    request_json = request.get_json()

    task = request_json.get('task') if request_json else 'Unnamed Task'

    return f"Task '{task}' added successfully!"