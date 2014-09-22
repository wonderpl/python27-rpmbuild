Name: diamond
Version: 3.4.421
Release: 1
Summary: Smart data producer for graphite graphing package
Group: Development/Libraries
License: MIT License
URL: https://github.com/BrightcoveOS/Diamond
Source0: http://pypi.python.org/packages/source/d/diamond/diamond-%{version}.tar.gz
Source1: diamond.conf
Source2: collector_defaults
Patch1: postgres-collector-replication.patch
Patch2: myrrix-collector.patch

BuildArch: noarch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools
Requires: python27-configobj python27-psycopg2

%description
Diamond is a python daemon that collects system metrics and publishes them to
Graphite (and others). It is capable of collecting cpu, memory, network, i/o,
load and disk metrics. Additionally, it features an API for implementing custom
collectors for gathering metrics from almost any source.

%prep
%setup -q -n diamond-%{version}
%patch1 -p0
%patch2 -p0

# Force Amazon Linux to be recognised like CentOS
sed -e "s/'centos', /'', &/" -i setup.py

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{__install} -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/diamond/
%{__rm} %{buildroot}%{_sysconfdir}/diamond/collectors/*
%{__install} -m 644 %{SOURCE2}/* %{buildroot}%{_sysconfdir}/diamond/collectors/

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add diamond

%preun
if [ $1 -eq 0 ]; then
	/sbin/service diamond stop >/dev/null 2>&1
	/sbin/chkconfig --del diamond
fi

%postun
if [ $1 -ge 1 ]; then
	/sbin/service diamond restart >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{python_sitelib}/*
%{_bindir}/diamond*
%{_datadir}/diamond
%{_sysconfdir}/diamond
%config(noreplace) %{_sysconfdir}/diamond/diamond.conf
%{_sysconfdir}/init.d/diamond
%{_localstatedir}/log/diamond

%changelog
* Thu Nov  7 2013 Paul Egan <paulegan@rockpack.com> - 3.3.286-6
- Added myrrix collector

* Tue Apr 09 2013 Paul Egan <paulegan@rockpack.com> - 3.3.286-1
- Initial release
