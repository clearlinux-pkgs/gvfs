#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gvfs
Version  : 1.32.1
Release  : 11
URL      : https://download.gnome.org/sources/gvfs/1.32/gvfs-1.32.1.tar.xz
Source0  : https://download.gnome.org/sources/gvfs/1.32/gvfs-1.32.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.0
Requires: gvfs-bin
Requires: gvfs-config
Requires: gvfs-lib
Requires: gvfs-data
Requires: gvfs-locales
Requires: gvfs-doc
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libarchive-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgdata-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(gcr-base-3)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libcap)
BuildRequires : pkgconfig(libgdata)
BuildRequires : pkgconfig(libsecret-unstable)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(smbclient)
BuildRequires : pkgconfig(systemd)
BuildRequires : python3-dev
BuildRequires : samba-dev
BuildRequires : sed
BuildRequires : valgrind

%description
gvfs is a userspace virtual filesystem designed to work with the i/o
abstractions of gio (a library availible in glib >= 2.15.1). It
installs several modules that are automatically used by applications
using the APIs of libgio. There is also fuse support that allows
applications not using gio to access the gvfs filesystems.

%package bin
Summary: bin components for the gvfs package.
Group: Binaries
Requires: gvfs-data
Requires: gvfs-config

%description bin
bin components for the gvfs package.


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
Requires: gvfs-lib
Requires: gvfs-bin
Requires: gvfs-data
Provides: gvfs-devel

%description dev
dev components for the gvfs package.


%package doc
Summary: doc components for the gvfs package.
Group: Documentation

%description doc
doc components for the gvfs package.


%package lib
Summary: lib components for the gvfs package.
Group: Libraries
Requires: gvfs-data
Requires: gvfs-config

%description lib
lib components for the gvfs package.


%package locales
Summary: locales components for the gvfs package.
Group: Default

%description locales
locales components for the gvfs package.


%prep
%setup -q -n gvfs-1.32.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492279464
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
%configure --disable-static --disable-gphoto2 \
--disable-udisks2 \
--disable-goa \
--disable-admin
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1492279464
rm -rf %{buildroot}
%make_install
%find_lang gvfs

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gvfs-cat
/usr/bin/gvfs-copy
/usr/bin/gvfs-info
/usr/bin/gvfs-less
/usr/bin/gvfs-ls
/usr/bin/gvfs-mime
/usr/bin/gvfs-mkdir
/usr/bin/gvfs-monitor-dir
/usr/bin/gvfs-monitor-file
/usr/bin/gvfs-mount
/usr/bin/gvfs-move
/usr/bin/gvfs-open
/usr/bin/gvfs-rename
/usr/bin/gvfs-rm
/usr/bin/gvfs-save
/usr/bin/gvfs-set-attribute
/usr/bin/gvfs-trash
/usr/bin/gvfs-tree
/usr/libexec/gvfsd
/usr/libexec/gvfsd-afp
/usr/libexec/gvfsd-afp-browse
/usr/libexec/gvfsd-archive
/usr/libexec/gvfsd-burn
/usr/libexec/gvfsd-computer
/usr/libexec/gvfsd-dav
/usr/libexec/gvfsd-ftp
/usr/libexec/gvfsd-fuse
/usr/libexec/gvfsd-google
/usr/libexec/gvfsd-http
/usr/libexec/gvfsd-localtest
/usr/libexec/gvfsd-metadata
/usr/libexec/gvfsd-network
/usr/libexec/gvfsd-recent
/usr/libexec/gvfsd-sftp
/usr/libexec/gvfsd-smb
/usr/libexec/gvfsd-smb-browse
/usr/libexec/gvfsd-trash

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/user/gvfs-daemon.service
/usr/lib/systemd/user/gvfs-metadata.service
/usr/lib/tmpfiles.d/gvfsd-fuse-tmpfiles.conf

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/gvfs-smb.convert
/usr/share/dbus-1/services/org.gtk.vfs.Daemon.service
/usr/share/dbus-1/services/org.gtk.vfs.Metadata.service
/usr/share/glib-2.0/schemas/org.gnome.system.gvfs.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.system.smb.gschema.xml
/usr/share/gvfs/mounts/afp-browse.mount
/usr/share/gvfs/mounts/afp.mount
/usr/share/gvfs/mounts/archive.mount
/usr/share/gvfs/mounts/burn.mount
/usr/share/gvfs/mounts/computer.mount
/usr/share/gvfs/mounts/dav.mount
/usr/share/gvfs/mounts/ftp.mount
/usr/share/gvfs/mounts/ftps.mount
/usr/share/gvfs/mounts/google.mount
/usr/share/gvfs/mounts/http.mount
/usr/share/gvfs/mounts/localtest.mount
/usr/share/gvfs/mounts/network.mount
/usr/share/gvfs/mounts/recent.mount
/usr/share/gvfs/mounts/sftp.mount
/usr/share/gvfs/mounts/smb-browse.mount
/usr/share/gvfs/mounts/smb.mount
/usr/share/gvfs/mounts/trash.mount
/usr/share/polkit-1/actions/org.gtk.vfs.file-operations.policy
/usr/share/polkit-1/rules.d/org.gtk.vfs.file-operations.rules

%files dev
%defattr(-,root,root,-)
/usr/include/gvfs-client/gvfs/gvfsurimapper.h
/usr/include/gvfs-client/gvfs/gvfsuriutils.h

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man7/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/gio/modules/libgioremote-volume-monitor.so
/usr/lib64/gio/modules/libgvfsdbus.so
/usr/lib64/gvfs/libgvfscommon.so
/usr/lib64/gvfs/libgvfsdaemon.so

%files locales -f gvfs.lang
%defattr(-,root,root,-)

