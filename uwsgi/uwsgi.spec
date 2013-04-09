Name: uwsgi
Version: 1.4.9
Release: 1%{?dist}
Summary: Fast, self-healing, application container server
Group: System Environment/Daemons   
License: GPLv2
URL: http://projects.unbit.it/uwsgi
Source0: http://projects.unbit.it/downloads/%{name}-%{version}.tar.gz
Patch0: uwsgi_fix_rpath.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python2-devel, libxml2-devel, libuuid-devel
BuildRequires: libyaml-devel

%description
uWSGI is a fast (pure C), self-healing, developer/sysadmin-friendly
application container server.  Born as a WSGI-only server, over time it has
evolved in a complete stack for networked/clustered web applications,
implementing message/object passing, caching, RPC and process management. 
It uses the uwsgi (all lowercase, already included by default in the Nginx
and Cherokee releases) protocol for all the networking/interprocess
communications.  Can be run in preforking mode, threaded,
asynchronous/evented and supports various form of green threads/co-routine
(like uGreen and Fiber).  Sysadmin will love it as it can be configured via
command line, environment variables, xml, .ini and yaml files and via LDAP. 
Being fully modular can use tons of different technology on top of the same
core.

%prep
%setup -q
cat >>buildconf/default.ini <<-EOF
	embedded_plugins = echo, ping, corerouter, http, python, carbon
	plugins = admin, cache, logfile
	_plugin_dir = %{_libdir}/%{name}
EOF
%patch0 -p1

%build
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --build

%install
%{__install} -d %{buildroot}%{_sbindir}
%{__install} -d %{buildroot}%{_includedir}/%{name}
%{__install} -d %{buildroot}%{_libdir}/%{name}
%{__install} -d %{buildroot}%{python_sitelib}
%{__install} -p -m 0755 uwsgi %{buildroot}%{_sbindir}
%{__install} -p -m 0644 *.h %{buildroot}%{_includedir}/%{name}
%{__install} -p -m 0755 *_plugin.so %{buildroot}%{_libdir}/%{name}
%{__install} -p -m 0644 uwsgidecorators.py %{buildroot}%{python_sitelib}

%files 
%doc ChangeLog LICENSE README
%{_sbindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_includedir}/%{name}
%{python_sitelib}/*

%changelog
* Tue Apr  9 2013 Paul Egan <paulegan@rockpack.com> - 1.4.9-1
- Bumped and enabled carbon plugin

* Mon Jan  7 2013 Paul Egan <paulegan@rockpack.com> - 1.4.4-1
- Initial release
