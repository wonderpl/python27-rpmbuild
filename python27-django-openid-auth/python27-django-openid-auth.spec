Name: python27-django-openid-auth
Version: 0.5
Release: 1
Summary: OpenID integration for django.contrib.auth
Group: Development/Libraries
License: BSD
URL: https://launchpad.net/django-openid-auth
Source0: http://pypi.python.org/packages/source/d/django-openid-auth/django-openid-auth-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-openid

%description
A library that can be used to add OpenID support to Django applications.  The
library integrates with Django's built in authentication system, so most
applications require minimal changes to support OpenID login.

%prep
%setup -q -n django-openid-auth-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt LICENSE.txt
%{python_sitelib}/*

%changelog
* Wed Apr 10 2013 Paul Egan <paulegan@rockpack.com> - 0.5-1
- Initial release
