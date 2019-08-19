#!/bin/bash

if ! command -v wget > /dev/null; then
    yum -y install wget
fi

yum -y remove *jdk*

echo "Now start download jdk-8u212-linux-x64.tar.gz"
wget https://github.com/frekele/oracle-java/releases/download/8u212-b10/jdk-8u212-linux-x64.tar.gz
tar zxvf jdk-8u212-linux-x64.tar.gz -C /usr/local/

if  ! ``grep -n "JAVA_HOME=" /etc/profile > /dev/null``; then
		echo "add jdk path to system"
	    echo '' >> /etc/profile
	    echo '# java ' >> /etc/profile
	    echo 'export JAVA_HOME=/usr/local/jdk1.8.0_212' >> /etc/profile
	    echo 'export JRE_HOME=${JAVA_HOME}/jre' >> /etc/profile
	    echo 'export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib' >> /etc/profile
	    echo 'export  PATH=${JAVA_HOME}/bin:$PATH' >> /etc/profile
        sleep 5
	    source /etc/profile
fi
# delete source file
rm -rf jdk-8u212-linux-x64.tar.gz

source /etc/profile
