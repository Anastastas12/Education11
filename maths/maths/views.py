from django.shortcuts import render, redirect
from .models import MathTask
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    tasks = MathTask.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        task_title = request.POST.get('task_name')
        description = request.POST.get('description')
        correct_answer = request.POST.get('correct_answer')  # Получаем введенный пользователем правильный ответ
        MathTask.objects.create(title=task_title, description=description, correct_answer=correct_answer)  # Сохраняем задачу с правильным ответом
        return redirect('view_tasks')
    return render(request, 'add_task.html')

def delete_task(request, task_id):
    # Получаем объект задачи или вызываем ошибку 404, если он не существует
    task = get_object_or_404(MathTask, pk=task_id)

    if request.method == 'POST':
        # Если запрос был отправлен методом POST, удаляем задачу и перенаправляем на главную страницу
        task.delete()
        return redirect('index')

    # Возвращаем шаблон для подтверждения удаления задачи
    return render(request, 'delete_task.html', {'task': task})
def solve_task(request, task_id):
    task = MathTask.objects.get(id=task_id)
    context = {
        'task': task,
    }
    return render(request, 'solve_task.html', context)
def view_tasks(request):
    tasks = MathTask.objects.all()
    return render(request, 'view_tasks.html', {'tasks': tasks})

