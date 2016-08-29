# Create docker-image

    $ docker build -t jubatus-rpm-centos6 -f CentOS6 .
    $ docker build -t jubatus-rpm-centos7 -f CentOS7 .

# Create docker-container

    $ docker run --name=jr6 --net=host -it jubatus-rpm-centos6
    $ docker run --name=jr7 --net=host -it jubatus-rpm-centos7

# Test RPM builder

    # cd /root/jubatus/tools/packaging/rpm
    # ./package.sh -ucai

# Remove docker-container

    $ docker rm jr6
    $ docker rm jr7
