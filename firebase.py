# import grpc

# from google.cloud.firestore_v1.gapic import firestore_client
# from google.cloud.firestore_v1.gapic.transports import firestore_grpc_transport
# from google.cloud.firestore_v1.services.firestore.client import FirestoreClient
# from google.cloud.firestore_v1.services.firestore.transports import FirestoreGrpcTransport

import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Firebase():
  """
  Initialize Firebase client with appropriate credentials for remote server access.

  The 'serviceAccount.json' contains various pieces of project metadata, including
  private key information for remote server access.  This is highly sensitive information,
  not to be distributed nor stored publicly (ie Version Control System).

  Args:
    local (bool): true when using local Firebase emulator, false otherwise
  """
  def __init__(self, local=True):
    if local:
      # Ensure environment variable to access firestor emulator has been set
      if not os.environ.get("FIRESTORE_EMULATOR_HOST"):
        raise Exception("FIRESTORE_EMULATOR_HOST environment variable not set - can't access Firebase Emulator")

    cred = credentials.Certificate("serviceAccount.json")
    firebase_admin.initialize_app(cred)
    self.db = firestore.client()

