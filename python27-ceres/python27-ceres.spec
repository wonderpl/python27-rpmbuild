Name: python27-ceres
Version: 0.10.0
Release: 1
Summary: Distributable time-series database
Group: Development/Libraries
License: ASL
URL: https://launchpad.net/graphite
Source0: https://github.com/graphite-project/ceres/archive/master.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
Distributable time-series database

%prep
%setup -q -n ceres-master

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/*
%{python_sitelib}/*

%changelog
* Wed Apr 10 2013 Paul Egan <paulegan@rockpack.com> - 0.10.0-1
- Initial release
