Name: python27-multi-mechanize
Version: 1.2.0
Release: 1
Summary: Multi-Mechanize - Performance Test Framework
Group: Development/Libraries
License: LGPL
URL: http://multimechanize.com
Source0: http://pypi.python.org/packages/source/m/multi-mechanize/multi-mechanize-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-matplotlib

%description
Multi-Mechanize is an open source framework for performance and load testing.
It runs concurrent Python scripts to generate load (synthetic transactions)
against a remote site or service.

Multi-Mechanize is most commonly used for web performance and scalability
testing, but can be used to generate workload against any remote API accessible
from Python.

%prep
%setup -q -n multi-mechanize-%{version}

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
%{python_sitelib}/*
%{_bindir}/*

%changelog
* Thu Apr 04 2013 Paul Egan <paulegan@rockpack.com> - 1.2.0-1
- Initial release
