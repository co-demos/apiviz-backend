#!/usr/bin/env python
# -*- encoding: utf-8 -*-

### good encoding of flash messages
### cf : https://stackoverflow.com/questions/8924014/how-to-handle-my-unicodedecodeerror
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

### import all from app.__init__
from . 	import *
from		flask 	import 	jsonify, flash, render_template, \
                  url_for, make_response, request, redirect, \
                  send_file

from .config_app.app_metas import app_metas
version = app_metas["version"]

# from 	werkzeug.security 	import 	generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### AUTH - TOKEN
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

########################################################################################
# Access token ### from prettyprinted youtube channel
"""
def token_required(f):
  @wraps(f)
  def decorated( *args, **kwargs ):

    token = None

    if 'x-access-token' in request.headers:
      token = request.headers['x-access-token']

    if not token:
      return jsonify({'message' : 'Token is missing!'}), 401

    try:
      data 			= jwt.decode(token, app.config['SECRET_KEY'])
      current_user 	= User.query.filter_by(public_id=data['public_id']).first()

    except:
      return jsonify({'message' : 'Token is invalid!'}), 401

    return f(current_user, *args, **kwargs)

  return decorated
"""


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### ERRORS HANDLERS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
@app.route("/error/<int:err_code>", defaults={ "error": BadRequest })
def errorHandler(error, err_code=400):

  if err_code == 404 : #  | error.code == 404 :
    error_code 	= 404
    template 		= "errors/404.html"

  elif err_code == 403 : # | error.code == 403 :
    error_code 	= 403
    template 		= "errors/403.html"

  elif err_code == 500 : # | error.code == 500 :
    error_code 	= 500
    template 		= "errors/500.html"

  else :
    error_code 	= 400
    template 		= "errors/400.html"

  app_config = getDocuments(mongo_config_global)

  return render_template(
    template,
    config_name			= config_name, # prod or default...
    site_section		= "error",
    error_code			= str(error_code),
    app_metas				= app_metas,
    app_config 			= app_config,
    language				= "fr" ,

    languages_dict	= app_languages_dict ,
    # error_msg				= u"accès interdit",
    # user_infos			= current_user.get_public_infos
  ), error_code




### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CONFIG ROUTES - BACKEND API
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

def DocOidToString(data):
  # log_app.debug("data : %s", data)
  obj = {}
  for key in data:
    if isinstance(data[key], ObjectId):
      obj[key] = str(data[key])
    else:
      obj[key] = data[key]
  # log_app.debug("obj : %s", obj)
  return obj

def getDocuments(collection, query={}, oid_to_id=True, as_list=False, field="field") :

  ### query collection and transform as list
  results = list(collection.find(query) )
  # log_app.debug("config app route / results - 1 : \n%s", pformat(results) )

  ### ObjectId to string
  if oid_to_id :
    results = [ DocOidToString(i) for i in results ]
    # log_app.debug("config app route / results - 2 : \n%s", pformat(results) )

  ### list to dict
  if as_list == False :
    results = { i[field] : i for i in results }
    # log_app.debug("config app route / results - 3 : \n%s", pformat(results) )

  return results

def getValueFromDictAndPathString(dictToSearch, path) : 
  """ 
  """ 
  print (" ")
  currentValue = dictToSearch
  path_splitted = path.split('/')
  while(len(path_splitted)):
    key = path_splitted.pop(0)
    currentValue = currentValue.get(key)
    if (type(currentValue) is not dict and len(path_splitted)):
      print("Path does not exist!")
      return None 

  return currentValue

  
