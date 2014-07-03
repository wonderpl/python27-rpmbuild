Name: python27-flask-script
Version: 2.0.5
Release: 1
Summary: Scripting support for Flask
Group: Development/Libraries
License: BSD
URL: http://github.com/smurfix/flask-script
Source0: http://pypi.python.org/packages/source/F/Flask-Script/Flask-Script-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-flask

%description
Flask support for writing external scripts.

%prep
%setup -q -n Flask-Script-%{version}

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
%doc README.rst LICENSE
%{python_sitelib}/*

%changelog
* Tue May  6 2014 Paul Egan <paulegan@rockpack.com> - 2.0.3-1
- Switched to new version

* Thu Feb 13 2014 Paul Egan <paulegan@rockpack.com> - 0.6.6-1
- Bumped

* Tue Mar 19 2013 Paul Egan <paulegan@rockpack.com> - 0.5.3-1
- Initial release
