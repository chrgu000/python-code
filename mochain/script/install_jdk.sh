#!/bin/sh


yum -y remove *openjdk*

wget https://github.com/frekele/oracle-java/releases/download/8u181-b13/jdk-8u181-linux-x64.tar.gz
tar zxf jdk-8u181-linux-x64.tar.gz -C /usr/local/

echo '' >> /etc/profile
echo '# java ' >> /etc/profile
echo 'export JAVA_HOME=/usr/local/jdk1.8.0_181' >> /etc/profile
echo 'export JRE_HOME=${JAVA_HOME}/jre' >> /etc/profile
echo 'export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib' >> /etc/profile
echo 'export  PATH=${JAVA_HOME}/bin:$PATH' >> /etc/profile


source /etc/profile