def checkJWT(token, roles_to_check, uuid="", url_check="http://localhost:4100/api/auth/tokens/confirm_access"):
  """ 
  authenticate a token 
  sending request to the auth url / service 
  specified in config
  ... doing so to avoid middle man risk when editing
  """

  print (". "*50)

  # is_authorized = True

  ### set the collection to user
  mongoColl = mongoConfigColls['endpoints']
  auth_mode = app.config['AUTH_MODE']
  log_app.debug("checkJWT / auth_mode : %s", auth_mode )
  log_app.debug("checkJWT / roles_to_check : %s", roles_to_check )

  ### retrieving the root_url for authentication in general given the AUTH_MODE
  root_auth_doc = mongoColl.find_one({'apiviz_front_uuid': uuid, 'field' : 'app_data_API_root_auth'})
  # log_app.debug("checkJWT / root_auth_doc : \n%s", pformat(root_auth_doc) )

  auth_url = root_auth_doc['root_url'][auth_mode]
  log_app.debug( "checkJWT / auth_url : %s", pformat(auth_url) )

  ### retrieving the root_url and args for authentication
  confirm_auth_doc = mongoColl.find_one({'apiviz_front_uuid': uuid, 'field' : 'app_data_API_user_auth'})
  confirm_rooturl = confirm_auth_doc['root_url']
  confirm_user_role_path = confirm_auth_doc['resp_fields']['user_role']['path']
  log_app.debug( "checkJWT / confirm_user_role_path : %s", confirm_user_role_path) 

  confirm_basestring = auth_url + confirm_rooturl
  # log_app.debug( "checkJWT / confirm_basestring : %s", pformat(confirm_basestring) )
  
  confirm_options = confirm_auth_doc['args_options']
  confirm_token_arg = ''
  for arg in confirm_options : 
    if arg['app_arg'] == 'authToken' : 
      confirm_arg = '?{}={}'.format(arg['arg'], token)
  
  confirm_url = confirm_basestring + confirm_arg
  # log_app.debug( "checkJWT / confirm_url : %s", pformat(confirm_url) )

  ### send request to service and read response
  auth_response = requests.get(confirm_url)
  auth_response_status = auth_response.status_code
  log_app.debug( "checkJWT / auth_response_status : %s", auth_response_status )
  auth_response_data = auth_response.json()
  # log_app.debug( "checkJWT / auth_response : \n%s", pformat(auth_response_data) )

  ### get role to check value in response
  auth_response_user_role = getValueFromDictAndPathString(auth_response_data, confirm_user_role_path)
  log_app.debug( "checkJWT / auth_response_user_role : %s", auth_response_user_role) 


  print (". "*50)

  # return is_authorized
  return auth_response_user_role in roles_to_check or 'all' in roles_to_check

