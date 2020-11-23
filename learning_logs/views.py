from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    return(request, 'learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}

    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    context = {'topic': topic, 'entries':entries}

    return render(request, 'learning_logs/topic.html', context)

#KNOW THIS FOR THE INTERVIEW PART OF THE EXAM
def new_topic(request):
    if request.method != 'POST':
        #load up a blank form
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    context = {'form':form}

    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            form.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryFornm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            ###is this supposed to be t_id or Topic_id?
            return redirect('learning_logs:topic', t_id=topic.id)

    #context has all of the data that the html skeleton needs below
    context = {'entry' :entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)
