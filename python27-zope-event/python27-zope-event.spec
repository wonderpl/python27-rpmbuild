Name: python27-zope-event
Version: 4.0.3
Release: 1
Summary: Zope Event Publication
Group: Development/Languages
License: ZPLv2.1
URL: http://pypi.python.org/pypi/zope.event/
Source0: http://pypi.python.org/packages/source/z/zope.event/zope.event-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
The zope.event package provides a simple event system. It provides
an event publishing system and a very simple event-dispatching system
on which more sophisticated event dispatching systems can be built.
(For example, a type-based event dispatching system that builds on
zope.event can be found in zope.component.)

%prep
%setup -q -n zope.event-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%check
%{__python} setup.py test
 
%files
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{python_sitelib}/zope*
%exclude %{python_sitelib}/zope/event/tests.py*

%changelog
* Tue Feb 26 2013 Paul Egan <paulegan@rockpack.com> - 3.5.1-1
- Initial release
