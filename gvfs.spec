#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gvfs
Version  : 1.38.1
Release  : 39
URL      : https://download.gnome.org/sources/gvfs/1.38/gvfs-1.38.1.tar.xz
Source0  : https://download.gnome.org/sources/gvfs/1.38/gvfs-1.38.1.tar.xz
Summary  : Virtual filesystem implementation for GIO
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.0
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : colord
BuildRequires : fuse-dev
BuildRequires : gvfs-dev
BuildRequires : libarchive-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgdata-dev
BuildRequires : libgpg-error-dev
BuildRequires : libgphoto2-dev
BuildRequires : libgudev-dev
BuildRequires : libmtp-dev
BuildRequires : libsecret-dev
BuildRequires : openssh
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libgdata)
BuildRequires : python3-dev
BuildRequires : samba-dev
BuildRequires : udisks2-dev
BuildRequires : valgrind
Patch1: fuse3.patch

%description
# GVfs
GVfs is a userspace virtual filesystem implementation for GIO (a library
available in GLib). GVfs comes with a set of backends, including trash support,
SFTP, SMB, HTTP, DAV, and many others. GVfs also contains modules for GIO that
implement volume monitors and persistent metadata storage. There is also FUSE
support that provides limited access to the GVfs filesystems for applications
not using GIO.

%prep
%setup -q -n gvfs-1.38.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549289744
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Dadmin=false -Ddnssd=false -Dafc=false -Dbluray=false -Dcdda=false -Dnfs=false  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gvfs
cp COPYING %{buildroot}/usr/share/package-licenses/gvfs/COPYING
cp daemon/trashlib/COPYING %{buildroot}/usr/share/package-licenses/gvfs/daemon_trashlib_COPYING
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