@app.route('/backend/api/config/<string:collection>/<string:doc_id>', methods=['GET','POST','DELETE'])
@app.route('/backend/api/config/<string:collection>', methods=['GET', 'POST'], defaults={"doc_id" : None})
# @app.route('/backend/api/config', methods=['GET'], defaults={'collection': 'global', "doc_id" : None})
def backend_configs(collection, doc_id=None):
  """
  Main route to GET and POST/PUT/DELETE
  choices 	: global | endpoints | styles | routes | socials
  variables : <collection> and <doc_id>
  arguments : as_list (bool), field (str)
  example 	: http://localhost:8100/backend/api/config?as_list=true
  """

  print ("")
  log_app.debug("config app route")
  log_app.debug("config app route / method : %s", request.method )
  log_app.debug("config app route / collection : %s", collection )
  log_app.debug("config app route / doc_id : %s", doc_id )

  ### target right config collection
  allowedCollections = ["global" , "footer", "navbar", "tabs", "endpoints" , "styles" , "routes", "socials" ]
  if collection in allowedCollections :
    mongoColl = mongoConfigColls[collection] ### imported from . (and from there from .api.__init__ )
  else :
    log_app.warning("error : -%s- is not a valid config collection (redirect)", collection)
    return redirect( "/error/400" )

  ### get request args if any
  apiviz_uuid = request.args.get('uuid',    default="", 	type=str)
  log_app.debug("config app route / apiviz_uuid : %s", apiviz_uuid )

  field 	= request.args.get('field', 	default='field', type=str)
  as_list = request.args.get('as_list', default=False,   type=bool)

  # role_to_check = request.args.get('role',    default='admin', type=str)
  roles_to_check = COLLECTIONS_AUTH_MODIFICATIONS[collection][request.method]
  log_app.debug("config app route / roles_to_check : %s", roles_to_check )

  # req_data 	  = request.data
  # log_app.debug("config app route / request.data : \n%s", pformat(request.data ))
  req_json    = request.get_json()
  log_app.debug("config app route / req_json : \n%s", pformat(req_json) )

  ### retrieve access token 
  token = request.args.get('token', default='', type=str)
  if req_json : 
    token = req_json.get('token', '')

  ### example of access token :
  # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTcwODI3OTQsIm5iZiI6MTU1NzA4Mjc5NCwianRpIjoiNjA4YWRhMDktMzA4My00ZmE1LTg1NDMtNjRkNDJmM2E4ZmZhIiwiZXhwIjoxNTU3MTI1OTk0LCJpZGVudGl0eSI6IjVjY2YzMmExODYyNmEwM2MzNmY1MzYzNCIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyIsInVzZXJfY2xhaW1zIjp7Il9pZCI6IjVjY2YzMmExODYyNmEwM2MzNmY1MzYzNCIsImluZm9zIjp7Im5hbWUiOiJFbGlub3IiLCJzdXJuYW1lIjoiT3N0cm9tIiwiZW1haWwiOiJlbGlub3Iub3N0cm9tQGVtYWlsbmEuY28iLCJwc2V1ZG8iOiJBbm9ueW1vdXMgVXNlciJ9LCJhdXRoIjp7InJvbGUiOiJndWVzdCIsImNvbmZfdXNyIjpmYWxzZX0sInByb2ZpbGUiOnsibGFuZyI6ImVuIiwiYWdyZWVtZW50IjpmYWxzZSwidXNyX3ZpZXciOiJtaW5pbWFsIiwidXNyX3Byb2ZpbGVzIjpbXX19fQ.Iux2Grzvv-6VBXzKME5ub31iLtl-LHYea_0JSdQ22eM

  ### filter out field arg to unique identifiers fields in documents
  if field not in ['_id', 'field'] :
    field = 'field'

  ### build basic query
  query = {'apiviz_front_uuid' : apiviz_uuid}
  if doc_id :
    query["_id"] = ObjectId(doc_id)

  log_app.debug("config app route / query : \n%s", query )


  ### check if token allows user to POST
  # if True : ### only for tests
  # if token != '' :
  #   log_app.debug("config app route / checking jwt..." )

  ### TO DO
  if request.method != 'GET':

    if request.method == 'POST':

      log_app.debug("config app route / POST" )

      query["_id"] = ObjectId(req_json['doc_id']) 
      log_app.debug("config app route / POST / query : \n%s", query )

      ### retrieve original document
      configDoc = mongoColl.find_one(query)
      log_app.debug("config app route / posT / configDoc : \n%s", pformat(configDoc) )
      
      is_authorized = checkJWT(token, roles_to_check, uuid=apiviz_uuid)

      if is_authorized and configDoc is not None :

        ### retrieve editionn config 
        doc_config = req_json['doc_config']
        doc_data = req_json['doc_data']
        log_app.debug("config app route / posT / doc_config : \n%s", pformat(doc_config) )
        
        ### not editable fields
        notAllowedFields = ['_id', 'apiviz_front_uuid', 'app_version', 'is_default']

        ### check if need for nested field update / f.i. navbar links
        editSubfield = False
        if doc_config['type'] == 'blocs_list' : 
          editSubfield = req_json['doc_subfield'].split('.')

        ### config edit specifics
        canAddKey = doc_config.get('canAddKeys', False) 
        canAddToList = doc_config.get('canAddToList', False) 
        canModifyKey = doc_config.get('canModifKeys', False) 

        ### target fields to update
        print() 
        update_query = {'$set' : {} }
        for k, v in doc_data.items() :
          # log_app.debug("config app route / posT / k:v : \n%s", pformat({k:v}) )
          # directly update field : for type == blocs || docs_list
          if canAddKey == False :
            if k not in notAllowedFields and k in [*configDoc] : 
              update_query['$set'][k] = v

          if canAddKey == False :
            if k not in notAllowedFields : 
              update_query['$set'][k] = v
          # print() 

        ### update version
        update_query['$set']['app_version'] = version
        log_app.debug("config app route / posT / update_query : \n%s", pformat(update_query) )

        ### save updated doc
        mongoColl.update_one(query, update_query)

        ### get back doc as updated
        updatedDoc = mongoColl.find_one(query)
        # log_app.debug("config app route / posT / updatedDoc : \n%s", pformat(updatedDoc) )

        formatedUpdatedConfig = DocOidToString(updatedDoc)
        # log_app.debug("config app route / posT / DocOidToString(updatedDoc) : \n%s", pformat( formatedUpdatedConfig ))
        # return "hello config master / POST ... praise be"
        return jsonify({
          'msg' : "the doc was updated",
          'query' : DocOidToString(query),
          'doc_updated' : formatedUpdatedConfig,
          'request' : req_json,
          })

      elif configDoc is None :
        return jsonify({ 
          "msg" : "noooope... can't find doc dammit....",
          'query' : DocOidToString(query),
          'request' : req_json,
        })

      else :
        return jsonify({ 
          "msg" : "noooope... you can't edit this ... mate",
          'query' : DocOidToString(query),
          'request' : req_json,
        })


    elif request.method == 'DELETE':

      log_app.debug("config app route / DELETE" )

      allowedCollsForDelete = [ "endpoints" , "routes" ]

      ### retrieve token from request and check it 
      req_data = json.loads(request.data)
      log_app.debug("config app route / req_data : \n%s", pformat(req_data) )
      token = req_data.get('token', '')

      is_authorized = checkJWT(token, roles_to_check, uuid=apiviz_uuid)

      if is_authorized and collection in allowedCollsForDelete :

        ### retrieve doc to delete to add to returned message
        configDoc = mongoColl.find_one(query)
        deletedDoc = DocOidToString(configDoc)

        ### delete doc 
        mongoColl.delete_one(query)

        return jsonify({
          'msg' : 'this doc was deleted',
          'query' : DocOidToString(query),
          'request' : req_json,
          'deleted_doc' : deletedDoc
        })

      else :
        return jsonify({ 
          'msg' : "noooope... not authorized to delete this ... mate ...",
          'query' : DocOidToString(query),
          'request' : req_json,
        })


  elif request.method == 'GET':

    app_config_dict = getDocuments(mongoColl, query=query, as_list=as_list, field=field)

    return jsonify( {
      "msg" 				: "this is the results from your query on the '%s' config collection" % collection,
      "query"				: query,
      "request"			: {
        "url" 				: request.url,
        "args" 				: request.args,
        "method"			: request.method,
        "collection"	: collection,
        "doc_id"			: doc_id,
      },
      "app_config" 	: app_config_dict
    } )


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### NEW CONFIG CREATION - BACKEND API
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

