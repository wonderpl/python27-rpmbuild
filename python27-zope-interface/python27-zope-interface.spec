Name: python27-zope-interface
Version: 4.1.0
Release: 1%{?dist}
Summary: Interfaces for Python
Group: Development/Libraries
License: ZPLv2.1
URL: http://pypi.python.org/pypi/zope.interface
Source0: http://pypi.python.org/packages/source/z/zope.interface/zope.interface-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools python27-zope-event

%description
Interfaces are a mechanism for labeling objects as conforming to a given API
or contract.

%prep
%setup -q -n zope.interface-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{__rm} -f %{buildroot}%{python_sitearch}/zope/interface/_zope_interface_coptimizations.c

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE.txt CHANGES.rst COPYRIGHT.txt docs/
%{python_sitearch}/*
%exclude %{python_sitearch}/zope/interface/tests/
%exclude %{python_sitearch}/zope/interface/common/tests/

%changelog
* Tue Feb 26 2013 Paul Egan <paulegan@rockpack.com> - 4.0.4-1
- Initial release
