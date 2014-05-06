Name: python27-apnsclient
Version: 0.1.8
Release: 2
Summary: Python client for Apple Push Notification service (APNs)
Group: Development/Libraries
License: ASL
URL: https://bitbucket.org/sardarnl/apns-client
Source0: https://pypi.python.org/packages/source/a/apns-client/apns-client-%{version}.tar.gz
Patch0: content_available.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-openssl

%description
Python client for `Apple Push Notification service (APNs) .

%prep
%setup -q -n apns-client-%{version}
%patch0 -p1

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
%doc README.rst LICENSE
%{python_sitelib}/apnsclient*
%{python_sitelib}/*.egg-info

%changelog
* Fri Oct 11 2013 Paul Egan <paulegan@rockpack.com> - 0.1.8-1
- Bumped to fix unicode payload size issue

* Wed Jul 31 2013 Paul Egan <paulegan@rockpack.com> - 0.1.6-1
- Initial release
