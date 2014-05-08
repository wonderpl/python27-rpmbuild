Name: python27-flask-admin
Version: 1.0.8
Release: 2
Summary: Simple and extensible admin interface framework for Flask
Group: Development/Libraries
License: BSD
URL: https://github.com/mrjoes/flask-admin/
Source0: http://pypi.python.org/packages/source/F/Flask-Admin/Flask-Admin-%{version}.tar.gz
Patch1: inlinemodelconverter.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
BuildRequires: wget unzip
Requires: python27-wtforms python27-setuptools

%description
This is library for building adminstrative interface on top of Flask framework.

Flask-Admin comes with few batteries out of the box: model scaffolding for
SQLAlchemy, MongoEngine and Peewee ORMs and simple file management interface.

%prep
%setup -q -n Flask-Admin-%{version}
%patch1 -p1
# Upgrade to bootstrap 2.3.2
wget http://getbootstrap.com/2.3.2/assets/bootstrap.zip
unzip -q -o -d flask_admin/static bootstrap.zip

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
%{python_sitelib}/*

%changelog
* Tue Oct 15 2013 Paul Egan <paulegan@rockpack.com> - 1.0.7-1
- Bumped to latest

* Wed Mar  6 2013 Paul Egan <paulegan@rockpack.com> - 1.0.4-2
- Added patch for inline models

* Fri Jan 11 2013 Paul Egan <paulegan@rockpack.com> - 1.0.4-1
- Initial release
