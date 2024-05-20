import sys
from firebase import Firebase
from tenant import Tenant
from user_info import UserInfo


def main():
    """
    Utility to extract currently active email address for all users under a tenant.

    User accounts are stored as documents in Firestore, a cloud-based, NoSql database
    offering from Google.  User documents reside under the 'users' collection within
    a given tenant document, following the hierarchy:

      tenants/<tenant_id>/users/<user_id>/

    A user registers an account using an email address as their username; this email
    address can be different from the email they configure for electronic communication.

    This utility extracts the currently configured email address for each user under
    the specified tenant id.
    """
    try:
        # Get user input specified in the command line
        tenant_id, local_db = get_input_values()

        # Setup database client
        db = Firebase(local=local_db).db

        # Create tenant object, validating supplied tenant ids
        tenant = Tenant(tenant_id, db)

        # Extract all user emails on this tenant, saving them to a file
        extract_emails(tenant)

    except Exception as e:
        print(e)


def extract_emails(tenant: Tenant):
    UserInfo.save_all(tenant=tenant)


def get_input_values():
    """
    Read values supplied by the user via command-line args.

    Returns:
      tenant_id (str): Unique tenant identifier
      local_db (bool): true when connecting to local Firestore emulator,
                       false when connecting to prod
    """
    if len(sys.argv) == 3:
        tenant_id = sys.argv[2] if sys.argv[1] == "--prod" else sys.argv[1]
        local_db = sys.argv[1] != "--prod" and sys.argv[2] != "--prod"
        return tenant_id, local_db
    elif len(sys.argv) == 2:
        return sys.argv[1], True

    exit(f"\nUsage: {sys.argv[0]} <tenant_id> [--prod]\n")


if __name__ == "__main__":
    main()
