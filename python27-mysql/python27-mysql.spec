Summary: An interface to MySQL
Name: python27-mysql
Version: 1.2.3
Release: 1%{?dist}
License: GPLv2+
Group: Development/Libraries
URL: http://sourceforge.net/projects/mysql-python/
Source0: http://prdownloads.sourceforge.net/mysql-python/MySQL-python-%{version}c1.tar.gz
Patch2: escape-fix.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools
BuildRequires: mysql mysql-devel zlib-devel

%description
Python interface to MySQL

MySQLdb is an interface to the popular MySQL database server for Python.
The design goals are:

-     Compliance with Python database API version 2.0 
-     Thread-safety 
-     Thread-friendliness (threads will not block each other) 
-     Compatibility with MySQL 3.23 and up

This module should be mostly compatible with an older interface
written by Joe Skinner and others. However, the older version is
a) not thread-friendly, b) written for MySQL 3.21, c) apparently
not actively maintained. No code from that version is used in MySQLdb.

%prep
%setup -q -n MySQL-python-%{version}c1

%patch2 -p1

%build
rm -f doc/*~
export libdirname=%{_lib}
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}

export libdirname=%{_lib}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README GPL doc/*
%dir %{python_sitearch}/MySQLdb
%{python_sitearch}/MySQLdb/*
%{python_sitearch}/MySQL*.egg-info
%{python_sitearch}/_mysql*

%changelog
* Mon Sep 30 2013 Paul Egan <paulegan@rockpack.com> - 1.2.3-1
- Imported from amzn
