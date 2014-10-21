Name: python27-simplejson
Version: 3.6.4
Release: 1%{?dist}
Summary: Simple, fast, extensible JSON encoder/decoder for Python
Group: Development/Languages
License: Python Software Foundation License
URL: http://undefined.org/python/#simplejson
Source0: http://pypi.python.org/packages/source/s/simplejson/simplejson-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python2-devel >= %python_version

%description
simplejson is a simple, fast, complete, correct and extensible JSON 
<http://json.org> encoder and decoder for Python 2.3+. It is pure 
Python code with no dependencies, but includes an optional C extension 
for a serious speed boost.

simplejson was formerly known as simple_json, but changed its name to 
comply with PEP 8 module naming guidelines.

The encoder may be subclassed to provide serialization in any kind of 
situation, without any special support by the objects to be serialized 
(somewhat like pickle).

The decoder can handle incoming JSON strings of any specified encoding 
(UTF-8 by default).


%prep
%setup -q -n simplejson-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc PKG-INFO README.rst
%{python_sitearch}/*

%changelog
* Tue May  6 2014 Paul Egan <paulegan@rockpack.com> - 3.4.1-1
- Bumped

* Fri Feb 14 2014 Paul Egan <paulegan@rockpack.com> - 3.3.2-1
- Bumped

* Fri Mar  8 2013 Paul Egan <paulegan@rockpack.com> - 3.1.0-1
- Bumped

* Thu Jan 10 2013 Paul Egan <paulegan@rockpack.com> - 2.3.3-1
- Initial release

