% Parameters declarations
    time = linspace(-pi,pi,2000);    

    nVec = [20 50 100];

    fOrig = zeros(size(time)); %We need to reset this for each case
%% Square Pulse
    
    fOrig( (time > -pi/2) & (time < pi/2) ) = 1;

    PlotFunctions(time, fOrig, nVec, 'Square Pulse');
    
    %% subquestion 2
    
    fOrig = zeros(size(time));
    fOrig( time>=0 ) = time( time>=0 );

    PlotFunctions(time, fOrig, nVec, 'subquestion 2');
    
    %% subquestion 3
    
    fOrig = zeros(size(time));
    
    fOrig( (time >= -pi/2) & (time <= 0) ) = 2*time( (time >= -pi/2) & (time <= 0) ) + pi;
    fOrig( (time >= 0) & (time <= pi/2) ) = -2*time( (time >= 0) & (time <= pi/2) ) + pi;
    
    PlotFunctions(time, fOrig, nVec, 'subquestion 3');
    
    %% subquestion 4
    
    fOrig = zeros(size(time));
    
    fOrig( (time >= -pi/2) & (time <= 0) ) = -pi;
    fOrig( (time >= 0) & (time <= pi/2) ) = 2*time( (time >= 0) & (time <= pi/2) ) - pi;
    
    
    PlotFunctions(time, fOrig, nVec, 'subquestion 4');
    
 function [fReconst] = FindFourierCoeff(time, fOrig, N)
    dx = time(2) - time(1);
    a0 = (1/pi) .* sum(fOrig.*dx);
        
    sumVal = 0;
    aN = zeros(N, 1);
    bN = zeros(N, 1);
    for iter = 1:N
        aN(iter) = (1/pi) .* sum(fOrig.*cos(iter*time).*dx);
        bN(iter) = (1/pi) .* sum(fOrig.*sin(iter*time).*dx);
        
        sumVal = sumVal + aN(iter).*cos(iter.*time) + bN(iter).*sin(iter.*time);
    end
    
    fReconst = a0/2 + sumVal;

end

function [] = PlotFunctions(time, fOrig, nVec, titleStr)
    
    fReconst1 = FindFourierCoeff(time, fOrig, nVec(1));
    fReconst2 = FindFourierCoeff(time, fOrig, nVec(2));
    fReconst3 = FindFourierCoeff(time, fOrig, nVec(3));

    figure;
    plot(time, fOrig, 'k');
    hold on;
    plot(time, fReconst1, 'g');
    hold on;
    plot(time, fReconst2, 'b');
    hold on;
    plot(time, fReconst3, 'm');
    
    str1 = sprintf('Reconstructed Signal N = %d', nVec(1));
    str2 = sprintf('Reconstructed Signal N = %d', nVec(2));
    str3 = sprintf('Reconstructed Signal N = %d', nVec(3));
   
    legend('Input Signal', str1 , str2, str3); 
    title(titleStr);
end