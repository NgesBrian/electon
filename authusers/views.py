from django.http import HttpResponse
from django.shortcuts import render, redirect
from voting.models import Elections, Position, Candidate,Voting
from django.core.files.storage import FileSystemStorage
import os.path

def home(request):
	context_object_name = 'Elections'
	
		#Return all elections ordered by dateAdded
	elections = Elections.objects.all();
	return render(request, 'authusers/home.html', {'elections':elections})
    #return HttpResponse("Hello, world. You're at the polls index.")
    
def dashboard(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'authusers/home.html')

def elections(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'authusers/home.html')

def election(request, id = 0):
    #get the election
    election = Elections.objects.get(pk= id)
    # get the various post assoicated with the elections.
    posts = Position.objects.filter(election_id = id)
    #get all the candidates for the election
    candidates = Candidate.objects.filter(election_id = id)
    votes = Voting.objects.filter(election_id = id)
    return render(request, 'authusers/election.html', { 'election': election, 'posts':posts, 'candidates':candidates, 'votes':votes})

#This function is to register the vote
def vote(request, id = 0):

	#get the candidate voted for
	candidate = Candidate.objects.get(pk = id)
	#Get all your voted candidates for that election
	elecs =  Voting.objects.filter(election_id = candidate.election_id, user_id = request.user.id)
	#get the position
	for elec in elecs:
		candi  = Candidate.objects.get(pk = elec.candidate_id) 
		if candi.position_id == candidate.position_id:
			elec.candidate_id = id
			elec.save()
			return election(request, id = candidate.election_id )
		
	#register the vote
	vote = Voting.objects.create(candidate_id = id, user_id = request.user.id, election_id = candidate.election_id)
	vote.save()
	return election(request, id = candidate.election_id )
	#call the election view

	return HttpResponse("Hello, world. You're at the polls index.")

#show all the elections to be selected
def results(request):
	#Return all elections ordered by dateAdded
	elections = Elections.objects.all();
	return render(request, 'authusers/results.html', {'elections':elections})

def result(request, id):
	election = Elections.objects.get(pk= id)
	#get all the votes of the election
	allvotes = Voting.objects.filter(election_id = id)
	#get all the candidates for the election
	candidates = Candidate.objects.filter(election_id = id)
	#get all the post
	posts = Position.objects.filter(election_id = id)
	return render(request, 'authusers/result.html', {'allvotes':allvotes, 'posts':posts, 'candidates':candidates, 'election':election})

#To Upload the users Profile Picture
def upload(request, id):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage('static/images')
        ouruser = request.user
        iden = str(ouruser.id)
        fileexist = FileSystemStorage('static/images/'+ iden)
        if os.path.exists('static/images/'+ iden):
        	 os.remove('static/images/'+ iden)
        filename = fs.save(str(ouruser.id), myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'authusers/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'authusers/simple_upload.html')

#to upload the pictures and save some data
def formupload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })