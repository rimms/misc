# Create docker-image

"""bash
$ docker build -t jubatus-rpm-centos6 -f CentOS6 .
$ docker build -t jubatus-rpm-centos7 -f CentOS7 .
"""

# Create docker-container

"""bash
$ docker run --name=jr6 --net=host -it jubatus-rpm-centos6
$ docker run --name=jr7 --net=host -it jubatus-rpm-centos7
"""

# Test RPM builder

"""bash
$ cd /root/jubatus/tools/packaging/rpm
$ ./package.sh -ucai
"""

# Remove docker-container

"""bash
$ docker rm jr6
$ docker rm jr7
"""
