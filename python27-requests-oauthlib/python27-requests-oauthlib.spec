Name: python27-requests-oauthlib
Version: 0.4.1
Release: 1
Summary: OAuthlib authentication support for Requests
Group: Development/Libraries
License: BSD
URL: https://github.com/requests/requests-oauthlib
Source0: https://pypi.python.org/packages/source/r/requests-oauthlib/requests-oauthlib-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-requests python27-oauthlib

%description
This project provides first-class OAuth library support for Requests.

%prep
%setup -q -n requests-oauthlib-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE
%{python_sitelib}/requests_oauthlib*

%changelog
* Mon Jul 07 2014 Paul Egan <paulegan@rockpack.com> - 0.4.1-1
- Initial release
