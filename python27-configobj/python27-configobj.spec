Name: python27-configobj
Version: 4.7.2
Release: 1
Summary: Config file reading, writing and validation
Group: Development/Libraries
License: BSD
URL: http://www.voidspace.org.uk/python/configobj.html
Source0: http://pypi.python.org/packages/source/c/configobj/configobj-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
ConfigObj is a simple but powerful config file reader and writer: an ini
file round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files.

%prep
%setup -q -n configobj-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc PKG-INFO
%{python_sitelib}/configobj*
%{python_sitelib}/validate*

%changelog
* Tue Apr 09 2013 Paul Egan <paulegan@rockpack.com> - 4.7.2-1
- Initial release
