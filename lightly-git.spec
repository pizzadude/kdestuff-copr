Name:           lightly-git
Version:        0.4.1
Release:        4%{?dist}
Summary:        A modern style for qt applications

License:        GPLv2+ and MIT
URL:            https://github.com/boehs/Lightly
Source0:        https://pizzadude.ca/rpmbuild/Lightly.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KDecoration2)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  kwin-devel
BuildRequires:  libepoxy-devel
BuildRequires:  cmake(KF5Init)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  kf5-kpackage-devel
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(KF5Wayland)

%description
Lightly is a fork of breeze theme style that aims to be visually modern and
minimalistic.

%prep
%autosetup -n Lightly

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/lightly-settings5
%{_libdir}/cmake/Lightly/
%{_libdir}/kconf_update_bin/kde4lightly
%{_libdir}/liblightlycommon5.so.*
%{_qt5_plugindir}/kstyle_lightly_config.so
%{_qt5_plugindir}/org.kde.kdecoration2/lightlydecoration.so
%{_qt5_plugindir}/styles/lightly.so
%dir %{_datadir}/color-schemes
%{_datadir}/color-schemes/Lightly.colors
%{_datadir}/kconf_update/kde4lightly.upd
%{_datadir}/kservices5/lightlydecorationconfig.desktop
%{_datadir}/kservices5/lightlystyleconfig.desktop
%{_datadir}/kstyle/themes/lightly.themerc
%{_datadir}/icons/hicolor/scalable/apps/lightly-settings.svgz


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar  4 12:42:39 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Wed Feb 17 03:04:44 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.4-1
- Initial build
