%define upstream_name    Perl-Critic-Deprecated
%define upstream_version 1.108

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Write C<$my_variable = 42> instead of C<$MyVariable = 42>
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(Perl::Critic::Policy)
BuildRequires: perl(Perl::Critic::TestUtils)
BuildRequires: perl(Perl::Critic::Utils)
BuildRequires: perl(Readonly)
BuildRequires: perl(Test::More)
BuildRequires: perl(base)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The included policies are:

* Perl::Critic::Policy::NamingConventions::ProhibitMixedCaseSubs

  Write '$my_variable = 42' instead of '$MyVariable = 42'. [Severity 1]

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


