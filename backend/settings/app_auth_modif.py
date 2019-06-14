# -*- encoding: utf-8 -*-

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CHOICES ONLY FOR ADMIN
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


""" 
available roles

"admin"     : { "help" : "can access all backoffice (lox level access)" },
"staff"     : { "help" : "can access backoffice (high level access)" },
"registred" : { "help" : "registred user" },
"guest"     : { "help" : "logged but not registred" },
"anonymous" : 
"""

APIVIZ_INSTANCE_AUTH = {
  "is_public" : {
    'POST'    : ['super_admin',  'admin'], 
    'DELETE'  : ['super_admin',  'admin'], 
    'GET'     : ['all']
  },
  "is_private" : {
    'POST'    : ['super_admin', 'admin', 'staff'], 
    'DELETE'  : ['super_admin', 'admin'], 
    'GET'     : ['super_admin', 'admin', 'staff', 'guest']
  }
}

COLLECTIONS_AUTH_MODIFICATIONS	= {
  "global"    : {
    'POST'    : ['super_admin',  'admin'], 
    'DELETE'  : ['super_admin',  'admin'], 
    'GET'     : ['all']
  },
  "endpoints" : {
    'POST'    : ['super_admin',  'admin'], 
    'DELETE'  : ['super_admin',  'admin'], 
    'GET'     : ['all']
  },
  "routes"    : {
    'POST'    : ['super_admin',  'admin'], 
    'DELETE'  : ['super_admin',  'admin'], 
    'GET'     : ['all']
  },
  "footer"    : {
    'POST'    : ['super_admin',  'admin', 'staff'], 
    'DELETE'  : ['super_admin',  'admin'], 
    'GET'     : ['all']
  },
  "navbar"    : {
    'POST'    : ['super_admin',  'admin', 'staff'], 
    'DELETE'  : ['super_admin',  'admin'], 
    'GET'     : ['all']
  },
  "tabs"    : {
    'POST'    : ['super_admin',  'admin', 'staff'], 
    'DELETE'  : ['super_admin',  'admin'], 
    'GET'     : ['all']
  },
  "styles"    : {
    'POST'    : ['super_admin',  'admin', 'staff'], 
    'DELETE'  : ['super_admin',  'admin'], 
    'GET'     : ['all']
  },
  "socials"   : {
    'POST'    : ['super_admin',  'admin', 'staff'], 
    'DELETE'  : ['super_admin',  'admin'], 
    'GET'     : ['all']
  },
}

