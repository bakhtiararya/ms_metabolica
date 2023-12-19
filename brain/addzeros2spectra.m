function addzeros2spectra(nozeros, inputfile, outputfile)
% Adds noise to the time domain signal (x). 
% Some appropriate noise levels are 0 for none, 1 for minimal, 10 for some,
% and 50 for a lot of noise.
% 4/4/2005 QB3, Esin
inputspectra = read_ddf_image(char(inputfile));
Nx= inputspectra.ddf.npix(1);
Ny=inputspectra.ddf.npix(2);
Nz = inputspectra.ddf.npix(3);
N = inputspectra.ddf.specpoints;

outputspectra.ddf = inputspectra.ddf;
outputspectra.ddf.specpoints = inputspectra.ddf.specpoints+nozeros;
for n1 = 1:Nx
    for n2 = 1:Ny
        for n3 = 1:Nz
            tempsignal = inputspectra.img(:,n1,n2,n3);
            tempsignal2 =  tempsignal; 
            tempsignal2(size(tempsignal,1)+1:size(tempsignal,1)+nozeros) = 0;
            outputspectra.img(:,n1,n2,n3) = tempsignal2; 
        end
    end
end
outputspectra.ddf.filename = strcat(char(outputfile), '.ddf');
write_ddf_image(char(outputfile), outputspectra);




