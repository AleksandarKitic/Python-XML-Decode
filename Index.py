# URL, EMAIL DECODE IN THE XML FILE
import random
import time
from xml.dom import minidom
import string

# CLASS FOR DECODE URL AND EMAIL IN XML FILE!


class InsertingUrl:
    # DEF __INIT__ IS FOR MAKING VARIABLES FOR ALL DEFS

    def __init__(self, url, email_user, decode_url, decode_email):
        self.url = url
        self.email_user = email_user
        self.decode_url = decode_url
        self.decode_email = decode_email
    # HERE WE GETTING URL AND STARTING CLASS

    def insert_url(self):
        # IN THIS DEF WE MAKE DECODE GENERATOR FOR OUR URL AND EMAIL
        def generator(size=40, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
            return ''.join(random.choice(chars) for _ in range(size))

        self.decode_url = generator()
        self.decode_email = generator()

        def encode_secret_token():
            getting_url = input('Insert url: ')
            getting_email = input('Insert email: ')

            print('Getting url..')
            time.sleep(1)
            print('Getting email..')
            time.sleep(1)

            self.url = getting_url
            self.email_user = getting_email

            if self.decode_url != self.url:
                password_decode = self.decode_url
                self.url = password_decode
                print(f'Url secret token: {self.url}, Url:{getting_url}')

            if self.decode_email != self.email_user:
                email_password_decode = self.decode_email
                self.email_user = email_password_decode
                print(f'Email secret token: {self.email_user}, Email:{getting_email}')

            print('-' * 30)
            print('Exporting data..')
            time.sleep(1)
            print('Writing data in xml file..')
            time.sleep(1)
            print('Done!')

            root = minidom.Document()

            xml = root.createElement('Url_and_Email_decode')
            root.appendChild(xml)

            userinfochild = root.createElement('Url')
            userinfochild.setAttribute('secret_token', self.url)

            userinfochild1 = root.createElement('Email')
            userinfochild1.setAttribute('secret_token', self.email_user)

            xml.appendChild(userinfochild)
            xml.appendChild(userinfochild1)

            xml_str = root.toprettyxml(indent='\t')

            save_path_file = 'url_email.xml'

            with open(save_path_file, 'w') as f:
                f.write(xml_str)

        encode_secret_token()


start_app = InsertingUrl('', '', '', '')
start_app.insert_url()
