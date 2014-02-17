Name: python27-yolk
Version: 0.4.3
Release: 1
Summary: Command-line tool for querying PyPI and Python packages installed on your system
Group: Development/Libraries
License: BSD
URL: https://github.com/cakebread/yolk
Source0: https://pypi.python.org/packages/source/y/yolk/yolk-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-setuptools

%description
Yolk is a Python tool for obtaining information about installed Python packages
and querying packages avilable on PyPI (Python Package Index).

You can see which packages are active, non-active or in development mode and
show you which have newer versions available by querying PyPI.

%prep
%setup -q -n yolk-%{version}

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
%doc README.rst
%{python_sitelib}/yolk*
%{_bindir}/*

%changelog
* Thu Feb 13 2014 Paul Egan <paulegan@rockpack.com> - 0.4.3-1
- Initial release
