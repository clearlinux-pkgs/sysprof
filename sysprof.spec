#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sysprof
Version  : 3.34.0
Release  : 3
URL      : https://download.gnome.org/sources/sysprof/3.34/sysprof-3.34.0.tar.xz
Source0  : https://download.gnome.org/sources/sysprof/3.34/sysprof-3.34.0.tar.xz
Summary  : Kernel based performance profiler
Group    : Development/Tools
License  : BSD-2-Clause-Patent GPL-2.0 GPL-3.0
Requires: sysprof-bin = %{version}-%{release}
Requires: sysprof-data = %{version}-%{release}
Requires: sysprof-libexec = %{version}-%{release}
Requires: sysprof-license = %{version}-%{release}
Requires: sysprof-locales = %{version}-%{release}
Requires: sysprof-services = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : libdazzle-dev
BuildRequires : pkgconfig(libdazzle-1.0)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : polkit-dev

%description
Sysprof is a sampling profiler that uses a kernel module to generate
stacktraces which are then interpreted by the userspace program
"sysprof".

%package bin
Summary: bin components for the sysprof package.
Group: Binaries
Requires: sysprof-data = %{version}-%{release}
Requires: sysprof-libexec = %{version}-%{release}
Requires: sysprof-license = %{version}-%{release}
Requires: sysprof-services = %{version}-%{release}

%description bin
bin components for the sysprof package.


%package data
Summary: data components for the sysprof package.
Group: Data

%description data
data components for the sysprof package.


%package dev
Summary: dev components for the sysprof package.
Group: Development
Requires: sysprof-bin = %{version}-%{release}
Requires: sysprof-data = %{version}-%{release}
Provides: sysprof-devel = %{version}-%{release}
Requires: sysprof = %{version}-%{release}

%description dev
dev components for the sysprof package.


%package doc
Summary: doc components for the sysprof package.
Group: Documentation

%description doc
doc components for the sysprof package.


%package libexec
Summary: libexec components for the sysprof package.
Group: Default
Requires: sysprof-license = %{version}-%{release}

%description libexec
libexec components for the sysprof package.


%package license
Summary: license components for the sysprof package.
Group: Default

%description license
license components for the sysprof package.


%package locales
Summary: locales components for the sysprof package.
Group: Default

%description locales
locales components for the sysprof package.


%package services
Summary: services components for the sysprof package.
Group: Systemd services

%description services
services components for the sysprof package.


%package staticdev
Summary: staticdev components for the sysprof package.
Group: Default
Requires: sysprof-dev = %{version}-%{release}

%description staticdev
staticdev components for the sysprof package.


%prep
%setup -q -n sysprof-3.34.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569965659
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Denable-gtk=true -Ddebugdir=/usr/lib/debug -Dhelp=true  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/sysprof
cp COPYING %{buildroot}/usr/share/package-licenses/sysprof/COPYING
cp COPYING.gpl-2 %{buildroot}/usr/share/package-licenses/sysprof/COPYING.gpl-2
cp src/libsysprof-capture/COPYING %{buildroot}/usr/share/package-licenses/sysprof/src_libsysprof-capture_COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang sysprof

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sysprof
/usr/bin/sysprof-cli

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Sysprof3.desktop
/usr/share/dbus-1/interfaces/org.gnome.Sysprof2.xml
/usr/share/dbus-1/interfaces/org.gnome.Sysprof3.Profiler.xml
/usr/share/dbus-1/interfaces/org.gnome.Sysprof3.Service.xml
/usr/share/dbus-1/system-services/org.gnome.Sysprof2.service
/usr/share/dbus-1/system-services/org.gnome.Sysprof3.service
/usr/share/dbus-1/system.d/org.gnome.Sysprof2.conf
/usr/share/dbus-1/system.d/org.gnome.Sysprof3.conf
/usr/share/glib-2.0/schemas/org.gnome.sysprof3.gschema.xml
/usr/share/icons/hicolor/scalable/actions/sysprof-trace-app.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.Sysprof.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Sysprof-symbolic.svg
/usr/share/metainfo/org.gnome.Sysprof3.appdata.xml
/usr/share/mime-packages/sysprof-mime.xml
/usr/share/polkit-1/actions/org.gnome.sysprof3.policy

