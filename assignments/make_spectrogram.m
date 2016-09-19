%
% make_spectrogram
% 
% Makes recording for 10s then produces spectrogram
%
%  (default sampling of 8000 /s)
%
fs=8000,nbits=16;
recObj = audiorecorder(fs,nbits,1);
disp('Start recording (10s duration) ')
recordblocking(recObj, 10);
disp('End of Recording.');

% Play back the recording.
%play(recObj);

% Store data in double-precision array.
y = getaudiodata(recObj);
fs=8000;   %% sampling rate
%
%Spectrogram
%
WIN = 500; %window sample size - number of samples  for each time step to average fourier transform.
OLAP = floor(WIN/2); %window overlap - how many samples of overlap %between neighboring windows.
%
F = 0:fs/10000:fs/4; %Define  the frequency vector and its resolution 
%
%% Default spectrogram in Matlab has time on vertical axis. This rotates it
figure(3)
[S,F,T] = spectrogram(y,WIN,OLAP,F,fs);  
surf(T,F,10*log10(abs(S)),'EdgeColor','none')
axis xy; axis tight; view(0,90);set(gca,'FontSize',14);

%% Make the plot look nice
%set(gca,'XTick',[])   % omit
colormap('gray') % cool is nice, bone is nice grayscale; default is jet
caxis([0 10]) % usual range of amplitude
axis([0 max(T) 30 fs/4]) 
colorbar
xlabel('Time [s]','FontSize',14)
ylabel('Frequency [Hz]','FontSize',14)
