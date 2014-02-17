Name: python27-eventlet
Version: 0.14.0
Release: 1%{?dist}
Summary: Highly concurrent networking library
Group: Development/Libraries
License: MIT
URL: http://eventlet.net/
Source0: https://pypi.python.org/packages/source/e/eventlet/eventlet-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools python27-devel python27-greenlet
Requires: python27-greenlet

%description
Eventlet is a concurrent networking library for Python that allows you to change how you run your code, not how you write it.
        
It uses epoll or libevent for highly scalable non-blocking I/O.  Coroutines ensure that the developer uses a blocking style of programming that is similar to threading, but provide the benefits of non-blocking I/O.  The event dispatch is implicit, which means you ca
n easily use Eventlet from the Python interpreter, or as a small part of a larger application.

%prep
%setup -q -n eventlet-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE
%{python_sitelib}/eventlet*


%changelog
* Mon Aug 12 2013 Allan Brisbane <allan@rockpack.com> - 0.12.1-1
- Initial release
