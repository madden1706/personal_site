

def debug_state():
    # WARNING: This needs to be update for deployment. 
    return True

def secret_key():
    return "lalalalalalalalalalalalalalalalalalalalala"

def hosts():
    DEBUG = debug_state()

    ALLOWED_HOSTS = []

    if DEBUG == True:
        ALLOWED_HOSTS = ["*"]
    elif DEBUG == False:
        ALLOWED_HOSTS = ["*"]

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


