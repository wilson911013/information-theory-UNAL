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

function punto1()
    div = 3 / (2**9 - 1)
    t = [0:div:3]
    y = 3*sin(2*%pi*t)
    
    //Frecuencia = 1
    tasa = 5
    muestreo = [0: 1/tasa: 3]
    y2 = 3*sin(2*%pi*muestreo)
    
    //plotWithHaars(y)
    h1 = haar(y)
    h11 = haar(h1)
    
    disp(size(y, "*"))
    disp(size(h1, "*"))
    disp(size(h11, "*"))
    
    plot(t, y)
    plot(t( 1: size(h1, "*") ), h1, "red")
    plot(t( 1: size(h11, "*") ), h11, "black")
endfunction

punto1()

