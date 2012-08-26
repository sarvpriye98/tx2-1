from django.conf.urls.defaults import patterns,  url


urlpatterns = patterns('',
                         
    # USER REGISTRATION , LOGIN AND RELATED STUFF
        #INDEX PAGES
        url(r'^login/$','Users.Views.UserViewIndex.LoginIndex'),
        url(r'^register/$','Users.Views.UserViewIndex.CreateUserIndex'),
        url(r'^password/change/$','Users.Views.UserViewIndex.ChangePassIndex'),
        url(r'^password/reset/$','Users.Views.UserViewIndex.ResetPasswordIndex'),
        url(r'^password/reset/$','Users.Views.UserViewIndex.ResendAuthenticationEmailIndex'),
        url(r'^authenticate/resendemail/$','Users.Views.UserViews.ResendAuthenticationEmail'), #ResendAuthenticationEmail
        url(r'^password/change/change/$','Users.Views.UserViews.ChangePass'),
        url(r'^password/reset/reset/$','Users.Views.UserViews.ResetPass'),
        
        # MENU URLS
        url(r'^menu/list/$','Users.Views.MenuViews.ListAllMenu'),
        url(r'^menu/add/$','Users.Views.MenuViews.AddMenuIndex'),
        url(r'^menu/edit/$','Users.Views.MenuViews.EditMenuIndex'),
        #url(r'^menu/delete/$','Users.Views.MenuViews.#TODO make view here'),
        
        # post-back for logging in 
        url(r'^login/post/$','Users.Views.UserViews.Login'),
        url(r'^logout/$','Users.Views.UserViews.log_out'),
        url(r'^dashboard/$','Users.Views.UserViews.view_dashboard'),
        url(r'^register/new/$','Users.Views.UserViews.CreateUserFromSite'),
        url(r'^authenticate/email/(?P<token>\S+)/(?P<refs>\d+)/$','Users.Views.UserViews.AuthenticateUserFromEmail'),
        
        url(r'^admin/$','Users.Views.UserAdminViews.ListAllUsers'),
        url(r'^admin/(?P<userid>\d+)/edit/$','Users.Views.UserAdminViews.EditUserIndex'),
        url(r'^admin/(?P<userid>\d+)/edit/edit/$','Users.Views.UserAdminViews.EditUser'),
        
        # MENU URLS #TODO
        #url(r'^menu/add/post/$','Users.Views.MenuViews.AddMenuIndex'),
        #url(r'^menu/edit/post/$','Users.Views.MenuViews.EditMenuIndex'),
        #url(r'^menu/delete/post/$','Users.Views.MenuViews.#TODO make view here'),
    ###########################################################################################
   url(r'^grouptype/$','Users.Views.GroupTypeViews.GroupTypeIndex'),
   url(r'^grouptype/create/$','Users.Views.GroupTypeViews.GroupTypeIndex'),
   url(r'^grouptype/create/new/$','Users.Views.GroupTypeViews.CreateNewGroup'), 
   
   url(r'^group/$','Users.Views.GroupViews.GroupIndex',{'__list':'true','__create':'false'}),
   url(r'^group/create/$','Users.Views.GroupViews.GroupIndex',{'__list':'false','__create':'true'}),
   url(r'^group/create/new/$','Users.Views.GroupViews.CreateNewGroup'), 
 #   url(r'^group/(?P<gid>\d+)/users/add/$','txUser.Views_Group.AddUsers_Index'),
  #  url(r'^group/(?P<gid>\d+)/users/add/new/$','txUser.Views_Group.AddUsersToGroup'),
  #  url(r'^group/(?P<gid>\d+)/users/edit/$','txUser.Views_Group.EditUsers_Index'),

    
    # admin
   # url(r'^admin/$','txUser.UserViews.ListUsers'),
)               
