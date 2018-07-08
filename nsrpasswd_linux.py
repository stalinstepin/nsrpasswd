import base64
import os
import logging

logging.basicConfig(filename='/nsr/logs/nsrpasswd.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s:%(process)d')

print("\n##########################################")
print("# NSRPASSWD - NMC Password Reset Utility #")
print("##########################################")
print("\nNOTE: Running this executable will stop the NetWorker Server process at the end, for the changes to be applied.\n")


# Sets to simplify if/else in determining correct answers.
yesChoice = ['yes', 'y']
noChoice = ['no', 'n']

# Prompt the user with a message and get their input.
# Convert their input to lowercase.
input = raw_input("Would you like to continue? (y/N) ").lower()

# Check if our answer is in one of two sets.
if input in yesChoice:
    # call method
    passwd = raw_input("Enter the new password: ")

#---------------------------------------#
# Converting raw text to encoded string:#
#---------------------------------------#

encoded_passwd = base64.b64encode(passwd)
#logging.info("\nThe encoded password is: ",encoded_passwd)
logging.info("Converting password to encoded format: Done.")

#------------------#
# Read in the file:#
#------------------#

with open('/opt/nsr/authc-server/scripts/authc-local-config.json.template', 'r') as file :
  filedata = file.read()
  logging.info("Reading the 'authc-local-config.json.template' file: Done.")

#---------------------------#
# Replace the target string:#
#---------------------------#


filedata = filedata.replace('your_username', 'administrator')
filedata = filedata.replace('your_encoded_password',encoded_passwd)
logging.info("Replacing the encoded password to the file: Done.")

#--------------------------#
# Write the file out again:#
#--------------------------#

with open('/nsr/authc/conf/authc-local-config.json', 'w') as file:
  file.write(filedata)
  logging.info("Saving file: Done.")

#--------------------------------------#
# Modifying the permission of the file:#
#--------------------------------------#


os.system('chmod 755 /nsr/authc/conf/authc-local-config.json')
logging.info("Modifying file permission: Done.")

#----------------------------------#
# Shutting down NetWorker Services:#
#----------------------------------#

os.system('nsr_shutdown > /dev/null 2>&1')
logging.info("Shutting down NetWorker services: Done.")

print("\nKindly start the NetWorker services and try logging in to NMC with the new password!")

if input in noChoice:
    print("Exiting the program")
