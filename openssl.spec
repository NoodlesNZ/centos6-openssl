--- SPECS/openssl.spec-dist	2013-08-31 18:30:57.000000000 -0400
+++ SPECS/openssl.spec	2013-08-31 18:54:38.000000000 -0400
@@ -10,6 +10,7 @@
 # 0.9.8jk + EAP-FAST soversion = 8
 # 1.0.0 soversion = 10
 %define soversion 10
+%define nofips 1
 
 # Number of threads to spawn when testing some threading fixes.
 %define thread_test_threads %{?threads:%{threads}}%{!?threads:1}
@@ -26,8 +27,9 @@
 # We have to remove certain patented algorithms from the openssl source
 # tarball with the hobble-openssl script which is included below.
 # The original openssl upstream tarball cannot be shipped in the .src.rpm.
-Source: openssl-%{version}-usa.tar.xz
-Source1: hobble-openssl
+###Source: openssl-%{version}-usa.tar.xz
+###Source1: hobble-openssl
+Source: openssl-%{version}.tar.gz
 Source2: Makefile.certificate
 Source6: make-dummy-cert
 Source7: renew-dummy-cert
@@ -55,22 +57,22 @@
 Patch36: openssl-1.0.0e-doc-noeof.patch
 Patch38: openssl-1.0.1-beta2-ssl-op-all.patch
 Patch39: openssl-1.0.1c-ipv6-apps.patch
-Patch40: openssl-1.0.1e-fips.patch
+##Patch40: openssl-1.0.1e-fips.patch
 Patch45: openssl-1.0.1e-env-zlib.patch
 Patch47: openssl-1.0.0-beta5-readme-warning.patch
 Patch49: openssl-1.0.1a-algo-doc.patch
 Patch50: openssl-1.0.1-beta2-dtls1-abi.patch
 Patch51: openssl-1.0.1e-version.patch
-Patch56: openssl-1.0.0c-rsa-x931.patch
-Patch58: openssl-1.0.1-beta2-fips-md5-allow.patch
+##Patch56: openssl-1.0.0c-rsa-x931.patch
+##Patch58: openssl-1.0.1-beta2-fips-md5-allow.patch
 Patch60: openssl-1.0.0d-apps-dgst.patch
 Patch63: openssl-1.0.0d-xmpp-starttls.patch
 Patch65: openssl-1.0.0e-chil-fixes.patch
 Patch66: openssl-1.0.1-pkgconfig-krb5.patch
-Patch68: openssl-1.0.1e-secure-getenv.patch
+##Patch68: openssl-1.0.1e-secure-getenv.patch
 Patch69: openssl-1.0.1c-dh-1024.patch
 Patch71: openssl-1.0.1e-manfix.patch
-Patch72: openssl-1.0.1e-fips-ctor.patch
+##Patch72: openssl-1.0.1e-fips-ctor.patch
 # Backported fixes including security fixes
 Patch81: openssl-1.0.1-beta2-padlock64.patch
 Patch82: openssl-1.0.1e-backports.patch
@@ -153,7 +155,7 @@
 
 # The hobble_openssl is called here redundantly, just to be sure.
 # The tarball has already the sources removed.
-%{SOURCE1} > /dev/null
+##%{SOURCE1} > /dev/null
 %patch1 -p1 -b .rpmbuild
 %patch2 -p1 -b .defaults
 %patch4 -p1 -b .enginesdir %{?_rawbuild}
@@ -172,25 +174,25 @@
 %patch36 -p1 -b .doc-noeof
 %patch38 -p1 -b .op-all
 %patch39 -p1 -b .ipv6-apps
-%patch40 -p1 -b .fips
+##%patch40 -p1 -b .fips
 %patch45 -p1 -b .env-zlib
 %patch47 -p1 -b .warning
 %patch49 -p1 -b .algo-doc
 %patch50 -p1 -b .dtls1-abi
 %patch51 -p1 -b .version
-%patch56 -p1 -b .x931
-%patch58 -p1 -b .md5-allow
+##%patch56 -p1 -b .x931
+##%patch58 -p1 -b .md5-allow
 %patch60 -p1 -b .dgst
 %patch63 -p1 -b .starttls
 %patch65 -p1 -b .chil
 %patch66 -p1 -b .krb5
