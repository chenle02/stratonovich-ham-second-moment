Initial positive-quadrature component check fails its unchanged1e-45relative
criterion atA60,s61,w10. Both integrals are about2.69e-261;the unscaled
absolute quadrature loses about4.8e-4relative accuracy. Initial script/driver
are preserved. The successor factors the exact commonexp(-min(A,s)*w)out
of BOTHsides before quadrature. Same60digits and1e-45relative criterion,
no clipping/tolerance relaxation. All68cases then pass,maxrelativeerror
1.82e-61. These are floating consistency checks,not certified enclosures.
