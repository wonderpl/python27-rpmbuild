Name: python27-pyes
Version: 0.20.1
Release: 1
Summary: Python Elastic Search driver
Group: Development/Libraries
License: BSD
URL: http://github.com/aparo/pyes/
Source0: http://pypi.python.org/packages/source/p/pyes/pyes-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-urllib3

%description
pyes is a connector to use elasticsearch from python.

%prep
%setup -q -n pyes-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE
%{python_sitelib}/pyes*

%changelog
* Thu Sep 12 2013 Paul Egan <paulegan@rockpack.com> - 0.20.1-1
- Bumped to latest

* Tue Apr 23 2013 Paul Egan <paulegan@rockpack.com> - 0.19.1-1
- Initial release
