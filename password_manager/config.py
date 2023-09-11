"""
Variables "MASTER_KEYS_DB_FILE" and "MASTER_KEYS_DB_TYPE" specify the
file name and file type where the master key and 'iv' for encoding and
decoding information generated when the program was first started and when
the password was first added to the password manager.

Variables 'PASSWORDS_DB_FILE' and 'PASSWORDS_DB_TYPE' specify the name of the
file and the file type where the encrypted user password data will be stored.

You can change the file names to anything you like, but the file type must be
one of the supported types.
Currently supported database types (file types for storage): "json".
"""

MASTER_KEYS_DB_FILE = 'master_keys.json'
MASTER_KEYS_DB_TYPE = 'json'

PASSWORDS_DB_FILE = 'passwords_db.json'
PASSWORDS_DB_TYPE = 'json'
