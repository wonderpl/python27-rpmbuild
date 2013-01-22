Name: python27-psycopg2
Version: 2.4.6
Release: 1%{?dist}
Summary: Python-PostgreSQL Database Adapter
Group: Development/Libraries
License: LGPL
URL: http://initd.org/psycopg/
Source0: http://pypi.python.org/packages/source/p/psycopg2/psycopg2-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools postgresql-devel

%description
psycopg2 is a PostgreSQL database adapter for the Python programming
language.  psycopg2 was written with the aim of being very small and fast,
and stable as a rock.

psycopg2 is different from the other database adapter because it was
designed for heavily multi-threaded applications that create and destroy
lots of cursors and make a conspicuous number of concurrent INSERTs or
UPDATEs.

%prep
%setup -q -n psycopg2-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README PKG-INFO LICENSE
%{python_sitearch}/psycopg2*


%changelog
* Mon Jan 14 2013 Paul Egan <paulegan@rockpack.com> - 2.4.6-1
- Initial release
