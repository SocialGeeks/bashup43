# Shellshock bash upgrade script

Upgrades version of bash found in $PATH with 4.3.27(1)-release which is the lastest official major/minor/patch level.  

* Upgrade shell script: https://gist.github.com/sgviking/7bb38938187e36308175  

## Requirements/Assumptions  

### Host machine  

* python2  
* python fabric library  

### Server being updated  

* wget  
* build tools  
* gpg  
* tar  
* sudo access  

### SELinux Warning  

I hacked in quick support for SELinux systems into the above upgrade shell script.  Being far from an SELinux expert you should double check my work if you are running systems with SELinux enabled. Previously the upgrade script, when ran on a SELinux enabled system, would lock you out because of the change to bash.  The new script turns off SELinux, installs bash, reapplies the proper context label and turns on SELinux.   

## Using fabric script  

The fabric script (fabfile.py) includes two functions: version and bashup  

### Setting up python virtual environment  

	git clone https://github.com/SocialGeeks/bashup43.git  
	cd bashup43/  
	virtualenv -p python2 .  
	source bin/activate  
	pip install -r requirements.txt  


### Updating multiple hosts (roles)  

You can edit fabfile.py and your hosts into env.roledefs.  The roledefs can be named anything you want and you can create as many or few hosts and roledefs as needed.  

	fab version -R rolename | tee rolename_version.log  
	fab bashup -R rolename | tee rolename_bashup.log  
	# verify script worked  
	fab version -R rolename  

### Updating single host  

	fab version -H [IP_ADDRESS]   
	fab bashup -H [IP_ADDRESS]  
	# verify script worked  
	fab version -H [IP_ADDRESS]  

