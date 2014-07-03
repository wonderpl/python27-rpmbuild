Name: python27-virtualenv
Version: 1.11.6
Release: 1
Summary: Tool to create isolated Python environments
Group: Development/Languages
License: MIT
URL: http://pypi.python.org/pypi/virtualenv
Source0: http://pypi.python.org/packages/source/v/virtualenv/virtualenv-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools

%description
virtualenv is a tool to create isolated Python environments. virtualenv
is a successor to workingenv, and an extension of virtual-python. It is
written by Ian Bicking, and sponsored by the Open Planning Project. It is
licensed under an MIT-style permissive license.

%prep
%setup -q -n virtualenv-%{version}
sed -i -e "1s|#!/usr/bin/env python||" virtualenv.py

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc docs/*.rst README.rst PKG-INFO AUTHORS.txt LICENSE.txt
%{python_sitelib}/*
%{_bindir}/*

%changelog
* Thu Jan 10 2013 Paul Egan <paulegan@rockpack.com> - 1.8.4-1
- Initial release