%files dev
%defattr(-,root,root,-)
/usr/include/sysprof-3/sysprof-address.h
/usr/include/sysprof-3/sysprof-battery-source.h
/usr/include/sysprof-3/sysprof-callgraph-profile.h
/usr/include/sysprof-3/sysprof-capture-condition.h
/usr/include/sysprof-3/sysprof-capture-cursor.h
/usr/include/sysprof-3/sysprof-capture-gobject.h
/usr/include/sysprof-3/sysprof-capture-reader.h
/usr/include/sysprof-3/sysprof-capture-symbol-resolver.h
/usr/include/sysprof-3/sysprof-capture-types.h
/usr/include/sysprof-3/sysprof-capture-writer.h
/usr/include/sysprof-3/sysprof-capture.h
/usr/include/sysprof-3/sysprof-check.h
/usr/include/sysprof-3/sysprof-clock.h
/usr/include/sysprof-3/sysprof-diskstat-source.h
/usr/include/sysprof-3/sysprof-display.h
/usr/include/sysprof-3/sysprof-elf-symbol-resolver.h
/usr/include/sysprof-3/sysprof-gjs-source.h
/usr/include/sysprof-3/sysprof-governor-source.h
/usr/include/sysprof-3/sysprof-hostinfo-source.h
/usr/include/sysprof-3/sysprof-jitmap-symbol-resolver.h
/usr/include/sysprof-3/sysprof-kernel-symbol-resolver.h
/usr/include/sysprof-3/sysprof-kernel-symbol.h
/usr/include/sysprof-3/sysprof-local-profiler.h
/usr/include/sysprof-3/sysprof-memory-source.h
/usr/include/sysprof-3/sysprof-model-filter.h
/usr/include/sysprof-3/sysprof-netdev-source.h
/usr/include/sysprof-3/sysprof-notebook.h
/usr/include/sysprof-3/sysprof-page.h
/usr/include/sysprof-3/sysprof-perf-counter.h
/usr/include/sysprof-3/sysprof-perf-source.h
/usr/include/sysprof-3/sysprof-platform.h
/usr/include/sysprof-3/sysprof-proc-source.h
/usr/include/sysprof-3/sysprof-process-model-item.h
/usr/include/sysprof-3/sysprof-process-model-row.h
/usr/include/sysprof-3/sysprof-process-model.h
/usr/include/sysprof-3/sysprof-profile.h
/usr/include/sysprof-3/sysprof-profiler.h
/usr/include/sysprof-3/sysprof-proxy-source.h
/usr/include/sysprof-3/sysprof-selection.h
/usr/include/sysprof-3/sysprof-source.h
/usr/include/sysprof-3/sysprof-spawnable.h
/usr/include/sysprof-3/sysprof-symbol-resolver.h
/usr/include/sysprof-3/sysprof-symbols-source.h
/usr/include/sysprof-3/sysprof-tracefd-source.h
/usr/include/sysprof-3/sysprof-ui.h
/usr/include/sysprof-3/sysprof-version-macros.h
/usr/include/sysprof-3/sysprof-version.h
/usr/include/sysprof-3/sysprof-visualizer-group.h
/usr/include/sysprof-3/sysprof-visualizer.h
/usr/include/sysprof-3/sysprof-zoom-manager.h
/usr/include/sysprof-3/sysprof.h
/usr/lib64/libsysprof-3.so
/usr/lib64/libsysprof-ui-3.so
/usr/lib64/pkgconfig/sysprof-3.pc
/usr/lib64/pkgconfig/sysprof-capture-3.pc
/usr/lib64/pkgconfig/sysprof-ui-3.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/sysprof/faq.page
/usr/share/help/C/sysprof/index.page
/usr/share/help/C/sysprof/introduction.page
/usr/share/help/C/sysprof/legal.xml
/usr/share/help/C/sysprof/profiling.page
/usr/share/help/cs/sysprof/faq.page
/usr/share/help/cs/sysprof/index.page
/usr/share/help/cs/sysprof/introduction.page
/usr/share/help/cs/sysprof/legal.xml
/usr/share/help/cs/sysprof/profiling.page
/usr/share/help/de/sysprof/faq.page
/usr/share/help/de/sysprof/index.page
/usr/share/help/de/sysprof/introduction.page
/usr/share/help/de/sysprof/legal.xml
/usr/share/help/de/sysprof/profiling.page
/usr/share/help/es/sysprof/faq.page
/usr/share/help/es/sysprof/index.page
/usr/share/help/es/sysprof/introduction.page
/usr/share/help/es/sysprof/legal.xml
/usr/share/help/es/sysprof/profiling.page
/usr/share/help/pl/sysprof/faq.page
/usr/share/help/pl/sysprof/index.page
/usr/share/help/pl/sysprof/introduction.page
/usr/share/help/pl/sysprof/legal.xml
/usr/share/help/pl/sysprof/profiling.page
/usr/share/help/pt_BR/sysprof/faq.page
/usr/share/help/pt_BR/sysprof/index.page
/usr/share/help/pt_BR/sysprof/introduction.page
/usr/share/help/pt_BR/sysprof/legal.xml
/usr/share/help/pt_BR/sysprof/profiling.page
/usr/share/help/sv/sysprof/faq.page
/usr/share/help/sv/sysprof/index.page
/usr/share/help/sv/sysprof/introduction.page
/usr/share/help/sv/sysprof/legal.xml
/usr/share/help/sv/sysprof/profiling.page

%files libexec
%defattr(-,root,root,-)
/usr/libexec/sysprofd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sysprof/COPYING
/usr/share/package-licenses/sysprof/COPYING.gpl-2
/usr/share/package-licenses/sysprof/src_libsysprof-capture_COPYING

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/sysprof2.service
/usr/lib/systemd/system/sysprof3.service

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libsysprof-capture-3.a

%files locales -f sysprof.lang
%defattr(-,root,root,-)

