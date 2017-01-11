%ifarch x86_64 
%global openssltarget linux-x86_64
%else
%global openssltarget linux-elf
%endif


AutoReqProv: no

Summary:	Secure Sockets Layer communications libs & utils
Name:		openssl-spotify
Version:	1.0.0
Release:        5%{?dist}
License:	OpenSSL
Group: 		System Environment/Libraries
URL:		http://www.openssl.org/
Source:		ftp://ftp.openssl.org/source/old/%{version}/openssl-%{version}.tar.gz

BuildRequires: 	coreutils, krb5-devel, perl, sed, zlib-devel, /usr/bin/cmp
BuildRequires: 	/usr/bin/rename
BuildRequires: 	/usr/bin/pod2man 
Provides:	openssl1 = %{version}-%{release}

%description
The openssl certificate management tool and the shared libraries that provide
various encryption and decription algorithms and protocols, including DES, RC4,
RSA and SSL.

NOTE: Only the shared library and the engines are provided with this source
rpm package.


%prep

%setup -q -n openssl-%{version}

%build 

RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -DPURIFY"

./Configure --prefix=/usr --openssldir=/etc/ssl --libdir=%{_libdir} \
		shared zlib enable-md2 %{openssltarget}


make depend
make


%install

install -Dm755 libssl.so.1.0.0 %{buildroot}/%{_libdir}/libssl.so.1.0.0
install -Dm755 libcrypto.so.1.0.0 %{buildroot}/%{_libdir}/libcrypto.so.1.0.0

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%{_libdir}/libssl.so.1.0.0
%{_libdir}/libcrypto.so.1.0.0

%changelog

* Wed Jan 11 2017 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.0-5
- Renamed

* Thu Apr 28 2016 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.0-4
- Rebuilt 

* Fri Sep 25 2015 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.0-3
- Rebuilt

* Thu Apr 16 2015 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.0-2
- Renamed

* Sun Jul 27 2014 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 1.0.0-1
- Initial build rpm

