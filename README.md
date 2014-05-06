Multi-site Python Git Updater
=============

This script allows you run a single command and update all of your various git repositories within your web directory.

Run it from a cronjob and automate your development server syncing with your git dev repos. I don't recommend running this in a production environment.

Originally created to handle auto-pulling git dev repos for various cpanel accounts on a single server.

Wherever you point the script to where your virtual hosts are located, it will scan the sub-folders for .git directories and attempt to git pull as the owner of that directory. The working virtual host directories must already be initialized with git and tested working properly. This script does not initialize or clone your git repos.


Usage
============

1) clone the py_git_update repo to your /root directory. 

2) edit py_git_update/git_update.py and set your settings as outline below

3) run as root: python py_git_update/git_update.py

You will need to run this as root in order for you to access multiple virtual host directories which are owned by vps account holders. The directories initialized with git should be initialized using the virtual host's user account to keep file permissions sane. You don't want root to own all of your .git directories and pull new files down with only root permission. And if you use suPHP, the client sites will not run if the owner/group permissions are not setup correctly.


Configuration
=============

set your virtual host directory location to scan for .git repos
cpanel uses /home/<account>/public_html - so set this to /home/
if you server your virtual hosts from /var/www/vhosts/<account>/html - you'd set this to /var/www/vhosts/

vhost_directory         = '/home/'


set your preferred git pull command and which branch to pull
remove the --quiet flag to get full git output

git_pull_command        = 'git pull origin dev --quiet'


Set show_all_output to True if you want to see output of which directoreis are being pulled. Setting to False will only output results of git pulls that resulted in new updates

show_all_output         = True


Cron Example
=============

Run git_update.py every 15 minutes, Mon - Fri, 8am - 6pm. Output to git_update.log file

*/15 08-18 * * 1-5 /usr/bin/python /root/git_update.py > /root/git_update.log 2>&1

