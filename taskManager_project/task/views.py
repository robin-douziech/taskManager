from django.shortcuts import render, redirect, get_object_or_404

from . import models, forms

def list(request):
	tasks = models.Task.objects.all()
	return render(request, 'task/list.html', {
		'tasks': tasks
	})

def details(request):
	task_id = request.GET.get('id', False)
	if task_id:
		task = get_object_or_404(models.Task, pk=task_id)
		form = forms.TaskForm(instance=task)
		if request.method == "POST":
			form = forms.TaskForm(request.POST, instance=task)
			if form.is_valid():
				form.save()
		return render(request, 'task/details.html', {'form': form, 'task':task})
		
	return redirect('/')

def create(request):
	form = forms.TaskForm()
	if request.method == "POST":
		form = forms.TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	return render(request, 'task/create.html', {'form': form})

def delete(request):
	task_id = request.GET.get('id', False)
	if task_id:
		task = get_object_or_404(models.Task, pk=task_id)
		task.delete()
	return redirect('/')