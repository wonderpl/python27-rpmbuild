Name: python27-scrapy
Version: 0.16.4
Release: 1
Summary: A high-level Python Screen Scraping framework
Group: Development/Libraries
License: BSD
URL: http://scrapy.org
Source0: http://pypi.python.org/packages/source/S/Scrapy/Scrapy-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-twisted python27-w3lib python27-lxml

%description
Scrapy is a fast high-level screen scraping and web crawling framework, used to
crawl websites and extract structured data from their pages. It can be used for
a wide range of purposes, from data mining to monitoring and automated testing.

%prep
%setup -q -n Scrapy-%{version}

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
%{python_sitelib}/*
%{_bindir}/*

%changelog
* Tue Feb 26 2013 Paul Egan <paulegan@rockpack.com> - 0.16.4-1
- Initial release
