function [res] = MIX(n,p)
%""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
% PURPOSE:
% Function that generates a MIX process, that is, a signal with both
% deterministic and stochastic components, each one to a greater or
% lesser extent depending on parameter p. For p=0, the signal will be
% completly deterministic and for p=1 the signal will be completly stochastic.
% USE:
% [res] = MIX(n,p)
% ARGUMENTS...
% ...INPUT:
% .-n ---> number of points in the resulting signal.
% .-p ---> parameter that controls the percentage of each signal
% component.
%...OUTPUT:
% .-res---> MIX process.
%""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
%Deterministic component
X = sqrt(2)*sin((2*pi*(1:n))/12);
%Stochastic component
Y = -sqrt(3) + 2*sqrt(3)*rand(1,n);
Z = zeros(1,n);
t = rand(1,n);
uno  = find(t<p);
cero = find(t>p);
Z(uno) = 1;
Z(cero)= 0;
%Final MIX process
res = (1-Z).*X+Z.*Y;