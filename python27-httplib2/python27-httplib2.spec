Name: python27-httplib2
Version: 0.9
Release: 1
Summary: A comprehensive HTTP client library
Group: System Environment/Libraries
License: MIT
URL: https://github.com/jcgregorio/httplib2
Source0: https://pypi.python.org/packages/source/h/httplib2/httplib2-%{version}.tar.gz
Patch1: python-httplib2.certfile.patch
Patch2: python-httplib2.getCertHost.patch
Patch3: python-httplib2.rfc2459.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
A comprehensive HTTP client library that supports many features left out of
other HTTP libraries.

%prep
%setup -q -n httplib2-%{version}
%patch1 -p0 -b .certfile
%patch2 -p0 -b .getCertHost
%patch3 -p0 -b .rfc2459

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%doc README.md
%{python_sitelib}/*

%changelog
* Fri Mar  8 2013 Paul Egan <paulegan@rockpack.com> - 0.7.7
- Initial release
