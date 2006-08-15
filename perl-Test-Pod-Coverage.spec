#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Pod-Coverage
Summary:	Test::Pod::Coverage - check for POD coverage in your CPAN distribution
Summary(pl):	Test::Pod::Coverage - sprawdzanie pokrycia POD w pakiecie CPAN
Name:		perl-Test-Pod-Coverage
Version:	1.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	33405cca7c75b7b89c06ba30eea66692
URL:		http://search.cpan.org/dist/Test-Pod-Coverage
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Pod-Coverage
BuildRequires:	perl-Test-Builder-Tester
BuildRequires:	perl-Test-Pod >= 1.14
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Checks for POD coverage in files for your CPAN distribution.

  use Test::Pod::Coverage tests=>1;
  pod_coverage_ok( "Foo::Bar", "Foo::Bar is covered" );

%description -l pl
Ten modu³ sprawdza pokrycie POD w plikach dla pakietu CPAN.

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
%{perl_vendorlib}/Test/Pod/*.pm
%{_mandir}/man3/*
