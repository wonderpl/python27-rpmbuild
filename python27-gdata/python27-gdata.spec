Name: python27-gdata
Version: 2.0.17
Release: 1
Summary: A Python module for accessing online Google services
Group: Development/Languages
License: ASL 2.0
URL: http://code.google.com/p/gdata-python-client/
Source0: http://gdata-python-client.googlecode.com/files/gdata-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-devel


%description
This is a Python module for accessing online Google services such as:
- Base
- Blogger
- Calendar
- Health
- Picasa Web Albums
- Spreadsheets
- Documents List
- Contacts
- YouTube
- Google Apps Provisioning
- Code Search
- Notebook
- Webmaster Tools API
- Google Analytics Data Export API
- Google Book Search Data API
- Google Finance Portfolio Data API
- Google Maps Data API
- Sites Data API
- Issue Tracker Data API


%prep
%setup -q -n gdata-%{version}
find samples src -type f -print0 | xargs -0 chmod a-x

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt RELEASE_NOTES.txt samples/
%{python_sitelib}/atom
%{python_sitelib}/gdata*

%changelog
* Wed Feb 13 2013 Paul Egan <paulegan@rockpack.com> - 2.0.17-1
- Initial release
