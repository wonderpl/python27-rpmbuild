Name: python27-alembic
Version: 0.4.2
Release: 2
Summary: A database migration tool for SQLAlchemy
Group: Development/Libraries
License: MIT
URL: http://bitbucket.org/zzzeek/alembic
Source0: http://pypi.python.org/packages/source/a/alembic/alembic-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-mako

%description
Alembic is a new database migrations tool, written by the author
of SQLAlchemy.  A migrations tool offers the following functionality:

* Can emit ALTER statements to a database in order to change the structure
  of tables and other constructs
* Provides a system whereby "migration scripts" may be constructed; each
  script indicates a particular series of steps that can "upgrade" a target
  database to a new version, and optionally a series of steps that can
  "downgrade" similarly, doing the same steps in reverse.
* Allows the scripts to execute in some sequential manner.

%prep
%setup -q -n alembic-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst README.unittests LICENSE
%{python_sitelib}/alembic*
%{_bindir}/*

%changelog
* Tue Mar 12 2013 Paul Egan <paulegan@rockpack.com> - 0.4.2-1
- Initial release
