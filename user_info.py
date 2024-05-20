import os
import csv
from datetime import datetime
from tenant import Tenant


class UserInfo:
  """
  A class to save user information as a CSV file to the file system.
  """
  output_dir = "emails"
  base_filename = "user_info"

  @classmethod
  def save_all(cls, tenant: Tenant):
    # Get output file to save user info
    output_csv = UserInfo.get_output_file()

    # Initialize a CSV writer
    with open(output_csv, "w", newline="", encoding="utf-8") as csv_file:
      field_names = ["first_name", "email"]
      csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
      csv_writer.writeheader()

      def save_user_info(first_name: str, email: str):
        print(f"First name {first_name}, email: {email}")
        csv_writer.writerow({"first_name": first_name, "email" : email})

      # Retrieve user information from tenant, saving each record as it is fetched from the server
      tenant.extract_emails(save_user_info)


  @classmethod
  def get_output_file(cls):
    """
    Returns path to the output file with a uniquely generated name using timestamp
    """
    if not os.path.exists(UserInfo.output_dir):
      os.makedirs(UserInfo.output_dir)

    timestamp = datetime.now().strftime("%b-%d-%Y.%H:%M:%S")

    return f"{UserInfo.output_dir}/{UserInfo.base_filename}.{timestamp}"

    
