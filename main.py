import os
import getpass
import face_crop
import face_dist
import pose_detect

os.system("tput setaf 2")
print("\t\t\t Welcome to My Menu Program")
os.system("tput setaf 7")
print("\t\t\t-----------------------------")

passwd = getpass.getpass("Enter your password :")
if passwd != "redhat":
    print("password incorrect")
    exit()

def intro():
    os.system("tput setaf 2")
    print("\t\t\t Welcome to My Menu Program")
    os.system("tput setaf 7")
    print("\t\t\t-----------------------------")
    os.system("tput setaf 7")

def nn():
      import os
      IP = input("\t\t\tGive your IP:")
      folder = input("\t\t\tFolder name for namenode:")
      os.system("rm -rf {}".format(folder))
      os.system("mkdir {}".format(folder))
      port = input("\t\t\tInsert Port Number at which you want to run namenode service:")
      hdfs = open("/etc/hadoop/hdfs-site.xml" , "w")
      data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(folder)
      hdfs.write(data)
      core = open("/etc/hadoop/core-site.xml", "w")
      data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(IP,port)
      core.write(data)

def start_nn():
      import os
      f=input("Enter directory name for formatting:")
      os.system("hadoop namenode -format {}".format(f))
      os.system("hadoop-daemon.sh start namenode")

def stop():
    print('''\t\t\t1.Stop Namenode
    \t\t\t2.Stop Datanode
    \t\t\t3.Admin report
    \t\t\t4.Process running
    \t\t\t5.Back\n''')
    ch=input("Enter your choice: ")
    if int(ch)==1:
        os.system("hadoop-daemon.sh stop namenode")
    elif int(ch)==2:
        os.system("hadoop-daemon.sh stop datanode")
    elif int(ch)==3:
        os.system("hadoop dfsadmin -report")
    elif int(ch)==4:
        os.system("jps")
    elif int(ch)==5:
        mainmenu()

def dn():
      import os
      IP = input("\t\t\tGive IP of your namenode:")
      folder = input("\t\t\tFolder name of datanode:")
      os.system("rm -rf {}".format(folder))
      os.system("mkdir {}".format(folder))
      port = input("\t\t\tInsert Port Number at which you want to run namenode service:")
      hdfs = open("/etc/hadoop/hdfs-site.xml" , "w")
      data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.data.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(folder)
      hdfs.write(data)
      core = open("/etc/hadoop/core-site.xml", "w")
      data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(IP,port)
      core.write(data)

def start_dn():
      import os
      os.system("hadoop-daemon.sh start datanode")

def webserver():
      import os
      os.system("yum install httpd")
      print("Webserver installed sucessfully")
      os.system("systemctl start httpd")

def docker():
      import os
      repo = open("/etc/yum.repos.d/docker.repo" , "w")
      data = '''[docker]
      baseurl=https://download.docker.com/linux/centos/7/x86_64/stable
      gpgcheck=0'''
      repo.write(data)
      os.system("yum install docker-ce --nobest  -y")
      print("Docker installed successfully")
      
def docker_service():
    while True:
       print('''\t\t\t1.Start docker service
        \t\t\t2.Docker images
        \t\t\t3.Docker running status
        \t\t\t4.Pull OS
        \t\t\t5.Launch 0S
        \t\t\t6.OS running
        \t\t\t7.Remove container
        \t\t\t8.Remove all containers
        \t\t\t9.Back to main menu\n''')
       ch=input("\t\t\t Enter your choice:")
       if int(ch) == 1:
           os.system("systemctl start docker")
       elif int(ch) == 2:
           os.system("docker images")
       elif int(ch) == 3:
           os.system("systemctl status docker")
       elif int(ch) == 4:
           os.system("docker pull {}".format(input("Enter os name you want to install: ")))
       elif int(ch) == 5:
           os_name = input("Enter image name: ")
           con_name = input("Enter name: ")
           os.system("docker run -d --name {} {}".format(os_name, con_name))
       elif int(ch) == 6:
           os.system("docker ps")
       elif int(ch) == 7:
           conname = input("Enter container name: ")
           os.system("docker rm -f {}".format(conname))
       elif int(ch) == 8:
           os.system("docker rm -f $(docker ps -a -q)")
       elif int(ch) == 9:
           mainmenu()

