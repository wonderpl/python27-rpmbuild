Name: python27-ooyala
Version: 2
Release: 1
Summary: A library for interacting with the Ooyala video platform
Group: Development/Libraries
License: MIT
URL: https://github.com/ooyala/python-v2-sdk
Source0: https://github.com/ooyala/python-v2-sdk/archive/master.zip

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
The Python SDK is a client class for our V2 API. It allows you to do GET, POST, 
PUT, PATCH and DELETE requests to our API by simply specifying the path to the 
and a (dictionary) parameter to represent the (JSON) data you want to send.

%prep
%setup -q -n python-v2-sdk-master

%build

%install
rm -rf %{buildroot}
%{__install} -D api.py %{buildroot}%{python_sitelib}/ooyala_api.py

%check
#PYTHONPATH=$PWD %{__python} test/api_test.py

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%{python_sitelib}/ooyala*

%changelog
* Wed Dec 04 2013 Paul Egan <paulegan@rockpack.com> - 2-1
- Initial release
