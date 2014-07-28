Name: python27-mccabe
Version: 0.2.1
Release: 1
Summary: McCabe checker, plugin for flake8
Group: Development/Libraries
License: MIT
URL: https://github.com/flintwork/mccabe
Source0: https://pypi.python.org/packages/source/m/mccabe/mccabe-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
Ned's script to check McCabe complexity.

This module provides a plugin for flake8, the Python code checker.

%prep
%setup -q -n mccabe-%{version}

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
%{python_sitelib}/mccabe*

%changelog
* Mon Jul 28 2014 Paul Egan <paulegan@rockpack.com> - 0.2.1-1
- Initial release
