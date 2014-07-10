Name: python27-openssl
Version: 0.14
Release: 1
Summary: Python wrapper module around the OpenSSL library
Group: Development/Libraries
License: ASL 2.0
URL: https://github.com/pyca/pyopenssl
Source0: http://pypi.python.org/packages/source/p/pyOpenSSL/pyOpenSSL-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-cryptography python27-six

%description
High-level wrapper around a subset of the OpenSSL library, includes
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes

%prep
%setup -q -n pyOpenSSL-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
#%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README LICENSE
%{python_sitelib}/*

%changelog
* Thu Jul 03 2014 Paul Egan <paulegan@rockpack.com> - 0.14-1
- Bumped to latest version

* Tue Feb 26 2013 Paul Egan <paulegan@rockpack.com> - 0.13-1
- Initial release
