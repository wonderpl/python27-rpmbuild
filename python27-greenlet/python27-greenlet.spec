Name: python27-greenlet
Version: 0.4.4
Release: 1%{?dist}
Summary: Lightweight in-process concurrent programming
Group: Development/Libraries
License: MIT
URL: https://github.com/python-greenlet/greenlet
Source0: http://pypi.python.org/packages/source/g/greenlet/greenlet-%{version}.zip

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools

%description
The greenlet package is a spin-off of Stackless, a version of CPython that
supports micro-threads called "tasklets". Tasklets run pseudo-concurrently
(typically in a single or a few OS-level threads) and are synchronized with
data exchanges on "channels".

%prep
%setup -q -n greenlet-%{version}

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
%{python_sitearch}/greenlet*
%{_includedir}/python%{python_version}/greenlet*

%changelog
* Mon Apr 22 2013 Paul Egan <paulegan@rockpack.com> - 0.4.0-1
- Initial release
