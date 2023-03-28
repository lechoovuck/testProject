from authapp.models import WebUser
from .models import Facility
from .forms import FacilSelectWebuserForm

#список со складами на каждой страничке
def webuserfacility(request):
    if (request.user.is_authenticated):
        facility_list = request.user.get_facility_list() #Facility.get_webuser_facility_list(request)
        # print(facility_list)
        current_facility_id = request.user.get_current_facility_id()
        if current_facility_id == "":
            current_facility_id = request.user.get_default_facility_id()

        formfacility = FacilSelectWebuserForm(facility_list, request.POST or None, initial={'facility_name': current_facility_id})
        return {'formuserfacility': formfacility}
    return {'formuserfacility': ""}