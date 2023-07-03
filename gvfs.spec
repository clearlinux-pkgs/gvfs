#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gvfs
Version  : 1.50.5
Release  : 78
URL      : https://download.gnome.org/sources/gvfs/1.50/gvfs-1.50.5.tar.xz
Source0  : https://download.gnome.org/sources/gvfs/1.50/gvfs-1.50.5.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.0
Requires: gvfs-config = %{version}-%{release}
Requires: gvfs-data = %{version}-%{release}
Requires: gvfs-lib = %{version}-%{release}
Requires: gvfs-libexec = %{version}-%{release}
Requires: gvfs-license = %{version}-%{release}
Requires: gvfs-locales = %{version}-%{release}
Requires: gvfs-services = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : colord
BuildRequires : fuse-dev
BuildRequires : gvfs-dev
BuildRequires : libarchive-dev
BuildRequires : libcap-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgdata-dev
BuildRequires : libgpg-error-dev
BuildRequires : libgphoto2-dev
BuildRequires : libmtp-dev
BuildRequires : openssh
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libgdata)
BuildRequires : pkgconfig(libsecret-unstable)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(udisks2)
BuildRequires : python3-dev
BuildRequires : samba-dev
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# GVfs
GVfs is a userspace virtual filesystem implementation for GIO (a library
available in GLib). GVfs comes with a set of backends, including trash support,
SFTP, SMB, HTTP, DAV, and many others. GVfs also contains modules for GIO that
implement volume monitors and persistent metadata storage. There is also FUSE
support that provides limited access to the GVfs filesystems for applications
not using GIO.

%package config
Summary: config components for the gvfs package.
Group: Default

%description config
config components for the gvfs package.


%package data
Summary: data components for the gvfs package.
Group: Data

%description data
data components for the gvfs package.


%package dev
Summary: dev components for the gvfs package.
Group: Development
Requires: gvfs-lib = %{version}-%{release}
Requires: gvfs-data = %{version}-%{release}
Provides: gvfs-devel = %{version}-%{release}
Requires: gvfs = %{version}-%{release}

%description dev
dev components for the gvfs package.


%package lib
Summary: lib components for the gvfs package.
Group: Libraries
Requires: gvfs-data = %{version}-%{release}
Requires: gvfs-libexec = %{version}-%{release}
Requires: gvfs-license = %{version}-%{release}

%description lib
lib components for the gvfs package.


%package libexec
Summary: libexec components for the gvfs package.
Group: Default
Requires: gvfs-config = %{version}-%{release}
Requires: gvfs-license = %{version}-%{release}

%description libexec
libexec components for the gvfs package.


%package license
Summary: license components for the gvfs package.
Group: Default

%description license
license components for the gvfs package.


%package locales
Summary: locales components for the gvfs package.
Group: Default

%description locales
locales components for the gvfs package.


%package services
Summary: services components for the gvfs package.
Group: Systemd services
Requires: systemd

%description services
services components for the gvfs package.


%package tests
Summary: tests components for the gvfs package.
Group: Default
Requires: gvfs = %{version}-%{release}
Requires: bzip2
Requires: python3-core
Requires: udisks2

%description tests
tests components for the gvfs package.


