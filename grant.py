import os
import pwd
import stat

# version of linux
os.system("uname -a")

# user name
print(os.name)

#user uid
print(os.getuid())

# Variable envirement variable HOME
print(pwd.getpwuid(os.getuid())[5])
# parameter
print(os.environ['HOME'] )

# run linux compile
os.system("pwd -L")

# check files and there permissions
os.system("ls -lah")

print(os.chmod("a.txt", stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR  ))

# check files and there permissions again

os.system("ls -lah")
