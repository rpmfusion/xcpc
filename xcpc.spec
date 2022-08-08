Name:           xcpc
Version:        0.37.0
Release:        3%{?dist}
Summary:        A portable Amstrad CPC 464/664/6128 emulator written in C

License:        GPLv2+
URL:            http://www.xcpc-emulator.net/
Source0:        https://bitbucket.org/ponceto/xcpc/downloads/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gtk3-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  portaudio-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme
Provides:       bundled(libdsk) = 1.4.2
Provides:       bundled(lib765) = 0.4.2


%description
Xcpc is a portable Amstrad CPC 464/664/6128 emulator written in C. It is
designed to run on any POSIX compliant system having an X11 server, including
Linux, BSD and Unix.


%prep
%autosetup

# Disable check for C++14 support in GCC
sed -i '/AX_CHECK_CXX14/d' configure.ac


%build
autoreconf -fvi
%configure --with-x11-toolkit=gtk3
%make_build


%install
%make_install

# fix desktop file
desktop-file-install \
  --delete-original \
  --remove-key Encoding \
  --set-icon=%{name} \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

# remove icon installed by make
rm %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
install -m 644 share/pixmaps/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/

# install AppData file
install -d %{buildroot}%{_metainfodir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml
%doc AUTHORS ChangeLog README.md
%license COPYING


%changelog
* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.37.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.37.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Andrea Musuruane <musuruan@gmail.com> - 0.37.0-1
- Updated to new upstream release (BZ #6026)

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0-0.28.20070122wip
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0-0.27.20070122wip
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0-0.26.20070122wip
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0-0.25.20070122wip
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Andrea Musuruane <musuruan@gmail.com> - 0.0-0.24.20070122wip
- Added gcc dependency
- Added AppData file
- Spec file cleanup

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0-0.23.20070122wip
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0-0.22.20070122wip
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0-0.21.20070122wip
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Sat Jul 28 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 0.0-0.20.20070122wip
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.0-0.19.20070122wip
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.0-0.18.20070122wip
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.0-0.17.20070122wip
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Andrea Musuruane <musuruan@gmail.com> - 0.0-0.16.20070122wip
- Built against motif because lesstif has been retired for F24

* Sun Jul 17 2016 Andrea Musuruane <musuruan@gmail.com> - 0.0-0.15.20070122wip
- Built against libXaw because lesstif has been retired for F24
- Updated URL
- Updated Source0
- Dropped cleaning at the beginning of %%install

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.0-0.14.20070122wip
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 13 2013 Andrea Musuruane <musuruan@gmail.com> 0.0-0.13.20070122wip
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- Dropped desktop vendor tag
- Updated icon cache scriptlets

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.0-0.12.20070122wip
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.0-0.11.20070122wip
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 11 2010 Andrea Musuruane <musuruan@gmail.com> 0.0-0.10.20070122wip
- rebuilt for F13+

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.0-0.9.20070122wip
- rebuild for new F11 features

* Thu Dec 04 2008 Andrea Musuruane <musuruan@gmail.com> 0.0-0.8.20070122wip
- Fixed unowned directory (BZ #214)
- Removed old Fedora stuff
- Cosmetic changes 

* Sat Jul 26 2008 Andrea Musuruane <musuruan@gmail.com> 0.0-0.7.20070122wip
- Changed license due to new guidelines
- Removed %%{?dist} tag from changelog
- Updated icon cache scriptlets to be compliant to new guidelines
- Improved macro usage
- Removed the icon extension from the desktop file
- Minor cleanup

* Sat Mar 17 2007 Andrea Musuruane <musuruan@gmail.com> 0.0-0.6.20070122wip
- Changed .desktop category to Game;Emulator;

* Mon Jan 22 2007 Andrea Musuruane <musuruan@gmail.com> 0.0-0.5.20070122wip
- Updated to latest snapshot
- Added %%date variable 

* Mon Jan 15 2007 Andrea Musuruane <musuruan@gmail.com> 0.0-0.4.20070108wip
- Added libICE-devel to the BR
- Fixed openmotif/lesstif BR depending on fedora version

* Sun Jan 14 2007 Andrea Musuruane <musuruan@gmail.com> 0.0-0.3.20070108wip
- Dropped --add-category=X-Fedora from desktop-file-install 

* Wed Jan 10 2007 Andrea Musuruane <musuruan@gmail.com> 0.0-0.2.20070108wip
- Updated to xcpc-20070108
- Removed no longer needed fix to run xcpc
- Changed .desktop category to "Application;Emulator;"

* Wed Dec 27 2006 Andrea Musuruane <musuruan@gmail.com> 0.0-0.1.20061218wip
- Initial release for Dribble

