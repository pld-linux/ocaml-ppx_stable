#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Stable types conversions generator
Summary(pl.UTF-8):	Generowanie konwersji typów stabilnych
Name:		ocaml-ppx_stable
Version:	0.14.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_stable/tags
Source0:	https://github.com/janestreet/ppx_stable/archive/v%{version}/ppx_stable-%{version}.tar.gz
# Source0-md5:	78fd32fd0e72ebfd8e522008949066b5
URL:		https://github.com/janestreet/ppx_stable
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.14.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
A ppx extension for easier implementation of conversion functions
between almost identical types.

This package contains files needed to run bytecode executables using
ppx_stable library.

%description -l pl.UTF-8
Rozszerzenie ppx do łatwej implementacji funkcji konwersji między
prawie identycznymi typami.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_stable.

%package devel
Summary:	Stable types conversions generator - development part
Summary(pl.UTF-8):	Generowanie konwersji typów stabilnych - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.14.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_stable library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_stable.

%prep
%setup -q -n ppx_stable-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_stable/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_stable

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_stable
%{_libdir}/ocaml/ppx_stable/META
%{_libdir}/ocaml/ppx_stable/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_stable/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_stable/*.cmi
%{_libdir}/ocaml/ppx_stable/*.cmt
%{_libdir}/ocaml/ppx_stable/*.cmti
%{_libdir}/ocaml/ppx_stable/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_stable/ppx_stable.a
%{_libdir}/ocaml/ppx_stable/*.cmx
%{_libdir}/ocaml/ppx_stable/*.cmxa
%endif
%{_libdir}/ocaml/ppx_stable/dune-package
%{_libdir}/ocaml/ppx_stable/opam
