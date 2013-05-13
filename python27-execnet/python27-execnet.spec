Name: python27-execnet
Version: 1.1
Release: 1
Summary: execnet: rapid multi-Python deployment
Group: Development/Libraries
License: GPL
URL: http://codespeak.net/execnet
Source0: http://pypi.python.org/packages/source/e/execnet/execnet-%{version}.zip

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
execnet provides carefully tested means to ad-hoc interact with Python
interpreters across version, platform and network barriers. It provides a
minimal and fast API targetting the following uses:

  * distribute tasks to local or remote CPUs
  * write and deploy hybrid multi-process applications
  * write scripts to administer a bunch of exec environments

%prep
%setup -q -n execnet-%{version}

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
%doc README.txt LICENSE
%{python_sitelib}/execnet*

%changelog
* Thu May 09 2013 Paul Egan <paulegan@rockpack.com> - 1.1-1
- Initial release
