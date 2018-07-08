import base64
import os
import time
import string
import logging

logging.basicConfig(filename='/nsr/logs/nsrpasswd.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s:%(process)d')

print("\n##########################################")
print("# NSRPASSWD - NMC Password Reset Utility #")
print("##########################################")


passwd = raw_input("\nEnter the password: ")

#--------------------------------------#
# Converting raw text to encoded string:#
#---------------------------------------#

print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
encoded_passwd = base64.b64encode(passwd)
logging.info("\nConverting password to encoded format: Done.")


#------------------#
# Read in the file:#
#------------------#

with open('C:\\Program Files\\EMC NetWorker\\nsr\\authc-server\\scripts\\authc-local-config.json.template', 'r') as file:
    filedata = file.read()
time.sleep(60)^Crompt in 60 seconds...')d to validate your new password: authc_mgmt -u administrator -p "replace_with_new_password" -e find-all-users')
[root@oracle12c backups]# cat
[root@oracle12c backups]# cat nsrpasswd.py
import base64
import os
import time
import string
import logging

logging.basicConfig(filename='/nsr/logs/nsrpasswd.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s:%(process)d')

print("\n##########################################")
print("# NSRPASSWD - NMC Password Reset Utility #")
print("##########################################")


passwd = raw_input("\nEnter the password: ")

#--------------------------------------#
# Converting raw text to encoded string:#
#---------------------------------------#

print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
encoded_passwd = base64.b64encode(passwd)
logging.info("\nConverting password to encoded format: Done.")


#------------------#
# Read in the file:#
#------------------#

with open('C:\\Program Files\\EMC NetWorker\\nsr\\authc-server\\scripts\\authc-local-config.json.template', 'r') as file:
    filedata = file.read()
logging.info("Reading the 'authc-local-config.json.template' file: Done.")

#---------------------------#
# Replace the target string:#
#---------------------------#

filedata = filedata.replace('your_username', 'administrator')
filedata = filedata.replace('your_encoded_password' ,encoded_passwd)
logging.info("Replacing the encoded password to the file: Done.")

#--------------------------#
# Write the file out again:#
#--------------------------#

with open('C:\\Program Files\\EMC NetWorker\\nsr\\authc-server\\tomcat\\conf\\authc-local-config.json', 'w') as file:
      file.write(filedata)
      logging.info("Saving file to 'C:\Program Files\EMC NetWorker\nsr\authc-server\tomcat\conf\authc-local-config.json': Done.\n")
      print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

#----------------------------------#
# Shutting down NetWorker Services:#
#----------------------------------#
print(string.upper("For the changes to be applied, restart of NetWorker service is mandate.\n"))
os.system('net stop nsrexecd')
print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

time.sleep(15)

#----------------------------------#
# Starting down NetWorker Services:#
#----------------------------------#
logging.info(string.upper("starting networker services:\n"))
os.system('net start nsrd')
os.system('net start gstd')

time.sleep(60)
print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
logging.info('Password Reset Complete!\n')
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
print('\nKindly use the following command to validate your new password: authc_mgmt -u administrator -p "replace_with_new_password" -e find-all-users')
print('Exiting prompt in 60 seconds...')
time.sleep(60)
