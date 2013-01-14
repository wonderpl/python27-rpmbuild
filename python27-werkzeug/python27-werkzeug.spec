Name: python27-werkzeug
Version: 0.8.3
Release: 1
Summary: The Swiss Army knife of Python web development 
Group: Development/Libraries
License: BSD
URL: http://werkzeug.pocoo.org/
Source0: http://pypi.python.org/packages/source/W/Werkzeug/Werkzeug-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
Werkzeug started as simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules.  It includes a powerful debugger, full featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

Werkzeug is unicode aware and doesn't enforce a specific template
engine, database adapter or anything else.  It doesn't even enforce
a specific way of handling requests and leaves all that up to the
developer. It's most useful for end user applications which should work
on as many server environments as possible (such as blogs, wikis,
bulletin boards, etc.).

%prep
%setup -q -n Werkzeug-%{version}
#%{__sed} -i 's/\r//' LICENSE
#%{__sed} -i '1d' werkzeug/testsuite/multipart/collect.py

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE PKG-INFO CHANGES
%{python_sitelib}/*

%changelog
* Fri Jan 11 2013 Paul Egan <paulegan@rockpack.com> - 0.8.3-1
- Initial release
