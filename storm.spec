# To build:
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
#
# wget https://raw.github.com/nmilford/rpm-storm/master/storm.spec -O ~/rpmbuild/SPECS/storm.spec
# wget https://dl.dropbox.com/u/133901206/storm-0.9.0-wip16.zip -O ~/rpmbuild/SOURCES/storm-0.9.0-wip16.zip
# wget https://raw.github.com/nmilford/rpm-storm/master/storm -O ~/rpmbuild/SOURCES/storm
# wget https://raw.github.com/nmilford/rpm-storm/master/storm-nimbus -O ~/rpmbuild/SOURCES/storm-nimbus
# wget https://raw.github.com/nmilford/rpm-storm/master/storm-supervisor -O ~/rpmbuild/SOURCES/storm-supervisor
# wget https://raw.github.com/nmilford/rpm-storm/master/storm-ui -O ~/rpmbuild/SOURCES/storm-ui
# wget https://raw.github.com/nmilford/rpm-storm/master/storm.nofiles.conf -O ~/rpmbuild/SOURCES/storm.nofiles.conf
# wget https://raw.github.com/nmilford/rpm-storm/master/cluster.xml -O ~/rpmbuild/SOURCES/cluster.xml
#
# rpmbuild -bb ~/rpmbuild/SPECS/storm.spec

%define storm_name storm
%define storm_branch 0.9
%define storm_ver 0.9.0_wip16
%define storm_version 0.9.0-wip16
%define release_version 4
%define storm_home /opt/%{storm_name}-%{storm_version}
%define etc_storm /etc/%{name}
%define config_storm %{etc_storm}/conf
%define storm_user storm
%define storm_group storm

Name: %{storm_name}
Version: %{storm_ver}
Release: %{release_version}
Summary: Storm is a distributed realtime computation system.
License: Eclipse Public License 1.0
URL: https://github.com/nathanmarz/storm/
Group: Development/Libraries
Source0: %{storm_name}-%{storm_version}.zip
Source1: cluster.xml
Source2: storm-ui
Source3: storm-supervisor
Source4: storm
Source5: storm.nofiles.conf
Source6: storm-nimbus
Source7: storm-drpc
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Requires: sh-utils, textutils, /usr/sbin/useradd, /usr/sbin/usermod, /sbin/chkconfig, /sbin/service
Provides: storm
Vendor: Nathan Marz <nathan.marz@gmail.com>
Packager: Nathan Milford <nathan@milford.io>
BuildArch: noarch

%description
Storm is a distributed realtime computation system. Similar to how Hadoop
provides a set of general primitives for doing batch processing, Storm provides
a set of general primitives for doing realtime computation.

%package nimbus
Summary: The Storm Nimbus node manages the Storm cluster.
Group: System/Daemons
Requires: %{name} = %{version}-%{release}, jzmq, jdk
BuildArch: noarch
%description nimbus
Nimbus is responsible for distributing code around the Storm cluster, assigning
tasks to machines, and monitoring for failures.

%package ui
Summary: The Storm UI exposes metrics for the Storm cluster.
Group: System/Daemons
Requires: %{name} = %{version}-%{release}, jdk
BuildArch: noarch
%description ui
The Storm UI exposes metrics on a web interface on port 8080 to give you
a high level view of the cluster.

%package supervisor
Summary: The Storm Supervisor is a worker process of the Storm cluster.
Group: System/Daemons
Requires: %{name} = %{version}-%{release}, jzmq, jdk
BuildArch: noarch
%description supervisor
The Supervisor listens for work assigned to its machine and starts and stops
worker processes as necessary based on what Nimbus has assigned to it.

%package drpc
Summary: Storm Distributed RPC daemon.
Group: System/Daemons
Requires: %{name} = %{version}-%{release}, jzmq, jdk
BuildArch: noarch
%description drpc
The DRPC server coordinates receiving an RPC request, sending the request to
the Storm topology, receiving the results from the Storm topology, and sending
the results back to the waiting client.

%prep
%setup -n %{storm_name}-%{storm_version}

%build

%clean
rm -rf %{buildroot}

