Name: python27-py
Version: 1.4.25
Release: 1
Summary: library with cross-python path, ini-parsing, io, code, log facilities
Group: Development/Libraries
License: MIT
URL: http://pylib.readthedocs.org/
Source0: http://pypi.python.org/packages/source/p/py/py-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
The py lib is a Python development support library featuring
the following tools and modules:

* py.path:  uniform local and svn path objects
* py.apipkg: explicit API control and lazy-importing
* py.iniconfig:  easy parsing of .ini files
* py.code: dynamic code generation and introspection
* py.path:  uniform local and svn path objects

%prep
%setup -q -n py-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt LICENSE
%{python_sitelib}/py*

%changelog
* Mon Oct 28 2013 Allan Brisbane <allan@rockpack.com> - 1.4.17-1
- Upgrade

* Thu Jan 24 2013 Paul Egan <paulegan@rockpack.com> - 1.4.12-1
- Initial release
