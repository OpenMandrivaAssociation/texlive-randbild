%global tl_name randbild
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Marginal pictures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/randbild
License:	lppl1.3b
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/randbild.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/randbild.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/randbild.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides environments randbild to draw small marginal plots (using the
packages pstricks and pst-plot), and randbildbasis (the same, only
without the automatically drawn coordinate system).

