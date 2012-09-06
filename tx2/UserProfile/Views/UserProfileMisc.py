'''
Created on 06-Aug-2012

@author: jivjot
'''
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import   LOGGER_USER_PROFILE
from tx2.UserProfile.BusinessFunctions.UserProfileMisc import UserProfileMisc
from django.contrib import messages
from tx2.UserProfile.models import MedicalInfo
from tx2.UserProfile.models import LegalInfo
import logging
import inspect
from django.core.exceptions import ObjectDoesNotExist
from tx2.Misc.MIscFunctions1 import is_integer
Logger_User = logging.getLogger(LOGGER_USER_PROFILE)

def MedicalInfoIndex(HttpRequest):
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
            messages.error(HttpRequest,'Please Login to continue')
            return HttpResponseRedirect('/user/login/')
    try:
      MedicalInfoObj = MedicalInfo.objects.get(User=int(logindetails["userid"]))
      # exists
      return render_to_response("UserProfile/MedicalInfo.html",{'MedicalInfoStatus':MedicalInfoObj},context_instance=RequestContext(HttpRequest))
    except ObjectDoesNotExist:
      # does not exists
      return render_to_response("UserProfile/MedicalInfo.html",context_instance=RequestContext(HttpRequest))
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
  
  
def LegalInfoIndex(HttpRequest):
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
            messages.error(HttpRequest,'Please Login to continue')
            return HttpResponseRedirect('/user/login/')
    try:
      LegalInfoObj = LegalInfo.objects.get(User=int(logindetails["userid"]))
      # exists
      return render_to_response("UserProfile/LegalInfo.html",{'LegalInfoStatus':LegalInfoObj},context_instance=RequestContext(HttpRequest))
    except ObjectDoesNotExist:
      # does not exists
      return render_to_response("UserProfile/LegalInfo.html",context_instance=RequestContext(HttpRequest))
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')
  

def MedicalInfoInsert(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        messages.error(HttpRequest,'Please Login to continue')
        return HttpResponseRedirect('/user/login/')
    try:
        UserProfileMiscObj=UserProfileMisc()
        flag=1
        if "Height" in HttpRequest.POST:
            Height=HttpRequest.POST["Height"]
            if is_integer(Height):
              Height=int(Height)
            else:
              messages.error(HttpRequest,"Error Height should be integer");
              flag=-1;
        else:
            messages.error(HttpRequest,"Error fetching data from form for Height");
            flag=-1;
        if "Weight" in HttpRequest.POST:
            Weight=HttpRequest.POST["Weight"]
            if is_integer(Weight):
              Weight=int(Weight)
            else:
              messages.error(HttpRequest,"Error Weight should be integer");
              flag=-1;
        else:
            messages.error(HttpRequest,"Error fetching data from form for Weight");
            flag=-1;
        if "LeftEye" in HttpRequest.POST:
            LeftEye=HttpRequest.POST["LeftEye"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for LeftEye");
            flag=-1;
        if "RightEye" in HttpRequest.POST:
            RightEye=HttpRequest.POST["RightEye"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for RightEye");
            flag=-1;
        if "DisabilityInfo" in HttpRequest.POST:
            DisabilityInfo=HttpRequest.POST["DisabilityInfo"]
        else:
            messages.error(HttpRequest,"Error fetching data from form for DisabilityInfo");
            flag=-1;
        if flag==-1:
            return HttpResponseRedirect('/message/')
        
        if "Id" in HttpRequest.POST:
            Id=HttpRequest.POST["Id"]
            result=UserProfileMiscObj.UpdateMedicalInfo(Id,logindetails["userid"], Height, Weight, LeftEye, RightEye, DisabilityInfo, logindetails["userid"], ip)
        else:
            result=UserProfileMiscObj.InsertMedicalInfo(logindetails["userid"], Height, Weight, LeftEye, RightEye, DisabilityInfo, logindetails["userid"], ip)
        if result['result']==-2:
          messages.error(HttpRequest,"You do not have privelege to this table.");
          messages.error(HttpRequest,"Either your profile is complete or you have not authenticated yourself");
        elif result['result']==1:
          messages.error(HttpRequest,"Congrats Your value has been saved");
          
        else:
          messages.error(HttpRequest,"result is %s"%result);
        return HttpResponseRedirect('/message/')
    except Exception, ex:
      frame = inspect.currentframe()
      args, _, _, values = inspect.getargvalues(frame)
      msg = ''
      for i in args:
        msg += "[%s : %s]" % (i,values[i])
      Logger_User.exception('%s : %s' % (inspect.getframeinfo(frame)[2],msg))
      messages.error(HttpRequest,'ERROR: ' + str(ex))
      return HttpResponseRedirect('/message/')