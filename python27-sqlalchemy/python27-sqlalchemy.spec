Name: python27-sqlalchemy
Version: 0.8.2
Release: 1
Summary: Modular and flexible ORM library for python
Group: Development/Libraries
License: MIT
URL: http://www.sqlalchemy.org/
Source0: http://downloads.sourceforge.net/sqlalchemy/SQLAlchemy-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools

%description
SQLAlchemy is an Object Relational Mappper (ORM) that provides a flexible,
high-level interface to SQL databases.  Database and domain concepts are
decoupled, allowing both sides maximum flexibility and power. SQLAlchemy
provides a powerful mapping layer that can work as automatically or as manually
as you choose, determining relationships based on foreign keys or letting you
define the join conditions explicitly, to bridge the gap between database and
domain.

%prep
%setup -q -n SQLAlchemy-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf doc/build

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE PKG-INFO CHANGES doc examples
%{python_sitearch}/*

%changelog
* Wed Aug 14 2013 Paul Egan <paulegan@rockpack.com> - 0.8.2-1
- Bumped to 0.8.2

* Mon Jan 21 2013 Paul Egan <paulegan@rockpack.com> - 0.8.0b2-1
- Bumped to 0.8 beta release

* Fri Jan 11 2013 Paul Egan <paulegan@rockpack.com> - 0.7.9-1
- Initial release
