clear
clc

function [tf, tf2]=haar(fx)
    n = size(fx, "*")
    if modulo(n, 2) == 1 then
        n = n - 1 //Ignore last element
    end
    
    tn = n / 2
    
    tf = zeros(1, tn)
    tf2 = zeros(1, tn)
    i = 1
    j = 1
    while( i < n )
        tf(j) = sqrt(2)*(fx(i) + fx(i + 1)) / 2
        tf2(j) = sqrt(2)*(fx(i + 1) - fx(i)) / 2
        i = i + 2
        j = j + 1
    end
endfunction

function plotWithHaars(fx)
    [h1, h2] = haar(fx)
    pH1 = zeros(1, size(y,"*"))
    pH2 = zeros(1, size(y,"*"))
    
    tn = size(h1, "*")
    i = 1
    while( i <= tn )
        pH1(i) = h1(i)
        pH1(i + tn)  = h1(i) 
    
        pH2(i) = h2(i)
        pH2(i + tn)  = h2(i)
        i = i + 1
    end
    plot(t, y)
    plot(t, pH1, "red")
    plot(t, pH2, "green")
endfunction

function y=f_p1(x)
    y = 3*sin(2*%pi*x)
endfunction

function punto1()
    div = 3 / (2**9 - 1)
    t = [0:div:3]
    y = f_p1(t)
    
    //Frecuencia = 1
    tasa = 5
    muestreo = [0: 1/tasa: 3]
    y2 = 3*sin(2*%pi*muestreo)
    
    //plotWithHaars(y)
    h1 = haar(y)
    h11 = haar(h1)
    
    //disp(size(y, "*"))
    //disp(size(h1, "*"))
    //disp(size(h11, "*"))
    
    plot(t, y)
    plot(t( 1: size(h1, "*") ), h1, "red")
    plot(t( 1: size(h11, "*") ), h11, "black")
endfunction

function [nh, div]=haar_n(sound, times)
    nh = haar(sound)
    i = 1
    while( i < times)
        nh = haar(nh)
        i = i + 1
    end
    div = 2**(times - 1)
endfunction

function [y, sample_rate, bits]=wav_sound()
    file_path = "C:\Users\amron\git\Information-theroy\voice-exercise\output"
    [y, sample_rate, bits] = wavread(file_path)
endfunction

function punto2()
    [y, sample_rate, bits] = wav_sound()
   
    disp("---Computing haar---")
    [h, div] = haar_n(y, 2)
    disp("---Haarp computed---")
    
    disp("Original sound size: " + string(size(y, "*")))
    disp("Transform size: " + string(size(h, "*")))
    disp("The transform size is " + string(ceil(100*size(h, "*")/size(y, "*"))) + "% of the original")
    
    //disp("Playing----")
    //sound(y, sample_rate)
    sound(h, sample_rate/div)
    //disp("End playing---")
endfunction

function punto3a()
    disp("FFT of the sin function")
    div = 3 / (2**9 - 1)
    t = [0:div:3]
    y = f_p1(t)
    N = size(y, "*")
    
    z = fft(y)/N
    
    frecuencies = (1/div)*(0:(N/2))/N
    disp(frecuencies(1), frecuencies(2))
    n = size(frecuencies, "*")
    disp(size(z,"*"))
    disp(n)
    plot(frecuencies, abs(z(1:n)))
endfunction

function punto3b()
    disp("FFT of the sound function")
    
    [y, sample_rate, bits]=wav_sound()
    N = size(y, "*")
    
    z = fft(y)/N
    
    frecuencies = sample_rate*(0:(N/2))/N
    n = size(frecuencies, "*")
    plot(frecuencies, abs(z(1:n)))
endfunction

//punto1()
//punto2()
//punto3a()
punto3b()













