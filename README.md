centos6-openssl
===============

Spec file for backport of OpenSSL 1.0.1 for CentOS 6


Quick Summary:
==============
Assuming you've built an RPM before, download the Fedora Core 20 source rpm for openssl-1.0.1e.

````
rpm -Uvh http://dl.fedoraproject.org/pub/fedora/linux/development/20/source/SRPMS/o/openssl-1.0.1e-19.fc20.src.rpm
cd /usr/src/redhat/SOURCES/
````

Revert the new syntax to the old syntax with the double-underscore prefix.

````
sed -i -e "s/secure_getenv/__secure_getenv/g" openssl-1.0.1e-env-zlib.patch
sed -i -e "s/secure_getenv/__secure_getenv/g" openssl-1.0.1e-fips-ctor.patch
````

Fetch this updated diff for the spec file, review it, and apply the patch.

````
cd /usr/src/redhat/SPECS/
wget http://www.ptudor.net/linux/openssl/resources/openssl-spec-patricktudor-fc20-19.diff
patch -p1 < openssl-spec-patricktudor-fc20-19.diff
time rpmbuild -ba openssl.spec
````

See also: 

https://www.ptudor.net/linux/openssl/

http://unix.stackexchange.com/questions/84283/how-can-i-get-tlsv1-2-support-in-apache-on-rhel6-centos-sl6/86326

http://www.centos.org/modules/newbb/viewtopic.php?topic_id=41784&forum=55&post_id=189679

