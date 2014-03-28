Name: python27-ndg-httpsclient
Version: 0.3.2
Release: 1
Summary: Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
Group: Development/Libraries
License: BSD
URL: http://ndg-security.ceda.ac.uk/wiki/ndg_httpsclient/
Source0: https://pypi.python.org/packages/source/n/ndg-httpsclient/ndg_httpsclient-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-openssl
Requires: python27-asn1

%description
This is a HTTPS client implementation for httplib and urllib2 based on
PyOpenSSL. PyOpenSSL provides a more fully featured SSL implementation over the
default provided with Python and importantly enables full verification of the
SSL peer.

%prep
%setup -q -n ndg_httpsclient-%{version}

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
%{python_sitelib}/ndg/httpsclient
%{python_sitelib}/ndg_httpsclient*
%{_bindir}/*

%changelog
* Fri Mar 28 2014 Paul Egan <paulegan@rockpack.com> - 0.3.2-1
- Initial release
