# Email Extractor
 A small utility program to extract user emails from a Firebase database.

 ## Description
User accounts are stored as documents in Firestore, a cloud-based, NoSql database offering from Google.  

User documents reside under the _users_ collection within
    a given tenant document, following the hierarchy:

      tenants/<tenant_id>/users/<user_id>/

A user registers an account using an email address as their username; this email address can be different from the email they configure for electronic communication.

This utility extracts the currently configured email address for each user under the specified tenant id.

## Usage
```
python main.py <tenant_id> [--prod]
```
where:
- _tenant_id_ --> unique identifier of the tenant document containing user accounts
- _--prod_ --> optional flag indicating target Firestore database is production.  By default, target database assumed is the local Firebase Emulator db.

