Name: python27-twisted
Version: 12.3.0
Release: 1%{?dist}
Summary: Event-based framework for internet applications
License: MIT
URL: http://twistedmatrix.com/
Source0: README.fedora
#Obtained by running python setup.py egg_info in the unitary tarball
Source1: PKG-INFO

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
Requires: %{name}-core   >= %{version}
Requires: %{name}-conch  >= %{version}
#Requires: %{name}-lore   >= %{version}
Requires: %{name}-mail   >= %{version}
Requires: %{name}-names  >= %{version}
#Requires: %{name}-news   >= %{version}
#Requires: %{name}-runner >= %{version}
Requires: %{name}-web    >= %{version}
#Requires: %{name}-words  >= %{version}
Provides: Twisted = %{version}-%{release}
Provides: twisted = %{version}-%{release}

%description
Twisted is an event-based framework for internet applications.  It includes a
web server, a telnet server, a chat server, a news server, a generic client
and server for remote object access, and APIs for creating new protocols and
services. Twisted supports integration of the Tk, GTK+, Qt or wxPython event
loop with its main event loop. The Win32 event loop is also supported, as is
basic support for running servers on top of Jython.

Installing this package brings all Twisted sub-packages into your system.

%prep
%setup -c -T
install -p -m 0644 %{SOURCE0} README

%install
install -d $RPM_BUILD_ROOT%{python_sitelib}
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{python_sitelib}/Twisted-%{version}-py2.7.egg-info

%files
%doc README
%{python_sitelib}/Twisted-%{version}-py2.7.egg-info

%changelog
* Tue Feb 26 2013 Paul Egan <paulegan@rockpack.com> - 12.3.0-1
- Initial release
