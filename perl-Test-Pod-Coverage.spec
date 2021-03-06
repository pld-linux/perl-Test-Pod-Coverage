#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Test
%define	pnam	Pod-Coverage
Summary:	Test::Pod::Coverage - check for POD coverage in your CPAN distribution
Summary(pl.UTF-8):	Test::Pod::Coverage - sprawdzanie pokrycia POD w pakiecie CPAN
Name:		perl-Test-Pod-Coverage
Version:	1.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c9ea5f4182415b13d2db18484a38c01b
URL:		https://metacpan.org/release/Test-Pod-Coverage
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Pod-Coverage
BuildRequires:	perl-Test-Pod >= 1.14
BuildRequires:	perl-Test-Simple >= 0.64
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Checks for POD coverage in files for your CPAN distribution.

  use Test::Pod::Coverage tests=>1;
  pod_coverage_ok( "Foo::Bar", "Foo::Bar is covered" );

%description -l pl.UTF-8
Ten moduł sprawdza pokrycie POD w plikach dla pakietu CPAN.

  use Test::Pod::Coverage tests=>1;
  pod_coverage_ok( "Foo::Bar", "Foo::Bar jest pokryte" );

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Test/Pod
%{perl_vendorlib}/Test/Pod/Coverage.pm
%{_mandir}/man3/Test::Pod::Coverage.3pm*
