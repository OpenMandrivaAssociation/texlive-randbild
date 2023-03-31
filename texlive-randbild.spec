Name:		texlive-randbild
Version:	15878
Release:	2
Summary:	Marginal pictures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/randbild
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randbild.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randbild.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randbild.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
