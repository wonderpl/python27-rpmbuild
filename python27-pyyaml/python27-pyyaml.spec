Name: python27-pyyaml
Version: 3.10
Release: 1%{?dist}
Summary: YAML parser and emitter for Python
Group: Development/Libraries
License: MIT
URL: http://pyyaml.org/wiki/PyYAML
Source0: http://pypi.python.org/packages/source/P/PyYAML/PyYAML-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools libyaml-devel

%description
YAML is a data serialization format designed for human readability
and interaction with scripting languages.  PyYAML is a YAML parser
and emitter for Python.

%prep
%setup -q -n PyYAML-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{python_sitearch}/*

%changelog
* Tue Mar 19 2013 Paul Egan <paulegan@rockpack.com> - 3.10-1
- Initial release
