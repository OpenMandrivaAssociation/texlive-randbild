# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/randbild
# catalog-date 2007-05-16 07:57:15 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-randbild
Version:	0.2
Release:	7
Summary:	Marginal pictures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/randbild
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randbild.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randbild.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randbild.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides environments randbild, to draw small marginal plots
(using the package pstricks package pst-plot), and
randbildbasis (the same, only without the automatically drawn
coordinate system).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/randbild/randbild.sty
%doc %{_texmfdistdir}/doc/latex/randbild/README
%doc %{_texmfdistdir}/doc/latex/randbild/randbild.pdf
#- source
%doc %{_texmfdistdir}/source/latex/randbild/randbild.dtx
%doc %{_texmfdistdir}/source/latex/randbild/randbild.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 755574
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719428
- texlive-randbild
- texlive-randbild
- texlive-randbild
- texlive-randbild

