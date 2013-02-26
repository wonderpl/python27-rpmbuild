Name: python27-lxml
Version: 3.1.0
Release: 1%{?dist}
Summary: ElementTree-like Python bindings for libxml2 and libxslt
Group: Development/Libraries
License: BSD
URL: http://lxml.de/
Source0: http://pypi.python.org/packages/source/l/lxml/lxml-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libxslt-devel Cython

%description
lxml provides a Python binding to the libxslt and libxml2 libraries.
It follows the ElementTree API as much as possible in order to provide
a more Pythonic interface to libxml2 and libxslt than the default
bindings.  In particular, lxml deals with Python Unicode strings
rather than encoded UTF-8 and handles memory management automatically,
unlike the default bindings.

%package docs
Summary: Documentation for %{name}
Group: Documentation
BuildArch: noarch
%description docs
This package provides the documentation for %{name}, e.g. the API as html.

%prep
%setup -q -n lxml-%{version}

# remove the C extension so that it will be rebuilt using the latest Cython
rm -f src/lxml/lxml.etree.c
rm -f src/lxml/lxml.etree_api.h
rm -f src/lxml/lxml.objectify.c

chmod a-x doc/rest2html.py
%{__sed} -i 's/\r//' doc/s5/ui/default/print.css \
    doc/s5/ep2008/atom.rng \
    doc/s5/ui/default/iepngfix.htc

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --no-compile --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSES.txt PKG-INFO CREDITS.txt CHANGES.txt
%{python_sitearch}/lxml
%{python_sitearch}/lxml-*.egg-info

%files docs
%defattr(-,root,root,-)
%doc doc/*

%changelog
* Tue Feb 26 2013 Paul Egan <paulegan@rockpack.com> - 3.1.0-1
- Initial release
