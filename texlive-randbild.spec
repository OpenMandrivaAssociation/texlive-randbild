# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/randbild
# catalog-date 2007-05-16 07:57:15 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-randbild
Version:	0.2
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides environments randbild, to draw small marginal plots
(using the package pstricks package pst-plot), and
randbildbasis (the same, only without the automatically drawn
coordinate system).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/randbild/randbild.sty
%doc %{_texmfdistdir}/doc/latex/randbild/README
%doc %{_texmfdistdir}/doc/latex/randbild/randbild.pdf
#- source
%doc %{_texmfdistdir}/source/latex/randbild/randbild.dtx
%doc %{_texmfdistdir}/source/latex/randbild/randbild.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
