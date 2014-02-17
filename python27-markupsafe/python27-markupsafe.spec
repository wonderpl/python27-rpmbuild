Name: python27-markupsafe
Version: 0.18
Release: 1%{?dist}
Summary: Implements a XML/HTML/XHTML Markup safe string for Python
Group: Development/Libraries
License: BSD
URL: http://pypi.python.org/pypi/MarkupSafe
Source0: http://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools

%description
A library for safe markup escaping.

%prep
%setup -q -n MarkupSafe-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm %{buildroot}/%{python_sitearch}/markupsafe/*.c

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README.rst
%{python_sitearch}/*

%changelog
* Thu Feb 13 2014 Paul Egan <paulegan@rockpack.com> - 0.19-1
- Bumped

* Fri Jan 11 2013 Paul Egan <paulegan@rockpack.com> - 0.15-1
- Initial release
