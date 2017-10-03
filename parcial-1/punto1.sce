clear
clc

t = [0:0.01:3.01]
//disp(size(t,"*"))
y = 3*sin(2*%pi*t)

//Frecuencia = 2*pi
tasa = 5//1/(2*%pi)
muestreo = [0: 1/tasa: 3]
y2 = 3*sin(2*%pi*muestreo)



//HAAR
//disp(muestreo(16))
disp(size(y,"*"))

h1 = zeros(1, size(y,"*"))
h2 = zeros(1, size(y,"*"))

i = 1
j = 1
while( i < size(y,"*") )
    //disp(i)
    h1(j) = sqrt(2)*(y(i) + y(i + 1))/2
    h2(j) = sqrt(2)*(y(i + 1) - y(i))/2
    
    i = i + 2
    j = j + 1
end
//


plot(t, y)
plot(t, h1, "red")
plot(t, h2, "green")
//plot(muestreo, y2, "r*")
//xgrid(5, 1, 7)


