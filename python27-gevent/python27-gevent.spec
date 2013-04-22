Name: python27-gevent
Version: 1.0rc2
Release: 1%{?dist}
Summary: Coroutine-based concurrency library for Python
Group: Development/Libraries
License: MIT
URL: http://www.gevent.org/
Source0: https://github.com/surfly/gevent/archive/%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools python27-greenlet
Requires: python27-greenlet

%description
gevent is a coroutine-based Python networking library.

Features include:

  * Fast event loop based on libev.
  * Lightweight execution units based on greenlet.
  * Familiar API that re-uses concepts from the Python standard library.
  * Cooperative sockets with SSL support.
  * DNS queries performed through c-ares or a threadpool.
  * Ability to use standard library and 3rd party modules written for standard blocking sockets

%prep
%setup -q -n gevent-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

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
%{python_sitearch}/gevent*


%changelog
* Mon Apr 22 2013 Paul Egan <paulegan@rockpack.com> - 0.13.8-1
- Initial release
