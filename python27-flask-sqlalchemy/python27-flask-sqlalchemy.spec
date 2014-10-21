Name: python27-flask-sqlalchemy
Version: 2.0
Release: 1
Summary: Adds SQLAlchemy support to your Flask application
Group: Development/Libraries
License: BSD
URL: http://github.com/mitsuhiko/flask-sqlalchemy
Source0: http://pypi.python.org/packages/source/F/Flask-SQLAlchemy/Flask-SQLAlchemy-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-flask python27-sqlalchemy

%description
Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy
to your application. It aims to simplify using SQLAlchemy with Flask by 
providing useful defaults and extra helpers that make it easier to accomplish
common tasks.

%prep
%setup -q -n Flask-SQLAlchemy-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README PKG-INFO CHANGES
%{python_sitelib}/*

%changelog
* Tue Oct 22 2013 Paul Egan <paulegan@rockpack.com> - 1.0-1
- Latest release

* Thu Jan 31 2013 Paul Egan <paulegan@rockpack.com> - 0.16-1
- Initial release