def getUuidDistinct(coll, uuid, distinctField):
  """
  Util to get a model's specs
  """
  # log_app.debug("getUuidDistinct / coll, uuid, distinctField : %s, %s, %s" %(coll, uuid, distinctField) )
  mongoColl = mongoConfigColls[coll]
  query = { 'apiviz_front_uuid' : uuid }
  results = mongoColl.find(query).distinct(distinctField)
  # log_app.debug("getUuidDistinct / results : %s", results )
  return results

def getUuidDocSubfield(coll, uuid, field, subField):
  """
  Util to get a model's subfield
  """
  mongoColl = mongoConfigColls[coll]
  query = { 'field' : field, 'apiviz_front_uuid' : uuid }
  result = mongoColl.find_one(query)
  log_app.debug("getUuidDocSubfield / result : %s", result )
  return result[subField]

@app.route('/backend/api/get_default_models', methods=['GET'])
def get_default_models():
  """
  Main route GET to get Apiviz uuids defined as usable models
  """

  print ("")
  log_app.debug("create_new_config")
  log_app.debug("create_new_config / method : %s", request.method )
  
  only_default = request.args.get('only_default', default=False, type=bool)

  models = None 

  ### check if uuid is new and not already used
  globalColl = mongoConfigColls['global']

  if only_default : 
    query = {'is_default' : True, 'can_be_used_as_model' : True }
  else :
    query = {'can_be_used_as_model' : True }

  results = list(globalColl.find(query, {'_id': 0 }))

  tempList = []
  if results : 
    for doc in results : 
      # trim fields
      model = get_config_model( doc['apiviz_front_uuid'], returnDict=True, noRemap=False)
      tempList.append(model)
    models = tempList

  # log_app.debug("create_new_config / models : \n%s", pformat(models) )

  return jsonify({
    'msg' : 'here comes the models defined as default and authorized to be copied',
    'models': models,
  })


