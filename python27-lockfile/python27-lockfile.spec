Name: python27-lockfile
Version: 0.9.1
Release: 1
Summary: Platform-independent file locking module
Group: Development/Libraries
License: MIT
URL: http://code.google.com/p/pylockfile/
Source0: http://pylockfile.googlecode.com/files/lockfile-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
The lockfile package exports a LockFile class which provides a simple API for
locking files.  Unlike the Windows msvcrt.locking function, the fcntl.lockf
and flock functions, and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows platforms.

%prep
%setup -q -n lockfile-%{version}

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
%{python_sitelib}/lockfile*

%changelog
* Tue Feb 05 2013 Paul Egan <paulegan@rockpack.com> - 0.9.1-1
- Initial release