%prep
%setup -q -n gvfs-1.50.5
cd %{_builddir}/gvfs-1.50.5
pushd ..
cp -a gvfs-1.50.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688410599
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddnssd=false \
-Dafc=false \
-Dbluray=false \
-Dcdda=false \
-Dnfs=false \
-Dinstalled_tests=true  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddnssd=false \
-Dafc=false \
-Dbluray=false \
-Dcdda=false \
-Dnfs=false \
-Dinstalled_tests=true  builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gvfs
cp %{_builddir}/gvfs-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gvfs/ec8f58b945698929990e5ab50ec5350ab184cfdd || :
cp %{_builddir}/gvfs-%{version}/daemon/trashlib/COPYING %{buildroot}/usr/share/package-licenses/gvfs/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gvfs
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/gvfsd-fuse-tmpfiles.conf

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/gvfs-smb.convert
/usr/share/dbus-1/services/org.gtk.vfs.Daemon.service
/usr/share/dbus-1/services/org.gtk.vfs.GPhoto2VolumeMonitor.service
/usr/share/dbus-1/services/org.gtk.vfs.GoaVolumeMonitor.service
/usr/share/dbus-1/services/org.gtk.vfs.MTPVolumeMonitor.service
/usr/share/dbus-1/services/org.gtk.vfs.Metadata.service
/usr/share/dbus-1/services/org.gtk.vfs.UDisks2VolumeMonitor.service
/usr/share/glib-2.0/schemas/org.gnome.system.gvfs.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.system.smb.gschema.xml
/usr/share/gvfs/mounts/admin.mount
/usr/share/gvfs/mounts/afp-browse.mount
/usr/share/gvfs/mounts/afp.mount
/usr/share/gvfs/mounts/archive.mount
/usr/share/gvfs/mounts/burn.mount
/usr/share/gvfs/mounts/computer.mount
/usr/share/gvfs/mounts/dav.mount
/usr/share/gvfs/mounts/ftp.mount
/usr/share/gvfs/mounts/ftpis.mount
/usr/share/gvfs/mounts/ftps.mount
/usr/share/gvfs/mounts/google.mount
/usr/share/gvfs/mounts/gphoto2.mount
/usr/share/gvfs/mounts/http.mount
/usr/share/gvfs/mounts/localtest.mount
/usr/share/gvfs/mounts/mtp.mount
/usr/share/gvfs/mounts/network.mount
/usr/share/gvfs/mounts/recent.mount
/usr/share/gvfs/mounts/sftp.mount
/usr/share/gvfs/mounts/smb-browse.mount
/usr/share/gvfs/mounts/smb.mount
/usr/share/gvfs/mounts/trash.mount
/usr/share/gvfs/remote-volume-monitors/goa.monitor
/usr/share/gvfs/remote-volume-monitors/gphoto2.monitor
/usr/share/gvfs/remote-volume-monitors/mtp.monitor
/usr/share/gvfs/remote-volume-monitors/udisks2.monitor
/usr/share/polkit-1/actions/org.gtk.vfs.file-operations.policy
/usr/share/polkit-1/rules.d/org.gtk.vfs.file-operations.rules