@app.route('/backend/api/get_config_model/<string:uuid>', methods=['GET'])
def get_config_model(uuid, returnDict=False, noRemap=False):
  """
  Main route GET to retrive an existing Apiviz instance field : 'global/app_title'
  """

  print ("")
  log_app.debug("get_config_model")
  log_app.debug("get_config_model / method : %s", request.method )
  log_app.debug("get_config_model / uuid : %s", uuid )

  ### remapper
  responseFields = ['image_preview', 'apiviz_front_uuid', 'content', 'app_version']
  remapper = {
    'image_preview' : 'preview', 
    'apiviz_front_uuid' : 'uuid', 
    'content' : 'name',
    'app_version' : 'app_version'
  }

  ### disctincts to retrieve
  distinctFields = [
    { 'coll' : 'routes', 'field' : 'dynamic_template' },
    { 'coll' : 'endpoints', 'field' : 'endpoint_type' },
  ]

  ### specs to retrieve
  specsFields = [
    { 'coll' : 'global', 'field' : 'app_languages', 'subfield' : 'languages' },
    { 'coll' : 'styles', 'field' : 'app_colors', 'subfield' : 'content' },
  ]

  mongoCollGlobal = mongoConfigColls['global'] ### imported from . (and from there from .api.__init__ )
  
  query = { 'field' : 'app_title', 'apiviz_front_uuid' : uuid }

  model = mongoCollGlobal.find_one(query)
  log_app.debug("get_config_model / model : \n%s", pformat(model) )

  if model is not None : 
    model = DocOidToString(model)
    responseFields = ['image_preview', 'apiviz_front_uuid', 'app_version', 'content']
    if model['can_be_used_as_model'] == True : 
      msg = 'here is the model you requested'
      model_uuid = model['apiviz_front_uuid']
      if noRemap : 
        model = { k : v for k,v in model.items() if k in responseFields}
      else : 
        model = { remapper[k] : v for k,v in model.items() if k in responseFields }
      model['distincts'] = {}
      for distinct in distinctFields : 
        model['distincts'][distinct['field']] = getUuidDistinct(distinct['coll'], model_uuid, distinct['field'])
      model['specs'] = {}
      for spec in specsFields : 
        model['specs'][spec['field']] = { spec['subfield'] : getUuidDocSubfield(spec['coll'], model_uuid, spec['field'], spec['subfield']) }
    else : 
      msg = "you can't use this as a model"
      model = None
  else : 
    model = None
    msg = 'there is no model as requested'

  if returnDict == False :
    return jsonify({
      'msg' : msg,
      'req_uuid' : uuid,
      'query' : query,
      'model' : model 
    })
  else : 
    return model


@app.route('/backend/api/add_document/<string:collection>', methods=['POST','DELETE'])
def add_document(collection, testMode=True):
  """
  Main route POST to create a new document for an existing Apiviz instance
  """

  print ("")
  log_app.debug("add_document")
  log_app.debug("add_document / method : %s", request.method )

  req_json    = request.get_json()
  # log_app.debug("add_document / req_json : \n%s", pformat(req_json) )

  # role_to_check = request.args.get('role',    default='admin', type=str)
  roles_to_check = COLLECTIONS_AUTH_MODIFICATIONS[collection][request.method]
  log_app.debug("add_document / roles_to_check : %s", roles_to_check )

  allowedCollections = ["tabs", "endpoints" , "routes" ]
  ### not editable fields
  notAllowedFields = ['_id', 'apiviz_front_uuid', 'app_version', 'is_default']

  if request.method == 'POST' and collection in allowedCollections :
  
    log_app.debug("config app route / POST" )

    token = req_json.get('token', '')
    apiviz_uuid = req_json['apiviz_front_uuid']
    is_authorized = checkJWT(token, roles_to_check, uuid=apiviz_uuid)

    if is_authorized : 

      ### trim request doc from not allowed fields + add 
      newDocData = req_json['doc_data']
      newDoc = { k: v for k, v in newDocData.items() if k not in notAllowedFields}    
      newDoc['apiviz_front_uuid'] = apiviz_uuid
      newDoc['app_version'] = version
      newDoc['is_default'] = testMode

      # insert newdoc to collection
      mongoColl = mongoConfigColls[collection]
      addedDoc = mongoColl.insert_one(newDoc)

      log_app.debug("add_document / newDoc : \n%s", pformat(DocOidToString(newDoc)) )

      msg = "you added this document to the collection"
      respDoc = DocOidToString(newDoc)

      return jsonify({
        'msg' : msg,
        'request' : req_json,
        'new_doc' : respDoc
      })

    else : 
      msg = "you don't have the authorization level to add a new document"
      return jsonify({
        'msg' : msg,
        'request' : req_json,
      })
  
  else : 
    msg = "you can't add this document to this collection or the method is not allowed..."
    return jsonify({
      'msg' : msg,
      'request' : req_json,
    })


