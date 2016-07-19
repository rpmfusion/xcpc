%define date 20070122

Name:           xcpc
Version:        0.0 
Release:        0.16.%{date}wip%{?dist}
Summary:        A portable Amstrad CPC464/CPC664/CPC6128 Emulator written in C

License:        GPLv2+
URL:            http://www.xcpc-emulator.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{date}.tar.gz

BuildRequires:  glib2-devel
BuildRequires:  libdsk-devel
BuildRequires:  libXmu-devel
BuildRequires:  motif-devel
BuildRequires:  libICE-devel
BuildRequires:  libtool
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme


%description
Xcpc is a portable Amstrad CPC464/CPC664/CPC6128 Emulator written in C.
 
It is designed to run on any POSIX system (Linux/BSD/UNIX-like OSes).


%prep
%setup -q -n %{name}-%{date}

# remove icon extension from desktop file
sed -i -e 's/^Icon=%{name}.xpm$/Icon=%{name}/g' src/%{name}.desktop 


%build
%configure --with-motif1
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

# install desktop file and fix categories
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --delete-original \
  --remove-category Application \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

# remove icon installed by make
rm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 644 src/%{name}.xpm %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.xpm
%doc AUTHORS ChangeLog COPYING README


%changelog
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

