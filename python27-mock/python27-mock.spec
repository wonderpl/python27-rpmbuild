Name: python27-mock
Version: 1.0.1
Release: 1
Summary: A Python Mocking and Patching Library for Testing
Group: Development/Libraries
License: BSD
URL: http://www.voidspace.org.uk/python/mock/
Source0: http://pypi.python.org/packages/source/m/mock/mock-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
mock is a library for testing in Python. It allows you to replace parts of
your system under test with mock objects and make assertions about how they
have been used.

%prep
%setup -q -n mock-%{version}

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
%doc README.txt LICENSE.txt
%{python_sitelib}/mock*

%changelog
* Thu Feb 14 2013 Paul Egan <paulegan@rockpack.com> - 1.0.1-1
- Initial release
