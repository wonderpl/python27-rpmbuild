Name: python27-flask-login
Version: 0.2.9
Release: 1
Summary: User session management for Flask
Group: Development/Libraries
License: MIT
URL: https://github.com/maxcountryman/flask-login
Source0: http://pypi.python.org/packages/source/F/Flask-Login/Flask-Login-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-flask

%description
Flask-Login provides user session management for Flask.  It handles the common
tasks of logging in, logging out, and remembering your users' sessions over
extended periods of time.

%prep
%setup -q -n Flask-Login-%{version}

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
%{python_sitelib}/*

%changelog
* Thu Feb 13 2014 Paul Egan <paulegan@rockpack.com> - 0.2.9-1
- Bumped

* Tue Oct 22 2013 Paul Egan <paulegan@rockpack.com> - 0.2.7-1
- Latest release

* Tue Jan 15 2013 Paul Egan <paulegan@rockpack.com> - 0.1.3-1
- Initial release
