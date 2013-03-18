Name: python27-blinker
Version: 1.2
Release: 1
Summary: Fast, simple object-to-object and broadcast signaling
Group: Development/Libraries
License: MIT
URL: http://discorporate.us/projects/Blinker/
Source0: http://pypi.python.org/packages/source/b/blinker/blinker-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
Blinker
=======

Blinker provides a fast dispatching system that allows any
number of interested parties to subscribe to events, or "signals".
Signal receivers can subscribe to specific senders or receive signals
sent by any sender.

%prep
%setup -q -n blinker-%{version}

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
%{python_sitelib}/blinker*

%changelog
* Mon Mar 18 2013 Paul Egan <paulegan@rockpack.com> - 1.2-1
- Initial release
