%global fontname navilu
%global fontconf 67-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        1.2
Release:        11%{?dist}
Summary:        Free Kannada opentype sans-serif font

License:        OFL
URL:            https://github.com/aravindavk/Navilu
Source0:        https://github.com/aravindavk/Navilu/archive/v%{version}.tar.gz#/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  fontforge
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Source1:        67-navilu.conf
Source2:        %{fontname}.metainfo.xml


%description
This package provides a free Kannada sans-serif opentype font.


%prep
%autosetup -n Navilu-%{version}

%build
make

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
       %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog README
%license COPYING
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Wed Jul 11 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 1.2-11
- Update Source tag

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 17 2014 Pravin Satpute <psatpute@redhat.com> - 1.2-5
- Added Metainfo for gnome-software.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 13 2012 Pravin Satpute <psatpute@redhat.com> - 1.2-1
- Resolves bug 842960

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Pravin Satpute <psatpute@redhat.com> - 1.1-1
- Initial build

