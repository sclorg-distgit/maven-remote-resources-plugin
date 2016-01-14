%global pkg_name maven-remote-resources-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.4
Release:        7.10%{?dist}
Summary:        Maven Remote Resources Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-remote-resources-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildArch: noarch

BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix}maven-plugin-plugin
BuildRequires: %{?scl_prefix}maven-compiler-plugin
BuildRequires: %{?scl_prefix}maven-install-plugin
BuildRequires: %{?scl_prefix}maven-jar-plugin
BuildRequires: %{?scl_prefix}maven-javadoc-plugin
BuildRequires: %{?scl_prefix}maven-resources-plugin
BuildRequires: %{?scl_prefix}maven-surefire-plugin
BuildRequires: %{?scl_prefix}maven-filtering
BuildRequires: %{?scl_prefix}plexus-containers-container-default
BuildRequires: %{?scl_prefix}velocity
BuildRequires: %{?scl_prefix}maven-artifact-resolver
BuildRequires: %{?scl_prefix}maven-common-artifact-filters
BuildRequires: %{?scl_prefix}maven-downloader
BuildRequires: %{?scl_prefix}plexus-interpolation
BuildRequires: %{?scl_prefix}plexus-utils
BuildRequires: %{?scl_prefix}plexus-velocity
BuildRequires: %{?scl_prefix}plexus-resources
BuildRequires: %{?scl_prefix_java_common}junit
BuildRequires: %{?scl_prefix}maven-plugin-testing-harness
BuildRequires: %{?scl_prefix}maven-wagon-provider-api
BuildRequires: %{?scl_prefix}maven-verifier
BuildRequires: %{?scl_prefix}maven-surefire-provider-junit
BuildRequires: %{?scl_prefix}modello


%description
Process resources packaged in JARs that have been deployed to
a remote repository. The primary use case being satisfied is
the consistent inclusion of common resources in a large set of
projects. Maven projects at Apache use this plug-in to satisfy
licensing requirements at Apache where each project much include
license and notice files for each release.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x

#Class org.apache.maven.shared.artifact.filter.collection.TransitivityFilter which ProcessRemoteResourcesMojo.java imports
#is renamed as org.apache.maven.shared.artifact.filter.collection.ProjectTransitivityFilter in
#the version 1.3 of maven-shared-common-artifact-filters package.
sed -i "s/TransitivityFilter/Project&/" `find -name ProcessRemoteResourcesMojo.java`

%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
# fix 613582
# we now use plexus-velocity which has the correct descriptor with a hint.
rm -f src/main/resources/META-INF/plexus/components.xml

%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc DEPENDENCIES LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc DEPENDENCIES LICENSE NOTICE

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.4-7.10
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.4-7.9
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-7.8
- Mass rebuild 2014-05-26

* Thu Feb 20 2014 Michael Simacek <msimacek@redhat.com> - 1.4-7.7
- Adjust maven-wagon R/BR

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-7.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-7.5
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-7.4
- Rebuild to fix incorrect auto-requires

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-7.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-7.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-7.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4-7
- Mass rebuild 2013-12-27

* Thu Aug 22 2013 Michal Srb <msrb@redhat.com> - 1.4-6
- Migrate away from mvn-rpmbuild (Resolves: #997483)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-5
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-4
- BuildRequire newer version of Plexus container

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-1
- Update to upstream version 1.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 23 2012 Tomas Radej <tradej@redhat.com> - 1.3-1
- Updated to latest upstream release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov  7 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.1-3
- Add plexus-resources to Requires

* Wed Sep 07 2011 Tomas Radej <tradej@redhat.com> - 1.2.1-2
- Added license files

* Tue Sep 6 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2.1-1
- Update to latest upstream release.

* Tue Jul 5 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2-3
- BR modello.

* Tue Jul 5 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2-2
- Add missing requires on maven-shared-downloader.

* Thu Mar 17 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2-1
- Update to upstream 1.2 release.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov  3 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-7
- Fix velocity dependency in pom.xml

* Thu Jul 15 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-6
- Fix bug #613582

* Tue Jul 13 2010 Hui Wang <huwang@redhat.com> - 1.1-5
- Add missing requires maven2

* Tue Jul 13 2010 Alexander Kurtakov <akurtako@redhat.com> 1.1-4
- Add missing maven-shared-artifact-resolver requires.

* Tue Jul 13 2010 Hui Wang <huwang@redhat.com> - 1.1-3
- Set '-Dmaven.test.skip=true' to fix Bug 613567

* Thu Jun 03 2010 Hui Wang <huwang@redhat.com> - 1.1-2
- Fixed descirption line length
- Added comment on patch0
- Used macro in add_to_maven_depmap

* Fri May 21 2010 Hui Wang <huwang@redhat.com> - 1.1-1
- Initial version of the package
