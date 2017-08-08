senal = randn(1000,1);   % señal 

%% NCD Incremental
A = 100;             % punto de inicio
B = 100;             % incremento utilizado

NCDi = [];

% % create temporal directory
% mkdir('tmp');
for s = A+B:B:length(senal)
    % creo X
    dlmwrite('tmp/x.txt', senal(1:s-A), ':');
    % creo Y
    dlmwrite('tmp/y.txt', senal(s-A+1:s), ':');
    % creo XY
    dlmwrite('tmp/xy.txt', senal(1:s), ':');
    
    % comprimo X
    fx = gzip('tmp/x.txt', 'tmp');
    % comprimo Y
    fy = gzip('tmp/y.txt', 'tmp');
    % comprimo XY
    fxy = gzip('tmp/xy.txt', 'tmp');
    
    % tamaño compresión X
    fI = dir(fx{1}); Cx = fI.bytes;
    
    % tamaño compresión Y
    fI = dir(fy{1}); Cy = fI.bytes;
    
    % tamaño compresión Z
    fI = dir(fxy{1}); Cxy = fI.bytes;
    
    NCDi(end+1) = (Cxy - min(Cx,Cy)) / max(Cx,Cy);
    
    % delete files
    aux = dir('tmp');
    for i = 3:length(aux), aux(i).name = ['tmp/', aux(i).name]; end
    aux = {aux.name}; delete(aux{3:end}); clear aux;
end

% figure; plot(A+B:B:length(senal), NCDi); xlim([0 length(senal)]); title('NCDi');

%% Calculo entropías h_*. h_delta y h_phi
disp('-----h_*, h_\delta, h_\Phi-----')
  
N = length(senal);
nbins = 100;
[Phi,iPhi,rampgini] = genrefx(nbins,N);
        
p = hist(senal,nbins)/N;
h_s = 1/max(p);         


p = hist(senal,nbins)/N;
h_delta = dot(iPhi,sort(senal)./max(senal));


p = hist(senal,nbins)/N;
h_phi = dot(Phi,p/max(p));


