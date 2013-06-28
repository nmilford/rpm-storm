rpm-storm
=========

An RPM spec file for the Storm distributed and fault-tolerant realtime computation system.

To build:

`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`wget https://raw.github.com/nmilford/specfiles/master/rpm-storm/storm.spec -O ~/rpmbuild/SPECS/storm.spec`
`wget https://dl.dropbox.com/u/133901206/storm-0.9.0-wip16.zip -O ~/rpmbuild/SOURCES/storm-0.9.0-wip16.zip`
`wget https://raw.github.com/nmilford/specfiles/master/rpm-storm/storm -O ~/rpmbuild/SOURCES/storm`
`wget https://raw.github.com/nmilford/specfiles/master/rpm-storm/storm-nimbus -O ~/rpmbuild/SOURCES/storm-nimbus`
`wget https://raw.github.com/nmilford/specfiles/master/rpm-storm/storm-supervisor -O ~/rpmbuild/SOURCES/storm-supervisor`
`wget https://raw.github.com/nmilford/specfiles/master/rpm-storm/storm-ui -O ~/rpmbuild/SOURCES/storm-ui`
`wget https://raw.github.com/nmilford/specfiles/master/rpm-storm/storm.nofiles.conf -O ~/rpmbuild/SOURCES/storm.nofiles.conf`
`wget https://raw.github.com/nmilford/specfiles/master/rpm-storm/cluster.xml -O ~/rpmbuild/SOURCES/cluster.xml

`rpmbuild -bb ~/rpmbuild/SPECS/storm.spec`