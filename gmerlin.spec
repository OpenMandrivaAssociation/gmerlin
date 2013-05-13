Name: gmerlin
Summary: A multimedia architecture for linux
Version: 1.0.0
Release: 3
Url: http://gmerlin.sourceforge.net/
License: LGPLv2+
Group: Video
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source0: http://downloads.sourceforge.net/gmerlin/%name-%version.tar.gz
Patch0: gmerlin-1.0.0-link.patch
BuildRequires: gavl-devel >= 1.2.0
BuildRequires: quicktime-devel
BuildRequires: pulseaudio-devel
BuildRequires: libalsa-devel
BuildRequires: jpeg-devel
BuildRequires: png-devel
BuildRequires: texinfo
BuildRequires: doxygen
BuildRequires: pkgconfig(libxml-2.0) >= 2.4.0
BuildRequires: fontconfig-devel >= 2.2.3
BuildRequires: freetype2-devel
BuildRequires: gtk2-devel >= 2.8.0
BuildRequires: pkgconfig(libcdio)
BuildRequires: pkgconfig(libvisual-0.4)
BuildRequires: tiff-devel
BuildRequires: pkgconfig(libcddb)
BuildRequires: musicbrainz-devel
BuildRequires: pkgconfig(libv4l1)
BuildRequires: mesagl-devel
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xv)
BuildRequires: esound-devel
BuildRequires: jackit-devel

%description
The gmerlin application framework consists of a toolkit indepentent
gmerlin library, which contains the player core, the transcoder core
and other utilities. It can be used to build custom multimedia
applications.

%files -f %name.lang
%defattr(-,root,root)
%doc %_datadir/doc/%name
%_bindir/*
%dir %_libdir/%name
%_libdir/%name/plugins
%_datadir/%name
%_datadir/applications/*.desktop
%_iconsdir/*/*/*/*
%_mandir/man1/*
%_infodir/*

#--------------------------------------------------------------------

%define major 0
%define libname %mklibname %name %major

%package -n %libname
Group: System/Libraries
Summary: Libraries for %name

%description -n %libname
This package contains shared libraries for %name.

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.%{major}*

#--------------------------------------------------------------------

%define develname %mklibname -d %name

%package -n %develname
Group: Development/Other
Summary: Development files for %name
Requires: %libname = %version
Provides: %name-devel = %version

%description -n %develname
This package contains development files for %name.

%files -n %develname
%defattr(-,root,root)
%_includedir/%name
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x --disable-rpath
%make

%install
%makeinstall_std

# drop la files
rm -fr %buildroot%_prefix/lib/%_prefix/lib/%name/plugins/*.la

%find_lang %name


%changelog
* Thu Oct 27 2011 Götz Waschk <waschk@mandriva.org> 1.0.0-2mdv2012.0
+ Revision: 707543
- rebuild for new libcdio

* Mon Jan 17 2011 Funda Wang <fwang@mandriva.org> 1.0.0-1
+ Revision: 631204
- fix BR and linkage
- 1.0.0

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Sun Feb 28 2010 Funda Wang <fwang@mandriva.org> 0.4.3-1mdv2010.1
+ Revision: 512583
- New version 0.4.3

* Thu Feb 25 2010 Funda Wang <fwang@mandriva.org> 0.4.2-1mdv2010.1
+ Revision: 511058
- new version 0.4.2

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 0.4.1-3mdv2010.1
+ Revision: 492341
- add patch fixing build with gtk > 2.18
- finally fix linkage
- rebuild for new libjpegv8

* Sat Aug 22 2009 Funda Wang <fwang@mandriva.org> 0.4.1-2mdv2010.0
+ Revision: 419464
- rebuild for new libjpegv7

* Wed Jul 29 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.1-1mdv2010.0
+ Revision: 404245
- Update to new version 0.4.1
- Remove upstream patch

* Thu Dec 18 2008 Funda Wang <fwang@mandriva.org> 0.4.0-1mdv2009.1
+ Revision: 315578
- fix str fmt
- new version 0.4.0

* Thu Nov 27 2008 Funda Wang <fwang@mandriva.org> 0.3.8-1mdv2009.1
+ Revision: 307269
- add virtual provdies
- import gmerlin


