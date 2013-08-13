Name: python27-GeoIP
Version: 1.2.8
Release: 1%{?dist}
Summary: Python bindings for the GeoIP geographical lookup libraries
Group: Development/Libraries
License: LGPLv2+
URL: http://dev.maxmind.com/geoip/legacy/geolite/
Source0: https://github.com/maxmind/geoip-api-python/archive/v%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python2-devel, GeoIP-devel
Requires: GeoIP

%description
This package contains the Python bindings for the GeoIP API, allowing IP to
location lookups to country, city and organization level within Python code.

%prep
%setup -q -n geoip-api-python-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
# To avoid adding un-needed dependencies
chmod -x test*.py

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README ChangeLog test*.py
%{python_sitearch}/GeoIP*

%changelog
* Tue Aug 13 2013 Paul Egan <paulegan@rockpack.com> - 1.2.8-1
- Initial release