@app.route('/backend/api/create_new_config', methods=['POST','DELETE'])
def create_new_config():
  """
  Main route POST/DELETE to create a whole new Apiviz instance
  """

  print ("")
  log_app.debug("create_new_config")
  log_app.debug("create_new_config / method : %s", request.method )

  req_json    = request.get_json()
  log_app.debug("create_new_config / req_json : \n%s", pformat(req_json) )

  new_uuid = req_json['model_uuid']

  ### target right config collection
  allowedCollections = ["global" , "footer", "navbar", "tabs", "endpoints" , "styles" , "routes", "socials" ]
    
  if request.method == 'POST':

    log_app.debug("config app route / POST" )
    
    ### check if model can be used
    modelCheck = get_config_model(new_uuid, returnDict=True, noRemap=True)
    log_app.debug("create_new_config / modelCheck : \n%s", pformat(modelCheck) )

    ### check if uuid is new and not already used
    globalColl = mongoConfigColls['global']
    usedUuids = globalColl.distinct('apiviz_front_uuid')
    log_app.debug("create_new_config / usedUuids : \n%s", pformat(usedUuids) )
    
    modelIsUsed = new_uuid in usedUuids
    # modelIsUsed = False ### only for debugging
    log_app.debug("create_new_config / modelIsUsed : %s", modelIsUsed )

    canUseModel = modelIsUsed == False and modelCheck != None 
    log_app.debug("create_new_config / canUseModel : %s", canUseModel )

    ### start copying documents if allowed
    if canUseModel : 

      query = {'apiviz_front_uuid' : new_uuid}
      
      # loop collections
      for coll in allowedCollections : 
        
        # get corresponding documents without _id
        mongoColl = mongoConfigColls[coll]
        results = list(mongoColl.find(query, {'_id':0 } ))
        
        # replace 'apiviz_front_uuid' field's value by new_uuid
        # set 'is_default' field's value as False
        for doc in results :

          log_app.debug("create_new_config / coll-doc['field'] : %s-%s" %(coll,doc['field']) )
          
          doc['apiviz_front_uuid'] = new_uuid
          doc['is_default'] = False

          # specific cases
          if doc['field'] == 'app_title' : 
            doc['content'] = req_json['new_title']

          if doc['field'] == 'app_logo' : 
            doc['url'] = req_json['new_logoUrl']

        # save documents list back in collection
        mongoColl.insert(results)

        print()

        msg = 'your new website is ready'
        resp_code = 200
    
    else : 
      msg = 'errors : '
      if modelIsUsed :
        msg += 'your current uuid is already used... '
      if modelCheck == None : 
        msg += "you can't use this model.. "
      resp_code = 500
      log_app.debug("create_new_config / msg : %s", msg )

    return jsonify({
      'msg' : msg,
      'uuid' : new_uuid,
      'request' : req_json,
    })




  ### TO DO 
  elif request.method == 'DELETE' : 

    log_app.debug("config app route / DELETE" )
    
    return jsonify({
      'msg' : 'your apiviz instance has been deleted',
      'uuid' : new_uuid,
      'request' : req_json,
    })


  # not a POST nor a DELETE request
  else : 
    return jsonify({
      'msg' : 'there was an error during the process (method not allowed)',
      'uuid' : new_uuid,
      'request' : req_json,
    }), 500


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### FILES ROUTES
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


@app.route('/download/<file_ext>/<file_name>', methods=['GET'] ) # this is a job for GET, not POST
def download_file(file_ext, file_name):
  """
  send file from server
  """

  log_app.debug("file_name : %s ", 	file_name)
  log_app.debug("file_ext : %s ", 	file_ext)
  log_app.info("file_ext in AUTHORIZED_FILETYPES_LIST: %s", (file_ext in AUTHORIZED_FILETYPES_LIST) )


  if file_ext in AUTHORIZED_FILETYPES_LIST :

    file_mimetype 		= AUTHORIZED_FILETYPES_DICT[file_ext]["mimetype"]
    file_foldername 	= AUTHORIZED_FILETYPES_DICT[file_ext]["folder"]
    file_folder 		= "static/{}/".format(file_foldername)
    file_name_ext 		= "{}.{}".format(file_name, file_ext)
    full_filepath 		= file_folder + file_name_ext

    try :

      return send_file(	full_filepath,
                mimetype			= file_mimetype,
                attachment_filename	= file_name_ext,
                as_attachment		= True
              )
    except :

      log_app.error("downloading this file is not working: %s.%s ", file_name, file_ext )

      return redirect(url_for('home'))

  else :

    log_app.error("downloading this file is not authorized: %s.%s ", file_name, file_ext )

    return redirect(url_for('home'))
