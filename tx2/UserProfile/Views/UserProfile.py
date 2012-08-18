'''
Created on 26-Jul-2012

@author: jivjot
'''
from django.http import HttpResponseRedirect, HttpRequest
from django.template import RequestContext
from django.shortcuts import render_to_response
from tx2.Misc.MIscFunctions1 import AppendMessageList
from tx2.Users.HelperFunctions.LoginDetails import GetLoginDetails
from tx2.CONFIG import  SESSION_MESSAGE, LoggerUser
from tx2.UserProfile.BusinessFunctions.UserProfile import UserProfile
from tx2.UserProfile.models import Degree,Branch,Category, StudentDetails
from tx2.Misc.MIscFunctions1 import is_integer
import logging
LogUser = logging.getLogger(LoggerUser)


#def UserHome(HttpRequest):
    

def BranchIndex(HttpRequest):
    return render_to_response("UserProfile/Branch.html",context_instance=RequestContext(HttpRequest))
def BranchInsert(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        UserProfileObj=UserProfile()
        flag=1
        if "BranchName" in HttpRequest.POST:
            BranchName=HttpRequest.POST["BranchName"]
        else:
            msglist.append("Error fetching data from form for BranchName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=UserProfileObj.InsertBranch(BranchName, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
def BranchUpdate(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        UserProfileObj=UserProfile()
        flag=1
        if "Id" in HttpRequest.POST:
            Id=HttpRequest.POST["Id"]
        else:
            msglist.append("Error fetching data from form for Id");
            flag=-1;
        if "BranchName" in HttpRequest.POST:
            BranchName=HttpRequest.POST["BranchName"]
        else:
            msglist.append("Error fetching data from form for BranchName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=UserProfileObj.UpdateBranch(Id, BranchName,logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y

def CategoryIndex(HttpRequest):
    return render_to_response("UserProfile/Category.html",context_instance=RequestContext(HttpRequest))
def CategoryInsert(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        UserProfileObj=UserProfile()
        flag=1
        if "CategoryName" in HttpRequest.POST:
            CategoryName=HttpRequest.POST["CategoryName"]
        else:
            msglist.append("Error fetching data from form for CategoryName");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=UserProfileObj.InsertCategory(CategoryName, logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y
def CategoryUpdate(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    logindetails = GetLoginDetails(HttpRequest)
    print logindetails
    if( logindetails["userid"] == -1):
        msglist.append('Please Login to continue')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/login/')
    try:
        UserProfileObj=UserProfile()
        flag=1
        if "CategoryName" in HttpRequest.POST:
            CategoryName=HttpRequest.POST["CategoryName"]
        else:
            msglist.append("Error fetching data from form for CategoryName");
            flag=-1;
        if "Id" in HttpRequest.POST:
            Id=HttpRequest.POST["Id"]
        else:
            msglist.append("Error fetching data from form for Id");
            flag=-1;
        if flag==-1:
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
        result=UserProfileObj.UpdateCategory(Id, CategoryName,logindetails["userid"], ip)
        msglist.append("result is %s"%result);
        return render_to_response("UserProfile/Message.html",{'mylist':msglist,})
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y

def StudentDetailsIndex(HttpRequest):
    print "here"
    msglist = AppendMessageList(HttpRequest)
    logindetails = GetLoginDetails(HttpRequest)
    if( logindetails["userid"] == -1):
            msglist.append('Please Login to continue')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/user/login/')
            
    if( StudentDetails.objects.filter(User=logindetails["userid"]).exists()):
        StudDetailStatus= False
    else:
        StudDetailStatus= True
    return render_to_response("TXtemplates/UserProfile/StudentDetails.html",{'StudDetailStatus':StudDetailStatus,'BranchList':Branch.objects.all(),'CategoryList':Category.objects.all(),'DegreeList':Degree.objects.all()},context_instance=RequestContext(HttpRequest))
            
def StudentDetailsInsert(HttpRequest):
        msglist = AppendMessageList(HttpRequest)
        ip = HttpRequest.META['REMOTE_ADDR']
        logindetails = GetLoginDetails(HttpRequest)
        print "here in student details"
        print msglist
        if( logindetails["userid"] == -1):
            msglist.append('Please Login to continue')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/user/login/')
        try:
            
            flag=1
            UserId=int(logindetails["userid"])
            RollNo = -1
            BranchMajor = -1
            BranchMinor = -1
            Degree = -1
            Category = -1
            ComputerProficiency = ""
            
            if "RollNo" in HttpRequest.POST:
                RollNo=HttpRequest.POST["RollNo"]
                if len(RollNo) == 0:
                      msglist.append("RollNo is required");
                      flag=-1;
            else:
                msglist.append("Error fetching data from form for RollNo");
                flag=-1;
            
            if "BranchMajor" in HttpRequest.POST:
                BranchMajor= int(HttpRequest.POST["BranchMajor"])
                if BranchMajor == -1:
                    msglist.append("Please select value for BranchMajor");
                    flag=-1;
            else:
                msglist.append("Error fetching data from form for BranchMajor");
                flag=-1;
            
            if "BranchMinor" in HttpRequest.POST:
                BranchMinor= int(HttpRequest.POST["BranchMinor"])
            else:
                msglist.append("Error fetching data from form for BranchMinor");
                flag=-1;                    
            
            if "Degree" in HttpRequest.POST:
                Degree=int(HttpRequest.POST["Degree"])
                if Degree == -1:
                    msglist.append("Please select value for Degree");
                    flag=-1;
            else:
                msglist.append("Error fetching data from form for Degree");
                flag=-1;
            
            if "Category" in HttpRequest.POST:
                Category=int(HttpRequest.POST["Category"])
                if Category == -1:
                    msglist.append("Please select value for Category");
                    flag=-1;
            else:
                msglist.append("Error fetching data from form for Category");
                flag=-1;
            
            if "ComputerProficiency" in HttpRequest.POST:
                ComputerProficiency=HttpRequest.POST["ComputerProficiency"]
            else:
                ComputerProficiency = "Not applicable"  
            if flag==-1:
                HttpRequest.session[SESSION_MESSAGE] = msglist
                return HttpResponseRedirect('/message/')
            else:
                print msglist
                UserProfileObj=UserProfile()
                BranchObj = Branch.objects.get(id=BranchMajor)
                Group = "GROUP_"  + BranchObj.BranchName  + "_UN-AUTHENTICATED"
                result=UserProfileObj.InsertStudentDetails(UserId, RollNo, BranchMajor, BranchMinor, Degree, Category, ComputerProficiency,UserId, ip, Group)
                msglist.append(result[1])
                print msglist
                HttpRequest.session[SESSION_MESSAGE] = msglist
                return HttpResponseRedirect('/message/')
        except Exception as inst:
            LogUser.exception('[%s][%s] == EXCEPTION ==' % (ip, 'StudentDetailsInsert'))
            msglist.append('Some Error has occoured')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')
