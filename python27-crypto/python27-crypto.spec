Name: python27-crypto
Version: 2.6
Release: 1%{?dist}
Summary: Cryptography library for Python
Group: Development/Libraries
License: Public Domain and Python
URL: http://www.pycrypto.org/
Source0: http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/pycrypto-%{version}.tar.gz
Patch0: python-crypto-2.4-optflags.patch
Patch1: python-crypto-2.4-fix-pubkey-size-divisions.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python2-devel >= 2.2, gmp-devel >= 4.1

%description
PyCrypto is a collection of both secure hash functions (such as MD5 and
SHA), and various encryption algorithms (AES, DES, RSA, ElGamal, etc.).

%prep
%setup -n pycrypto-%{version} -q

# Use distribution compiler flags rather than upstream's
%patch0 -p1

# Fix divisions within benchmarking suite:
%patch1 -p1

%build
CFLAGS="%{optflags} -fno-strict-aliasing" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Remove group write permissions on shared objects
find %{buildroot}%{python_sitearch} -name '*.so' -exec chmod -c g-w {} \;

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README TODO ACKS ChangeLog LEGAL/ COPYRIGHT Doc/
%{python_sitearch}/Crypto/
%{python_sitearch}/*.egg-info

%changelog
* Thu Feb 21 2013 Paul Egan <paulegan@rockpack.com> - 2.6-1
- Initial release
