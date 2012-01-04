# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/subeqn
# catalog-date 2007-01-15 00:27:07 +0100
# catalog-license lppl
# catalog-version 2.0b
Name:		texlive-subeqn
Version:	2.0b
Release:	2
Summary:	Package for subequation numbering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/subeqn
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subeqn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subeqn.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subeqn.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Sometimes it is necessary to be able to refer to subexpressions
of an equation. In order to do that these subexpressions should
be numbered. In standard LaTeX there is no provision for this.
To solve this problem Stephen Gildea once wrote subeqn.sty for
LaTeX 2.09; Donald Arsenau rewrote the macros and Johannes
Braams made them available for LaTeX2e. Note that this package
is not compatible with the package subeqnarray (written by
Johannes Braams), but it can be used together with the LaTeX
class options leqno and fleqn.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/subeqn/subeqn.sty
%doc %{_texmfdistdir}/doc/latex/subeqn/manifest.txt
%doc %{_texmfdistdir}/doc/latex/subeqn/subeqn.pdf
%doc %{_texmfdistdir}/doc/latex/subeqn/subeqn.tex
#- source
%doc %{_texmfdistdir}/source/latex/subeqn/subeqn.dtx
%doc %{_texmfdistdir}/source/latex/subeqn/subeqn.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
