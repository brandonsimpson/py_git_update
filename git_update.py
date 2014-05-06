#!/usr/bin/env python
import os
import grp
import pwd
import subprocess

# update these settings to match your server settings
vhost_directory 	= '/home/'	# cpanel uses /home - most linux servers use a variation of /var/www/vhosts
git_pull_command 	= 'git pull origin dev --quiet'		# set to your preferred git pull command, and what branch to pull
show_all_output		= True

# don't change anything below here, unless of course you need to
for dirname, dirnames, filenames in os.walk(vhost_directory):

    # if /home/<username>/.git directory exists, run git pull as user
    if '.git' in dirnames:

        git_path = os.path.join(dirname, '.git')
        stat_info = os.stat(git_path)
        uid = stat_info.st_uid
        user = pwd.getpwuid(uid)[0]

        git_cmd = '/sbin/runuser -l ' + user + ' -c "cd ' + dirname + '; ' + git_pull_command + '"'

        proc = subprocess.Popen([git_cmd], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()

	if show_all_output == True:
        	print user, dirname
		print out
        	print
	else:
		# only show git pull output if updates were pulled
        	if "Already up-to-date." not in out:
        		print user, dirname
        	       	print out
