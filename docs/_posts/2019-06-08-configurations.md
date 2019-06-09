---
title : API - configurations
categories:
  - api
tags:
  - documentation
  - configuration
  - api
toc: true
toc_label: " contents"
toc_sticky: true
---

--------

The API for Apiviz configurations

--------

## CONFIGURATION COLLECTIONS AND DOCUMENTS

### BASE URLs

#### Collection level

```sh
curl 'http:/localhost:8100/backend/api/config/<string:collection>?<args>'
```

or 

```sh
curl --header "Content-Type: application/json" \
  --request POST \
  --data '<payload>' \
  'http:/localhost:8100/backend/api/config/<string:collection>?<args>'
``` 

- methods : `GET`, `POST`
- variables : 
  - `<string:collection>` : the name of the collection in the database


#### Document level

```sh
curl 'http:/localhost:8100/backend/api/config/<string:collection>/<string:doc_id>?<args>'
``` 

or

```sh
curl --header "Content-Type: application/json" \
  --request POST | DELETE \
  --data '<payload>' \
  'http:/localhost:8100/backend/api/config/<string:collection>/<string:doc_id>?<args>'
``` 

- methods : `GET`, `POST`, `DELETE`
- variables
  - `<string:collection>` : the name of the collection in the database
  - `<string:doc_id>` : the obejct ID (as string) of a document in a collection

--------

### GET METHOD

#### arguments

- `uuid` : your model's uuid
- `token` : your user's acces token
- `field` : retrieve results corresponding to this field name
- `as_list` : retrieve results as a list of documents

#### examples


--------

### POST METHOD

#### payload structure

#### arguments

- `uuid` : your model's uuid
- `token` : your user's acces token
- `field` : retrieve results corresponding to this field name

#### examples


--------

### DELETE METHOD

#### payload structure

#### arguments

- `uuid` : your model's uuid
- `token` : your user's acces token

#### examples


--------


## ADD DOCUMENT TO A COLLECTION

### BASE URLs

```sh
curl --header "Content-Type: application/json" \
  --request POST | DELETE \
  --data '<payload>' \
  'http:/localhost:8100/backend/api/add_document/<string:collection>'
``` 

- methods : `POST`, `DELETE`
- variables : 
  - `<string:collection>` : the model's UUID (as string)

--------

### POST METHOD

#### payload structure

#### examples


--------

### DELETE METHOD

#### payload structure

#### examples

