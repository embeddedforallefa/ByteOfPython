import os
import time

# 1. The files and directories to be backed up are
# specified in a list
# Example on windows:
source = ['"C:\\Users\VEERESH\Documents"']
# Example on linux:
# source = ['/Users/vee/notes']
# Notice we have to use double quotes inside a string
# for names with spaces in it. We could have also used
# a raw string by writing [r'C:\My Documents'].

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
target_dir = 'H:\\Backup'
# Example on Mac OS X and Linux:
# target_dir = '/Users/swa/backup'
# Remember to change this to which folder you will be using

# 3. The files are backed up in to a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create a target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # make directory

# 5. We us the zip command to put the files in a zip archive
zip_commad = 'zip -r {0}, {1}'.format(target, ' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_commad)
print('Running....')
if os.system(zip_commad) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')