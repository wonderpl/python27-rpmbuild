Name: python27-w3lib
Version: 1.2
Release: 1
Summary: Library of web-related functions
Group: Development/Libraries
License: BSD
URL: http://github.com/scrapy/w3lib
Source0: http://pypi.python.org/packages/source/w/w3lib/w3lib-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
This is a Python library of web-related functions, such as:

- remove comments, or tags from HTML snippets
- extract base url from HTML snippets
- translate entites on HTML strings
- encoding mulitpart/form-data
- convert raw HTTP headers to dicts and vice-versa
- construct HTTP auth header
- converting HTML pages to unicode
- RFC-compliant url joining
- sanitize urls (like browsers do)
- extract arguments from urls


%prep
%setup -q -n w3lib-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc 
%{python_sitelib}/w3lib*

%changelog
* Tue Feb 26 2013 Paul Egan <paulegan@rockpack.com> - 1.2-1
- Initial release
