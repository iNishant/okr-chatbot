import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import os

cred = credentials.Certificate(os.environ['FIREBASE_CREDENTIALS_FILE_PATH'])
firebase_admin.initialize_app(
    cred, { 'projectId': os.environ['FIREBASE_PROJECT_ID'] }
)
db = firestore.client()
usersRef = db.collection('users')


def createOrGetUser(userEmail):
    userRef = None
    query = usersRef.where('email', '==', userEmail).get()
    for d in query:
        userRef = usersRef.document(d.id)
        break  # will be one item at max
    if not userRef:
        userRef = usersRef.document()  # create new document ref
        userRef.set({
            'email': userEmail,
        })
    return userRef


def createNewOKR(okrBody, userEmail):
    userRef = createOrGetUser(userEmail)
    okrRef = userRef.collection('okrs').document()  # new okr document ref
    okrRef = okrRef.set({
        'body': okrBody,
        'timestamp': time.time(),
    })
    return okrRef


def updateExistingOKR(okrId, newOkrBody, userEmail):
    userRef = createOrGetUser(userEmail)
    okrRef = userRef.collection('okrs').document(okrId)
    okrRef.update({
        'body': newOkrBody,
    })

def deleteExistingOKR(okrId, userEmail):
    userRef = createOrGetUser(userEmail)
    okrRef = userRef.collection('okrs').document(okrId)
    okrRef.delete()


def listOKRs(userEmail):  # returns array of okrs with ids included
    userRef = createOrGetUser(userEmail)
    query = userRef.collection('okrs').get()
    result = []
    for d in query:
        okrDict = d.to_dict()
        okrDict['id'] = d.id
        result.append(okrDict)
    return result