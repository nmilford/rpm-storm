rpm-storm
=========

An RPM spec file for the Storm distributed and fault-tolerant realtime computation system.

To build:

`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`wget https://raw.github.com/nmilford/rpm-storm/master/storm.spec -O ~/rpmbuild/SPECS/storm.spec`
`wget https://dl.dropbox.com/u/133901206/storm-0.9.0-wip16.zip -O ~/rpmbuild/SOURCES/storm-0.9.0-wip16.zip`
`wget https://raw.github.com/nmilford/rpm-storm/master/storm -O ~/rpmbuild/SOURCES/storm`
`wget https://raw.github.com/nmilford/rpm-storm/master/storm-nimbus -O ~/rpmbuild/SOURCES/storm-nimbus`
`wget https://raw.github.com/nmilford/rpm-storm/master/storm-supervisor -O ~/rpmbuild/SOURCES/storm-supervisor`
`wget https://raw.github.com/nmilford/rpm-storm/master/storm-ui -O ~/rpmbuild/SOURCES/storm-ui`
`wget https://raw.github.com/nmilford/rpm-storm/master/storm.nofiles.conf -O ~/rpmbuild/SOURCES/storm.nofiles.conf`
`wget https://raw.github.com/nmilford/rpm-storm/master/cluster.xml -O ~/rpmbuild/SOURCES/cluster.xml`

`rpmbuild -bb ~/rpmbuild/SPECS/storm.spec`

