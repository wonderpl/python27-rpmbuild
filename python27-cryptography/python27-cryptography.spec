Name: python27-cryptography
Version: 0.4
Release: 1%{?dist}
Summary: cryptography is a package which provides cryptographic recipes and primitives
Group: Development/Libraries
License: ASL 2.0
URL: https://github.com/pyca/cryptography
Source0: https://pypi.python.org/packages/source/c/cryptography/cryptography-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: gcc libffi-devel python-devel openssl-devel
BuildRequires: python27-setuptools

%description
Cryptography is a package which provides cryptographic recipes and primitives
to Python developers. Our goal is for it to be your "cryptographic standard
library". It supports Python 2.6-2.7, Python 3.2+, and PyPy.

Cryptography includes both high level recipes, and low level interfaces to
common cryptographic algorithms such as symmetric ciphers, message digests and
key derivation functions.

%prep
%setup -q -n cryptography-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst
%{python_sitearch}/cryptography*

%changelog
* Thu Jul 03 2014 Paul Egan <paulegan@rockpack.com> - 0.4-1
- Initial release
