Name: python27-google-api-client
Version: 1.1
Release: 1
Summary: Google API Client Library for Python
Group: Development/Libraries
License: ASL
URL: http://code.google.com/p/google-api-client/
Source0: http://google-api-python-client.googlecode.com/files/google-api-python-client-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools python27-gflags
Requires: python27-httplib2 python27-gflags

%description
The Google API Client for Python is a client library for accessing the Plus,
Moderator, and many other Google APIs.

%prep
%setup -q -n google-api-python-client-%{version}

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
%doc README FAQ LICENSE
%{python_sitelib}/apiclient
%{python_sitelib}/oauth2client
%{python_sitelib}/uritemplate
%{python_sitelib}/*.egg-info
%exclude %{_bindir}/*

%changelog
* Wed Apr 24 2013 Paul Egan <paulegan@rockpack.com> - 1.1-1
- Initial release
