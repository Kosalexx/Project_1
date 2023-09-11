from faker import Faker
from faker.providers import lorem
from typing import Optional
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib

from config import (MASTER_KEYS_DB_FILE, MASTER_KEYS_DB_TYPE,
                    PASSWORDS_DB_FILE, PASSWORDS_DB_TYPE)

from providers import provide_db, provide_passwords_file


master_key_db = provide_db(MASTER_KEYS_DB_FILE, MASTER_KEYS_DB_TYPE)
passwords_db = provide_db(PASSWORDS_DB_FILE, PASSWORDS_DB_TYPE)


class MasterKey:
    """Generates a database to store the master key on the first run"""
    def __init__(self) -> None:
        self.key: str = self._generate_key()

    def _generate_key(self) -> str:
        """Generates a database to store the master key on the first run"""
        try:
            exist_key = master_key_db.key_exist()
        except FileNotFoundError:
            master_key_db.write_data(data_dict={}, mode='w')
            exist_key = master_key_db.key_exist()
        if exist_key is None:
            fake = Faker()
            fake.add_provider(lorem)
            random_string: str = ''.join(fake.words())
            result: str = random_string
            print(f'The master key was generated: "{result}".')
            print('Please remember it!')
            field = 'key'
            data_dict: dict[str, str] = {
                field: result
            }
            master_key_db.write_data(data_dict, mode='w')
        else:
            result = exist_key
        return result


class AESCoder:
    """Designed to encryption and decryption data.

    :param master_key: master-key for encryption and decryption information
    :type master_key: str
    """
    def __init__(
            self,
            master_key: str
            ) -> None:
        self.master_key = master_key
        self.byte_master_key = hashlib.sha256(
            self.master_key.encode("utf-8")).digest()
        self.iv: Optional[str] = self._get_iv()

    def _get_iv(self) -> Optional[str]:
        """Gets IV (Initialization vector) from the database.

        :rtype: Optional[str]
        :return: Initialization vector for encryption and decryption.
        """
        exist_data = master_key_db.read_data()
        exist_iv = exist_data.get('iv')
        return exist_iv

    def encrypt_data(self, data: str) -> str:
        """Encrypts data using the AES256 algorithm.

        :param data: data that must be encrypted
        :type data: str

        :rtype: str
        :result: encrypted data
        """
        byte_data: bytes = data.encode()
        if self.iv is None:
            cipher = AES.new(
                key=self.byte_master_key, mode=AES.MODE_CBC)
            res_iv: str = base64.b64encode(cipher.iv).decode('utf-8')
            data_dict: dict[str, str] = {
                'iv': res_iv
            }
            master_key_db.write_data(data_dict=data_dict, mode='a')
            self.iv = res_iv
        else:
            iv: bytes = base64.b64decode(self.iv)
            cipher = AES.new(
                key=self.byte_master_key, mode=AES.MODE_CBC, iv=iv)
        cipher_text_b = cipher.encrypt(pad(byte_data, AES.block_size))
        result = base64.b64encode(cipher_text_b).decode('utf-8')
        return result

    def decrypt_data(self, cipher_text: str) -> str:
        """Decrypts data using the AES256 algorithm.

        :param cipher_text: data that must be decrypted
        :type cipher_text: str

        :rtype: str
        :result: decrypted data
        """
        str_iv: str = str(self.iv)
        iv = base64.b64decode(str_iv)
        cipher = AES.new(self.byte_master_key, AES.MODE_CBC, iv)
        password = unpad(cipher.decrypt(base64.b64decode(cipher_text)),
                         AES.block_size)
        return password.decode()


class PasswordManager(AESCoder):
    """Designed to work with password data.

    Used to save passwords to a database, retrieve from a database, delete,
    export all passwords to a file.

    :param master_key: master-key for encryption and decryption information
    :type master_key: str
    """
    def __init__(self, master_key: str) -> None:
        super().__init__(master_key)
        self._create_storage()

    def _create_storage(self) -> None:
        """Creates a database file at the first start of the program."""
        try:
            passwords_db.read_data()
        except FileNotFoundError:
            passwords_db.write_data(data_dict={}, mode='w')

    def add_new_password(
            self,
            identifier: str,
            password: str
            ) -> None:
        """Adds the encrypted password to the database.

        :param identifier: identifier of added password
        :type identifier: str
        :param password: added to the database password
        :type password: str
        """
        res = self.encrypt_data(password)
        data_dict: dict[str, str] = {
            identifier: res
        }
        passwords_db.write_data(data_dict=data_dict, mode='a')

    def get_password(
            self,
            identifier: str
            ) -> str:
        """Gets concrete decrypted password from database.

        :param identifier: identifier of searched password
        :type identifier: str

        :rtype: str
        :return: the password you are looking for, or a message telling you
                 there is no password
        """
        exist_data = passwords_db.read_data()
        if exist_data.get(identifier) is None:
            result: str = (f'There are no passwords for "{identifier}" '
                           'ID in the database.')
        else:
            cipher_pass = exist_data[identifier]
            result = self.decrypt_data(cipher_pass)
        return result

    def get_id_list(self) -> str:
        """Returns information about identifiers available in the database.

        :rtype: str
        :return: string info about identifiers available in the database
        """
        data = passwords_db.read_data()
        result = '| '
        for identifier in data.keys():
            result += str(identifier)
            result += ' | '
        return result

    def delete_password(self, identifier: str) -> str:
        """Deletes password from the database.

        :param identifier: identifier of deleted password
        :type identifier: str

        :rtype: str
        :return: information about the successful deletion of the
        information or the absence of the password with the passed
        identifier in the database.
        """
        data = passwords_db.read_data()
        if data.get(identifier) is None:
            result = (f'There is no password with the identifier'
                      f'"{identifier}" in the database.')
        else:
            data.pop(identifier)
            result = (f'The password for "{identifier}" has been deleted.')
        passwords_db.write_data(data_dict=data, mode='w')
        return result

    def export_passwords_to_file(self, file_format: str) -> None:
        """Exports all existing passwords to a file of the selected type.

        :param file_format: type of file in which passwords will be exported
        :type file_format: str
        """
        export_file = provide_passwords_file(file_type=file_format)
        data = passwords_db.read_data()
        result: dict[str, str] = {}
        for key, value in data.items():
            result[key] = self.decrypt_data(value)
        export_file.create_export_file(result)
