Name: python27-flask-cache
Version: 0.13.1
Release: 1
Summary: Adds cache support to your Flask application
Group: Development/Libraries
License: BSD
URL: http://github.com/thadeusb/flask-cache
Source0: https://pypi.python.org/packages/source/F/Flask-Cache/Flask-Cache-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-flask

%description
Adds cache support to your Flask application

%prep
%setup -q -n Flask-Cache-%{version}

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
%doc README LICENSE docs/
%{python_sitelib}/Flask_Cache*.egg-info
%{python_sitelib}/flask_cache*

%changelog
* Tue Feb 18 2014 Paul Egan <paulegan@rockpack.com> - 0.12-1
- Initial release
