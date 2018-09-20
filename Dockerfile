FROM centos:6.8

RUN yum install -y epel-release && \
    yum install -y lighttpd vim && \
    yum install -y gcc g++ make git patch perl perl-dev perl-CPAN curl wget
 
RUN mkdir /var/www/htdocs
RUN mkdir /var/www/cgi-bin
RUN curl -L http://cpanmin.us | perl - App::cpanminus

# copy files
COPY ./index.html /var/www/htdocs
COPY ./index.cgi /var/www/cgi-bin
COPY ./lighttpd.conf /etc/lighttpd
COPY ./cgi.conf /etc/lighttpd/conf.d
COPY ./modules.conf /etc/lighttpd


RUN cd
COPY ./cpanfile .
RUN cpanm --installdeps .

WORKDIR /var/www
 
# start web server
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
