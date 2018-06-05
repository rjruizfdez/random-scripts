import os, sys, getpass

aes_password="ricardo"
keypath="keys"


def decrypt_(fname):
	os.system("openssl aes-256-cbc -pass pass:"+aes_password+" -in "+fname+" -d -out "+fname+".1")
	os.system("openssl rsautl -decrypt -inkey "+keypath+"/private_unencrypted.pem -in "+fname+".1 -out "+fname+".2")
	os.system("openssl aes-256-cbc -pass pass:"+aes_password+" -in "+fname+".2 -d -out "+fname+".3")
	os.system("mv "+fname+".3 $(echo "+fname+".3 | sed 's/.enc.3//')")
	os.system("rm "+fname+"")
	os.system("rm "+fname+".1")
	os.system("rm "+fname+".2")


def dec_files(dir_):
	onlyfiles = [f for f in os.listdir(dir_) if os.path.isfile(os.path.join(dir_, f))]
	for f in onlyfiles:
		file=os.path.join(dir_, f)
		print "Decrypting",file,"..."
		decrypt_(file)


def loop(looped_dir):
	#Files in the root dir
	dec_files(looped_dir)
	#Directories inside
	for root,directories,filenames in os.walk(looped_dir):
		for directory in directories:
			dir=os.path.join(root, directory)
			if directory not in excluded_dirs:
				print "Entering",dir,"..."
				dec_files(dir)


loop(sys.argv[1])