%install
install -d -m 755 %{buildroot}/%{storm_home}/
install    -m 644 %{_builddir}/%{storm_name}-%{storm_version}/*.jar           %{buildroot}/%{storm_home}/
install    -m 644 %{_builddir}/%{storm_name}-%{storm_version}/RELEASE         %{buildroot}/%{storm_home}/
install    -m 644 %{_builddir}/%{storm_name}-%{storm_version}/LICENSE.html    %{buildroot}/%{storm_home}/
install    -m 644 %{_builddir}/%{storm_name}-%{storm_version}/README.markdown %{buildroot}/%{storm_home}/

install -d -m 755 %{buildroot}/%{storm_home}/bin/
install    -m 755 %{_builddir}/%{storm_name}-%{storm_version}/bin/*.sh         %{buildroot}/%{storm_home}/bin
install    -m 755 %{_builddir}/%{storm_name}-%{storm_version}/bin/storm        %{buildroot}/%{storm_home}/bin

install -d -m 755 %{buildroot}/%{storm_home}/conf/
install    -m 644 %{_builddir}/%{storm_name}-%{storm_version}/conf/*           %{buildroot}/%{storm_home}/conf

install -d -m 755 %{buildroot}/%{storm_home}/lib/
install    -m 644 %{_builddir}/%{storm_name}-%{storm_version}/lib/*            %{buildroot}/%{storm_home}/lib

install -d -m 755 %{buildroot}/%{storm_home}/logback/
install    -m 644 %_sourcedir/cluster.xml                                      %{buildroot}/%{storm_home}/logback/cluster.xml

install -d -m 755 %{buildroot}/%{storm_home}/logs/

install -d -m 755 %{buildroot}/%{storm_home}/public/

install -d -m 755 %{buildroot}/%{storm_home}/public/css/
install    -m 644 %{_builddir}/%{storm_name}-%{storm_version}/public/css/*     %{buildroot}/%{storm_home}/public/css/

install -d -m 755 %{buildroot}/%{storm_home}/public/js/
install    -m 644 %{_builddir}/%{storm_name}-%{storm_version}/public/js/*      %{buildroot}/%{storm_home}/public/js/

cd %{buildroot}/opt/
ln -s %{storm_name}-%{storm_version} %{storm_name}
cd -

install -d -m 755 %{buildroot}/etc/
cd %{buildroot}/etc
ln -s %{storm_home}/conf %{storm_name}
cd -

install -d -m 755 %{buildroot}/%{_initrddir}
install    -m 755 %_sourcedir/storm-nimbus     %{buildroot}/%{_initrddir}/storm-nimbus
install    -m 755 %_sourcedir/storm-ui         %{buildroot}/%{_initrddir}/storm-ui
install    -m 755 %_sourcedir/storm-supervisor %{buildroot}/%{_initrddir}/storm-supervisor
install    -m 755 %_sourcedir/storm-drpc       %{buildroot}/%{_initrddir}/storm-drpc
install -d -m 755 %{buildroot}/%{_sysconfdir}/sysconfig
install    -m 644 %_sourcedir/storm            %{buildroot}/%{_sysconfdir}/sysconfig/storm
install -d -m 755 %{buildroot}/%{_sysconfdir}/security/limits.d/
install    -m 644 %_sourcedir/storm.nofiles.conf %{buildroot}/%{_sysconfdir}/security/limits.d/storm.nofiles.conf

install -d -m 755 %{buildroot}/usr/bin/
cd %{buildroot}/usr/bin
ln -s %{storm_home}/bin/%{storm_name} %{storm_name}
cd -

install -d -m 755 %{buildroot}/var/log/
cd %{buildroot}/var/log/
ln -s %{storm_home}/logs %{storm_name}
cd -

install -d -m 755 %{buildroot}/var/run/storm/

install -d -m 755 %{buildroot}/%{storm_home}/local/
echo 'storm.local.dir: "/opt/storm/local/"' >> %{buildroot}/%{storm_home}/conf/storm.yaml.example

%pre
getent group %{storm_group} >/dev/null || groupadd -r %{storm_group}
getent passwd %{storm_user} >/dev/null || /usr/sbin/useradd --comment "Storm Daemon User" --shell /bin/bash -M -r -g %{storm_group} --home /opt/%{storm_name}} %{storm_user}

%files
%defattr(-,%{storm_user},%{storm_group})

/opt/%{storm_name}
%{storm_home}
%{storm_home}/*
%attr(755,%{storm_user},%{storm_group}) %{storm_home}/bin/*
/etc/storm
/var/log/*
/var/run/storm/
/usr/bin/storm
/etc/sysconfig/storm
/etc/security/limits.d/storm.nofiles.conf


%define service_macro() \
%files %1 \
%defattr(-,root,root) \
%{_initrddir}/%{storm_name}-%1 \
%post %1 \
chkconfig --add %{storm_name}-%1 \
\
%preun %1 \
if [ $1 = 0 ]; then \
  service %{storm_name}-%1 stop > /dev/null 2>&1 \
  chkconfig --del %{storm_name}-%1 \
fi

%service_macro nimbus
%service_macro ui
%service_macro supervisor
%service_macro drpc

%changelog
* Mon Jul 31 2013 Nathan Milford <nathan@milford.io> - 0.9.0-wip16-3
- Bumped RPM release version.
- Merged DRPC init script and package declaration by Vitaliy Fuks <https://github.com/vitaliyf>
- Merged init script additions by Daniel Damiani <https://github.com/ddamiani>

* Mon May 13 2013 Nathan Milford <nathan@milford.io> - 0.9.0-wip16
- Storm 0.9.0-wip16

* Wed Aug 08 2012 Nathan Milford <nathan@milford.io> - 0.8.0
- Storm 0.8.0
