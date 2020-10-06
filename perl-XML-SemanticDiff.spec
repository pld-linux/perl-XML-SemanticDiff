#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	XML
%define		pnam	SemanticDiff
Summary:	XML::SemanticDiff - Perl extension for comparing XML documents
Summary(pl.UTF-8):	XML::SemanticDiff - rozszerzenie Perla do porównywania dokumentów XML
Name:		perl-XML-SemanticDiff
Version:	1.0007
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3e9742bcce195473018ba4edcedda303
URL:		https://metacpan.org/release/XML-SemanticDiff
BuildRequires:	perl-Module-Build >= 0.28
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-Encode
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-XML-Parser
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::SematicDiff provides a way to compare the contents and structure
of two XML documents. By default, it returns a list of hashrefs where
each hashref describes a single difference between the two docs.

%description -l pl.UTF-8
XML::SemanticDiff zapewnia możliwość porównywania zawartości i
struktury dwóch dokumentów XML. Domyślnie zwraca listę hashrefów, w
której każdy hashref opisuje pojedynczą różnicę między dokumentami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/SemanticDiff.pm
%{perl_vendorlib}/XML/SemanticDiff
%{_mandir}/man3/XML::SemanticDiff*.3pm*
%{_examplesdir}/%{name}-%{version}
