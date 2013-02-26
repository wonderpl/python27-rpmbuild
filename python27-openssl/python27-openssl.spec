Name: python27-openssl
Version: 0.13
Release: 1%{?dist}
Summary: Python wrapper module around the OpenSSL library
Group: Development/Libraries
License: ASL 2.0
Url: http://pyopenssl.sourceforge.net/
Source0: http://pypi.python.org/packages/source/p/pyOpenSSL/pyOpenSSL-%{version}.tar.gz
Patch2: pyOpenSSL-elinks.patch
Patch3: pyOpenSSL-nopdfout.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: elinks openssl-devel

%description
High-level wrapper around a subset of the OpenSSL library, includes among others
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes

%prep
%setup -q -n pyOpenSSL-%{version}
%patch2 -p1 -b .elinks
%patch3 -p1 -b .nopdfout

# Fix permissions for debuginfo package
%{__chmod} -x OpenSSL/ssl/connection.c

%build
CFLAGS="%{optflags} -fno-strict-aliasing" %{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitearch}/*

%changelog
* Tue Feb 26 2013 Paul Egan <paulegan@rockpack.com> - 0.13-1
- Initial release
