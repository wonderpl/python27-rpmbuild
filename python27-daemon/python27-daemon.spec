Name: python27-daemon
Version: 1.6
Release: 1
Summary: Library to implement a well-behaved Unix daemon process
Group: Development/Languages
License: Python
URL: http://pypi.python.org/pypi/python-daemon/
Source0: http://pypi.python.org/packages/source/p/python-daemon/python-daemon-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools python27-lockfile
Requires: python27-lockfile

%description
This library implements the well-behaved daemon specification of PEP 3143,
"Standard daemon process library".

%prep
%setup -q -n python-daemon-%{version}
sed -i -e '/^#!\//, 1d' daemon/version/version_info.py

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}%{python_sitelib}/tests

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.PSF-2
%{python_sitelib}/*daemon*

%changelog
* Tue Feb 05 2013 Paul Egan <paulegan@rockpack.com> - 1.6-1
- Initial release
