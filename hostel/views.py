from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .decorators import *
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.



#  --------------------------------------------------------------------------
#                             LOGIN PAGE
# ---------------------------------------------------------------------------
@unauthenticated_user
def loginPage(request):
    # Checking to see if the request method is POST
    if request.method == 'POST':
        # if true sef the username to the username of the POST
        username = request.POST.get('username')

        # if true sef the username to the username of the POST
        password = request.POST.get('password')

        # authenticate the user
        user = authenticate(request,username = username, password = password)

        # Checking to see if the user exists
        if user is not None:
            # if the user exists login the user 
            login(request,user)
            return redirect('homePage')
        else:
            messages.info(request,'Incorrect Username or password (They are case sensitive)')

    return render(request, 'login.htm')


#  --------------------------------------------------------------------------
#                             LOGOUT
# ---------------------------------------------------------------------------
def logoutUser(request):
    logout(request)
    return redirect('loginPage')


#  --------------------------------------------------------------------------
#                             DASHBOARD
# ---------------------------------------------------------------------------
@login_required(login_url='loginPage')
def homePage(request):
    occupants = Occupant.objects.all()
    rooms = Room.objects.all()
    workers = Worker.objects.all()

    total_spaces_available = 0
    amount_received = 0

    for room in rooms:
        total_spaces_available += room.spaces_available

    for occupant in occupants:
        amount_received += occupant.amount_paid

    context = {
        'occupants':occupants,
        'rooms':rooms,
        'workers':workers,
        'total_spaces_available': total_spaces_available,
        'amount_received': amount_received,
    }
    return render(request, 'index.htm',context)


#  --------------------------------------------------------------------------
#                             ROOMS
# ---------------------------------------------------------------------------
@login_required(login_url='loginPage')
def rooms(request):
    rooms = Room.objects.all()
    
    context = {
        'rooms': rooms
    }
    return render(request, 'rooms.htm',context)


#  --------------------------------------------------------------------------
#                             ADD ROOMS
# ---------------------------------------------------------------------------
@login_required(login_url='loginPage')
def addRoom(request):
    roomForm = RoomForm()

    if request.method == 'POST':
        roomForm = RoomForm(request.POST)
        if roomForm.is_valid():
            roomForm.save()
            return redirect('rooms')
    
    context = {
        'roomForm':roomForm
    }

    return render(request,'adds/add-room.htm',context)


#  --------------------------------------------------------------------------
#                            UPDATE ROOMS
# ---------------------------------------------------------------------------
@login_required(login_url='loginPage')
def updateRoom(request,pk):
    room = Room.objects.get(id = pk)
    roomForm = RoomForm(instance = room)
    
    if request.method == 'POST':
        roomForm = RoomForm(request.POST, instance = room)
        if roomForm.is_valid():
            roomForm.save()
            return redirect('rooms')

    context = {
        'room':room,
        'roomForm':roomForm
    }
    return render(request,'updates/update_room.htm',context)


#  --------------------------------------------------------------------------
#                             WORKERS
# ---------------------------------------------------------------------------
@login_required(login_url='loginPage')
def workers(request):
    # Getting all workers registered in the database
    workers = Worker.objects.all()

    context = {
        'workers':workers
    }
    return render(request, 'workers.htm',context)


#  --------------------------------------------------------------------------
#                             ADD WORKERS
# ---------------------------------------------------------------------------
@login_required(login_url='loginPage')
def addWorker(request):
    workerForm = WorkerForm()

    if request.method == 'POST':
        workerForm = WorkerForm(request.POST)

        if workerForm.is_valid():
            workerForm.save()
            return redirect('workers')



    context = {
        'workerForm':workerForm
    }
    return render(request,'adds/add-worker.htm',context)


#  --------------------------------------------------------------------------
#                             UPDATE WORKERS
# ---------------------------------------------------------------------------
@login_required(login_url='loginPage')
def updateWorker(request,pk):
    worker = Worker.objects.get(id = pk)
    workerForm = WorkerForm(instance = worker)

    if request.method == 'POST':
        workerForm = WorkerForm(request.POST,instance = worker)
        if workerForm.is_valid():
            workerForm.save()
            return redirect('workers')

    context = {
        'workerForm':workerForm,
        'worker':worker
    }
    return render(request,'updates/update_worker.htm',context)



#  --------------------------------------------------------------------------
#                             DELETE WORKER
# ---------------------------------------------------------------------------
@login_required(login_url='loginPage')
def deleteWorker(request,pk):
    worker = Worker.objects.get(id = pk)
    worker.delete()
    return redirect('workers')




#  --------------------------------------------------------------------------
#                             OCCUPANTS
# ---------------------------------------------------------------------------
@login_required(login_url='loginPage')
def occupants(request):
    occupants = Occupant.objects.all()
    context = {
        'occupants':occupants
    }

    return render(request,'occupants.htm',context)


#  --------------------------------------------------------------------------
#                            ADD OCCUPANTS
# ---------------------------------------------------------------------------
@login_required(login_url='loginPage')
def addOccupant(request):
    occupantForm = OccupantForm()
    if request.method == 'POST':
        occupantForm = OccupantForm(request.POST)
        if occupantForm.is_valid():
            occupantForm.save()
            return redirect('occupants')

    context = {
        'occupantForm':occupantForm
    }

    return render(request,'adds/add-occupant.htm',context)



#  --------------------------------------------------------------------------
#                            UPDATE OCCUPANTS
# ---------------------------------------------------------------------------
@login_required(login_url='loginPage')
def updateOccupant(request,pk):
    occupant = Occupant.objects.get(id = pk)
    occupantForm = OccupantForm(instance = occupant)

    if request.method == 'POST':
        occupantForm = OccupantForm(request.POST, instance = occupant)
        if occupantForm.is_valid():
            occupantForm.save()
            return redirect('occupants')

    context = {
        'occupant':occupant,
        'occupantForm' : occupantForm
    }        
    return render(request, 'updates/update_occupant.htm',context)


#  --------------------------------------------------------------------------
#                            DELETE OCCUPANTS
# ---------------------------------------------------------------------------
@login_required(login_url='loginPage')
def deleteOccupant(request,pk):
    occupant = Occupant.objects.get(id = pk)
    occupant.delete()
    messages.warning(request,f'{occupant} has been deleted')
    return redirect('occupants')