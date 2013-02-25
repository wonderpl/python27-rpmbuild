Name: python27-pyoauth2
Version: 0.0.1
Release: 1
Summary: OAuth 2.0 Client and Provider Library
Group: Development/Libraries
License: BSD
URL: https://github.com/StartTheShift/pyoauth2
Source0: https://github.com/StartTheShift/pyoauth2/archive/master.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-requests

%description
This library currently implements a very small subset of the OAuth 2.0
draft specification. Supported sections include:
* Authorization Code Grant flow
* Bearer token type

%prep
%setup -q -n pyoauth2-master

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc 
%{python_sitelib}/pyoauth2*

%changelog
* Thu Feb 21 2013 Paul Egan <paulegan@rockpack.com> - 0.0.1-1
- Initial release
