Name: python27-gflags
Version: 2.0
Release: 1
Summary: Google Commandline Flags Module
Group: Development/Libraries
License: BSD
URL: http://code.google.com/p/python-gflags
Source0: http://python-gflags.googlecode.com/files/python-gflags-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
This project is the python equivalent of gflags, a commandline flag
implementation for C++ originally written by Google. It is intended to be used
in situations where a project wants to mimic the command-line flag handling of
a C++ app that uses gflags, or for a Python app that, via swig or some other
means, is linked with a C++ app that uses gflags.

%prep
%setup -q -n python-gflags-%{version}

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
%doc README
%{python_sitelib}/*gflags*
%exclude %{_bindir}/*

%changelog
* Wed Apr 24 2013 Paul Egan <paulegan@rockpack.com> - 2.0-1
- Initial release
