clear
clc
file_path = "C:\Users\amron\git\Information-theroy\ex1-prac\discovery"
[y, sample_rate, bits] = wavread(file_path)


first_channel = y(1, :)
N = size(first_channel, "*")

z = fft(first_channel)
frecuencies = sample_rate*(0:(N/2))/N
n = size(frecuencies, "*")
disp(size(z,"*"))

clf()
plot2d(frecuencies, abs(z(1:n)))