-%patch68 -p1 -b .secure-getenv
+##%patch68 -p1 -b .secure-getenv
 %patch69 -p1 -b .dh1024
 
 %patch81 -p1 -b .padlock64
 %patch82 -p1 -b .backports
 %patch71 -p1 -b .manfix
-%patch72 -p1 -b .fips-ctor
+##%patch72 -p1 -b .fips-ctor
 %patch83 -p1 -b .bad-mac
 %patch84 -p1 -b .trusted-first
 
@@ -247,7 +249,7 @@
 ./Configure \
 	--prefix=%{_prefix} --openssldir=%{_sysconfdir}/pki/tls ${sslflags} \
 	zlib enable-camellia enable-seed enable-tlsext enable-rfc3779 \
-	enable-cms enable-md2 no-mdc2 no-rc5 no-ec no-ec2m no-ecdh no-ecdsa no-srp \
+	enable-cms enable-md2 no-mdc2 no-rc5 enable-ec enable-ec2m enable-ecdh enable-ecdsa enable-srp \
 	--with-krb5-flavor=MIT --enginesdir=%{_libdir}/openssl/engines \
 	--with-krb5-dir=/usr shared  ${sslarch} %{?!nofips:fips}
 
@@ -290,10 +292,10 @@
     %{?__debug_package:%{__debug_install_post}} \
     %{__arch_install_post} \
     %{__os_install_post} \
-    crypto/fips/fips_standalone_hmac $RPM_BUILD_ROOT%{_libdir}/libcrypto.so.%{version} >$RPM_BUILD_ROOT%{_libdir}/.libcrypto.so.%{version}.%{version}-%{release}.hmac \
-    ln -sf .libcrypto.so.%{version}.%{version}-%{release}.hmac $RPM_BUILD_ROOT%{_libdir}/.libcrypto.so.%{soversion}.%{version}-%{release}.hmac \
-    crypto/fips/fips_standalone_hmac $RPM_BUILD_ROOT%{_libdir}/libssl.so.%{version} >$RPM_BUILD_ROOT%{_libdir}/.libssl.so.%{version}.%{version}-%{release}.hmac \
-    ln -sf .libssl.so.%{version}.%{version}-%{release}.hmac $RPM_BUILD_ROOT%{_libdir}/.libssl.so.%{soversion}.%{version}-%{release}.hmac \
+##    crypto/fips/fips_standalone_hmac $RPM_BUILD_ROOT%{_libdir}/libcrypto.so.%{version} >$RPM_BUILD_ROOT%{_libdir}/.libcrypto.so.%{version}.%{version}-%{release}.hmac \
+##    ln -sf .libcrypto.so.%{version}.%{version}-%{release}.hmac $RPM_BUILD_ROOT%{_libdir}/.libcrypto.so.%{soversion}.%{version}-%{release}.hmac \
+##    crypto/fips/fips_standalone_hmac $RPM_BUILD_ROOT%{_libdir}/libssl.so.%{version} >$RPM_BUILD_ROOT%{_libdir}/.libssl.so.%{version}.%{version}-%{release}.hmac \
+##    ln -sf .libssl.so.%{version}.%{version}-%{release}.hmac $RPM_BUILD_ROOT%{_libdir}/.libssl.so.%{soversion}.%{version}-%{release}.hmac \
 %{nil}
 
 %define __provides_exclude_from %{_libdir}/openssl
@@ -454,8 +456,8 @@
 
 %files fips
 %defattr(-,root,root)
-%attr(0644,root,root) %{_libdir}/.libcrypto.so.*.hmac
-%attr(0644,root,root) %{_libdir}/.libssl.so.*.hmac
+##%attr(0644,root,root) %{_libdir}/.libcrypto.so.*.hmac
+##%attr(0644,root,root) %{_libdir}/.libssl.so.*.hmac
 # We don't want to depend on prelink for this directory
 %dir %{_sysconfdir}/prelink.conf.d
 %{_sysconfdir}/prelink.conf.d/openssl-fips.conf
