import pprint
from typing import Callable
# from user import User
# from device_token import DeviceToken

"""
A Function taking as parameters a user's first name and email.
"""
UserInfoCallback = Callable[[str,str], None]

class Tenant:
  """
  In-memory representation of a tenant Firestore document.

  A tenant is a container for a group of user accounts.  Each tenant
  document resides under the root collection in the database at:

    tenants/<tenant_id>

  where <tenant_id> uniquely identifies the tenant document.
  """

  def __init__(self, tid, db):
    self.tid = tid
    self.db = db
    self.__validate_tid()


  def __validate_tid(self):
    """
    Ensures that the tenant id exists in the database.
    """
    doc_ref = self.db.collection("tenants").document(self.tid)
    doc = doc_ref.get()
    if not doc.exists:
        raise ValueError(f"Invalid tenant_id {self.tid}")


  def __str__(self):
    return f"({self.tid})"
  

  def extract_emails(self, onUserInfo: UserInfoCallback):
    docs = self.db.collection(f"tenants/{self.tid}/users").get()
    if not docs:
      raise Exception("No users found on this tenant")
    
    for doc in docs:
      data = doc.to_dict()
      onUserInfo(data["firstName"], data["email"])
 