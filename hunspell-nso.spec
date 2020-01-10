Name: hunspell-nso
Summary: Northern Sotho hunspell dictionaries
%define upstreamid 20091201
Version: 0.%{upstreamid}
Release: 5%{?dist}
Source: http://extensions.services.openoffice.org/files/3139/1/dict-ns_ZA-2009.12.01.oxt
Group: Applications/Text
URL: http://www.translate.org.za/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Northern Sotho hunspell dictionaries.

%prep
%setup -q -c -n hunspell-nso

%build
for i in README-ns_ZA.txt package-description.txt release-notes-ns_ZA.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ns_ZA.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/nso_ZA.dic
cp -p ns_ZA.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/nso_ZA.aff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README-ns_ZA.txt package-description.txt release-notes-ns_ZA.txt
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20091201-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20091201-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20091201-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20091201-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 02 2009 Caolan McNamara <caolanm@redhat.com> - 0.20091201-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060120-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 12 2008 Caolan McNamara <caolanm@redhat.com> - 0.20060120-1
- initial version
