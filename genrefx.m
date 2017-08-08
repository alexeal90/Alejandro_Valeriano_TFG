function [Phi,iPhi,rampgini] = genrefx(nbins,N)

% assume all probability is in [mu-var,mu+var]
nvar = 1;
X = -nvar:2*nvar/nbins:nvar-1/nbins; % a reference signal of variance sigma2 = 1
Phi = (1/(sqrt(2*pi)))*exp(-X.^2/2);

K = 50000; iPhi = zeros(N,1); iPHI = zeros(K,N);
for k = K, iPHI(k,:) = sort(randn(N,1)); end,
for k = 1:N, iPhi(k) = mean(iPHI(:,k)); end,
iPhitmp = iPhi(1:(N/2))-flipud(iPhi((N/2+1):end));
iPhi = [iPhitmp;-flipud(iPhitmp)];

rampgini = 1:nbins;

% figure, 
% subplot(121), plot(iPhi), grid,
% title('iPhi = inv(sort(pmf))')
% subplot(122), plot(Phi), grid,
% title('Phi = pmf')