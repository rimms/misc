# Create docker-image

    $ docker build -t jubatus-deb-ubuntu12 -f Ubuntu12 .
    $ docker build -t jubatus-deb-ubuntu14 -f Ubuntu14 .
    $ docker build -t jubatus-deb-ubuntu16 -f Ubuntu16 .

# Create docker-container

    $ docker run --name=jd12 --net=host -it jubatus-deb-ubuntu12
    $ docker run --name=jd14 --net=host -it jubatus-deb-ubuntu14
    $ docker run --name=jd16 --net=host -it jubatus-deb-ubuntu16

# Test Deb builder

    # export DEBEMAIL="jubatus-team@googlegroups.com"
    # export DEBFULLNAME="PFN & NTT"
    # cd /root/jubatus/tools/packaging/allinone
    # ./jubapkg -f -c -d -b -p deb

# Remove docker-container

    $ docker rm jd12
    $ docker rm jd14
    $ docker rm jd16
