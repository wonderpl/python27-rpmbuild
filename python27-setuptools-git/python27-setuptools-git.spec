Name: python27-setuptools-git
Version: 1.0b1
Release: 1
Summary: Setuptools revision control system plugin for Git
Group: Development/Libraries
License: BSD
URL: https://github.com/wichert/setuptools-git
Source0: http://pypi.python.org/packages/source/s/setuptools-git/setuptools-git-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
This is a plugin for setuptools that enables git integration. Once
installed, Setuptools can be told to include in a package distribution
all the files tracked by git. This is an alternative to explicit
inclusion specifications with MANIFEST.in.

%prep
%setup -q -n setuptools-git-%{version}

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
%doc README.rst LICENSE.txt
%{python_sitelib}/setuptools_git*

%changelog
* Tue Jan 22 2013 Paul Egan <paulegan@rockpack.com> - 1.0b1-1
- Initial release
