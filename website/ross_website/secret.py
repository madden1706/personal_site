import os

# Defaults the DEBUG states to false.
if 'DEBUG' in os.environ:
    print(os.environ['DEBUG'])
else:
    os.environ['DEBUG'] = "True"
    print('Set: ', os.environ['DEBUG'])

def debug_state():
    
    debug = os.environ['DEBUG']
    state = ''

    if debug == 'True':
        state = True
    elif debug == 'False':
        state = False

    return state
    

# DEBUG = debug_state()

def secret_key():

    key = ''

    if os.environ['DEBUG'] == 'True':
        key = "lalalalalalalalalalalalalalalalalalalalala"
    elif os.environ['DEBUG'] == 'False':
        key = os.environ['SECRET_KEY']

    return key

def hosts():    

    ALLOWED_HOSTS = []

    if os.environ['DEBUG'] == 'True':
        ALLOWED_HOSTS = ["*"]
    elif os.environ['DEBUG'] == 'False':
        ALLOWED_HOSTS = ['.herokuapp.com']
        #os.environ['ALLOWED_HOSTS'].split('|')

    return ALLOWED_HOSTS

# files:
#     "/etc/httpd/conf.d/ssl_rewrite.conf":
#         mode: "000644"
#         owner: root
#         group: root
#         content: |
#             RewriteEngine On
#             <If "-n '%{HTTP:X-Forwarded-Proto}' && %{HTTP:X-Forwarded-Proto} != 'https'">
#             RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [R,L]
#             </If>


#     "/etc/httpd/conf.d/www_rewrite.conf":
#         mode: "000644"
#         owner: root
#         group: root
#         content: |
#             RewriteEngine On
#             <If"'%{HTTP_HOST}' !~ /^www\./" >
#             RewriteRule ^ (.*)$ http: // www. % {HTTP_HOST} % {REQUEST_URI}[R =Permanent, L]
#             </If >