def shellinabox():
    os.system("firefox https://localhost:4200")

def linux():
  while True:
     os.system("tput setaf 6") 
     print('''\t\t\t1.Run Date
     \t\t\t2.Run Calendar
     \t\t\t3.Show IP address
     \t\t\t4.Show RAM
     \t\t\t5.Memory
     \t\t\t6.Who am I?
     \t\t\t7.Current Directory
     \t\t\t8.View contents of directory
     \t\t\t9.Back\n''')
     os.system("tput setaf 7")
     ch=input("Enter your choice:")
     if int(ch)==1:
         os.system("date")
     elif int(ch)==2:
         os.system("cal")
     elif int(ch)==3:
         os.system("ifconfig")
     elif int(ch)==4:
         os.system("free -m")
     elif int(ch)==5:
         os.system("df -h")
     elif int(ch)==6:
         os.system("whoami")
     elif int(ch)==7:
         os.system("pwd")
     elif int(ch)==8:
         os.system("ls")
     elif int(ch)==9:
         mainmenu()

def aws():
    while True:
        print('''\t\t\t1.Create Key Pair
        \t\t\t2.Create Security Group
        \t\t\t3.Launch instance
        \t\t\t4.Create Volume
        \t\t\t5.Attach Volume
        \t\t\t6.Create Bucket
        \t\t\t7.Go to main menu''')
        
        r=input("Enter your choice :")
        if int(r) == 1:
            os.system("aws ec2 create-key-pair --key-name {}".format(input("Enter key name:")))
        elif int(r)==2:
            os.system("aws ec2 create-security-group --group-name {} --description {}".format(input("enter group name\n"),input("enter group description\n")))
        elif int(r)==3:
            os.system("aws ec2 run-instances --image-id {} --instance-type {} --key-name {}  --count 1".format(input("enter image id\n"),input("enter instance type\n"),input("enter key name\n"),input("enter security group id\n")))
        elif int(r)==4:
            os.system("aws ec2 create-volume --availability-zone {} --volume-type {} --size {}".format(input("enter availability zone \n"),input("enter volume type \n"),input("enter size \n")))
        elif int(r)==5:
            os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device {}".format(input("enter instance id\n"),input("enter volume id \n"),input("enetr device name \n")))
        elif int(r)==6:
            os.system("aws s3api create-bucket --bucket {} --create-bucket-configuration LocationConstraint=ap-south-1 --acl {}".format(input("enter unique name of bucket \n"),input("enter readable view i.e acl\n")))
        elif int(r)==7:
            mainmenu()

def mainmenu():
   while True:
      intro() 
      import os
      os.system("tput setaf 4")
      print('''\t\t\t 1.Configure Hadoop Namenode
      \t\t\t 2.Configure Hadoop Datanode
      \t\t\t 3.Create Partition
      \t\t\t 4.Configure Webserver
      \t\t\t 5.Configure Docker
      \t\t\t 6.Amazon Web Service
      \t\t\t 7.Hadoop services
      \t\t\t 8.Basic Linux commands
      \t\t\t 9.cropping face
      \t\t\t 10.measure distance from face
      \t\t\t 11.pose detection
      \t\t\t 12.Web based CLI
      \t\t\t 13.Exit program\n''')
      os.system("tput setaf 7")
      ch=input("\t\t\tEnter your choice: ")
      if int(ch) == 1:
          nn()
          start_nn()
      elif int(ch) == 2:
          dn()
          start_dn()
      elif int(ch) == 3:
          partition()  
      elif int(ch) == 4:
          webserver()
      elif int(ch) == 5:
          docker()
          docker_service()
      elif int(ch) == 6:
          AWS()
      elif int(ch) == 7:
          stop()
      elif int(ch) == 8:
          Linux()
      elif int(ch) == 9:
          face_crop.cropp()
      elif int(ch) == 10:
          face_dist.dist()
      elif int(ch) == 11:
          pose_detect.detect()
      elif int(ch) == 12:
          shellinabox()
      elif int(ch) == 13:
          exit()
      else:
          print("Try again")
      input("Press Enter to Continue...")
      os.system("clear")

mainmenu()