%files dev
%defattr(-,root,root,-)
/usr/include/gvfs-client/gvfs/gvfsurimapper.h
/usr/include/gvfs-client/gvfs/gvfsuriutils.h

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gio/modules/libgioremote-volume-monitor.so
/V3/usr/lib64/gio/modules/libgvfsdbus.so
/V3/usr/lib64/gvfs/libgvfscommon.so
/V3/usr/lib64/gvfs/libgvfsdaemon.so
/usr/lib64/gio/modules/libgioremote-volume-monitor.so
/usr/lib64/gio/modules/libgvfsdbus.so
/usr/lib64/gvfs/libgvfscommon.so
/usr/lib64/gvfs/libgvfsdaemon.so

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/gvfs-goa-volume-monitor
/V3/usr/libexec/gvfs-gphoto2-volume-monitor
/V3/usr/libexec/gvfs-mtp-volume-monitor
/V3/usr/libexec/gvfs-udisks2-volume-monitor
/V3/usr/libexec/gvfsd
/V3/usr/libexec/gvfsd-admin
/V3/usr/libexec/gvfsd-afp
/V3/usr/libexec/gvfsd-afp-browse
/V3/usr/libexec/gvfsd-archive
/V3/usr/libexec/gvfsd-burn
/V3/usr/libexec/gvfsd-computer
/V3/usr/libexec/gvfsd-dav
/V3/usr/libexec/gvfsd-ftp
/V3/usr/libexec/gvfsd-fuse
/V3/usr/libexec/gvfsd-google
/V3/usr/libexec/gvfsd-gphoto2
/V3/usr/libexec/gvfsd-http
/V3/usr/libexec/gvfsd-localtest
/V3/usr/libexec/gvfsd-metadata
/V3/usr/libexec/gvfsd-mtp
/V3/usr/libexec/gvfsd-network
/V3/usr/libexec/gvfsd-recent
/V3/usr/libexec/gvfsd-sftp
/V3/usr/libexec/gvfsd-smb
/V3/usr/libexec/gvfsd-smb-browse
/V3/usr/libexec/gvfsd-trash
/usr/libexec/gvfs-goa-volume-monitor
/usr/libexec/gvfs-gphoto2-volume-monitor
/usr/libexec/gvfs-mtp-volume-monitor
/usr/libexec/gvfs-udisks2-volume-monitor
/usr/libexec/gvfsd
/usr/libexec/gvfsd-admin
/usr/libexec/gvfsd-afp
/usr/libexec/gvfsd-afp-browse
/usr/libexec/gvfsd-archive
/usr/libexec/gvfsd-burn
/usr/libexec/gvfsd-computer
/usr/libexec/gvfsd-dav
/usr/libexec/gvfsd-ftp
/usr/libexec/gvfsd-fuse
/usr/libexec/gvfsd-google
/usr/libexec/gvfsd-gphoto2
/usr/libexec/gvfsd-http
/usr/libexec/gvfsd-localtest
/usr/libexec/gvfsd-metadata
/usr/libexec/gvfsd-mtp
/usr/libexec/gvfsd-network
/usr/libexec/gvfsd-recent
/usr/libexec/gvfsd-sftp
/usr/libexec/gvfsd-smb
/usr/libexec/gvfsd-smb-browse
/usr/libexec/gvfsd-trash

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gvfs/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/gvfs/ec8f58b945698929990e5ab50ec5350ab184cfdd

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/gvfs-daemon.service
/usr/lib/systemd/user/gvfs-goa-volume-monitor.service
/usr/lib/systemd/user/gvfs-gphoto2-volume-monitor.service
/usr/lib/systemd/user/gvfs-metadata.service
/usr/lib/systemd/user/gvfs-mtp-volume-monitor.service
/usr/lib/systemd/user/gvfs-udisks2-volume-monitor.service

%files tests
%defattr(-,root,root,-)
/usr/libexec/installed-tests/gvfs/files/bogus-cd.iso.bz2
/usr/libexec/installed-tests/gvfs/files/joliet.iso.bz2
/usr/libexec/installed-tests/gvfs/files/powershot.ioctl
/usr/libexec/installed-tests/gvfs/files/powershot.umockdev
/usr/libexec/installed-tests/gvfs/files/source-gphoto/IMG_0001.jpg
/usr/libexec/installed-tests/gvfs/files/source-gphoto/IMG_0002.jpg
/usr/libexec/installed-tests/gvfs/files/ssh_host_rsa_key
/usr/libexec/installed-tests/gvfs/files/ssh_host_rsa_key.pub
/usr/libexec/installed-tests/gvfs/files/testcert.pem
/usr/libexec/installed-tests/gvfs/files/vfat.img.bz2
/usr/libexec/installed-tests/gvfs/gphoto2.monitor
/usr/libexec/installed-tests/gvfs/gvfs-test
/usr/libexec/installed-tests/gvfs/org.gtk.vfs.Daemon.service
/usr/libexec/installed-tests/gvfs/org.gtk.vfs.GPhoto2VolumeMonitor.service
/usr/libexec/installed-tests/gvfs/org.gtk.vfs.Metadata.service
/usr/libexec/installed-tests/gvfs/org.gtk.vfs.UDisks2VolumeMonitor.service
/usr/libexec/installed-tests/gvfs/session.conf
/usr/libexec/installed-tests/gvfs/udisks2.monitor
/usr/share/installed-tests/gvfs/gvfs-all-tests.test

%files locales -f gvfs.lang
%defattr(-,root,root,-)

