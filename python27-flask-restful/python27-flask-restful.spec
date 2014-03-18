Name: python27-flask-restful
Version: 0.2.12
Release: 1
Summary: Simple framework for creating REST APIs
Group: Development/Libraries
License: MIT
URL: https://www.github.com/twilio/flask-restful/
Source0: https://pypi.python.org/packages/source/F/Flask-RESTful/Flask-RESTful-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-aniso8601 python27-flask python27-six python27-pytz

%description
Flask-RESTful is an extension for Flask that adds support for quickly building
REST APIs. It is a lightweight abstraction that works with your existing
ORM/libraries. Flask-RESTful encourages best practices with minimal setup. If
you are familiar with Flask, Flask-RESTful should be easy to pick up.

%prep
%setup -q -n Flask-RESTful-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc PKG-INFO
%{python_sitelib}/Flask_RESTful*.egg-info
%{python_sitelib}/flask_restful

%changelog
* Tue Mar 18 2014 Paul Egan <paulegan@rockpack.com> - 0.2.12-1
- Initial release
