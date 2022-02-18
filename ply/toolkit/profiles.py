from community.models import Community,VHost
from ply.toolkit.logger import getLogger
from profiles.models import Profile
# get_vhost_community: Find the right community node for the given Vhost.
# To match VHosts, we must at least match the host name, and optionally, the iapddr.
# 

logging = getLogger('toolkit.vhosts',name='toolkit.vhosts')
#print(vhost_logger)

# get_active_profile will match the 'uuid' stored in request.session to the active profile from the database and return it. 
# if there is no profile set it will select the first available profile that is active, unblocked and unarchived that matches the user in request.user.

def get_active_profile(request):
   if 'profile' not in request.session:
       profile = Profile.objects.filter(creator=request.user,archived=False,blocked=False,system=False,placeholder=False)[0]
       request.session['profile'] = str(profile.uuid)
       request.session.modified = True
   else:
       profile = Profile.objects.filter(uuid=request.session['profile'])[0]
   request.session.placeholder = False
   return profile
    
# Returns all the profiles associated with the User:        
def get_all_profiles(request):
    profiles = Profile.objects.filter(creator=request.user,archived=False,blocked=False,system=False,placeholder=False)
    return profiles
    


# create_placeholder_profile create a new 'placeholder' profile that will be hopefully populated by the user. This is a "new" profile that would be used as the basis of a new character by the forge module, for example.
# NOTE: It's up to the forge, or whatever module is creating this profile to UNPLACEHOLDER it, and to create the dynaPage structure needed for the profile to render correctly at all.
def get_placeholder_profile(request):
       profile = Profile.objects.get_or_create(creator=request.user,archived=False,blocked=False,placeholder=True)[0]
       request.session['profile'] = str(profile.uuid)
       request.session.modified = True
       request.session.placeholder = True
       return profile

# Get a profile from the active, available ones assigned to the user:
def get_profile(request,puuid):
       profile = Profile.objects.get(pk=puuid,creator=request.user,archived=False,blocked=False,placeholder=False,system=False)
       request.session['profile'] = str(profile.uuid)
       return profile 
